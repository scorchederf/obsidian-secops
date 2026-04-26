---
sigma_id: "7df1713a-1a5b-4a4b-a071-dc83b144a101"
title: "Esentutl Gather Credentials"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_esentutl_params.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_esentutl_params.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7df1713a-1a5b-4a4b-a071-dc83b144a101"
  - "Esentutl Gather Credentials"
attack_technique_ids:
  - "T1003"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Esentutl Gather Credentials

Conti recommendation to its affiliates to use esentutl to access NTDS dumped file. Trickbot also uses this utilities to get MSEdge info via its module pwgrab.

## Metadata

- Rule ID: 7df1713a-1a5b-4a4b-a071-dc83b144a101
- Status: test
- Level: medium
- Author: sam0x90
- Date: 2021-08-06
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_esentutl_params.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

### Software Tags

- S0404

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - esentutl
  - ' /p'
condition: selection
```

## False Positives

- To be determined

## References

- https://twitter.com/vxunderground/status/1423336151860002816
- https://thedfirreport.com/2021/08/01/bazarcall-to-conti-ransomware-via-trickbot-and-cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_esentutl_params.yml)
