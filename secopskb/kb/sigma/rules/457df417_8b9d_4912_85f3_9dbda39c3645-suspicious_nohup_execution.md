---
sigma_id: "457df417-8b9d-4912-85f3-9dbda39c3645"
title: "Suspicious Nohup Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_nohup_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_nohup_susp_execution.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "457df417-8b9d-4912-85f3-9dbda39c3645"
  - "Suspicious Nohup Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of binaries located in potentially suspicious locations via "nohup"

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|endswith: /nohup
  CommandLine|contains: /tmp/
condition: selection
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_nohup_susp_execution.yml)
