---
sigma_id: "1327381e-6ab0-4f38-b583-4c1b8346a56b"
title: "Potential Command Line Path Traversal Evasion Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_commandline_path_traversal_evasion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_commandline_path_traversal_evasion.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1327381e-6ab0-4f38-b583-4c1b8346a56b"
  - "Potential Command Line Path Traversal Evasion Attempt"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Command Line Path Traversal Evasion Attempt

Detects potential evasion or obfuscation attempts using bogus path traversal via the commandline

## Metadata

- Rule ID: 1327381e-6ab0-4f38-b583-4c1b8346a56b
- Status: test
- Level: medium
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-10-26
- Modified: 2023-03-29
- Source Path: rules/windows/process_creation/proc_creation_win_susp_commandline_path_traversal_evasion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_1:
  Image|contains: \Windows\
  CommandLine|contains:
  - \..\Windows\
  - \..\System32\
  - \..\..\
selection_2:
  CommandLine|contains: .exe\..\
filter_optional_google_drive:
  CommandLine|contains: \Google\Drive\googledrivesync.exe\..\
filter_optional_citrix:
  CommandLine|contains: \Citrix\Virtual Smart Card\Citrix.Authentication.VirtualSmartcard.Launcher.exe\..\
condition: 1 of selection_* and not 1 of filter_optional_*
```

## False Positives

- Google Drive
- Citrix

## References

- https://twitter.com/hexacorn/status/1448037865435320323
- https://twitter.com/Gal_B1t/status/1062971006078345217

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_commandline_path_traversal_evasion.yml)
