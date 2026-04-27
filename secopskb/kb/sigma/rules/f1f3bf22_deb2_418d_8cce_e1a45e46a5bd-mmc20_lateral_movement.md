---
sigma_id: "f1f3bf22-deb2-418d-8cce-e1a45e46a5bd"
title: "MMC20 Lateral Movement"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mmc_mmc20_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_mmc20_lateral_movement.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f1f3bf22-deb2-418d-8cce-e1a45e46a5bd"
  - "MMC20 Lateral Movement"
attack_technique_ids:
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects MMC20.Application Lateral Movement; specifically looks for the spawning of the parent MMC.exe with a command line of "-Embedding" as a child of svchost.exe

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]

## Detection

```yaml
selection:
  ParentImage|endswith: \svchost.exe
  Image|endswith: \mmc.exe
  CommandLine|contains: -Embedding
condition: selection
```

## False Positives

- Unlikely

## References

- https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-object/
- https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view?usp=sharing

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_mmc20_lateral_movement.yml)
