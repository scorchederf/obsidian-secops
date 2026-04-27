---
sigma_id: "de46c52b-0bf8-4936-a327-aace94f94ac6"
title: "Process Explorer Driver Creation By Non-Sysinternals Binary"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_procexp_driver_susp_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_procexp_driver_susp_creation.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "de46c52b-0bf8-4936-a327-aace94f94ac6"
  - "Process Explorer Driver Creation By Non-Sysinternals Binary"
attack_technique_ids:
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Explorer Driver Creation By Non-Sysinternals Binary

Detects creation of the Process Explorer drivers by processes other than Process Explorer (procexp) itself.
Hack tools or malware may use the Process Explorer driver to elevate privileges, drops it to disk for a few moments, runs a service using that driver and removes it afterwards.

## Metadata

- Rule ID: de46c52b-0bf8-4936-a327-aace94f94ac6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2023-05-05
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_procexp_driver_susp_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

## Detection

```yaml
selection:
  TargetFilename|contains: \PROCEXP
  TargetFilename|endswith: .sys
filter_main_process_explorer:
  Image|endswith:
  - \procexp.exe
  - \procexp64.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Some false positives may occur with legitimate renamed process explorer binaries

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer
- https://github.com/Yaxser/Backstab
- https://www.elastic.co/security-labs/stopping-vulnerable-driver-attacks
- https://news.sophos.com/en-us/2023/04/19/aukill-edr-killer-malware-abuses-process-explorer-driver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_procexp_driver_susp_creation.yml)
