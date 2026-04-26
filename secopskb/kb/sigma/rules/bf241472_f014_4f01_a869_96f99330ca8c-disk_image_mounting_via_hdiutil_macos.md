---
sigma_id: "bf241472-f014-4f01-a869-96f99330ca8c"
title: "Disk Image Mounting Via Hdiutil - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_hdiutil_mount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_hdiutil_mount.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "bf241472-f014-4f01-a869-96f99330ca8c"
  - "Disk Image Mounting Via Hdiutil - MacOS"
attack_technique_ids:
  - "T1566.001"
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disk Image Mounting Via Hdiutil - MacOS

Detects the execution of the hdiutil utility in order to mount disk images.

## Metadata

- Rule ID: bf241472-f014-4f01-a869-96f99330ca8c
- Status: test
- Level: medium
- Author: Omar Khaled (@beacon_exe)
- Date: 2024-08-10
- Source Path: rules/macos/process_creation/proc_creation_macos_hdiutil_mount.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]
- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection:
  Image|endswith: /hdiutil
  CommandLine|contains:
  - 'attach '
  - 'mount '
condition: selection
```

## False Positives

- Legitimate usage of hdiutil by administrators and users.

## References

- https://www.loobins.io/binaries/hdiutil/
- https://www.sentinelone.com/blog/from-the-front-linesunsigned-macos-orat-malware-gambles-for-the-win/
- https://ss64.com/mac/hdiutil.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_hdiutil_mount.yml)
