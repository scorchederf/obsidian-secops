---
sigma_id: "a34f79a3-8e5f-4cc3-b765-de00695452c2"
title: "HackTool - PowerTool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_powertool.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_powertool.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a34f79a3-8e5f-4cc3-b765-de00695452c2"
  - "HackTool - PowerTool Execution"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - PowerTool Execution

Detects the execution of the tool PowerTool which has the ability to kill a process, delete its process file, unload drivers, and delete the driver files

## Metadata

- Rule ID: a34f79a3-8e5f-4cc3-b765-de00695452c2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-29
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_powertool.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
- Image|endswith:
  - \PowerTool.exe
  - \PowerTool64.exe
- OriginalFileName: PowerTool.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/
- https://www.trendmicro.com/en_us/research/22/i/play-ransomware-s-attack-playbook-unmasks-it-as-another-hive-aff.html
- https://twitter.com/gbti_sa/status/1249653895900602375?lang=en
- https://www.softpedia.com/get/Antivirus/Removal-Tools/ithurricane-PowerTool.shtml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_powertool.yml)
