---
sigma_id: "30a8cb77-8eb3-4cfb-8e79-ad457c5a4592"
title: "Renamed Powershell Under Powershell Channel"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_renamed_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_renamed_powershell.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / ps_classic_start"
aliases:
  - "30a8cb77-8eb3-4cfb-8e79-ad457c5a4592"
  - "Renamed Powershell Under Powershell Channel"
attack_technique_ids:
  - "T1059.001"
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed Powershell Under Powershell Channel

Detects a renamed Powershell execution, which is a common technique used to circumvent security controls and bypass detection logic that's dependent on process names and process paths.

## Metadata

- Rule ID: 30a8cb77-8eb3-4cfb-8e79-ad457c5a4592
- Status: test
- Level: low
- Author: Harish Segar, frack113
- Date: 2020-06-29
- Modified: 2025-01-20
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_renamed_powershell.yml

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection:
  Data|contains: HostName=ConsoleHost
filter_main_ps:
  Data|contains:
  - HostApplication=powershell
  - HostApplication=C:\Windows\System32\WindowsPowerShell\v1.0\powershell
  - HostApplication=C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell
  - HostApplication=C:/Windows/System32/WindowsPowerShell/v1.0/powershell
  - HostApplication=C:/Windows/SysWOW64/WindowsPowerShell/v1.0/powershell
  - HostApplication=C:\\\\WINDOWS\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe
  - HostApplication=C:\\\\WINDOWS\\\\SysWOW64\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe
filter_main_host_application_null:
  Data|re: HostId=[a-zA-Z0-9-]{36}\s+EngineVersion=
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_renamed_powershell.yml)
