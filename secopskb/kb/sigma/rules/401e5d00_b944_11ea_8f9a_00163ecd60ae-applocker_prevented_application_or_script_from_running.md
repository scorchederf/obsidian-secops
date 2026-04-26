---
sigma_id: "401e5d00-b944-11ea-8f9a-00163ecd60ae"
title: "AppLocker Prevented Application or Script from Running"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/applocker/win_applocker_application_was_prevented_from_running.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/applocker/win_applocker_application_was_prevented_from_running.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / applocker"
aliases:
  - "401e5d00-b944-11ea-8f9a-00163ecd60ae"
  - "AppLocker Prevented Application or Script from Running"
attack_technique_ids:
  - "T1204.002"
  - "T1059.001"
  - "T1059.003"
  - "T1059.005"
  - "T1059.006"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AppLocker Prevented Application or Script from Running

Detects when AppLocker prevents the execution of an Application, DLL, Script, MSI, or Packaged-App from running.

## Metadata

- Rule ID: 401e5d00-b944-11ea-8f9a-00163ecd60ae
- Status: test
- Level: medium
- Author: Pushkarev Dmitry
- Date: 2020-06-28
- Modified: 2025-12-03
- Source Path: rules/windows/builtin/applocker/win_applocker_application_was_prevented_from_running.yml

## Logsource

- product: windows
- service: applocker

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.006]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection:
  EventID:
  - 8004
  - 8007
  - 8022
  - 8025
condition: selection
```

## False Positives

- Unlikely, since this event notifies about blocked application execution. Tune your applocker rules to avoid blocking legitimate applications.

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/applocker/what-is-applocker
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/applocker/using-event-viewer-with-applocker
- https://nxlog.co/documentation/nxlog-user-guide/applocker.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/applocker/win_applocker_application_was_prevented_from_running.yml)
