---
sigma_id: "b99a1518-1ad5-4f65-bc95-1ffff97a8fd0"
title: "HackTool - Inveigh Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_inveigh.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_inveigh.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "b99a1518-1ad5-4f65-bc95-1ffff97a8fd0"
  - "HackTool - Inveigh Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of Inveigh a cross-platform .NET IPv4/IPv6 machine-in-the-middle tool

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
- Image|endswith: \Inveigh.exe
- OriginalFileName:
  - \Inveigh.exe
  - \Inveigh.dll
- Description: Inveigh
- CommandLine|contains:
  - ' -SpooferIP'
  - ' -ReplyToIPs '
  - ' -ReplyToDomains '
  - ' -ReplyToMACs '
  - ' -SnifferIP'
condition: selection
```

## False Positives

- Very unlikely

## References

- https://github.com/Kevin-Robertson/Inveigh
- https://thedfirreport.com/2020/11/23/pysa-mespinoza-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_inveigh.yml)
