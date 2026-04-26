---
sigma_id: "1f358e2e-cb63-43c3-b575-dfb072a6814f"
title: "System and Hardware Information Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_system_info_discovery2.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_system_info_discovery2.yml"
build_date: "2026-04-26 14:14:37"
status: "stable"
level: "informational"
logsource: "linux / auditd"
aliases:
  - "1f358e2e-cb63-43c3-b575-dfb072a6814f"
  - "System and Hardware Information Discovery"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System and Hardware Information Discovery

Detects system information discovery commands

## Metadata

- Rule ID: 1f358e2e-cb63-43c3-b575-dfb072a6814f
- Status: stable
- Level: informational
- Author: Ömer Günal, oscd.community
- Date: 2020-10-08
- Modified: 2022-11-26
- Source Path: rules/linux/auditd/path/lnx_auditd_system_info_discovery2.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
  type: PATH
  name:
  - /sys/class/dmi/id/bios_version
  - /sys/class/dmi/id/product_name
  - /sys/class/dmi/id/chassis_vendor
  - /proc/scsi/scsi
  - /proc/ide/hd0/model
  - /proc/version
  - /etc/*version
  - /etc/*release
  - /etc/issue
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1082/T1082.md#atomic-test-4---linux-vm-check-via-hardware

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_system_info_discovery2.yml)
