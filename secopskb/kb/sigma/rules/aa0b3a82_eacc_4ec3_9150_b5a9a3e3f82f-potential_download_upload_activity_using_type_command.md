---
sigma_id: "aa0b3a82-eacc-4ec3-9150-b5a9a3e3f82f"
title: "Potential Download/Upload Activity Using Type Command"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_type_arbitrary_file_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_type_arbitrary_file_download.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "aa0b3a82-eacc-4ec3-9150-b5a9a3e3f82f"
  - "Potential Download/Upload Activity Using Type Command"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Download/Upload Activity Using Type Command

Detects usage of the "type" command to download/upload data from WebDAV server

## Metadata

- Rule ID: aa0b3a82-eacc-4ec3-9150-b5a9a3e3f82f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-14
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_type_arbitrary_file_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_upload:
  CommandLine|contains|all:
  - 'type '
  - ' > \\\\'
selection_download:
  CommandLine|contains|all:
  - type \\\\
  - ' > '
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://mr0range.com/a-new-lolbin-using-the-windows-type-command-to-upload-download-files-81d7b6179e22

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_type_arbitrary_file_download.yml)
