---
sigma_id: "eee00933-a761-4cd0-be70-c42fe91731e7"
title: "Arbitrary File Download Via GfxDownloadWrapper.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gfxdownloadwrapper_arbitrary_file_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gfxdownloadwrapper_arbitrary_file_download.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "eee00933-a761-4cd0-be70-c42fe91731e7"
  - "Arbitrary File Download Via GfxDownloadWrapper.EXE"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via GfxDownloadWrapper.EXE

Detects execution of GfxDownloadWrapper.exe with a URL as an argument to download file.

## Metadata

- Rule ID: eee00933-a761-4cd0-be70-c42fe91731e7
- Status: test
- Level: medium
- Author: Victor Sergeev, oscd.community
- Date: 2020-10-09
- Modified: 2023-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_gfxdownloadwrapper_arbitrary_file_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|endswith: \GfxDownloadWrapper.exe
  CommandLine|contains:
  - http://
  - https://
filter_main_known_urls:
  CommandLine|contains: https://gameplayapi.intel.com/
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/HonorableMentions/GfxDownloadWrapper/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gfxdownloadwrapper_arbitrary_file_download.yml)
