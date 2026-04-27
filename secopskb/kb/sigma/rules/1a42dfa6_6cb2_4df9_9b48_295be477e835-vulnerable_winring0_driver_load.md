---
sigma_id: "1a42dfa6-6cb2-4df9-9b48-295be477e835"
title: "Vulnerable WinRing0 Driver Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_vuln_winring0_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_vuln_winring0_driver.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "windows / driver_load"
aliases:
  - "1a42dfa6-6cb2-4df9-9b48-295be477e835"
  - "Vulnerable WinRing0 Driver Load"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the load of a signed WinRing0 driver often used by threat actors, crypto miners (XMRIG) or malware for privilege escalation

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]

## Detection

```yaml
selection:
- Hashes|contains: IMPHASH=D41FA95D4642DC981F10DE36F4DC8CD7
- ImageLoaded|endswith:
  - \WinRing0x64.sys
  - \WinRing0.sys
  - \WinRing0.dll
  - \WinRing0x64.dll
  - \winring00x64.sys
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/xmrig/xmrig/tree/master/bin/WinRing0
- https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_vuln_winring0_driver.yml)
