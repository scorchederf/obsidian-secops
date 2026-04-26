---
sigma_id: "9a132afa-654e-11eb-ae93-0242ac130002"
title: "PUA - AdFind Suspicious Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_adfind_susp_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_adfind_susp_usage.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9a132afa-654e-11eb-ae93-0242ac130002"
  - "PUA - AdFind Suspicious Execution"
attack_technique_ids:
  - "T1018"
  - "T1087.002"
  - "T1482"
  - "T1069.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - AdFind Suspicious Execution

Detects AdFind execution with common flags seen used during attacks

## Metadata

- Rule ID: 9a132afa-654e-11eb-ae93-0242ac130002
- Status: test
- Level: high
- Author: Janantha Marasinghe (https://github.com/blueteam0ps), FPT.EagleEye Team, omkar72, oscd.community
- Date: 2021-02-02
- Modified: 2025-10-24
- Source Path: rules/windows/process_creation/proc_creation_win_pua_adfind_susp_usage.yml

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
selection:
  CommandLine|contains:
  - domainlist
  - trustdmp
  - dcmodes
  - adinfo
  - -sc dclist
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
condition: selection
```

## False Positives

- Legitimate admin activity

## Simulation

### Adfind - Enumerate Active Directory Computer Objects

- Atomic Test: [[kb/atomic/tests/a889f5be_2d54_4050_bd05_884578748bb4-adfind_enumerate_active_directory_computer_objects|a889f5be-2d54-4050-bd05-884578748bb4]]
- atomic_guid: a889f5be-2d54-4050-bd05-884578748bb4
- name: Adfind - Enumerate Active Directory Computer Objects
- technique: T1018
- type: atomic-red-team

### Adfind - Enumerate Active Directory Domain Controller Objects

- Atomic Test: [[kb/atomic/tests/5838c31e_a0e2_4b9f_b60a_d79d2cb7995e-adfind_enumerate_active_directory_domain_controller_objects|5838c31e-a0e2-4b9f-b60a-d79d2cb7995e]]
- atomic_guid: 5838c31e-a0e2-4b9f-b60a-d79d2cb7995e
- name: Adfind - Enumerate Active Directory Domain Controller Objects
- technique: T1018
- type: atomic-red-team

## References

- https://www.joeware.net/freetools/tools/adfind/
- https://thedfirreport.com/2020/05/08/adfind-recon/
- https://thedfirreport.com/2021/01/11/trickbot-still-alive-and-well/
- https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/
- https://social.technet.microsoft.com/wiki/contents/articles/7535.adfind-command-examples.aspx
- https://github.com/center-for-threat-informed-defense/adversary_emulation_library/blob/bf62ece1c679b07b5fb49c4bae947fe24c81811f/fin6/Emulation_Plan/Phase1.md
- https://github.com/redcanaryco/atomic-red-team/blob/0f229c0e42bfe7ca736a14023836d65baa941ed2/atomics/T1087.002/T1087.002.md#atomic-test-7---adfind---enumerate-active-directory-user-objects

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_adfind_susp_usage.yml)
