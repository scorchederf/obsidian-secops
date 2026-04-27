---
sigma_id: "e92a4287-e072-4a40-9739-370c106bb750"
title: "HackTool - SOAPHound Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_soaphound_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_soaphound_execution.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e92a4287-e072-4a40-9739-370c106bb750"
  - "HackTool - SOAPHound Execution"
attack_technique_ids:
  - "T1087"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of SOAPHound, a .NET tool for collecting Active Directory data, using specific command-line arguments that may indicate an attempt to extract sensitive AD information.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087: Account Discovery]]

## Detection

```yaml
selection_1:
  CommandLine|contains:
  - ' --buildcache '
  - ' --bhdump '
  - ' --certdump '
  - ' --dnsdump '
selection_2:
  CommandLine|contains:
  - ' -c '
  - ' --cachefilename '
  - ' -o '
  - ' --outputdirectory'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/FalconForceTeam/SOAPHound
- https://medium.com/falconforce/soaphound-tool-to-collect-active-directory-data-via-adws-165aca78288c

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_soaphound_execution.yml)
