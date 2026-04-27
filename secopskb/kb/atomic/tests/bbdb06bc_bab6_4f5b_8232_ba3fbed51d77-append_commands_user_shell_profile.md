---
atomic_guid: "bbdb06bc-bab6-4f5b-8232-ba3fbed51d77"
title: "Append commands user shell profile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.004"
attack_technique_name: "Event Triggered Execution: .bash_profile .bashrc and .shrc"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "bbdb06bc-bab6-4f5b-8232-ba3fbed51d77"
  - "Append commands user shell profile"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Append commands user shell profile

An adversary may wish to establish persistence by executing malicious commands from the users ~/.profile every time the "user" logs in.

## Metadata

- Atomic GUID: bbdb06bc-bab6-4f5b-8232-ba3fbed51d77
- Technique: T1546.004: Event Triggered Execution: .bash_profile .bashrc and .shrc
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1546.004/T1546.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.004]]

## Input Arguments

### text_to_append

- description: Text to append to the ~/.profile file
- type: string
- default: # Atomic Red Team was here... T1546.004

## Executor

- elevation_required: False
- name: sh

### Command

```bash
echo '#{text_to_append}' >> ~/.profile
```

### Cleanup

```bash
sed -i "s/# Atomic Red Team was here... T1546.004//" ~/.profile
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml)
