---
sigma_id: "ec52985a-d024-41e3-8ff6-14169039a0b3"
title: "Mount Execution With Hidepid Parameter"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_mount_hidepid.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_mount_hidepid.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "ec52985a-d024-41e3-8ff6-14169039a0b3"
  - "Mount Execution With Hidepid Parameter"
attack_technique_ids:
  - "T1564"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Mount Execution With Hidepid Parameter

Detects execution of the "mount" command with "hidepid" parameter to make invisible processes to other users from the system

## Metadata

- Rule ID: ec52985a-d024-41e3-8ff6-14169039a0b3
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-01-12
- Source Path: rules/linux/process_creation/proc_creation_lnx_mount_hidepid.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Detection

```yaml
selection:
  Image|endswith: /mount
  CommandLine|contains|all:
  - hidepid=2
  - ' -o '
condition: selection
```

## False Positives

- Unknown

## References

- https://blogs.blackberry.com/
- https://www.cyberciti.biz/faq/linux-hide-processes-from-other-users/
- https://twitter.com/Joseliyo_Jstnk/status/1620131033474822144

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_mount_hidepid.yml)
