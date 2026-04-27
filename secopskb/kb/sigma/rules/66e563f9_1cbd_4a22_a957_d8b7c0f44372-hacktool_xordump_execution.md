---
sigma_id: "66e563f9-1cbd-4a22-a957-d8b7c0f44372"
title: "HackTool - XORDump Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_xordump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_xordump.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "66e563f9-1cbd-4a22-a957-d8b7c0f44372"
  - "HackTool - XORDump Execution"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious use of XORDump process memory dumping utility

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
- Image|endswith: \xordump.exe
- CommandLine|contains:
  - ' -process lsass.exe '
  - ' -m comsvcs '
  - ' -m dbghelp '
  - ' -m dbgcore '
condition: selection
```

## False Positives

- Another tool that uses the command line switches of XORdump

## References

- https://github.com/audibleblink/xordump

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_xordump.yml)
