---
atomic_guid: "8f2a5d2b-4018-46d4-8f3f-0fea53754690"
title: "System Service Discovery - Linux init scripts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "8f2a5d2b-4018-46d4-8f3f-0fea53754690"
  - "System Service Discovery - Linux init scripts"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# System Service Discovery - Linux init scripts

Enumerates system services by listing SysV init scripts and runlevel
symlinks under /etc/init.d and /etc/rc*.d.

## Metadata

- Atomic GUID: 8f2a5d2b-4018-46d4-8f3f-0fea53754690
- Technique: T1007: System Service Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1007/T1007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Executor

- name: sh

### Command

```bash
echo "[*] Listing SysV init scripts (/etc/init.d):"
if [ -d /etc/init.d ]; then ls -l /etc/init.d; else echo "/etc/init.d not present on this system"; fi
echo
echo "[*] Listing runlevel directories (/etc/rc*.d):"
ls -ld /etc/rc*.d 2>/dev/null || echo "No /etc/rc*.d directories found"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
