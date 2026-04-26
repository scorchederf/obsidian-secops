---
sigma_id: "21d856f9-9281-4ded-9377-51a1a6e2a432"
title: "Potential Persistence Via Logon Scripts - CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_logon_script.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_logon_script.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "21d856f9-9281-4ded-9377-51a1a6e2a432"
  - "Potential Persistence Via Logon Scripts - CommandLine"
attack_technique_ids:
  - "T1037.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via Logon Scripts - CommandLine

Detects the addition of a new LogonScript to the registry value "UserInitMprLogonScript" for potential persistence

## Metadata

- Rule ID: 21d856f9-9281-4ded-9377-51a1a6e2a432
- Status: test
- Level: high
- Author: Tom Ueltschi (@c_APT_ure)
- Date: 2019-01-12
- Modified: 2023-06-09
- Source Path: rules/windows/process_creation/proc_creation_win_registry_logon_script.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.001]]

## Detection

```yaml
selection:
  CommandLine|contains: UserInitMprLogonScript
condition: selection
```

## False Positives

- Legitimate addition of Logon Scripts via the command line by administrators or third party tools

## References

- https://cocomelonc.github.io/persistence/2022/12/09/malware-pers-20.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_logon_script.yml)
