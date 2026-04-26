---
sigma_id: "4a6713f6-3331-11ed-a261-0242ac120002"
title: "Taskkill Symantec Endpoint Protection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_taskkill_sep.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_taskkill_sep.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4a6713f6-3331-11ed-a261-0242ac120002"
  - "Taskkill Symantec Endpoint Protection"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Taskkill Symantec Endpoint Protection

Detects one of the possible scenarios for disabling Symantec Endpoint Protection.
Symantec Endpoint Protection antivirus software services incorrectly implement the protected service mechanism.
As a result, the NT AUTHORITY/SYSTEM user can execute the taskkill /im command several times ccSvcHst.exe /f, thereby killing the process belonging to the service, and thus shutting down the service.

## Metadata

- Rule ID: 4a6713f6-3331-11ed-a261-0242ac120002
- Status: test
- Level: high
- Author: Ilya Krestinichev, Florian Roth (Nextron Systems)
- Date: 2022-09-13
- Source Path: rules/windows/process_creation/proc_creation_win_taskkill_sep.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - taskkill
  - ' /F '
  - ' /IM '
  - ccSvcHst.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.exploit-db.com/exploits/37525
- https://community.spiceworks.com/topic/2195015-batch-script-to-uninstall-symantec-endpoint-protection
- https://community.broadcom.com/symantecenterprise/communities/community-home/digestviewer/viewthread?MessageKey=6ce94b67-74e1-4333-b16f-000b7fd874f0&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=digestviewer

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_taskkill_sep.yml)
