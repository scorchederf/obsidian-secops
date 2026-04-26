---
atomic_guid: "6d27df5d-69d4-4c91-bc33-5983ffe91692"
title: "Password Cracking with Hashcat"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.002"
attack_technique_name: "Brute Force: Password Cracking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.002/T1110.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "6d27df5d-69d4-4c91-bc33-5983ffe91692"
  - "Password Cracking with Hashcat"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Cracking with Hashcat

Execute Hashcat.exe with provided SAM file from registry of Windows and Password list to crack against

## Metadata

- Atomic GUID: 6d27df5d-69d4-4c91-bc33-5983ffe91692
- Technique: T1110.002: Brute Force: Password Cracking
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1110.002/T1110.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.002]]

## Input Arguments

### hashcat_exe

- description: Path to Hashcat executable
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\hashcat6\hashcat-6.1.1\hashcat.exe

### input_file_passwords

- description: Path to password list
- type: string
- default: PathToAtomicsFolder\T1110.002\src\password.lst

### input_file_sam

- description: Path to SAM file
- type: string
- default: PathToAtomicsFolder\T1110.002\src\sam.txt

## Dependencies

Hashcat must exist on disk at specified location (#{hashcat_exe})

### Prerequisite Check

```text
if (Test-Path  $(cmd /c echo "#{hashcat_exe}")) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://www.7-zip.org/a/7z1900.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\7z1900.exe"
Start-Process -FilePath "PathToAtomicsFolder\..\ExternalPayloads\7z1900.exe" -ArgumentList "/S /D=PathToAtomicsFolder\..\ExternalPayloads\7zi" -NoNewWindow
Invoke-WebRequest "https://hashcat.net/files/hashcat-6.1.1.7z" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\hashcat6.7z"
Start-Process cmd.exe -Args  "/c %temp%\7z\7z.exe x %temp%\hashcat6.7z -aoa -o%temp%\hashcat-unzip" -Wait
New-Item -ItemType Directory (Split-Path $(cmd /c echo #{hashcat_exe})) -Force | Out-Null
Move-Item "PathToAtomicsFolder\..\ExternalPayloads\hashcat-unzip\hashcat-6.1.1\*" $(cmd /c echo #{hashcat_exe}\..) -Force -ErrorAction Ignore
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
cd #{hashcat_exe}\..
#{hashcat_exe} -a 0 -m 1000 -r .\rules\Incisive-leetspeak.rule #{input_file_sam} #{input_file_passwords}
```

### Cleanup

```commandprompt
del "PathToAtomicsFolder\..\ExternalPayloads\hashcat6.7z" >nul 2>&1
del "PathToAtomicsFolder\..\ExternalPayloads\7z1900.exe" >nul 2>&1
del "PathToAtomicsFolder\..\ExternalPayloads\7z" /Q /S >nul 2>&1
del "PathToAtomicsFolder\..\ExternalPayloads\hashcat-unzip" /Q /S >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.002/T1110.002.yaml)
