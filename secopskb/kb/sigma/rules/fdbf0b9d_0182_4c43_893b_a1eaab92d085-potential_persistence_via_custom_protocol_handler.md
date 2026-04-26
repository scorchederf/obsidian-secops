---
sigma_id: "fdbf0b9d-0182-4c43-893b-a1eaab92d085"
title: "Potential Persistence Via Custom Protocol Handler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_custom_protocol_handler.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_custom_protocol_handler.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "fdbf0b9d-0182-4c43-893b-a1eaab92d085"
  - "Potential Persistence Via Custom Protocol Handler"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Custom Protocol Handler

Detects potential persistence activity via the registering of a new custom protocole handlers. While legitimate applications register protocole handlers often times during installation. And attacker can abuse this by setting a custom handler to be used as a persistence mechanism.

## Metadata

- Rule ID: fdbf0b9d-0182-4c43-893b-a1eaab92d085
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-05-30
- Modified: 2023-05-12
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_custom_protocol_handler.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|startswith: HKCR\
  Details|startswith: 'URL:'
filter_main_ms_trusted:
  Details|startswith: URL:ms-
filter_main_generic_locations:
  Image|startswith:
  - C:\Program Files (x86)
  - C:\Program Files\
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Many legitimate applications can register a new custom protocol handler. Additional filters needs to applied according to your environment.

## References

- https://ladydebug.com/blog/2019/06/21/custom-protocol-handler-cph/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_custom_protocol_handler.yml)
