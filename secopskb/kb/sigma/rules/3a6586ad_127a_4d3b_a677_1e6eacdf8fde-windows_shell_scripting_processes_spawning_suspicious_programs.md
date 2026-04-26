---
sigma_id: "3a6586ad-127a-4d3b-a677-1e6eacdf8fde"
title: "Windows Shell/Scripting Processes Spawning Suspicious Programs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_shell_spawn_susp_program.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_shell_spawn_susp_program.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "3a6586ad-127a-4d3b-a677-1e6eacdf8fde"
  - "Windows Shell/Scripting Processes Spawning Suspicious Programs"
attack_technique_ids:
  - "T1059.005"
  - "T1059.001"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Shell/Scripting Processes Spawning Suspicious Programs

Detects suspicious child processes of a Windows shell and scripting processes such as wscript, rundll32, powershell, mshta...etc.

## Metadata

- Rule ID: 3a6586ad-127a-4d3b-a677-1e6eacdf8fde
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Tim Shelton
- Date: 2018-04-06
- Modified: 2023-05-23
- Source Path: rules/windows/process_creation/proc_creation_win_susp_shell_spawn_susp_program.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \rundll32.exe
  - \cscript.exe
  - \wscript.exe
  - \wmiprvse.exe
  - \regsvr32.exe
  Image|endswith:
  - \schtasks.exe
  - \nslookup.exe
  - \certutil.exe
  - \bitsadmin.exe
  - \mshta.exe
filter_ccmcache:
  CurrentDirectory|contains: \ccmcache\
filter_amazon:
  ParentCommandLine|contains:
  - \Program Files\Amazon\WorkSpacesConfig\Scripts\setup-scheduledtask.ps1
  - \Program Files\Amazon\WorkSpacesConfig\Scripts\set-selfhealing.ps1
  - \Program Files\Amazon\WorkSpacesConfig\Scripts\check-workspacehealth.ps1
  - \nessus_
filter_nessus:
  CommandLine|contains: \nessus_
filter_sccm_install:
  ParentImage|endswith: \mshta.exe
  Image|endswith: \mshta.exe
  ParentCommandLine|contains|all:
  - C:\MEM_Configmgr_
  - \splash.hta
  - '{1E460BD7-F1C3-4B2E-88BF-4E770A288AF5}'
  CommandLine|contains|all:
  - C:\MEM_Configmgr_
  - \SMSSETUP\BIN\
  - \autorun.hta
  - '{1E460BD7-F1C3-4B2E-88BF-4E770A288AF5}'
condition: selection and not 1 of filter_*
```

## False Positives

- Administrative scripts
- Microsoft SCCM

## References

- https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_shell_spawn_susp_program.yml)
