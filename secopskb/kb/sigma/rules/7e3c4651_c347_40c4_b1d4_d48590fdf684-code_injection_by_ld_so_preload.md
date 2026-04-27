---
sigma_id: "7e3c4651-c347-40c4-b1d4-d48590fdf684"
title: "Code Injection by ld.so Preload"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_ldso_preload_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_ldso_preload_injection.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "7e3c4651-c347-40c4-b1d4-d48590fdf684"
  - "Code Injection by ld.so Preload"
attack_technique_ids:
  - "T1574.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the ld.so preload persistence file. See `man ld.so` for more information.

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574006-dynamic-linker-hijacking|T1574.006: Dynamic Linker Hijacking]]

## Detection

```yaml
keywords:
- /etc/ld.so.preload
condition: keywords
```

## False Positives

- Rare temporary workaround for library misconfiguration

## References

- https://man7.org/linux/man-pages/man8/ld.so.8.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_ldso_preload_injection.yml)
