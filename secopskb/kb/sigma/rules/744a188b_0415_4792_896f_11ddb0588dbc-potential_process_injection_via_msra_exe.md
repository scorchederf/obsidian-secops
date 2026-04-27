---
sigma_id: "744a188b-0415-4792-896f-11ddb0588dbc"
title: "Potential Process Injection Via Msra.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msra_process_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msra_process_injection.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "744a188b-0415-4792-896f-11ddb0588dbc"
  - "Potential Process Injection Via Msra.EXE"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential process injection via Microsoft Remote Asssistance (Msra.exe) by looking at suspicious child processes spawned from the aforementioned process. It has been a target used by many threat actors and used for discovery and persistence tactics

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

## Detection

```yaml
selection:
  ParentImage|endswith: \msra.exe
  ParentCommandLine|endswith: msra.exe
  Image|endswith:
  - \arp.exe
  - \cmd.exe
  - \net.exe
  - \netstat.exe
  - \nslookup.exe
  - \route.exe
  - \schtasks.exe
  - \whoami.exe
condition: selection
```

## False Positives

- Legitimate use of Msra.exe

## References

- https://www.microsoft.com/security/blog/2021/12/09/a-closer-look-at-qakbots-latest-building-blocks-and-how-to-knock-them-down/
- https://www.fortinet.com/content/dam/fortinet/assets/analyst-reports/ar-qakbot.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msra_process_injection.yml)
