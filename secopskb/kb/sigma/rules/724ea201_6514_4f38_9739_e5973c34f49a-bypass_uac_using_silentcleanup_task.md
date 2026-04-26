---
sigma_id: "724ea201-6514-4f38-9739-e5973c34f49a"
title: "Bypass UAC Using SilentCleanup Task"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_bypass_uac_using_silentcleanup_task.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bypass_uac_using_silentcleanup_task.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "724ea201-6514-4f38-9739-e5973c34f49a"
  - "Bypass UAC Using SilentCleanup Task"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC Using SilentCleanup Task

Detects the setting of the environement variable "windir" to a non default value.
Attackers often abuse this variable in order to trigger a UAC bypass via the "SilentCleanup" task.
The SilentCleanup task located in %windir%\system32\cleanmgr.exe is an auto-elevated task that can be abused to elevate any file with administrator privileges without prompting UAC.

## Metadata

- Rule ID: 724ea201-6514-4f38-9739-e5973c34f49a
- Status: test
- Level: high
- Author: frack113, Nextron Systems
- Date: 2022-01-06
- Modified: 2024-01-30
- Source Path: rules/windows/registry/registry_set/registry_set_bypass_uac_using_silentcleanup_task.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Environment\windir
filter_main_default:
  Details: '%SystemRoot%'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## Simulation

### Bypass UAC using SilentCleanup Task

- Atomic Test: [[kb/atomic/tests/28104f8a_4ff1_4582_bcf6_699dce156608-bypass_uac_using_silentcleanup_task|28104f8a-4ff1-4582-bcf6-699dce156608]]
- atomic_guid: 28104f8a-4ff1-4582-bcf6-699dce156608
- name: Bypass UAC using SilentCleanup Task
- technique: T1548.002
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1548.002/T1548.002.md#atomic-test-9---bypass-uac-using-silentcleanup-task
- https://www.reddit.com/r/hacking/comments/ajtrws/bypassing_highest_uac_level_windows_810/
- https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bypass_uac_using_silentcleanup_task.yml)
