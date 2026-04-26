---
sigma_id: "9ec9fb1b-e059-4489-9642-f270c207923d"
title: "Hiding User Account Via SpecialAccounts Registry Key - CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_special_accounts_hide_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_special_accounts_hide_user.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9ec9fb1b-e059-4489-9642-f270c207923d"
  - "Hiding User Account Via SpecialAccounts Registry Key - CommandLine"
attack_technique_ids:
  - "T1564.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hiding User Account Via SpecialAccounts Registry Key - CommandLine

Detects changes to the registry key "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\Userlist" where the value is set to "0" in order to hide user account from being listed on the logon screen.

## Metadata

- Rule ID: 9ec9fb1b-e059-4489-9642-f270c207923d
- Status: test
- Level: medium
- Author: @Kostastsale, TheDFIRReport
- Date: 2022-05-14
- Modified: 2024-08-23
- Source Path: rules/windows/process_creation/proc_creation_win_registry_special_accounts_hide_user.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.002]]

## Detection

```yaml
selection:
  Image|endswith: \reg.exe
  CommandLine|contains|all:
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList
  - add
  - /v
  - /d 0
condition: selection
```

## False Positives

- System administrator activities

## References

- https://thedfirreport.com/2024/01/29/buzzing-on-christmas-eve-trigona-ransomware-in-3-hours/
- https://thedfirreport.com/2024/04/01/from-onenote-to-ransomnote-an-ice-cold-intrusion/
- https://thedfirreport.com/2024/04/29/from-icedid-to-dagon-locker-ransomware-in-29-days/
- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_special_accounts_hide_user.yml)
