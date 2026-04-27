---
sigma_id: "8c521530-5169-495d-a199-0a3a881ad24e"
title: "NTFS Alternate Data Stream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_ntfs_ads_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_ntfs_ads_access.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "8c521530-5169-495d-a199-0a3a881ad24e"
  - "NTFS Alternate Data Stream"
attack_technique_ids:
  - "T1564.004"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# NTFS Alternate Data Stream

Detects writing data into NTFS alternate data streams from powershell. Needs Script Block Logging.

## Metadata

- Rule ID: 8c521530-5169-495d-a199-0a3a881ad24e
- Status: test
- Level: high
- Author: Sami Ruohonen
- Date: 2018-07-24
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_ntfs_ads_access.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_content:
  ScriptBlockText|contains:
  - set-content
  - add-content
selection_stream:
  ScriptBlockText|contains: -stream
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20220614030603/http://www.powertheshell.com/ntfsstreams/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.004/T1564.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_ntfs_ads_access.yml)
