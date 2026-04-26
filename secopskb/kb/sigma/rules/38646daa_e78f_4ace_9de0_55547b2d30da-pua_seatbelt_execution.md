---
sigma_id: "38646daa-e78f-4ace-9de0-55547b2d30da"
title: "PUA - Seatbelt Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_seatbelt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_seatbelt.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "38646daa-e78f-4ace-9de0-55547b2d30da"
  - "PUA - Seatbelt Execution"
attack_technique_ids:
  - "T1526"
  - "T1087"
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - Seatbelt Execution

Detects the execution of the PUA/Recon tool Seatbelt via PE information of command line parameters

## Metadata

- Rule ID: 38646daa-e78f-4ace-9de0-55547b2d30da
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-18
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_pua_seatbelt.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1526-cloud_service_discovery|T1526]]
- [[kb/attack/techniques/T1087-account_discovery|T1087]]
- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection_img:
- Image|endswith: \Seatbelt.exe
- OriginalFileName: Seatbelt.exe
- Description: Seatbelt
- CommandLine|contains:
  - ' DpapiMasterKeys'
  - ' InterestingProcesses'
  - ' InterestingFiles'
  - ' CertificateThumbprints'
  - ' ChromiumBookmarks'
  - ' ChromiumHistory'
  - ' ChromiumPresence'
  - ' CloudCredentials'
  - ' CredEnum'
  - ' CredGuard'
  - ' FirefoxHistory'
  - ' ProcessCreationEvents'
selection_group_list:
  CommandLine|contains:
  - ' -group=misc'
  - ' -group=remote'
  - ' -group=chromium'
  - ' -group=slack'
  - ' -group=system'
  - ' -group=user'
  - ' -group=all'
selection_group_output:
  CommandLine|contains: ' -outputfile='
condition: selection_img or all of selection_group_*
```

## False Positives

- Unlikely

## References

- https://github.com/GhostPack/Seatbelt
- https://www.bluetangle.dev/2022/08/fastening-seatbelt-on-threat-hunting.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_seatbelt.yml)
