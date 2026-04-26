---
sigma_id: "38879043-7e1e-47a9-8d46-6bec88e201df"
title: "Potential Persistence Attempt Via Existing Service Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_service_tamper_for_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_service_tamper_for_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "38879043-7e1e-47a9-8d46-6bec88e201df"
  - "Potential Persistence Attempt Via Existing Service Tampering"
attack_technique_ids:
  - "T1543.003"
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Attempt Via Existing Service Tampering

Detects the modification of an existing service in order to execute an arbitrary payload when the service is started or killed as a potential method for persistence.

## Metadata

- Rule ID: 38879043-7e1e-47a9-8d46-6bec88e201df
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-09-29
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_sc_service_tamper_for_persistence.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection_sc:
- CommandLine|contains|all:
  - 'sc '
  - 'config '
  - binpath=
- CommandLine|contains|all:
  - 'sc '
  - failure
  - command=
selection_reg_img:
- CommandLine|contains|all:
  - 'reg '
  - 'add '
  - FailureCommand
- CommandLine|contains|all:
  - 'reg '
  - 'add '
  - ImagePath
selection_reg_ext:
  CommandLine|contains:
  - .sh
  - .exe
  - .dll
  - .bin$
  - .bat
  - .cmd
  - .js
  - .msh$
  - .reg$
  - .scr
  - .ps
  - .vb
  - .jar
  - .pl
condition: selection_sc or all of selection_reg_*
```

## False Positives

- Unknown

## References

- https://pentestlab.blog/2020/01/22/persistence-modify-existing-service/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_service_tamper_for_persistence.yml)
