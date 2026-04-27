---
sigma_id: "3f6b7b62-61aa-45db-96bd-9c31b36b653c"
title: "RDP Sensitive Settings Changed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_terminal_server_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_terminal_server_tampering.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "3f6b7b62-61aa-45db-96bd-9c31b36b653c"
  - "RDP Sensitive Settings Changed"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# RDP Sensitive Settings Changed

Detects tampering of RDP Terminal Service/Server sensitive settings.
Such as allowing unauthorized users access to a system via the 'fAllowUnsolicited' or enabling RDP via 'fDenyTSConnections', etc.

Below is a list of registry keys/values that are monitored by this rule:

- Shadow: Used to enable Remote Desktop shadowing, which allows an administrator to view or control a user's session.
- DisableRemoteDesktopAntiAlias: Disables anti-aliasing for remote desktop sessions.
- DisableSecuritySettings: Disables certain security settings for Remote Desktop connections.
- fAllowUnsolicited: Allows unsolicited remote assistance offers.
- fAllowUnsolicitedFullControl: Allows unsolicited remote assistance offers with full control.
- InitialProgram: Specifies a program to run automatically when a user logs on to a remote computer.
- ServiceDll: Used in RDP hijacking techniques to specify a custom DLL to be loaded by the Terminal Services service.
- SecurityLayer: Specifies the security layer used for RDP connections.

## Metadata

- Rule ID: 3f6b7b62-61aa-45db-96bd-9c31b36b653c
- Status: test
- Level: high
- Author: Samir Bousseaden, David ANDRE, Roberto Rodriguez @Cyb3rWard0g, Nasreddine Bencherchali
- Date: 2022-08-06
- Modified: 2025-11-22
- Source Path: rules/windows/registry/registry_set/registry_set_terminal_server_tampering.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_shadow:
  TargetObject|contains:
  - \Control\Terminal Server\
  - \Windows NT\Terminal Services\
  TargetObject|endswith: \Shadow
  Details:
  - DWORD (0x00000001)
  - DWORD (0x00000002)
  - DWORD (0x00000003)
  - DWORD (0x00000004)
selection_terminal_services_key:
  TargetObject|contains:
  - \Control\Terminal Server\
  - \Windows NT\Terminal Services\
  TargetObject|endswith:
  - \DisableRemoteDesktopAntiAlias
  - \DisableSecuritySettings
  - \fAllowUnsolicited
  - \fAllowUnsolicitedFullControl
  Details: DWORD (0x00000001)
selection_tamper_only:
  TargetObject|contains:
  - \Control\Terminal Server\InitialProgram
  - \Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram
  - \services\TermService\Parameters\ServiceDll
  - \Terminal Server\WinStations\RDP-Tcp\SecurityLayer
  - \Windows NT\Terminal Services\InitialProgram
filter_main_securitylayer_tls:
  TargetObject|endswith: \SecurityLayer
  Details: DWORD (0x00000002)
condition: (selection_shadow or selection_terminal_services_key or selection_tamper_only)
  and not 1 of filter_main_*
```

## False Positives

- Some of the keys mentioned here could be modified by an administrator while setting group policy (it should be investigated either way)

## References

- http://etutorials.org/Microsoft+Products/microsoft+windows+server+2003+terminal+services/Chapter+6+Registry/Registry+Keys+for+Terminal+Services/
- http://woshub.com/rds-shadow-how-to-connect-to-a-user-session-in-windows-server-2012-r2/
- https://admx.help/HKLM/SOFTWARE/Policies/Microsoft/Windows%20NT/Terminal%20Services
- https://bazaar.abuse.ch/sample/6f3aa9362d72e806490a8abce245331030d1ab5ac77e400dd475748236a6cc81/
- https://blog.sekoia.io/darkgate-internals/
- https://blog.talosintelligence.com/understanding-the-phobos-affiliate-structure/
- https://github.com/redcanaryco/atomic-red-team/blob/02c7d02fe1f1feb0fc7944550408ea8224273994/atomics/T1112/T1112.md#atomic-test-63---disable-remote-desktop-anti-alias-setting-through-registry
- https://github.com/redcanaryco/atomic-red-team/blob/02c7d02fe1f1feb0fc7944550408ea8224273994/atomics/T1112/T1112.md#atomic-test-64---disable-remote-desktop-security-settings-through-registry
- https://github.com/redcanaryco/atomic-red-team/blob/dd526047b8c399c312fee47d1e6fb531164da54d/atomics/T1112/T1112.yaml#L790
- https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-terminalservices-rdp-winstationextensions-securitylayer
- https://threathunterplaybook.com/hunts/windows/190407-RegModEnableRDPConnections/notebook.html
- https://twitter.com/SagieSec/status/1469001618863624194?t=HRf0eA0W1YYzkTSHb-Ky1A&s=03
- https://web.archive.org/web/20200929062532/https://blog.menasec.net/2019/02/threat-hunting-rdp-hijacking-via.html
- https://www.trendmicro.com/en_us/research/25/i/unmasking-the-gentlemen-ransomware.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_terminal_server_tampering.yml)
