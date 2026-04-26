---
sigma_id: "c2c76b77-32be-4d1f-82c9-7e544bdfe0eb"
title: "Potential Suspicious Activity Using SeCEdit"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_secedit_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_secedit_execution.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c2c76b77-32be-4d1f-82c9-7e544bdfe0eb"
  - "Potential Suspicious Activity Using SeCEdit"
attack_technique_ids:
  - "T1562.002"
  - "T1547.001"
  - "T1505.005"
  - "T1556.002"
  - "T1562"
  - "T1574.007"
  - "T1564.002"
  - "T1546.008"
  - "T1546.007"
  - "T1547.014"
  - "T1547.010"
  - "T1547.002"
  - "T1557"
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious Activity Using SeCEdit

Detects potential suspicious behaviour using secedit.exe. Such as exporting or modifying the security policy

## Metadata

- Rule ID: c2c76b77-32be-4d1f-82c9-7e544bdfe0eb
- Status: test
- Level: medium
- Author: Janantha Marasinghe
- Date: 2022-11-18
- Modified: 2022-12-30
- Source Path: rules/windows/process_creation/proc_creation_win_secedit_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]
- [[kb/attack/techniques/T1505-server_software_component|T1505.005]]
- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.002]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.007]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.002]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.007]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.014]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.010]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.002]]
- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_img:
- Image|endswith: \secedit.exe
- OriginalFileName: SeCEdit
selection_flags_discovery:
  CommandLine|contains|all:
  - /export
  - /cfg
selection_flags_configure:
  CommandLine|contains|all:
  - /configure
  - /db
condition: selection_img and (1 of selection_flags_*)
```

## False Positives

- Legitimate administrative use

## References

- https://blueteamops.medium.com/secedit-and-i-know-it-595056dee53d
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_secedit_execution.yml)
