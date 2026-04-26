---
sigma_id: "c453ab7a-1f5c-4716-a3b4-dea8135fb43a"
title: "Registry Manipulation via WMI Stdregprov"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_stdregprov_reg_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_stdregprov_reg_modification.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c453ab7a-1f5c-4716-a3b4-dea8135fb43a"
  - "Registry Manipulation via WMI Stdregprov"
attack_technique_ids:
  - "T1047"
  - "T1112"
  - "T1012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Manipulation via WMI Stdregprov

Detects the usage of wmic.exe to manipulate Windows registry via the WMI StdRegProv class.
This behaviour could be potentially suspicious because it uses an alternative method to modify registry keys instead of legitimate registry tools like reg.exe or regedit.exe.
Attackers specifically choose this technique to evade detection and bypass security monitoring focused on traditional registry modification commands.

## Metadata

- Rule ID: c453ab7a-1f5c-4716-a3b4-dea8135fb43a
- Status: experimental
- Level: medium
- Author: Daniel Koifman (KoifSec)
- Date: 2025-07-30
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_stdregprov_reg_modification.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1012-query_registry|T1012]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains|all:
  - call
  - stdregprov
condition: all of selection_*
```

## False Positives

- Legitimate administrative activity

## References

- https://www.bitdefender.com/en-us/blog/businessinsights/shrinklocker-decryptor-from-friend-to-foe-and-back-again
- https://trustedsec.com/blog/command-line-underdog-wmic-in-action
- https://trustedsec.com/blog/wmi-for-script-kiddies

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_stdregprov_reg_modification.yml)
