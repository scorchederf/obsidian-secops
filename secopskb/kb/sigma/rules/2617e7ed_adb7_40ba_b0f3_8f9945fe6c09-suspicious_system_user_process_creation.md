---
sigma_id: "2617e7ed-adb7-40ba-b0f3-8f9945fe6c09"
title: "Suspicious SYSTEM User Process Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_system_user_anomaly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_system_user_anomaly.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2617e7ed-adb7-40ba-b0f3-8f9945fe6c09"
  - "Suspicious SYSTEM User Process Creation"
attack_technique_ids:
  - "T1134"
  - "T1003"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious SYSTEM User Process Creation

Detects a suspicious process creation as SYSTEM user (suspicious program or command line parameter)

## Metadata

- Rule ID: 2617e7ed-adb7-40ba-b0f3-8f9945fe6c09
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), David ANDRE (additional keywords)
- Date: 2021-12-20
- Modified: 2025-10-19
- Source Path: rules/windows/process_creation/proc_creation_win_susp_system_user_anomaly.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection:
  IntegrityLevel:
  - System
  - S-1-16-16384
  User|contains:
  - AUTHORI
  - AUTORI
selection_special:
- Image|endswith:
  - \calc.exe
  - \cscript.exe
  - \forfiles.exe
  - \hh.exe
  - \mshta.exe
  - \ping.exe
  - \wscript.exe
- CommandLine|re: net\s+user\s+
- CommandLine|contains:
  - ' -NoP '
  - ' -W Hidden '
  - ' -decode '
  - ' /decode '
  - ' /urlcache '
  - ' -urlcache '
  - ' -e* JAB'
  - ' -e* SUVYI'
  - ' -e* SQBFAFgA'
  - ' -e* aWV4I'
  - ' -e* IAB'
  - ' -e* PAA'
  - ' -e* aQBlAHgA'
  - vssadmin delete shadows
  - reg SAVE HKLM
  - ' -ma '
  - Microsoft\Windows\CurrentVersion\Run
  - .downloadstring(
  - .downloadfile(
  - ' /ticket:'
  - 'dpapi::'
  - event::clear
  - event::drop
  - id::modify
  - 'kerberos::'
  - 'lsadump::'
  - 'misc::'
  - 'privilege::'
  - 'rpc::'
  - 'sekurlsa::'
  - 'sid::'
  - 'token::'
  - vault::cred
  - vault::list
  - ' p::d '
  - ;iex(
  - MiniDump
filter_main_ping:
  CommandLine|contains|all:
  - ping
  - 127.0.0.1
  - ' -n '
filter_vs:
  Image|endswith: \PING.EXE
  ParentCommandLine|contains: \DismFoDInstall.cmd
filter_config_mgr:
  ParentImage|contains: :\Packages\Plugins\Microsoft.GuestConfiguration.ConfigurationforWindows\
filter_java:
  ParentImage|contains:
  - :\Program Files (x86)\Java\
  - :\Program Files\Java\
  ParentImage|endswith: \bin\javaws.exe
  Image|contains:
  - :\Program Files (x86)\Java\
  - :\Program Files\Java\
  Image|endswith: \bin\jp2launcher.exe
  CommandLine|contains: ' -ma '
condition: all of selection* and not 1 of filter_*
```

## False Positives

- Administrative activity
- Scripts and administrative tools used in the monitored environment
- Monitoring activity

## References

- Internal Research
- https://tools.thehacker.recipes/mimikatz/modules

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_system_user_anomaly.yml)
