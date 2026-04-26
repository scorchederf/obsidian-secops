---
sigma_id: "7ed2c9f7-c59d-4c82-a7e2-f859aa676099"
title: "Suspicious MacOS Firmware Activity"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_susp_macos_firmware_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_macos_firmware_activity.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "7ed2c9f7-c59d-4c82-a7e2-f859aa676099"
  - "Suspicious MacOS Firmware Activity"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious MacOS Firmware Activity

Detects when a user manipulates with Firmward Password on MacOS. NOTE - this command has been disabled on silicon-based apple computers.

## Metadata

- Rule ID: 7ed2c9f7-c59d-4c82-a7e2-f859aa676099
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-30
- Modified: 2022-10-09
- Source Path: rules/macos/process_creation/proc_creation_macos_susp_macos_firmware_activity.yml

## Logsource

- category: process_creation
- product: macos

## Detection

```yaml
selection1:
  Image: /usr/sbin/firmwarepasswd
  CommandLine|contains:
  - setpasswd
  - full
  - delete
  - check
condition: selection1
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/usnistgov/macos_security/blob/932a51f3e819dd3e02ebfcf3ef433cfffafbe28b/rules/os/os_firmware_password_require.yaml
- https://www.manpagez.com/man/8/firmwarepasswd/
- https://support.apple.com/guide/security/firmware-password-protection-sec28382c9ca/web

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_macos_firmware_activity.yml)
