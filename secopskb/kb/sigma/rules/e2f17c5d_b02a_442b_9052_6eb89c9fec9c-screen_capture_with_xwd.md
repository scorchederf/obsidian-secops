---
sigma_id: "e2f17c5d-b02a-442b-9052-6eb89c9fec9c"
title: "Screen Capture with Xwd"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_screencaputre_xwd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_screencaputre_xwd.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "e2f17c5d-b02a-442b-9052-6eb89c9fec9c"
  - "Screen Capture with Xwd"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Screen Capture with Xwd

Detects adversary creating screen capture of a full with xwd. Highly recommended using rule on servers, due high usage of screenshot utilities on user workstations

## Metadata

- Rule ID: e2f17c5d-b02a-442b-9052-6eb89c9fec9c
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-09-13
- Modified: 2022-12-18
- Source Path: rules/linux/auditd/execve/lnx_auditd_screencaputre_xwd.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection:
  type: EXECVE
  a0: xwd
xwd_root_window:
  a1: -root
  a2: -out
  a3|endswith: .xwd
xwd_no_root_window:
  a1: -out
  a2|endswith: .xwd
condition: selection and 1 of xwd_*
```

## False Positives

- Legitimate use of screenshot utility

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1113/T1113.md#atomic-test-3---x-windows-capture
- https://linux.die.net/man/1/xwd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_screencaputre_xwd.yml)
