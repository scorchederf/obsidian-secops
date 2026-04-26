---
sigma_id: "1cf98dc2-fcb0-47c9-8aea-654c9284d1ae"
title: "Disk Image Creation Via Hdiutil - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_hdiutil_create.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_hdiutil_create.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "1cf98dc2-fcb0-47c9-8aea-654c9284d1ae"
  - "Disk Image Creation Via Hdiutil - MacOS"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disk Image Creation Via Hdiutil - MacOS

Detects the execution of the hdiutil utility in order to create a disk image.

## Metadata

- Rule ID: 1cf98dc2-fcb0-47c9-8aea-654c9284d1ae
- Status: test
- Level: medium
- Author: Omar Khaled (@beacon_exe)
- Date: 2024-08-10
- Source Path: rules/macos/process_creation/proc_creation_macos_hdiutil_create.yml

## Logsource

- category: process_creation
- product: macos

## Detection

```yaml
selection:
  Image|endswith: /hdiutil
  CommandLine|contains: create
condition: selection
```

## False Positives

- Legitimate usage of hdiutil by administrators and users.

## References

- https://www.loobins.io/binaries/hdiutil/
- https://www.sentinelone.com/blog/from-the-front-linesunsigned-macos-orat-malware-gambles-for-the-win/
- https://ss64.com/mac/hdiutil.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_hdiutil_create.yml)
