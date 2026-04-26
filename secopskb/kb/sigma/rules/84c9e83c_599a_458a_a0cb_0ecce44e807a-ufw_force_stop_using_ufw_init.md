---
sigma_id: "84c9e83c-599a-458a-a0cb-0ecce44e807a"
title: "Ufw Force Stop Using Ufw-Init"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_disable_ufw.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_disable_ufw.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "84c9e83c-599a-458a-a0cb-0ecce44e807a"
  - "Ufw Force Stop Using Ufw-Init"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Ufw Force Stop Using Ufw-Init

Detects attempts to force stop the ufw using ufw-init

## Metadata

- Rule ID: 84c9e83c-599a-458a-a0cb-0ecce44e807a
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-01-18
- Source Path: rules/linux/process_creation/proc_creation_lnx_disable_ufw.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection_init:
  CommandLine|contains|all:
  - -ufw-init
  - force-stop
selection_ufw:
  CommandLine|contains|all:
  - ufw
  - disable
condition: 1 of selection_*
```

## False Positives

- Network administrators

## References

- https://blogs.blackberry.com/
- https://twitter.com/Joseliyo_Jstnk/status/1620131033474822144

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_disable_ufw.yml)
