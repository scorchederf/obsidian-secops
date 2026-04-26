---
sigma_id: "871b9555-69ca-4993-99d3-35a59f9f3599"
title: "Suspicious UltraVNC Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ultravnc_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ultravnc_susp_execution.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "871b9555-69ca-4993-99d3-35a59f9f3599"
  - "Suspicious UltraVNC Execution"
attack_technique_ids:
  - "T1021.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious UltraVNC Execution

Detects suspicious UltraVNC command line flag combination that indicate a auto reconnect upon execution, e.g. startup (as seen being used by Gamaredon threat group)

## Metadata

- Rule ID: 871b9555-69ca-4993-99d3-35a59f9f3599
- Status: test
- Level: high
- Author: Bhabesh Raj
- Date: 2022-03-04
- Modified: 2022-03-09
- Source Path: rules/windows/process_creation/proc_creation_win_ultravnc_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.005]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - '-autoreconnect '
  - '-connect '
  - '-id:'
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20220224045756/https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine
- https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution
- https://uvnc.com/docs/uvnc-viewer/52-ultravnc-viewer-commandline-parameters.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ultravnc_susp_execution.yml)
