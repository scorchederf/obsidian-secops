---
atomic_guid: "d304b2dc-90b4-4465-a650-16ddd503f7b5"
title: "Overwrite Linux Log"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "d304b2dc-90b4-4465-a650-16ddd503f7b5"
  - "Overwrite Linux Log"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Overwrite Linux Log

This test overwrites the specified log. This technique was used by threat actor Rocke during the exploitation of Linux web servers.

## Metadata

- Atomic GUID: d304b2dc-90b4-4465-a650-16ddd503f7b5
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Input Arguments

### log_path

- description: Path of specified log
- type: path
- default: /var/log/secure

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo 0> #{log_path}
```

### Cleanup

```bash
if [ "/var/log/secure" != "#{log_path}" ] ; then rm -f #{log_path} ; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
