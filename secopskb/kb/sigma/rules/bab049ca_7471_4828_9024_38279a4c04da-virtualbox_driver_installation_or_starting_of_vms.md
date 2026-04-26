---
sigma_id: "bab049ca-7471-4828-9024-38279a4c04da"
title: "Virtualbox Driver Installation or Starting of VMs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_virtualbox_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_virtualbox_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "bab049ca-7471-4828-9024-38279a4c04da"
  - "Virtualbox Driver Installation or Starting of VMs"
attack_technique_ids:
  - "T1564.006"
  - "T1564"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Virtualbox Driver Installation or Starting of VMs

Adversaries can carry out malicious operations using a virtual instance to avoid detection. This rule is built to detect the registration of the Virtualbox driver or start of a Virtualbox VM.

## Metadata

- Rule ID: bab049ca-7471-4828-9024-38279a4c04da
- Status: test
- Level: low
- Author: Janantha Marasinghe
- Date: 2020-09-26
- Modified: 2025-07-29
- Source Path: rules/windows/process_creation/proc_creation_win_virtualbox_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.006]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Detection

```yaml
selection_1:
  CommandLine|contains:
  - VBoxRT.dll,RTR3Init
  - VBoxC.dll
  - VBoxDrv.sys
selection_2:
  CommandLine|contains:
  - startvm
  - controlvm
condition: 1 of selection_*
```

## False Positives

- This may have false positives on hosts where Virtualbox is legitimately being used for operations

## References

- https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/
- https://threatpost.com/maze-ransomware-ragnar-locker-virtual-machine/159350/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_virtualbox_execution.yml)
