---
atomic_guid: "6904235f-0f55-4039-8aed-41c300ff7733"
title: "Use PsExec to elevate to NT Authority\\SYSTEM account"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "6904235f-0f55-4039-8aed-41c300ff7733"
  - "Use PsExec to elevate to NT Authority\\SYSTEM account"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

PsExec is a powerful tool most known for its remote management capability. However, it can also be used to run processes as the local system account.

The local system account is a default windows account which has unrestricted access to all system resources.

Upon successful execution, PsExec.exe will spawn a command prompt which will run 'whoami' as the local system account and then exit.

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

## Dependencies

PsExec tool from Sysinternals must exist in the ExternalPayloads directory

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe") { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" -Force
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" -accepteula -s %COMSPEC% /c whoami
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
