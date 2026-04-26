---
sigma_id: "dc5c24af-6995-49b2-86eb-a9ff62199e82"
title: "COM Hijacking via TreatAs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_treatas_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_treatas_persistence.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "dc5c24af-6995-49b2-86eb-a9ff62199e82"
  - "COM Hijacking via TreatAs"
attack_technique_ids:
  - "T1546.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# COM Hijacking via TreatAs

Detect modification of TreatAs key to enable "rundll32.exe -sta" command

## Metadata

- Rule ID: dc5c24af-6995-49b2-86eb-a9ff62199e82
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-28
- Modified: 2025-07-11
- Source Path: rules/windows/registry/registry_set/registry_set_treatas_persistence.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Detection

```yaml
selection:
  TargetObject|endswith: TreatAs\(Default)
filter_office:
  Image|startswith: C:\Program Files\Common Files\Microsoft Shared\ClickToRun\
  Image|endswith: \OfficeClickToRun.exe
filter_office2:
  Image:
  - C:\Program Files\Microsoft Office\root\integration\integrator.exe
  - C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe
filter_svchost:
  Image: C:\Windows\system32\svchost.exe
filter_misexec:
  Image:
  - C:\Windows\system32\msiexec.exe
  - C:\Windows\SysWOW64\msiexec.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1546.015/T1546.015.md
- https://www.youtube.com/watch?v=3gz1QmiMhss&t=1251s

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_treatas_persistence.yml)
