---
sigma_id: "fa00b701-44c6-4679-994d-5a18afa8a707"
title: "PUA - AdvancedRun Suspicious Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_advancedrun_priv_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advancedrun_priv_user.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fa00b701-44c6-4679-994d-5a18afa8a707"
  - "PUA - AdvancedRun Suspicious Execution"
attack_technique_ids:
  - "T1134.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - AdvancedRun Suspicious Execution

Detects the execution of AdvancedRun utility in the context of the TrustedInstaller, SYSTEM, Local Service or Network Service accounts

## Metadata

- Rule ID: fa00b701-44c6-4679-994d-5a18afa8a707
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-20
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_pua_advancedrun_priv_user.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.002]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - /EXEFilename
  - /CommandLine
selection_runas:
- CommandLine|contains:
  - ' /RunAs 8 '
  - ' /RunAs 4 '
  - ' /RunAs 10 '
  - ' /RunAs 11 '
- CommandLine|endswith:
  - /RunAs 8
  - /RunAs 4
  - /RunAs 10
  - /RunAs 11
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/splinter_code/status/1483815103279603714
- https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3
- https://www.elastic.co/security-labs/operation-bleeding-bear
- https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-windows/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advancedrun_priv_user.yml)
