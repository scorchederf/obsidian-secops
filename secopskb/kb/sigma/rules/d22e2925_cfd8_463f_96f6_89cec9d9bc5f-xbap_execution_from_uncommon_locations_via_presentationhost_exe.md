---
sigma_id: "d22e2925-cfd8-463f-96f6-89cec9d9bc5f"
title: "XBAP Execution From Uncommon Locations Via PresentationHost.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_presentationhost_uncommon_location_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_presentationhost_uncommon_location_exec.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d22e2925-cfd8-463f-96f6-89cec9d9bc5f"
  - "XBAP Execution From Uncommon Locations Via PresentationHost.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# XBAP Execution From Uncommon Locations Via PresentationHost.EXE

Detects the execution of ".xbap" (Browser Applications) files via PresentationHost.EXE from an uncommon location. These files can be abused to run malicious ".xbap" files any bypass AWL

## Metadata

- Rule ID: d22e2925-cfd8-463f-96f6-89cec9d9bc5f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-01
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_presentationhost_uncommon_location_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \presentationhost.exe
- OriginalFileName: PresentationHost.exe
selection_cli:
  CommandLine|contains: .xbap
filter_main_generic:
  CommandLine|contains:
  - ' C:\Windows\'
  - ' C:\Program Files'
condition: all of selection* and not 1 of filter_main_*
```

## False Positives

- Legitimate ".xbap" being executed via "PresentationHost"

## References

- https://lolbas-project.github.io/lolbas/Binaries/Presentationhost/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_presentationhost_uncommon_location_exec.yml)
