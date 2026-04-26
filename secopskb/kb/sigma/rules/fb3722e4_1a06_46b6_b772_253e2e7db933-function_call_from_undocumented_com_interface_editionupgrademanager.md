---
sigma_id: "fb3722e4-1a06-46b6-b772-253e2e7db933"
title: "Function Call From Undocumented COM Interface EditionUpgradeManager"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_uac_bypass_editionupgrademanagerobj.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_uac_bypass_editionupgrademanagerobj.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_access"
aliases:
  - "fb3722e4-1a06-46b6-b772-253e2e7db933"
  - "Function Call From Undocumented COM Interface EditionUpgradeManager"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Function Call From Undocumented COM Interface EditionUpgradeManager

Detects function calls from the EditionUpgradeManager COM interface. Which is an interface that is not used by standard executables.

## Metadata

- Rule ID: fb3722e4-1a06-46b6-b772-253e2e7db933
- Status: test
- Level: medium
- Author: oscd.community, Dmitry Uchakin
- Date: 2020-10-07
- Modified: 2023-11-30
- Source Path: rules/windows/process_access/proc_access_win_uac_bypass_editionupgrademanagerobj.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  CallTrace|contains: editionupgrademanagerobj.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://www.snip2code.com/Snippet/4397378/UAC-bypass-using-EditionUpgradeManager-C/
- https://gist.github.com/hfiref0x/de9c83966623236f5ebf8d9ae2407611

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_uac_bypass_editionupgrademanagerobj.yml)
