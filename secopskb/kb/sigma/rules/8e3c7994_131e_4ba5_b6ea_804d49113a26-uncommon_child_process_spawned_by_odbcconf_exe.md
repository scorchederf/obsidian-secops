---
sigma_id: "8e3c7994-131e-4ba5-b6ea-804d49113a26"
title: "Uncommon Child Process Spawned By Odbcconf.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_uncommon_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_uncommon_child_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8e3c7994-131e-4ba5-b6ea-804d49113a26"
  - "Uncommon Child Process Spawned By Odbcconf.EXE"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Child Process Spawned By Odbcconf.EXE

Detects an uncommon child process of "odbcconf.exe" binary which normally shouldn't have any child processes.

## Metadata

- Rule ID: 8e3c7994-131e-4ba5-b6ea-804d49113a26
- Status: test
- Level: medium
- Author: Harjot Singh @cyb3rjy0t
- Date: 2023-05-22
- Source Path: rules/windows/process_creation/proc_creation_win_odbcconf_uncommon_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.008]]

## Detection

```yaml
selection:
  ParentImage|endswith: \odbcconf.exe
condition: selection
```

## False Positives

- In rare occurrences where "odbcconf" crashes. It might spawn a "werfault" process
- Other child processes will depend on the DLL being registered by actions like "regsvr". In case where the DLLs have external calls (which should be rare). Other child processes might spawn and additional filters need to be applied.

## References

- https://learn.microsoft.com/en-us/sql/odbc/odbcconf-exe?view=sql-server-ver16
- https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/
- https://medium.com/@cyberjyot/t1218-008-dll-execution-using-odbcconf-exe-803fa9e08dac

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_uncommon_child_process.yml)
