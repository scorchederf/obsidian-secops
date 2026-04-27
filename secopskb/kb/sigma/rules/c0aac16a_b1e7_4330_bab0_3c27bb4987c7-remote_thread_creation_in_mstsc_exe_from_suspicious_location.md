---
sigma_id: "c0aac16a-b1e7-4330-bab0-3c27bb4987c7"
title: "Remote Thread Creation In Mstsc.Exe From Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_mstsc_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_mstsc_susp_location.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "c0aac16a-b1e7-4330-bab0-3c27bb4987c7"
  - "Remote Thread Creation In Mstsc.Exe From Suspicious Location"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote thread creation in the "mstsc.exe" process by a process located in a potentially suspicious location.
This technique is often used by attackers in order to hook some APIs used by DLLs loaded by "mstsc.exe" during RDP authentications in order to steal credentials.

## Logsource

- category: create_remote_thread
- product: windows

## Detection

```yaml
selection:
  TargetImage|endswith: \mstsc.exe
  SourceImage|contains:
  - :\Temp\
  - :\Users\Public\
  - :\Windows\PerfLogs\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/S12cybersecurity/RDPCredentialStealer/blob/1b8947cdd065a06c1b62e80967d3c7af895fcfed/APIHookInjectorBin/APIHookInjectorBin/Inject.h#L25

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_mstsc_susp_location.yml)
