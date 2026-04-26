---
sigma_id: "9c226817-8dc9-46c2-a58d-66655aafd7dc"
title: "Modify User Shell Folders Startup Value"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_user_shell_folders.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_user_shell_folders.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "9c226817-8dc9-46c2-a58d-66655aafd7dc"
  - "Modify User Shell Folders Startup Value"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify User Shell Folders Startup Value

Detect modification of the User Shell Folders registry values for Startup or Common Startup which could indicate persistence attempts.
Attackers may modify User Shell Folders registry keys to point to malicious executables or scripts that will be executed during startup.
This technique is often used to maintain persistence on a compromised system by ensuring that the malicious payload is executed automatically.

## Metadata

- Rule ID: 9c226817-8dc9-46c2-a58d-66655aafd7dc
- Status: test
- Level: high
- Author: frack113, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2022-10-01
- Modified: 2026-01-05
- Source Path: rules/windows/registry/registry_set/registry_set_susp_user_shell_folders.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
  TargetObject|endswith:
  - \Common Startup
  - \Startup
filter_main_details_null:
  Details: null
filter_main_programdata_startup:
  Details|contains:
  - C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
  - '%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup'
filter_main_userprofile_startup_1:
  Details|contains:
  - '%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
  - '%%USERPROFILE%%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
filter_main_userprofile_startup_2:
  Details|contains|all:
  - C:\Users\
  - \AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## Simulation

### Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value

- Atomic Test: [[kb/atomic/tests/acfef903_7662_447e_a391_9c91c2f00f7b-change_startup_folder_hklm_modify_user_shell_folders_common_startup_value|acfef903-7662-447e-a391-9c91c2f00f7b]]
- atomic_guid: acfef903-7662-447e-a391-9c91c2f00f7b
- name: Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value
- technique: T1547.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/9e5b12c4912c07562aec7500447b11fa3e17e254/atomics/T1547.001/T1547.001.md
- https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_user_shell_folders.yml)
