---
sigma_id: "7eedcc9d-9fdb-4d94-9c54-474e8affc0c7"
title: "Invoke-Obfuscation COMPRESS OBFUSCATION"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_compress.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_compress.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7eedcc9d-9fdb-4d94-9c54-474e8affc0c7"
  - "Invoke-Obfuscation COMPRESS OBFUSCATION"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation COMPRESS OBFUSCATION

Detects Obfuscated Powershell via COMPRESS OBFUSCATION

## Metadata

- Rule ID: 7eedcc9d-9fdb-4d94-9c54-474e8affc0c7
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-18
- Modified: 2022-12-29
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_compress.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - new-object
  - text.encoding]::ascii
  CommandLine|contains:
  - system.io.compression.deflatestream
  - system.io.streamreader
  - readtoend(
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_compress.yml)
