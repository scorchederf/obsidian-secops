---
sigma_id: "f548a603-c9f2-4c89-b511-b089f7e94549"
title: "Potential Persistence Via Microsoft Compatibility Appraiser"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_persistence_windows_telemetry.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_persistence_windows_telemetry.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f548a603-c9f2-4c89-b511-b089f7e94549"
  - "Potential Persistence Via Microsoft Compatibility Appraiser"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Microsoft Compatibility Appraiser

Detects manual execution of the "Microsoft Compatibility Appraiser" task via schtasks.
In order to trigger persistence stored in the "\AppCompatFlags\TelemetryController" registry key.

## Metadata

- Rule ID: f548a603-c9f2-4c89-b511-b089f7e94549
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-09-29
- Modified: 2023-02-10
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_persistence_windows_telemetry.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_cli:
  CommandLine|contains|all:
  - 'run '
  - \Application Experience\Microsoft Compatibility Appraiser
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.trustedsec.com/blog/abusing-windows-telemetry-for-persistence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_persistence_windows_telemetry.yml)
