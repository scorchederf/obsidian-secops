---
sigma_id: "d937b75f-a665-4480-88a5-2f20e9f9b22a"
title: "Possible Privilege Escalation via Weak Service Permissions"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_change_sevice_image_path_by_non_admin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_change_sevice_image_path_by_non_admin.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d937b75f-a665-4480-88a5-2f20e9f9b22a"
  - "Possible Privilege Escalation via Weak Service Permissions"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Possible Privilege Escalation via Weak Service Permissions

Detection of sc.exe utility spawning by user with Medium integrity level to change service ImagePath or FailureCommand

## Metadata

- Rule ID: d937b75f-a665-4480-88a5-2f20e9f9b22a
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov
- Date: 2019-10-26
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_sc_change_sevice_image_path_by_non_admin.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
scbynonadmin:
  Image|endswith: \sc.exe
  IntegrityLevel:
  - Medium
  - S-1-16-8192
selection_binpath:
  CommandLine|contains|all:
  - config
  - binPath
selection_failure:
  CommandLine|contains|all:
  - failure
  - command
condition: scbynonadmin and 1 of selection_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment
- https://pentestlab.blog/2017/03/30/weak-service-permissions/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_change_sevice_image_path_by_non_admin.yml)
