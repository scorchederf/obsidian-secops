---
atomic_guid: "b385996c-0e7d-4e27-95a4-aca046b119a7"
title: "Create Volume Shadow Copy with diskshadow"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "b385996c-0e7d-4e27-95a4-aca046b119a7"
  - "Create Volume Shadow Copy with diskshadow"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test is intended to be run on a domain controller
An alternative to using vssadmin to create a Volume Shadow Copy for extracting ntds.dit

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

## Input Arguments

### filename

- description: Location of the script
- type: Path
- default: PathToAtomicsFolder\T1003.003\src\diskshadow.txt

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
mkdir c:\exfil
diskshadow.exe /s #{filename}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
