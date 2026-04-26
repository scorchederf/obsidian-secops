---
sigma_id: "214e7e6c-f21b-47ff-bb6f-551b2d143fcf"
title: "Clipboard Collection with Xclip Tool - Auditd"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_clipboard_collection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_clipboard_collection.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "214e7e6c-f21b-47ff-bb6f-551b2d143fcf"
  - "Clipboard Collection with Xclip Tool - Auditd"
attack_technique_ids:
  - "T1115"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clipboard Collection with Xclip Tool - Auditd

Detects attempts to collect data stored in the clipboard from users with the usage of xclip tool.
Xclip has to be installed.
Highly recommended using rule on servers, due to high usage of clipboard utilities on user workstations.

## Metadata

- Rule ID: 214e7e6c-f21b-47ff-bb6f-551b2d143fcf
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-09-24
- Modified: 2022-11-26
- Source Path: rules/linux/auditd/execve/lnx_auditd_clipboard_collection.yml

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
  a3: -o
condition: selection
```

## False Positives

- Legitimate usage of xclip tools

## References

- https://linux.die.net/man/1/xclip
- https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_clipboard_collection.yml)
