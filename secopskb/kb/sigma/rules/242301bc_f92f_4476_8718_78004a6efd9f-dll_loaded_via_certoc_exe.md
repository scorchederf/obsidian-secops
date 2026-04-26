---
sigma_id: "242301bc-f92f-4476-8718-78004a6efd9f"
title: "DLL Loaded via CertOC.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "242301bc-f92f-4476-8718-78004a6efd9f"
  - "DLL Loaded via CertOC.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DLL Loaded via CertOC.EXE

Detects when a user installs certificates by using CertOC.exe to loads the target DLL file.

## Metadata

- Rule ID: 242301bc-f92f-4476-8718-78004a6efd9f
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-10-23
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \certoc.exe
- OriginalFileName: CertOC.exe
selection_cli:
  CommandLine|contains|windash: ' -LoadDLL '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/sblmsrsn/status/1445758411803480072?s=20
- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-fe98e74189873d6df72a15df2eaa0315c59ba9cdaca93ecd68afc4ea09194ef2
- https://lolbas-project.github.io/lolbas/Binaries/Certoc/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml)
