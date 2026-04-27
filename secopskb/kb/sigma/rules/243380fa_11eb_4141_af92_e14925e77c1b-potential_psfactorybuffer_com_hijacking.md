---
sigma_id: "243380fa-11eb-4141-af92-e14925e77c1b"
title: "Potential PSFactoryBuffer COM Hijacking"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_comhijack_psfactorybuffer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_comhijack_psfactorybuffer.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "243380fa-11eb-4141-af92-e14925e77c1b"
  - "Potential PSFactoryBuffer COM Hijacking"
attack_technique_ids:
  - "T1546.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential PSFactoryBuffer COM Hijacking

Detects changes to the PSFactory COM InProcServer32 registry. This technique was used by RomCom to create persistence storing a malicious DLL.

## Metadata

- Rule ID: 243380fa-11eb-4141-af92-e14925e77c1b
- Status: test
- Level: high
- Author: BlackBerry Threat Research and Intelligence Team - @Joseliyo_Jstnk
- Date: 2023-06-07
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_comhijack_psfactorybuffer.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Detection

```yaml
selection:
  TargetObject|endswith: \CLSID\{c90250f3-4d7d-4991-9b69-a5c5bc1c2ae6}\InProcServer32\(Default)
filter_main:
  Details:
  - '%windir%\System32\ActXPrxy.dll'
  - C:\Windows\System32\ActXPrxy.dll
condition: selection and not filter_main
```

## False Positives

- Unknown

## References

- https://blogs.blackberry.com/en/2023/06/romcom-resurfaces-targeting-ukraine
- https://strontic.github.io/xcyclopedia/library/clsid_C90250F3-4D7D-4991-9B69-A5C5BC1C2AE6.html
- https://www.virustotal.com/gui/file/6d3ab9e729bb03ae8ae3fcd824474c5052a165de6cb4c27334969a542c7b261d/detection
- https://www.trendmicro.com/en_us/research/23/e/void-rabisu-s-use-of-romcom-backdoor-shows-a-growing-shift-in-th.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_comhijack_psfactorybuffer.yml)
