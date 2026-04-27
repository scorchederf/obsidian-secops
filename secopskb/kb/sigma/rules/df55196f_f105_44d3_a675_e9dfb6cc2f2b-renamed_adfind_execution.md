---
sigma_id: "df55196f-f105-44d3-a675-e9dfb6cc2f2b"
title: "Renamed AdFind Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_adfind.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_adfind.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "df55196f-f105-44d3-a675-e9dfb6cc2f2b"
  - "Renamed AdFind Execution"
attack_technique_ids:
  - "T1018"
  - "T1087.002"
  - "T1482"
  - "T1069.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Renamed AdFind Execution

Detects the use of a renamed Adfind.exe. AdFind continues to be seen across majority of breaches. It is used to domain trust discovery to plan out subsequent steps in the attack chain.

## Metadata

- Rule ID: df55196f-f105-44d3-a675-e9dfb6cc2f2b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-21
- Modified: 2025-02-26
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_adfind.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Detection

```yaml
selection_1:
  CommandLine|contains:
  - domainlist
  - trustdmp
  - dcmodes
  - adinfo
  - ' dclist '
  - computer_pwdnotreqd
  - objectcategory=
  - -subnets -f
  - name="Domain Admins"
  - '-sc u:'
  - domainncs
  - dompol
  - ' oudmp '
  - subnetdmp
  - gpodmp
  - fspdmp
  - users_noexpire
  - computers_active
  - computers_pwdnotreqd
selection_2:
  Hashes|contains:
  - IMPHASH=BCA5675746D13A1F246E2DA3C2217492
  - IMPHASH=53E117A96057EAF19C41380D0E87F1C2
  - IMPHASH=d144de8117df2beceaba2201ad304764
  - IMPHASH=12ce1c0f3f5837ecc18a3782408fa975
  - IMPHASH=4fbf3f084fbbb2470b80b2013134df35
  - IMPHASH=49b639b4acbecc49d72a01f357aa4930
  - IMPHASH=680dad9e300346e05a85023965867201
  - IMPHASH=21aa085d54992511b9f115355e468782
selection_3:
  OriginalFileName: AdFind.exe
filter:
  Image|endswith: \AdFind.exe
condition: 1 of selection* and not filter
```

## False Positives

- Unknown

## References

- https://www.joeware.net/freetools/tools/adfind/
- https://thedfirreport.com/2020/05/08/adfind-recon/
- https://thedfirreport.com/2021/01/11/trickbot-still-alive-and-well/
- https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/
- https://social.technet.microsoft.com/wiki/contents/articles/7535.adfind-command-examples.aspx
- https://github.com/center-for-threat-informed-defense/adversary_emulation_library/blob/bf62ece1c679b07b5fb49c4bae947fe24c81811f/fin6/Emulation_Plan/Phase1.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_adfind.yml)
