---
sigma_id: "7e3c4651-c347-40c4-b1d4-d48590fdf684"
title: "Code Injection by ld.so Preload"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_ldso_preload_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_ldso_preload_injection.yml"
build_date: "2026-04-26 17:03:18"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Code Injection by ld.so Preload

Detects the ld.so preload persistence file. See `man ld.so` for more information.

## Metadata

- Rule ID: 7e3c4651-c347-40c4-b1d4-d48590fdf684
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-05-05
- Modified: 2022-10-09
- Source Path: rules/linux/builtin/lnx_ldso_preload_injection.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.006]]

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
