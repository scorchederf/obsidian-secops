---
sigma_id: "214641c2-c579-4ecb-8427-0cf19df6842e"
title: "Remote File Download Via Desktopimgdownldr Utility"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_desktopimgdownldr_remote_file_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_remote_file_download.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "214641c2-c579-4ecb-8427-0cf19df6842e"
  - "Remote File Download Via Desktopimgdownldr Utility"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote File Download Via Desktopimgdownldr Utility

Detects the desktopimgdownldr utility being used to download a remote file. An adversary may use desktopimgdownldr to download arbitrary files as an alternative to certutil.

## Metadata

- Rule ID: 214641c2-c579-4ecb-8427-0cf19df6842e
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-27
- Source Path: rules/windows/process_creation/proc_creation_win_desktopimgdownldr_remote_file_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|endswith: \desktopimgdownldr.exe
  ParentImage|endswith: \desktopimgdownldr.exe
  CommandLine|contains: /lockscreenurl:http
condition: selection
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/remote-file-download-via-desktopimgdownldr-utility.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_remote_file_download.yml)
