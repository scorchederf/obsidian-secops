---
sigma_id: "a1b1fd53-9c4a-444c-bae0-34a330fc7aa8"
title: "Potential Persistence Via DLLPathOverride"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_natural_language.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_natural_language.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "a1b1fd53-9c4a-444c-bae0-34a330fc7aa8"
  - "Potential Persistence Via DLLPathOverride"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via DLLPathOverride

Detects when an attacker adds a new "DLLPathOverride" value to the "Natural Language" key in order to achieve persistence which will get invoked by "SearchIndexer.exe" process

## Metadata

- Rule ID: a1b1fd53-9c4a-444c-bae0-34a330fc7aa8
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_natural_language.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection_root:
  TargetObject|contains: \SYSTEM\CurrentControlSet\Control\ContentIndex\Language\
selection_values:
  TargetObject|contains:
  - \StemmerDLLPathOverride
  - \WBDLLPathOverride
  - \StemmerClass
  - \WBreakerClass
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://persistence-info.github.io/Data/naturallanguage6.html
- https://www.hexacorn.com/blog/2018/12/30/beyond-good-ol-run-key-part-98/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_natural_language.yml)
