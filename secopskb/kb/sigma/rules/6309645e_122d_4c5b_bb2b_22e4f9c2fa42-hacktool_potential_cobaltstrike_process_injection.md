---
sigma_id: "6309645e-122d-4c5b-bb2b-22e4f9c2fa42"
title: "HackTool - Potential CobaltStrike Process Injection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_hktl_cobaltstrike.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_hktl_cobaltstrike.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "6309645e-122d-4c5b-bb2b-22e4f9c2fa42"
  - "HackTool - Potential CobaltStrike Process Injection"
attack_technique_ids:
  - "T1055.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a potential remote threat creation with certain characteristics which are typical for Cobalt Strike beacons

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]

## Detection

```yaml
selection:
  StartAddress|endswith:
  - 0B80
  - 0C7C
  - 0C88
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/@olafhartong/cobalt-strike-remote-threads-detection-206372d11d0f
- https://blog.cobaltstrike.com/2018/04/09/cobalt-strike-3-11-the-snake-that-eats-its-tail/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_hktl_cobaltstrike.yml)
