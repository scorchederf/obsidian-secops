---
sigma_id: "35bc7e28-ee6b-492f-ab04-da58fcf6402e"
title: "Windows Network Access Suspicious desktop.ini Action"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_net_share_obj_susp_desktop_ini.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_net_share_obj_susp_desktop_ini.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "35bc7e28-ee6b-492f-ab04-da58fcf6402e"
  - "Windows Network Access Suspicious desktop.ini Action"
attack_technique_ids:
  - "T1547.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Network Access Suspicious desktop.ini Action

Detects unusual processes accessing desktop.ini remotely over network share, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.

## Metadata

- Rule ID: 35bc7e28-ee6b-492f-ab04-da58fcf6402e
- Status: test
- Level: medium
- Author: Tim Shelton (HAWK.IO)
- Date: 2021-12-06
- Modified: 2022-01-16
- Source Path: rules/windows/builtin/security/win_security_net_share_obj_susp_desktop_ini.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.009]]

## Detection

```yaml
selection:
  EventID: 5145
  ObjectType: File
  RelativeTargetName|endswith: \desktop.ini
  AccessList|contains:
  - WriteData
  - DELETE
  - WriteDAC
  - AppendData
  - AddSubdirectory
condition: selection
```

## False Positives

- Read only access list authority

## References

- https://isc.sans.edu/forums/diary/Desktopini+as+a+postexploitation+tool/25912/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_net_share_obj_susp_desktop_ini.yml)
