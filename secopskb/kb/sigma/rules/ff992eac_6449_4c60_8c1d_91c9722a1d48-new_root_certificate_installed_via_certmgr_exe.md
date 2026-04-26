---
sigma_id: "ff992eac-6449-4c60-8c1d-91c9722a1d48"
title: "New Root Certificate Installed Via CertMgr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certmgr_certificate_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certmgr_certificate_installation.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ff992eac-6449-4c60-8c1d-91c9722a1d48"
  - "New Root Certificate Installed Via CertMgr.EXE"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Root Certificate Installed Via CertMgr.EXE

Detects execution of "certmgr" with the "add" flag in order to install a new certificate on the system.
Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary controlled web servers.

## Metadata

- Rule ID: ff992eac-6449-4c60-8c1d-91c9722a1d48
- Status: test
- Level: medium
- Author: oscd.community, @redcanary, Zach Stanford @svch0st
- Date: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_certmgr_certificate_installation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \CertMgr.exe
- OriginalFileName: CERTMGT.EXE
selection_cli:
  CommandLine|contains|all:
  - /add
  - root
condition: all of selection_*
```

## False Positives

- Help Desk or IT may need to manually add a corporate Root CA on occasion. Need to test if GPO push doesn't trigger FP

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.004/T1553.004.md
- https://securelist.com/to-crypt-or-to-mine-that-is-the-question/86307/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certmgr_certificate_installation.yml)
