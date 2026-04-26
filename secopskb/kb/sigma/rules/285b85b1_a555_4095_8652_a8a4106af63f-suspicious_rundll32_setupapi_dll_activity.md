---
sigma_id: "285b85b1-a555-4095-8652-a8a4106af63f"
title: "Suspicious Rundll32 Setupapi.dll Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "285b85b1-a555-4095-8652-a8a4106af63f"
  - "Suspicious Rundll32 Setupapi.dll Activity"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Rundll32 Setupapi.dll Activity

setupapi.dll library provide InstallHinfSection function for processing INF files. INF file may contain instructions allowing to create values in the registry, modify files and install drivers. This technique could be used to obtain persistence via modifying one of Run or RunOnce registry keys, run process or use other DLLs chain calls (see references) InstallHinfSection function in setupapi.dll calls runonce.exe executable regardless of actual content of INF file.

## Metadata

- Rule ID: 285b85b1-a555-4095-8652-a8a4106af63f
- Status: test
- Level: medium
- Author: Konstantin Grishchenko, oscd.community
- Date: 2020-10-07
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  Image|endswith: \runonce.exe
  ParentImage|endswith: \rundll32.exe
  ParentCommandLine|contains|all:
  - setupapi.dll
  - InstallHinfSection
condition: selection
```

## False Positives

- Scripts and administrative tools that use INF files for driver installation with setupapi.dll

## References

- https://lolbas-project.github.io/lolbas/Libraries/Setupapi/
- https://gist.githubusercontent.com/bohops/0cc6586f205f3691e04a1ebf1806aabd/raw/baf7b29891bb91e76198e30889fbf7d6642e8974/calc_exe.inf
- https://raw.githubusercontent.com/huntresslabs/evading-autoruns/master/shady.inf
- https://twitter.com/Z3Jpa29z/status/1313742350292746241?s=20

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml)
