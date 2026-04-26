---
sigma_id: "51cbac1e-eee3-4a90-b1b7-358efb81fa0a"
title: "Potential Windows Defender Tampering Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_namespace_defender.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_namespace_defender.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "51cbac1e-eee3-4a90-b1b7-358efb81fa0a"
  - "Potential Windows Defender Tampering Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Windows Defender Tampering Via Wmic.EXE

Detects potential tampering with Windows Defender settings such as adding exclusion using wmic

## Metadata

- Rule ID: 51cbac1e-eee3-4a90-b1b7-358efb81fa0a
- Status: test
- Level: high
- Author: frack113
- Date: 2022-12-11
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_namespace_defender.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection_img:
- OriginalFileName: wmic.exe
- Image|endswith: \WMIC.exe
selection_cli:
  CommandLine|contains: /Namespace:\\\\root\\Microsoft\\Windows\\Defender
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/5c1e6f1b4fafd01c8d1ece85f510160fc1275fbf/atomics/T1562.001/T1562.001.md
- https://www.bleepingcomputer.com/news/security/gootkit-malware-bypasses-windows-defender-by-setting-path-exclusions/
- https://www.bleepingcomputer.com/news/security/iobit-forums-hacked-to-spread-ransomware-to-its-members/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_namespace_defender.yml)
