---
atomic_guid: "a960185f-aef6-4547-8350-d1ce16680d09"
title: "Detect Virtualization Environment via ioreg"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "a960185f-aef6-4547-8350-d1ce16680d09"
  - "Detect Virtualization Environment via ioreg"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

ioreg contains registry entries for all the device drivers in the system. If it's a virtual machine, one of the device manufacturer will be a Virtualization Software.

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
if (ioreg -l | grep -e Manufacturer -e 'Vendor Name' | grep -iE 'Oracle|VirtualBox|VMWare|Parallels') then echo 'Virtualization Environment detected'; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
