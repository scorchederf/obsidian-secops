---
sigma_id: "cbb9e3d1-2386-4e59-912e-62f1484f7a89"
title: "Conhost Spawned By Uncommon Parent Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_conhost_uncommon_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_uncommon_parent.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cbb9e3d1-2386-4e59-912e-62f1484f7a89"
  - "Conhost Spawned By Uncommon Parent Process"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Conhost Spawned By Uncommon Parent Process

Detects when the Console Window Host (conhost.exe) process is spawned by an uncommon parent process, which could be indicative of potential code injection activity.

## Metadata

- Rule ID: cbb9e3d1-2386-4e59-912e-62f1484f7a89
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-28
- Modified: 2025-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_conhost_uncommon_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  Image|endswith: \conhost.exe
  ParentImage|endswith:
  - \explorer.exe
  - \lsass.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \services.exe
  - \smss.exe
  - \spoolsv.exe
  - \svchost.exe
  - \userinit.exe
  - \wininit.exe
  - \winlogon.exe
filter_main_svchost:
  ParentCommandLine|contains:
  - -k apphost -s AppHostSvc
  - -k imgsvc
  - -k localService -p -s RemoteRegistry
  - -k LocalSystemNetworkRestricted -p -s NgcSvc
  - -k NetSvcs -p -s NcaSvc
  - -k netsvcs -p -s NetSetupSvc
  - -k netsvcs -p -s wlidsvc
  - -k NetworkService -p -s DoSvc
  - -k wsappx -p -s AppXSvc
  - -k wsappx -p -s ClipSVC
  - -k wusvcs -p -s WaaSMedicSvc
filter_optional_dropbox:
  ParentCommandLine|contains:
  - C:\Program Files (x86)\Dropbox\Client\
  - C:\Program Files\Dropbox\Client\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/conhost-spawned-by-suspicious-parent-process.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_uncommon_parent.yml)
