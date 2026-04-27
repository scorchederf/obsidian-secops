---
atomic_guid: "aefd6866-d753-431f-a7a4-215ca7e3f13d"
title: "New shim database files created in the default shim database directory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.011"
attack_technique_name: "Event Triggered Execution: Application Shimming"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.011/T1546.011.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "aefd6866-d753-431f-a7a4-215ca7e3f13d"
  - "New shim database files created in the default shim database directory"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# New shim database files created in the default shim database directory

Upon execution, check the "C:\Windows\apppatch\Custom\" folder for the new shim database

https://www.fireeye.com/blog/threat-research/2017/05/fin7-shim-databases-persistence.html

## Metadata

- Atomic GUID: aefd6866-d753-431f-a7a4-215ca7e3f13d
- Technique: T1546.011: Event Triggered Execution: Application Shimming
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1546.011/T1546.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item "$PathToAtomicsFolder\T1546.011\bin\T1546.011CompatDatabase.sdb" C:\Windows\apppatch\Custom\T1546.011CompatDatabase.sdb
Copy-Item "$PathToAtomicsFolder\T1546.011\bin\T1546.011CompatDatabase.sdb" C:\Windows\apppatch\Custom\Custom64\T1546.011CompatDatabase.sdb
```

### Cleanup

```powershell
Remove-Item C:\Windows\apppatch\Custom\T1546.011CompatDatabase.sdb -ErrorAction Ignore
Remove-Item C:\Windows\apppatch\Custom\Custom64\T1546.011CompatDatabase.sdb -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.011/T1546.011.yaml)
