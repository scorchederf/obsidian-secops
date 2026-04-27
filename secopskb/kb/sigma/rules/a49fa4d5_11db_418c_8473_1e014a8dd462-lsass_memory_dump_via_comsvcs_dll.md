---
sigma_id: "a49fa4d5-11db-418c-8473-1e014a8dd462"
title: "Lsass Memory Dump via Comsvcs DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_dump_comsvcs_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_dump_comsvcs_dll.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "a49fa4d5-11db-418c-8473-1e014a8dd462"
  - "Lsass Memory Dump via Comsvcs DLL"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects adversaries leveraging the MiniDump export function from comsvcs.dll via rundll32 to perform a memory dump from lsass.

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
  TargetImage|endswith: \lsass.exe
  SourceImage|endswith: \rundll32.exe
  CallTrace|contains: comsvcs.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/shantanukhande/status/1229348874298388484
- https://modexp.wordpress.com/2019/08/30/minidumpwritedump-via-com-services-dll/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_dump_comsvcs_dll.yml)
