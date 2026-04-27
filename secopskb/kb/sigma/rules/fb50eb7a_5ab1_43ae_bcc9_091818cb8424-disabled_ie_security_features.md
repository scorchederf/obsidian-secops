---
sigma_id: "fb50eb7a-5ab1-43ae-bcc9-091818cb8424"
title: "Disabled IE Security Features"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_disable_ie_features.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_disable_ie_features.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fb50eb7a-5ab1-43ae-bcc9-091818cb8424"
  - "Disabled IE Security Features"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects command lines that indicate unwanted modifications to registry keys that disable important Internet Explorer security features

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection1:
  CommandLine|contains|all:
  - ' -name IEHarden '
  - ' -value 0 '
selection2:
  CommandLine|contains|all:
  - ' -name DEPOff '
  - ' -value 1 '
selection3:
  CommandLine|contains|all:
  - ' -name DisableFirstRunCustomize '
  - ' -value 2 '
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://unit42.paloaltonetworks.com/operation-ke3chang-resurfaces-with-new-tidepool-malware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_disable_ie_features.yml)
