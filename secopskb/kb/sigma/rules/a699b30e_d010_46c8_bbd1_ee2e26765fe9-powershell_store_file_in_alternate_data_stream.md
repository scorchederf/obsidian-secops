---
sigma_id: "a699b30e-d010-46c8-bbd1-ee2e26765fe9"
title: "Powershell Store File In Alternate Data Stream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_store_file_in_alternate_data_stream.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_store_file_in_alternate_data_stream.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "a699b30e-d010-46c8-bbd1-ee2e26765fe9"
  - "Powershell Store File In Alternate Data Stream"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Store File In Alternate Data Stream

Storing files in Alternate Data Stream (ADS) similar to Astaroth malware.

## Metadata

- Rule ID: a699b30e-d010-46c8-bbd1-ee2e26765fe9
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-09-02
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_store_file_in_alternate_data_stream.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection_compspec:
  ScriptBlockText|contains|all:
  - Start-Process
  - '-FilePath "$env:comspec" '
  - '-ArgumentList '
  - '>'
condition: selection_compspec
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.004/T1564.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_store_file_in_alternate_data_stream.yml)
