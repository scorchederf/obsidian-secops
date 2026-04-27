---
atomic_guid: "e04d2e89-de15-4d90-92f9-a335c7337f0f"
title: "Detect Virtualization Environment using system_profiler"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "e04d2e89-de15-4d90-92f9-a335c7337f0f"
  - "Detect Virtualization Environment using system_profiler"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

system_profiler provides system hardware and software configuration and the Model Identifier should provide the value similar to (sysctl -n hw.model). 
We should be able to find whether virtualization is enabled by checking whether the Model Identifier does not contain "Mac".

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]

## Executor

- name: sh

### Command

```bash
if [ "$(system_profiler SPHardwareDataType | grep "Model Identifier" | grep -v 'Mac')" != "" ]; then echo 'Virtualization Environment detected'; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
