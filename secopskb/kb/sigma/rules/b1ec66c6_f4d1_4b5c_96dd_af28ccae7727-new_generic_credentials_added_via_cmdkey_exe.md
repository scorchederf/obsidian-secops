---
sigma_id: "b1ec66c6-f4d1-4b5c-96dd-af28ccae7727"
title: "New Generic Credentials Added Via Cmdkey.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmdkey_adding_generic_creds.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmdkey_adding_generic_creds.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b1ec66c6-f4d1-4b5c-96dd-af28ccae7727"
  - "New Generic Credentials Added Via Cmdkey.EXE"
attack_technique_ids:
  - "T1003.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Generic Credentials Added Via Cmdkey.EXE

Detects usage of "cmdkey.exe" to add generic credentials.
As an example, this can be used before connecting to an RDP session via command line interface.

## Metadata

- Rule ID: b1ec66c6-f4d1-4b5c-96dd-af28ccae7727
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-03
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_cmdkey_adding_generic_creds.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmdkey.exe
- OriginalFileName: cmdkey.exe
selection_cli_generic:
  CommandLine|contains|windash: ' -g'
selection_cli_user:
  CommandLine|contains|windash: ' -u'
selection_cli_password:
  CommandLine|contains|windash: ' -p'
condition: all of selection_*
```

## False Positives

- Legitimate usage for administration purposes

## Simulation

### RDP to DomainController

- atomic_guid: 355d4632-8cb9-449d-91ce-b566d0253d3e
- name: RDP to DomainController
- technique: T1021.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.001/T1021.001.md#t1021001---remote-desktop-protocol

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmdkey_adding_generic_creds.yml)
