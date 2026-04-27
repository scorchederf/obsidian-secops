---
atomic_guid: "502a7dc4-9d6f-4d28-abf2-f0e84692562d"
title: "Detect Virtualization Environment (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "502a7dc4-9d6f-4d28-abf2-f0e84692562d"
  - "Detect Virtualization Environment (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Management Instrumentation(WMI) objects contains system information which helps to detect virtualization. This command will specifically attempt to get the CurrentTemperature value from this object and will check to see if the attempt results in an error that contains the word supported. This is meant to find the result of Not supported, which is the result if run in a virtual machine

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$error.clear()
Get-WmiObject -Query "SELECT * FROM MSAcpi_ThermalZoneTemperature" -ErrorAction SilentlyContinue
if($error) {echo "Virtualization Environment detected"}
```

### Cleanup

```powershell
$error.clear()
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
