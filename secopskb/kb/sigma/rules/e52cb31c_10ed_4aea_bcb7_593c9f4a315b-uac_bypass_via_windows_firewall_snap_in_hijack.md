---
sigma_id: "e52cb31c-10ed-4aea-bcb7-593c9f4a315b"
title: "UAC Bypass via Windows Firewall Snap-In Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_hijacking_firwall_snap_in.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_hijacking_firwall_snap_in.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e52cb31c-10ed-4aea-bcb7-593c9f4a315b"
  - "UAC Bypass via Windows Firewall Snap-In Hijack"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass via Windows Firewall Snap-In Hijack

Detects attempts to bypass User Account Control (UAC) by hijacking the Microsoft Management Console (MMC) Windows Firewall snap-in

## Metadata

- Rule ID: e52cb31c-10ed-4aea-bcb7-593c9f4a315b
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-27
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_hijacking_firwall_snap_in.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  ParentImage|endswith: \mmc.exe
  ParentCommandLine|contains: WF.msc
filter:
  Image|endswith: \WerFault.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/uac-bypass-via-windows-firewall-snap-in-hijack.html#uac-bypass-via-windows-firewall-snap-in-hijack

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_hijacking_firwall_snap_in.yml)
