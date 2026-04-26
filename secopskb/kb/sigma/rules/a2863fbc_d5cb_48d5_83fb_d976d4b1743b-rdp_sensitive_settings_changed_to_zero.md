---
sigma_id: "a2863fbc-d5cb-48d5-83fb-d976d4b1743b"
title: "RDP Sensitive Settings Changed to Zero"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_terminal_server_suspicious.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_terminal_server_suspicious.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "a2863fbc-d5cb-48d5-83fb-d976d4b1743b"
  - "RDP Sensitive Settings Changed to Zero"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RDP Sensitive Settings Changed to Zero

Detects tampering of RDP Terminal Service/Server sensitive settings.
Such as allowing unauthorized users access to a system via the 'fAllowUnsolicited' or enabling RDP via 'fDenyTSConnections', etc.

## Metadata

- Rule ID: a2863fbc-d5cb-48d5-83fb-d976d4b1743b
- Status: test
- Level: medium
- Author: Samir Bousseaden, David ANDRE, Roberto Rodriguez @Cyb3rWard0g, Nasreddine Bencherchali
- Date: 2022-09-29
- Modified: 2022-11-26
- Source Path: rules/windows/registry/registry_set/registry_set_terminal_server_suspicious.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith:
  - \fDenyTSConnections
  - \fSingleSessionPerUser
  - \UserAuthentication
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Some of the keys mentioned here could be modified by an administrator while setting group policy (it should be investigated either way)

## References

- https://web.archive.org/web/20200929062532/https://blog.menasec.net/2019/02/threat-hunting-rdp-hijacking-via.html
- http://woshub.com/rds-shadow-how-to-connect-to-a-user-session-in-windows-server-2012-r2/
- https://twitter.com/SagieSec/status/1469001618863624194?t=HRf0eA0W1YYzkTSHb-Ky1A&s=03
- https://threathunterplaybook.com/hunts/windows/190407-RegModEnableRDPConnections/notebook.html
- https://bazaar.abuse.ch/sample/6f3aa9362d72e806490a8abce245331030d1ab5ac77e400dd475748236a6cc81/
- http://etutorials.org/Microsoft+Products/microsoft+windows+server+2003+terminal+services/Chapter+6+Registry/Registry+Keys+for+Terminal+Services/
- https://admx.help/HKLM/SOFTWARE/Policies/Microsoft/Windows%20NT/Terminal%20Services

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_terminal_server_suspicious.yml)
