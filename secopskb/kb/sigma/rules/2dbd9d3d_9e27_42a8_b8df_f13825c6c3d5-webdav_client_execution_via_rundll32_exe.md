---
sigma_id: "2dbd9d3d-9e27-42a8-b8df-f13825c6c3d5"
title: "WebDav Client Execution Via Rundll32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_execution.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2dbd9d3d-9e27-42a8-b8df-f13825c6c3d5"
  - "WebDav Client Execution Via Rundll32.EXE"
attack_technique_ids:
  - "T1048.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WebDav Client Execution Via Rundll32.EXE

Detects "svchost.exe" spawning "rundll32.exe" with command arguments like "C:\windows\system32\davclnt.dll,DavSetCookie".
This could be an indicator of exfiltration or use of WebDav to launch code (hosted on a WebDav server).

## Metadata

- Rule ID: 2dbd9d3d-9e27-42a8-b8df-f13825c6c3d5
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-05-02
- Modified: 2023-09-18
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \svchost.exe
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains: C:\windows\system32\davclnt.dll,DavSetCookie
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/17
- https://github.com/OTRF/ThreatHunter-Playbook/blob/2d4257f630f4c9770f78d0c1df059f891ffc3fec/docs/evals/apt29/detections/7.B.4_C10730EA-6345-4934-AA0F-B0EFCA0C4BA6.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_execution.yml)
