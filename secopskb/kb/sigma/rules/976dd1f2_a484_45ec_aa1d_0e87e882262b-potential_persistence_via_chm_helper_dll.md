---
sigma_id: "976dd1f2-a484-45ec-aa1d-0e87e882262b"
title: "Potential Persistence Via CHM Helper DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_chm.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_chm.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "976dd1f2-a484-45ec-aa1d-0e87e882262b"
  - "Potential Persistence Via CHM Helper DLL"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Persistence Via CHM Helper DLL

Detects when an attacker modifies the registry key "HtmlHelp Author" to achieve persistence

## Metadata

- Rule ID: 976dd1f2-a484-45ec-aa1d-0e87e882262b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_chm.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Software\Microsoft\HtmlHelp Author\Location
  - \Software\WOW6432Node\Microsoft\HtmlHelp Author\Location
condition: selection
```

## False Positives

- Unknown

## References

- https://persistence-info.github.io/Data/htmlhelpauthor.html
- https://www.hexacorn.com/blog/2018/04/22/beyond-good-ol-run-key-part-76/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_chm.yml)
