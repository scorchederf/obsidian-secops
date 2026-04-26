---
sigma_id: "145322e4-0fd3-486b-81ca-9addc75736d8"
title: "Use of UltraVNC Remote Access Software"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ultravnc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ultravnc.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "145322e4-0fd3-486b-81ca-9addc75736d8"
  - "Use of UltraVNC Remote Access Software"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of UltraVNC Remote Access Software

An adversary may use legitimate desktop support and remote access software,to establish an interactive command and control channel to target systems within networks

## Metadata

- Rule ID: 145322e4-0fd3-486b-81ca-9addc75736d8
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-10-02
- Source Path: rules/windows/process_creation/proc_creation_win_ultravnc.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
- Description: VNCViewer
- Product: UltraVNC VNCViewer
- Company: UltraVNC
- OriginalFileName: VNCViewer.exe
condition: selection
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/9e5b12c4912c07562aec7500447b11fa3e17e254/atomics/T1219/T1219.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ultravnc.yml)
