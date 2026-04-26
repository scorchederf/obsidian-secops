---
sigma_id: "b37998de-a70b-4f33-b219-ec36bf433dc0"
title: "PUA - PingCastle Execution From Potentially Suspicious Parent"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_pingcastle_script_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_pingcastle_script_parent.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b37998de-a70b-4f33-b219-ec36bf433dc0"
  - "PUA - PingCastle Execution From Potentially Suspicious Parent"
attack_technique_ids:
  - "T1595"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - PingCastle Execution From Potentially Suspicious Parent

Detects the execution of PingCastle, a tool designed to quickly assess the Active Directory security level via a script located in a potentially suspicious or uncommon location.

## Metadata

- Rule ID: b37998de-a70b-4f33-b219-ec36bf433dc0
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), X__Junior (Nextron Systems)
- Date: 2024-01-11
- Source Path: rules/windows/process_creation/proc_creation_win_pua_pingcastle_script_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1595-active_scanning|T1595]]

## Detection

```yaml
selection_parent_ext:
  ParentCommandLine|contains:
  - .bat
  - .chm
  - .cmd
  - .hta
  - .htm
  - .html
  - .js
  - .lnk
  - .ps1
  - .vbe
  - .vbs
  - .wsf
selection_parent_path_1:
  ParentCommandLine|contains:
  - :\Perflogs\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp
  - \AppData\Roaming\
  - \Temporary Internet
selection_parent_path_2:
- ParentCommandLine|contains|all:
  - :\Users\
  - \Favorites\
- ParentCommandLine|contains|all:
  - :\Users\
  - \Favourites\
- ParentCommandLine|contains|all:
  - :\Users\
  - \Contacts\
selection_cli:
- Image|endswith: \PingCastle.exe
- OriginalFileName: PingCastle.exe
- Product: Ping Castle
- CommandLine|contains:
  - --scanner aclcheck
  - --scanner antivirus
  - --scanner computerversion
  - --scanner foreignusers
  - --scanner laps_bitlocker
  - --scanner localadmin
  - --scanner nullsession
  - --scanner nullsession-trust
  - --scanner oxidbindings
  - --scanner remote
  - --scanner share
  - --scanner smb
  - --scanner smb3querynetwork
  - --scanner spooler
  - --scanner startup
  - --scanner zerologon
- CommandLine|contains: --no-enum-limit
- CommandLine|contains|all:
  - --healthcheck
  - --level Full
- CommandLine|contains|all:
  - --healthcheck
  - '--server '
condition: 1 of selection_parent_* and selection_parent_ext and selection_cli
```

## False Positives

- Unknown

## References

- https://github.com/vletoux/pingcastle
- https://thedfirreport.com/2023/10/30/netsupport-intrusion-results-in-domain-compromise/
- https://github.com/fengjixuchui/Start-ADEnum/blob/e237a739db98b6104427d833004836507da36a58/Functions/Start-ADEnum.ps1#L450
- https://github.com/lkys37en/Start-ADEnum/blob/5b42c54215fe5f57fc59abc52c20487d15764005/Functions/Start-ADEnum.ps1#L680
- https://github.com/projectHULK/AD_Recon/blob/dde2daba9b3393a9388cbebda87068972cc0bd3b/SecurityAssessment.ps1#L2699
- https://github.com/802-1x/Compliance/blob/2e53df8b6e89686a0b91116b3f42c8f717dca820/Ping%20Castle/Get-PingCastle-HTMLComplianceReport.ps1#L8
- https://github.com/EvotecIT/TheDashboard/blob/481a9ce8f82f2fd55fe65220ee6486bae6df0c9d/Examples/RunReports/PingCastle.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_pingcastle_script_parent.yml)
