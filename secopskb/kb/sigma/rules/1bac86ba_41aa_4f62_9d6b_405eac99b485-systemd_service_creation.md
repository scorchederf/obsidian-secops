---
sigma_id: "1bac86ba-41aa-4f62-9d6b-405eac99b485"
title: "Systemd Service Creation"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_systemd_service_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_systemd_service_creation.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "1bac86ba-41aa-4f62-9d6b-405eac99b485"
  - "Systemd Service Creation"
attack_technique_ids:
  - "T1543.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Systemd Service Creation

Detects a creation of systemd services which could be used by adversaries to execute malicious code.

## Metadata

- Rule ID: 1bac86ba-41aa-4f62-9d6b-405eac99b485
- Status: test
- Level: medium
- Author: Pawel Mazur
- Date: 2022-02-03
- Modified: 2022-02-06
- Source Path: rules/linux/auditd/path/lnx_auditd_systemd_service_creation.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.002]]

## Detection

```yaml
path:
  type: PATH
  nametype: CREATE
name_1:
  name|startswith:
  - /usr/lib/systemd/system/
  - /etc/systemd/system/
name_2:
  name|contains: /.config/systemd/user/
condition: path and 1 of name_*
```

## False Positives

- Admin work like legit service installs.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1543.002/T1543.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_systemd_service_creation.yml)
