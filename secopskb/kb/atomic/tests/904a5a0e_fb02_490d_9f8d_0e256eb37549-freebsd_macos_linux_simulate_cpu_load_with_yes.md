---
atomic_guid: "904a5a0e-fb02-490d-9f8d-0e256eb37549"
title: "FreeBSD/macOS/Linux - Simulate CPU Load with Yes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1496"
attack_technique_name: "Resource Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1496/T1496.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "904a5a0e-fb02-490d-9f8d-0e256eb37549"
  - "FreeBSD/macOS/Linux - Simulate CPU Load with Yes"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# FreeBSD/macOS/Linux - Simulate CPU Load with Yes

This test simulates a high CPU load as you might observe during cryptojacking attacks.
End the test by using CTRL/CMD+C to break.

## Metadata

- Atomic GUID: 904a5a0e-fb02-490d-9f8d-0e256eb37549
- Technique: T1496: Resource Hijacking
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1496/T1496.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1496-resource_hijacking|T1496]]

## Executor

- name: sh

### Command

```bash
yes > /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1496/T1496.yaml)
