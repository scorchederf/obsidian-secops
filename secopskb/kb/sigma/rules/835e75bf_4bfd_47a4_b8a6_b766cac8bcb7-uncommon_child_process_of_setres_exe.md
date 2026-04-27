---
sigma_id: "835e75bf-4bfd-47a4-b8a6-b766cac8bcb7"
title: "Uncommon Child Process Of Setres.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_setres_uncommon_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_setres_uncommon_child_process.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "835e75bf-4bfd-47a4-b8a6-b766cac8bcb7"
  - "Uncommon Child Process Of Setres.EXE"
attack_technique_ids:
  - "T1218"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects uncommon child process of Setres.EXE.
Setres.EXE is a Windows server only process and tool that can be used to set the screen resolution.
It can potentially be abused in order to launch any arbitrary file with a name containing the word "choice" from the current execution path.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detection

```yaml
selection:
  ParentImage|endswith: \setres.exe
  Image|contains: \choice
filter_main_legit_location:
  Image|endswith:
  - C:\Windows\System32\choice.exe
  - C:\Windows\SysWOW64\choice.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://lolbas-project.github.io/lolbas/Binaries/Setres/
- https://twitter.com/0gtweet/status/1583356502340870144
- https://strontic.github.io/xcyclopedia/library/setres.exe-0E30E4C09637D7A128A37B59A3BC4D09.html
- https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731033(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_setres_uncommon_child_process.yml)
