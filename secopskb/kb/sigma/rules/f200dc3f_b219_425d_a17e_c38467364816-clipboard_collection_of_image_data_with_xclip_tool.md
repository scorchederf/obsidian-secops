---
sigma_id: "f200dc3f-b219-425d-a17e-c38467364816"
title: "Clipboard Collection of Image Data with Xclip Tool"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_clipboard_image_collection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_clipboard_image_collection.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "f200dc3f-b219-425d-a17e-c38467364816"
  - "Clipboard Collection of Image Data with Xclip Tool"
attack_technique_ids:
  - "T1115"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clipboard Collection of Image Data with Xclip Tool

Detects attempts to collect image data stored in the clipboard from users with the usage of xclip tool.
Xclip has to be installed.
Highly recommended using rule on servers, due to high usage of clipboard utilities on user workstations.

## Metadata

- Rule ID: f200dc3f-b219-425d-a17e-c38467364816
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-10-01
- Modified: 2022-10-09
- Source Path: rules/linux/auditd/execve/lnx_auditd_clipboard_image_collection.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1115-clipboard_data|T1115]]

## Detection

```yaml
selection:
  type: EXECVE
  a0: xclip
  a1:
  - -selection
  - -sel
  a2:
  - clipboard
  - clip
  a3: -t
  a4|startswith: image/
  a5: -o
condition: selection
```

## False Positives

- Legitimate usage of xclip tools

## References

- https://linux.die.net/man/1/xclip

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_clipboard_image_collection.yml)
