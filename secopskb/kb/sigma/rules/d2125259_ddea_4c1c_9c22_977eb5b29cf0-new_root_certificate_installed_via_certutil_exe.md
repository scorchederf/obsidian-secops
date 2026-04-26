---
sigma_id: "d2125259-ddea-4c1c-9c22-977eb5b29cf0"
title: "New Root Certificate Installed Via Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certutil_certificate_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_certificate_installation.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d2125259-ddea-4c1c-9c22-977eb5b29cf0"
  - "New Root Certificate Installed Via Certutil.EXE"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Root Certificate Installed Via Certutil.EXE

Detects execution of "certutil" with the "addstore" flag in order to install a new certificate on the system.
Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary controlled web servers.

## Metadata

- Rule ID: d2125259-ddea-4c1c-9c22-977eb5b29cf0
- Status: test
- Level: medium
- Author: oscd.community, @redcanary, Zach Stanford @svch0st
- Date: 2023-03-05
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_certutil_certificate_installation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \certutil.exe
- OriginalFileName: CertUtil.exe
selection_cli_add:
  CommandLine|contains|windash: -addstore
selection_cli_store:
  CommandLine|contains: root
condition: all of selection_*
```

## False Positives

- Help Desk or IT may need to manually add a corporate Root CA on occasion. Need to test if GPO push doesn't trigger FP

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.004/T1553.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_certificate_installation.yml)
