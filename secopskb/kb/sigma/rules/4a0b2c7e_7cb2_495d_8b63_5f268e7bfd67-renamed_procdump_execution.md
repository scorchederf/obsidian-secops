---
sigma_id: "4a0b2c7e-7cb2-495d-8b63-5f268e7bfd67"
title: "Renamed ProcDump Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_sysinternals_procdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_procdump.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4a0b2c7e-7cb2-495d-8b63-5f268e7bfd67"
  - "Renamed ProcDump Execution"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Renamed ProcDump Execution

Detects the execution of a renamed ProcDump executable.
This often done by attackers or malware in order to evade defensive mechanisms.

## Metadata

- Rule ID: 4a0b2c7e-7cb2-495d-8b63-5f268e7bfd67
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-11-18
- Modified: 2024-06-25
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_sysinternals_procdump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection_ofn:
  OriginalFileName: procdump
selection_cli_dump_flag:
  CommandLine|contains|windash:
  - ' -ma '
  - ' -mp '
selection_cli_eula_flag:
  CommandLine|contains|windash: ' /accepteula'
filter_main_known_names:
  Image|endswith:
  - \procdump.exe
  - \procdump64.exe
condition: (selection_ofn or all of selection_cli_*) and not 1 of filter_main_*
```

## False Positives

- Procdump illegally bundled with legitimate software.
- Administrators who rename binaries (should be investigated).

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/procdump

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_procdump.yml)
