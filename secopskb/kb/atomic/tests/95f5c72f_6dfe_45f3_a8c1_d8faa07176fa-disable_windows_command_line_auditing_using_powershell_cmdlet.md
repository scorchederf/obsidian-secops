---
atomic_guid: "95f5c72f-6dfe-45f3-a8c1-d8faa07176fa"
title: "Disable Windows Command Line Auditing using Powershell Cmdlet"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "95f5c72f-6dfe-45f3-a8c1-d8faa07176fa"
  - "Disable Windows Command Line Auditing using Powershell Cmdlet"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable Windows Command Line Auditing using Powershell Cmdlet

In Windows operating systems, command line auditing is controlled through the following registry value:

  Registry Path: HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit
  
  Registry Value: ProcessCreationIncludeCmdLine_Enabled

When command line auditing is enabled, the system records detailed information about command execution, including the command executed, the user account responsible for executing the command, and the timestamp of the execution.
This information is crucial for security monitoring and forensic analysis, as it helps organizations detect and investigate unauthorized or malicious activities within their systems.
By default, command line auditing may not be enabled in Windows systems, and administrators must manually configure the appropriate registry settings to activate it.
Conversely, attackers may attempt to tamper with these registry keys to disable command line auditing, as part of their efforts to evade detection and cover their tracks while perpetrating malicious activities.

Because this attack runs a Powershell cmdlet, this attack can be detected by monitoring both:
  Powershell Logging (Windows Powershell Event ID 400, 800, 4103, 4104)
  Registry events (Windows Event ID 4657, Sysmon Event ID 13)

Read more here:
https://securitydatasets.com/notebooks/atomic/windows/defense_evasion/SDWIN-220703123711.html
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-itemproperty?view=powershell-7.4#example-2-add-a-registry-entry-to-a-key

## Metadata

- Atomic GUID: 95f5c72f-6dfe-45f3-a8c1-d8faa07176fa
- Technique: T1562.003: Impair Defenses: Impair Command History Logging
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.003/T1562.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.003]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit" -Name "ProcessCreationIncludeCmdLine_Enabled" -Value 0 -PropertyType DWORD -Force -ErrorAction Ignore
```

### Cleanup

```powershell
New-ItemProperty -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit" -Name "ProcessCreationIncludeCmdLine_Enabled" -Value 1 -PropertyType DWORD -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
