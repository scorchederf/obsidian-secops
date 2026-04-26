---
sigma_id: "48917adc-a28e-4f5d-b729-11e75da8941f"
title: "Suspicious Windows Defender Folder Exclusion Added Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_defender_exclusion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_defender_exclusion.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "48917adc-a28e-4f5d-b729-11e75da8941f"
  - "Suspicious Windows Defender Folder Exclusion Added Via Reg.EXE"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Windows Defender Folder Exclusion Added Via Reg.EXE

Detects the usage of "reg.exe" to add Defender folder exclusions. Qbot has been seen using this technique to add exclusions for folders within AppData and ProgramData.

## Metadata

- Rule ID: 48917adc-a28e-4f5d-b729-11e75da8941f
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-13
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_reg_defender_exclusion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  Image|endswith: \reg.exe
  CommandLine|contains:
  - SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths
  - SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths
  CommandLine|contains|all:
  - 'ADD '
  - '/t '
  - 'REG_DWORD '
  - '/v '
  - '/d '
  - '0'
condition: selection
```

## False Positives

- Legitimate use

## References

- https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/
- https://redcanary.com/threat-detection-report/threats/qbot/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_defender_exclusion.yml)
