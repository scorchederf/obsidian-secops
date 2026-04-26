---
sigma_id: "821bcf4d-46c7-4b87-bc57-9509d3ba7c11"
title: "Root Account Enable Via Dsenableroot"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_dsenableroot_enable_root_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_dsenableroot_enable_root_account.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "821bcf4d-46c7-4b87-bc57-9509d3ba7c11"
  - "Root Account Enable Via Dsenableroot"
attack_technique_ids:
  - "T1078"
  - "T1078.001"
  - "T1078.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Root Account Enable Via Dsenableroot

Detects attempts to enable the root account via "dsenableroot"

## Metadata

- Rule ID: 821bcf4d-46c7-4b87-bc57-9509d3ba7c11
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-08-22
- Source Path: rules/macos/process_creation/proc_creation_macos_dsenableroot_enable_root_account.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.001]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Detection

```yaml
selection:
  Image|endswith: /dsenableroot
filter_main_disable:
  CommandLine|contains: ' -d '
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/b27a3cb25025161d49ac861cb216db68c46a3537/atomics/T1078.003/T1078.003.md
- https://github.com/elastic/detection-rules/blob/4312d8c9583be524578a14fe6295c3370b9a9307/rules/macos/persistence_enable_root_account.toml
- https://ss64.com/osx/dsenableroot.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_dsenableroot_enable_root_account.yml)
