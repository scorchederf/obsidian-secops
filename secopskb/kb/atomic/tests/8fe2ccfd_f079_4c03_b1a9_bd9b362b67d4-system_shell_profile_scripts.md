---
atomic_guid: "8fe2ccfd-f079-4c03-b1a9-bd9b362b67d4"
title: "System shell profile scripts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.004"
attack_technique_name: "Event Triggered Execution: .bash_profile .bashrc and .shrc"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "8fe2ccfd-f079-4c03-b1a9-bd9b362b67d4"
  - "System shell profile scripts"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may wish to establish persistence by adding commands into any of the script files in the /etc/profile.d/ directory, which are executed every time "any" user logs in.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]]

## Input Arguments

### text_to_append

- description: Text to append to the /etc/profile.d/bash_completion.sh file
- type: string
- default: # Atomic Red Team was here... T1546.004

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo '#{text_to_append}' >> /etc/profile.d/bash_completion.sh
```

### Cleanup

```bash
sed -i "s/# Atomic Red Team was here... T1546.004//" /etc/profile.d/bash_completion.sh
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml)
