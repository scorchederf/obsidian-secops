---
atomic_guid: "870fe8fb-5e23-4f5f-b89d-dd7fe26f3b5f"
title: "GPP Passwords (findstr)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.006"
attack_technique_name: "Unsecured Credentials: Group Policy Preferences"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.006/T1552.006.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "870fe8fb-5e23-4f5f-b89d-dd7fe26f3b5f"
  - "GPP Passwords (findstr)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# GPP Passwords (findstr)

Look for the encrypted cpassword value within Group Policy Preference files on the Domain Controller. This value can be decrypted with gpp-decrypt on Kali Linux.

## Metadata

- Atomic GUID: 870fe8fb-5e23-4f5f-b89d-dd7fe26f3b5f
- Technique: T1552.006: Unsecured Credentials: Group Policy Preferences
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1552.006/T1552.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.006]]

## Dependencies

Computer must be domain joined

### Prerequisite Check

```text
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Write-Host Joining this computer to a domain must be done manually
```

## Executor

- name: command_prompt

### Command

```commandprompt
findstr /S cpassword %logonserver%\sysvol\*.xml
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.006/T1552.006.yaml)
