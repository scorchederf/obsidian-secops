---
atomic_guid: "40075d5f-3a70-4c66-9125-f72bee87247d"
title: "Windows Disable LSA Protection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562"
attack_technique_name: "Impair Defenses"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "40075d5f-3a70-4c66-9125-f72bee87247d"
  - "Windows Disable LSA Protection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Disable LSA Protection

The following Atomic adds a registry entry to disable LSA Protection.

The LSA controls and manages user rights information, password hashes and other important bits of information in memory. Attacker tools, such as mimikatz, rely on accessing this content to scrape password hashes or clear-text passwords. Enabling LSA Protection configures Windows to control the information stored in memory in a more secure fashion - specifically, to prevent non-protected processes from accessing that data.
Upon successful execution, the registry will be modified and RunAsPPL will be set to 0, disabling Lsass protection.
https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection#how-to-disable-lsa-protection
https://blog.netwrix.com/2022/01/11/understanding-lsa-protection/
https://thedfirreport.com/2022/03/21/phosphorus-automates-initial-access-using-proxyshell/

## Metadata

- Atomic GUID: 40075d5f-3a70-4c66-9125-f72bee87247d
- Technique: T1562: Impair Defenses
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562/T1562.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add HKLM\SYSTEM\CurrentControlSet\Control\LSA /v RunAsPPL /t REG_DWORD /d 0 /f
```

### Cleanup

```commandprompt
reg delete HKLM\SYSTEM\CurrentControlSet\Control\LSA /v RunAsPPL /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml)
