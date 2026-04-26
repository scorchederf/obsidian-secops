---
sigma_id: "95d61234-7f56-465c-6f2d-b562c6fedbc4"
title: "Linux Package Uninstall"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_remove_package.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_remove_package.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "95d61234-7f56-465c-6f2d-b562c6fedbc4"
  - "Linux Package Uninstall"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Package Uninstall

Detects linux package removal using builtin tools such as "yum", "apt", "apt-get" or "dpkg".

## Metadata

- Rule ID: 95d61234-7f56-465c-6f2d-b562c6fedbc4
- Status: test
- Level: low
- Author: Tuan Le (NCSGroup), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-09
- Source Path: rules/linux/process_creation/proc_creation_lnx_remove_package.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection_yum:
  Image|endswith: /yum
  CommandLine|contains:
  - erase
  - remove
selection_apt:
  Image|endswith:
  - /apt
  - /apt-get
  CommandLine|contains:
  - remove
  - purge
selection_dpkg:
  Image|endswith: /dpkg
  CommandLine|contains:
  - '--remove '
  - ' -r '
selection_rpm:
  Image|endswith: /rpm
  CommandLine|contains: ' -e '
condition: 1 of selection_*
```

## False Positives

- Administrator or administrator scripts might delete packages for several reasons (debugging, troubleshooting).

## References

- https://sysdig.com/blog/mitre-defense-evasion-falco
- https://www.tutorialspoint.com/how-to-install-a-software-on-linux-using-yum-command
- https://linuxhint.com/uninstall_yum_package/
- https://linuxhint.com/uninstall-debian-packages/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_remove_package.yml)
