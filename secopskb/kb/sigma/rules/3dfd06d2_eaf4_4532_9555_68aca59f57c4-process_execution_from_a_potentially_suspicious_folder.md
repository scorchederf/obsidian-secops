---
sigma_id: "3dfd06d2-eaf4-4532-9555-68aca59f57c4"
title: "Process Execution From A Potentially Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_execution_path.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_execution_path.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "3dfd06d2-eaf4-4532-9555-68aca59f57c4"
  - "Process Execution From A Potentially Suspicious Folder"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a potentially suspicious execution from an uncommon folder.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]

## Detection

```yaml
selection:
  Image|contains:
  - :\Perflogs\
  - :\Users\All Users\
  - :\Users\Default\
  - :\Users\NetworkService\
  - :\Windows\addins\
  - :\Windows\debug\
  - :\Windows\Fonts\
  - :\Windows\Help\
  - :\Windows\IME\
  - :\Windows\Media\
  - :\Windows\repair\
  - :\Windows\security\
  - :\Windows\System32\Tasks\
  - :\Windows\Tasks\
  - $Recycle.bin
  - \config\systemprofile\
  - \Intel\Logs\
  - \RSA\MachineKeys\
filter_optional_ibm:
  Image|startswith: C:\Users\Public\IBM\ClientSolutions\Start_Programs\
filter_optional_citrix:
  Image|startswith: C:\Windows\SysWOW64\config\systemprofile\Citrix\UpdaterBinaries\
  Image|endswith: \CitrixReceiverUpdater.exe
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://github.com/mbevilacqua/appcompatprocessor/blob/6c847937c5a836e2ce2fe2b915f213c345a3c389/AppCompatSearch.txt
- https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses
- https://www.crowdstrike.com/resources/reports/2019-crowdstrike-global-threat-report/
- https://github.com/ThreatHuntingProject/ThreatHunting/blob/cb22598bb70651f88e0285abc8d835757d2cb596/hunts/suspicious_process_creation_via_windows_event_logs.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_execution_path.yml)
