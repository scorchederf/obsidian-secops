---
sigma_id: "b7916c2a-fa2f-4795-9477-32b731f70f11"
title: "Registry Persistence via Explorer Run Key"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_reg_persist_explorer_run.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_reg_persist_explorer_run.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "b7916c2a-fa2f-4795-9477-32b731f70f11"
  - "Registry Persistence via Explorer Run Key"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Registry Persistence via Explorer Run Key

Detects a possible persistence mechanism using RUN key for Windows Explorer and pointing to a suspicious folder

## Metadata

- Rule ID: b7916c2a-fa2f-4795-9477-32b731f70f11
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), oscd.community
- Date: 2018-07-18
- Modified: 2023-12-11
- Source Path: rules/windows/registry/registry_set/registry_set_susp_reg_persist_explorer_run.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
  Details|contains:
  - :\$Recycle.bin\
  - :\ProgramData\
  - :\Temp\
  - :\Users\Default\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
condition: selection
```

## False Positives

- Unknown

## References

- https://researchcenter.paloaltonetworks.com/2018/07/unit42-upatre-continues-evolve-new-anti-analysis-techniques/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_reg_persist_explorer_run.yml)
