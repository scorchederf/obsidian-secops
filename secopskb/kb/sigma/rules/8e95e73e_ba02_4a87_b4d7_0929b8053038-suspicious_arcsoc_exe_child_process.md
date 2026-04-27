---
sigma_id: "8e95e73e-ba02-4a87-b4d7-0929b8053038"
title: "Suspicious ArcSOC.exe Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_arcsoc_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_arcsoc_susp_child_process.yml"
build_date: "2026-04-26 17:03:22"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8e95e73e-ba02-4a87-b4d7-0929b8053038"
  - "Suspicious ArcSOC.exe Child Process"
attack_technique_ids:
  - "T1059"
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious ArcSOC.exe Child Process

Detects script interpreters, command-line tools, and similar suspicious child processes of ArcSOC.exe.
ArcSOC.exe is the process name which hosts ArcGIS Server REST services. If an attacker compromises an ArcGIS
Server system and uploads a malicious Server Object Extension (SOE), they can send crafted requests to the corresponding
service endpoint and remotely execute code from the ArcSOC.exe process.

## Metadata

- Rule ID: 8e95e73e-ba02-4a87-b4d7-0929b8053038
- Status: experimental
- Level: high
- Author: Micah Babinski
- Date: 2025-11-25
- Source Path: rules/windows/process_creation/proc_creation_win_arcsoc_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]

## Detection

```yaml
selection:
  ParentImage|endswith: \ArcSOC.exe
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wmic.exe
  - \wscript.exe
filter_main_cmd:
  Image|endswith: \cmd.exe
  CommandLine: cmd.exe /c "ver"
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://reliaquest.com/blog/threat-spotlight-inside-flax-typhoons-arcgis-compromise/
- https://enterprise.arcgis.com/en/server/12.0/administer/windows/inside-an-arcgis-server-site.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_arcsoc_susp_child_process.yml)
