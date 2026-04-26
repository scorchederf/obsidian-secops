---
sigma_id: "ec127035-a636-4b9a-8555-0efd4e59f316"
title: "Clipboard Collection with Xclip Tool"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_clipboard_collection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_clipboard_collection.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "ec127035-a636-4b9a-8555-0efd4e59f316"
  - "Clipboard Collection with Xclip Tool"
attack_technique_ids:
  - "T1115"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clipboard Collection with Xclip Tool

Detects attempts to collect data stored in the clipboard from users with the usage of xclip tool. Xclip has to be installed.
Highly recommended using rule on servers, due to high usage of clipboard utilities on user workstations.

## Metadata

- Rule ID: ec127035-a636-4b9a-8555-0efd4e59f316
- Status: test
- Level: low
- Author: Pawel Mazur, Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
- Date: 2021-10-15
- Modified: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_clipboard_collection.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1115-clipboard_data|T1115]]

## Detection

```yaml
selection:
  Image|contains: xclip
  CommandLine|contains|all:
  - -sel
  - clip
  - -o
condition: selection
```

## False Positives

- Legitimate usage of xclip tools.

## References

- https://www.packetlabs.net/posts/clipboard-data-security/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_clipboard_collection.yml)
