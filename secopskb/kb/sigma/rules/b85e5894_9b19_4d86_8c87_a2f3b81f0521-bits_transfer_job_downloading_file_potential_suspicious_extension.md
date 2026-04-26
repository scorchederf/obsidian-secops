---
sigma_id: "b85e5894-9b19-4d86-8c87-a2f3b81f0521"
title: "BITS Transfer Job Downloading File Potential Suspicious Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/bits_client/win_bits_client_new_transfer_saving_susp_extensions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_saving_susp_extensions.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / bits-client"
aliases:
  - "b85e5894-9b19-4d86-8c87-a2f3b81f0521"
  - "BITS Transfer Job Downloading File Potential Suspicious Extension"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# BITS Transfer Job Downloading File Potential Suspicious Extension

Detects new BITS transfer job saving local files with potential suspicious extensions

## Metadata

- Rule ID: b85e5894-9b19-4d86-8c87-a2f3b81f0521
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-01
- Modified: 2023-03-27
- Source Path: rules/windows/builtin/bits_client/win_bits_client_new_transfer_saving_susp_extensions.yml

## Logsource

- product: windows
- service: bits-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Detection

```yaml
selection:
  EventID: 16403
  LocalName|endswith:
  - .bat
  - .dll
  - .exe
  - .hta
  - .ps1
  - .psd1
  - .sh
  - .vbe
  - .vbs
filter_optional_generic:
  LocalName|contains: \AppData\
  RemoteName|contains: .com
condition: selection and not 1 of filter_optional_*
```

## False Positives

- While the file extensions in question can be suspicious at times. It's best to add filters according to your environment to avoid large amount false positives

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1197/T1197.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_saving_susp_extensions.yml)
