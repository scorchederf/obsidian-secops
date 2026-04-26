---
sigma_id: "a29808fd-ef50-49ff-9c7a-59a9b040b404"
title: "HackTool - Pypykatz Credentials Dumping Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_pypykatz.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_pypykatz.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a29808fd-ef50-49ff-9c7a-59a9b040b404"
  - "HackTool - Pypykatz Credentials Dumping Activity"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Pypykatz Credentials Dumping Activity

Detects the usage of "pypykatz" to obtain stored credentials. Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database through Windows registry where the SAM database is stored

## Metadata

- Rule ID: a29808fd-ef50-49ff-9c7a-59a9b040b404
- Status: test
- Level: high
- Author: frack113
- Date: 2022-01-05
- Modified: 2023-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_pypykatz.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection:
  Image|endswith:
  - \pypykatz.exe
  - \python.exe
  CommandLine|contains|all:
  - live
  - registry
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/skelsec/pypykatz
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/T1003.002.md#atomic-test-2---registry-parse-with-pypykatz

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_pypykatz.yml)
