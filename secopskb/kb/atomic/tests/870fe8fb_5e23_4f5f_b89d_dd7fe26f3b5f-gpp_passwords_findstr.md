---
atomic_guid: "870fe8fb-5e23-4f5f-b89d-dd7fe26f3b5f"
title: "GPP Passwords (findstr)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.006"
attack_technique_name: "Unsecured Credentials: Group Policy Preferences"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.006/T1552.006.yaml"
build_date: "2026-04-27 19:12:28"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Look for the encrypted cpassword value within Group Policy Preference files on the Domain Controller. This value can be decrypted with gpp-decrypt on Kali Linux.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]

## Dependencies

Computer must be domain joined

### Prerequisite Check

```powershell
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Joining this computer to a domain must be done manually
```

## Executor

- name: command_prompt

### Command

```cmd
findstr /S cpassword %logonserver%\sysvol\*.xml
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.006/T1552.006.yaml)
