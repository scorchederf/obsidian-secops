---
atomic_guid: "01df0353-d531-408d-a0c5-3161bf822134"
title: "Compress Data and lock with password for Exfiltration with winzip"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "01df0353-d531-408d-a0c5-3161bf822134"
  - "Compress Data and lock with password for Exfiltration with winzip"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Compress Data and lock with password for Exfiltration with winzip

Note: Requires winzip installation
wzzip sample.zip -s"blueblue" *.txt (VARIANT)

## Metadata

- Atomic GUID: 01df0353-d531-408d-a0c5-3161bf822134
- Technique: T1560.001: Archive Collected Data: Archive via Utility
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1560.001/T1560.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Input Arguments

### winzip_exe

- description: Path to installed Winzip executable
- type: path
- default: %ProgramFiles%\WinZip\winzip64.exe

### winzip_hash

- description: File hash of the Windows Credential Editor zip file
- type: string
- default: B59DB592B924E963C21DA8709417AC0504F6158CFCB12FE5536F4A0E0D57D7FB

### winzip_url

- description: Path to download Windows Credential Editor zip file
- type: url
- default: https://download.winzip.com/gl/nkln/winzip24-home.exe

## Dependencies

Winzip must be installed

### Prerequisite Check

```powershell
cmd /c 'if not exist "#{winzip_exe}" (echo 1) else (echo 0)'
```

### Get Prerequisite

```powershell
IEX(IWR "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-WebRequestVerifyHash.ps1" -UseBasicParsing)
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
if(Invoke-WebRequestVerifyHash "#{winzip_url}" "PathToAtomicsFolder\..\ExternalPayloads\winzip.exe" #{winzip_hash}){
  Write-Host Follow the installation prompts to continue
  cmd /c "PathToAtomicsFolder\..\ExternalPayloads\winzip.exe"
}
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
path=%path%;"C:\Program Files (x86)\winzip"
mkdir .\tmp\victim-files
cd .\tmp\victim-files
echo "This file will be encrypted" > .\encrypted_file.txt
"#{winzip_exe}" -min -a -s"hello" archive.zip *
dir
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
