---
sigma_id: "70ad0861-d1fe-491c-a45f-fa48148a300d"
title: "File Download via CertOC.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certoc_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certoc_download.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "70ad0861-d1fe-491c-a45f-fa48148a300d"
  - "File Download via CertOC.EXE"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download via CertOC.EXE

Detects when a user downloads a file by using CertOC.exe

## Metadata

- Rule ID: 70ad0861-d1fe-491c-a45f-fa48148a300d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-05-16
- Modified: 2023-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_certoc_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- Image|endswith: \certoc.exe
- OriginalFileName: CertOC.exe
selection_cli:
  CommandLine|contains|all:
  - -GetCACAPS
  - http
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Certoc/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certoc_download.yml)
