---
car_id: "CAR-2020-09-004"
title: "Credentials in Files & Registry"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-09-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-004.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-09-004"
  - "Credentials in Files & Registry"
attack_technique_ids:
  - "T1552"
  - "T1552.001"
  - "T1552.002"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2020-09-004: Credentials in Files & Registry

## Metadata

- CAR ID: CAR-2020-09-004
- Submission Date: 2020/09/10
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process, Registry
- Contributors: Olaf Hartong

## Description

Adversaries may search the Windows Registry on compromised systems for insecurely stored credentials for credential access. This can be accomplished using the query functionality of the reg.exe system utility, by looking for keys and values that contain strings such as "password". In addition, adversaries may use toolkits such as [PowerSploit](https://powersploit.readthedocs.io/en/latest/) in order to dump credentials from various applications such as IIS.Accordingly, this analytic looks for invocations of reg.exe in this capacity as well as that of several powersploit modules with similar functionality.

## ATT&CK Coverage

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]
  - [[kb/attack/techniques/T1552-unsecured_credentials|T1552.002]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
  cred_processes = filter processes where (
  command_line = "*reg* query HKLM /f password /t REG_SZ /s*" OR
  command_line = "reg* query HKCU /f password /t REG_SZ /s" OR
  command_line = "*Get-UnattendedInstallFile*" OR
  command_line = "*Get-Webconfig*" OR
  command_line = "*Get-ApplicationHost*" OR
  command_line = "*Get-SiteListPassword*" OR
  command_line = "*Get-CachedGPPPassword*" OR
  command_line = "*Get-RegistryAutoLogon*")
output cred_processes
```

### Splunk

This Splunk search looks for command lines of reg.exe used to search for passwords, as well as those of powersploit modules for the same purpose.

- Data Model: Sysmon native

```splunk
((index=__your_sysmon_index__ EventCode=1) OR (index=__your_win_syslog_index__ EventCode=4688)) (CommandLine="*reg* query HKLM /f password /t REG_SZ /s*" OR CommandLine="reg* query HKCU /f password /t REG_SZ /s" OR CommandLine="*Get-UnattendedInstallFile*" OR CommandLine="*Get-Webconfig*" OR CommandLine="*Get-ApplicationHost*" OR CommandLine="*Get-SiteListPassword*" OR CommandLine="*Get-CachedGPPPassword*" OR CommandLine="*Get-RegistryAutoLogon*")
```

### LogPoint

This LogPoint search looks for command lines of reg.exe used to search for passwords, as well as those of powersploit modules for the same purpose.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 command IN ["*reg* query HKLM /f password /t REG_SZ /s*", "reg* query HKCU /f password /t REG_SZ /s", "*Get-UnattendedInstallFile*", "*Get-Webconfig*", "*Get-ApplicationHost*", "*Get-SiteListPassword*", "*Get-CachedGPPPassword*", "*Get-RegistryAutoLogon*"]
```

## Data Model References

- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-09-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-004.yaml)
