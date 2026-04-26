---
sigma_id: "179b3686-6271-4d87-807d-17d843a8af73"
title: "Suspicious Filename with Embedded Base64 Commands"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_susp_filename_with_embedded_base64_command.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_susp_filename_with_embedded_base64_command.yml"
build_date: "2026-04-26 15:01:52"
status: "experimental"
level: "high"
logsource: "linux / file_event"
aliases:
  - "179b3686-6271-4d87-807d-17d843a8af73"
  - "Suspicious Filename with Embedded Base64 Commands"
attack_technique_ids:
  - "T1059.004"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Filename with Embedded Base64 Commands

Detects files with specially crafted filenames that embed Base64-encoded bash payloads designed to execute when processed by shell scripts.
These filenames exploit shell interpretation quirks to trigger hidden commands, a technique observed in VShell malware campaigns.

## Metadata

- Rule ID: 179b3686-6271-4d87-807d-17d843a8af73
- Status: experimental
- Level: high
- Author: @kostastsale
- Date: 2025-11-22
- Source Path: rules/linux/file_event/file_event_lnx_susp_filename_with_embedded_base64_command.yml

## Logsource

- category: file_event
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection:
  TargetFilename|contains:
  - '{echo'
  - '{base64,-d}'
condition: selection
```

## False Positives

- Legitimate files with similar naming patterns (very unlikely).

## References

- https://www.trellix.com/blogs/research/the-silent-fileless-threat-of-vshell/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_susp_filename_with_embedded_base64_command.yml)
