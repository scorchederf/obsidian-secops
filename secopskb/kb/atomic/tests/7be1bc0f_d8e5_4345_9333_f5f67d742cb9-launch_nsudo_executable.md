---
atomic_guid: "7be1bc0f-d8e5-4345-9333-f5f67d742cb9"
title: "Launch NSudo Executable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.001"
attack_technique_name: "Access Token Manipulation: Token Impersonation/Theft"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.001/T1134.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "7be1bc0f-d8e5-4345-9333-f5f67d742cb9"
  - "Launch NSudo Executable"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Launches the NSudo executable for a short period of time and then exits.
NSudo download observed after maldoc execution. NSudo is a system management tool for advanced users to launch programs with full privileges.

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]

## Input Arguments

### nsudo_path

- description: Path to the NSudoLG.exe file
- type: path
- default: PathToAtomicsFolder\T1134.001\bin\NSudoLG.exe

## Dependencies

NSudoLG.exe must exist in the specified path #{nsudo_path}

### Prerequisite Check

```powershell
if (Test-Path "#{nsudo_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\NSudo_8.2_All_Components.zip" "https://github.com/M2Team/NSudo/releases/download/8.2/NSudo_8.2_All_Components.zip"
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\NSudo_8.2_All_Components.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\NSudo_8.2_All_Components" -Force
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\NSudo_8.2_All_Components\NSudo Launcher\x64\NSudoLG.exe" "#{nsudo_path}"
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\NSudo_8.2_All_Components.zip" -Recurse -ErrorAction Ignore
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\NSudo_8.2_All_Components" -Recurse -ErrorAction Ignore
```

## Executor

- name: powershell

### Command

```powershell
Start-Process "#{nsudo_path}" -Argument "-U:T -P:E cmd"
Start-Sleep -Second 5
Stop-Process -Name "cmd" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.001/T1134.001.yaml)
