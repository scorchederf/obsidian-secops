---
sigma_id: "b2ddd389-f676-4ac4-845a-e00781a48e5f"
title: "Using SettingSyncHost.exe as LOLBin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_settingsynchost.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_settingsynchost.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b2ddd389-f676-4ac4-845a-e00781a48e5f"
  - "Using SettingSyncHost.exe as LOLBin"
attack_technique_ids:
  - "T1574.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects using SettingSyncHost.exe to run hijacked binary

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]

## Detection

```yaml
system_utility:
  Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
parent_is_settingsynchost:
  ParentCommandLine|contains|all:
  - cmd.exe /c
  - RoamDiag.cmd
  - -outputpath
condition: not system_utility and parent_is_settingsynchost
```

## False Positives

- Unknown

## References

- https://www.hexacorn.com/blog/2020/02/02/settingsynchost-exe-as-a-lolbin

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_settingsynchost.yml)
