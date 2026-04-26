---
sigma_id: "dbe4b9c5-c254-4258-9688-d6af0b7967fd"
title: "Screen Capture with Import Tool"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_screencapture_import.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_screencapture_import.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "dbe4b9c5-c254-4258-9688-d6af0b7967fd"
  - "Screen Capture with Import Tool"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Screen Capture with Import Tool

Detects adversary creating screen capture of a desktop with Import Tool.
Highly recommended using rule on servers, due to high usage of screenshot utilities on user workstations.
ImageMagick must be installed.

## Metadata

- Rule ID: dbe4b9c5-c254-4258-9688-d6af0b7967fd
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-09-21
- Modified: 2022-10-09
- Source Path: rules/linux/auditd/execve/lnx_auditd_screencapture_import.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
import:
  type: EXECVE
  a0: import
import_window_root:
  a1: -window
  a2: root
  a3|endswith:
  - .png
  - .jpg
  - .jpeg
import_no_window_root:
  a1|endswith:
  - .png
  - .jpg
  - .jpeg
condition: import and (import_window_root or import_no_window_root)
```

## False Positives

- Legitimate use of screenshot utility

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1113/T1113.md
- https://linux.die.net/man/1/import
- https://imagemagick.org/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_screencapture_import.yml)
