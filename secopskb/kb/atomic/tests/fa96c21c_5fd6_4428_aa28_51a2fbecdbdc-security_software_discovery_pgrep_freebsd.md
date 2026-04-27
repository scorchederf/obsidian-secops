---
atomic_guid: "fa96c21c-5fd6-4428-aa28-51a2fbecdbdc"
title: "Security Software Discovery - pgrep (FreeBSD)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "fa96c21c-5fd6-4428-aa28-51a2fbecdbdc"
  - "Security Software Discovery - pgrep (FreeBSD)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Security Software Discovery - pgrep (FreeBSD)

Methods to identify Security Software on an endpoint
when sucessfully executed, command shell is going to display AV/Security software it is running.

## Metadata

- Atomic GUID: fa96c21c-5fd6-4428-aa28-51a2fbecdbdc
- Technique: T1518.001: Software Discovery: Security Software Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1518.001/T1518.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Executor

- name: sh

### Command

```bash
pgrep -l 'bareos-fd|icinga2|cbagentd|wazuh-agent|packetbeat|filebeat|osqueryd'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
