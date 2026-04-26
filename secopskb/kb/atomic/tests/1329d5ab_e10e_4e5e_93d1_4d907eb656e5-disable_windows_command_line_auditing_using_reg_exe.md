---
atomic_guid: "1329d5ab-e10e-4e5e-93d1-4d907eb656e5"
title: "Disable Windows Command Line Auditing using reg.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "1329d5ab-e10e-4e5e-93d1-4d907eb656e5"
  - "Disable Windows Command Line Auditing using reg.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Windows Command Line Auditing using reg.exe

In Windows operating systems, command line auditing is controlled through the following registry value:

  Registry Path: HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit
  
  Registry Value: ProcessCreationIncludeCmdLine_Enabled

When command line auditing is enabled, the system records detailed information about command execution, including the command executed, the user account responsible for executing the command, and the timestamp of the execution.
This information is crucial for security monitoring and forensic analysis, as it helps organizations detect and investigate unauthorized or malicious activities within their systems.
By default, command line auditing may not be enabled in Windows systems, and administrators must manually configure the appropriate registry settings to activate it.
Conversely, attackers may attempt to tamper with these registry keys to disable command line auditing, as part of their efforts to evade detection and cover their tracks while perpetrating malicious activities.

Because this attack executes reg.exe using a command prompt, this attack can be detected by monitoring both:
  Process Creation events for reg.exe (Windows Event ID 4688, Sysmon Event ID 1)
  Registry events (Windows Event ID 4657, Sysmon Event ID 13)

Read more here:
https://securitydatasets.com/notebooks/atomic/windows/defense_evasion/SDWIN-220703123711.html

## Metadata

- Atomic GUID: 1329d5ab-e10e-4e5e-93d1-4d907eb656e5
- Technique: T1562.003: Impair Defenses: Impair Command History Logging
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.003/T1562.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.003]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit /v ProcessCreationIncludeCmdLine_Enabled /t REG_DWORD /d 0 /f
```

### Cleanup

```commandprompt
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit /v ProcessCreationIncludeCmdLine_Enabled /t REG_DWORD /d 1 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
