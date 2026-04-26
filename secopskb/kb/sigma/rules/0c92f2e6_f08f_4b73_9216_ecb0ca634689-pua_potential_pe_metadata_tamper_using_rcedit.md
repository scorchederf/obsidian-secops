---
sigma_id: "0c92f2e6-f08f-4b73-9216-ecb0ca634689"
title: "PUA - Potential PE Metadata Tamper Using Rcedit"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_rcedit_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_rcedit_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0c92f2e6-f08f-4b73-9216-ecb0ca634689"
  - "PUA - Potential PE Metadata Tamper Using Rcedit"
attack_technique_ids:
  - "T1036.003"
  - "T1036"
  - "T1027.005"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Potential PE Metadata Tamper Using Rcedit

Detects the use of rcedit to potentially alter executable PE metadata properties, which could conceal efforts to rename system utilities for defense evasion.

## Metadata

- Rule ID: 0c92f2e6-f08f-4b73-9216-ecb0ca634689
- Status: test
- Level: medium
- Author: Micah Babinski
- Date: 2022-12-11
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_pua_rcedit_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]
- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.005]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \rcedit-x64.exe
  - \rcedit-x86.exe
- Description: Edit resources of exe
- Product: rcedit
selection_flags:
  CommandLine|contains: --set-
selection_attributes:
  CommandLine|contains:
  - OriginalFileName
  - CompanyName
  - FileDescription
  - ProductName
  - ProductVersion
  - LegalCopyright
condition: all of selection_*
```

## False Positives

- Legitimate use of the tool by administrators or users to update metadata of a binary

## References

- https://security.stackexchange.com/questions/210843/is-it-possible-to-change-original-filename-of-an-exe
- https://www.virustotal.com/gui/file/02e8e8c5d430d8b768980f517b62d7792d690982b9ba0f7e04163cbc1a6e7915
- https://github.com/electron/rcedit

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_rcedit_execution.yml)
