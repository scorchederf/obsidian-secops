---
sigma_id: "0d5675be-bc88-4172-86d3-1e96a4476536"
title: "Potential Tampering With RDP Related Registry Keys Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_rdp_keys_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_rdp_keys_tamper.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0d5675be-bc88-4172-86d3-1e96a4476536"
  - "Potential Tampering With RDP Related Registry Keys Via Reg.EXE"
attack_technique_ids:
  - "T1021.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Tampering With RDP Related Registry Keys Via Reg.EXE

Detects the execution of "reg.exe" for enabling/disabling the RDP service on the host by tampering with the 'CurrentControlSet\Control\Terminal Server' values

## Metadata

- Rule ID: 0d5675be-bc88-4172-86d3-1e96a4476536
- Status: test
- Level: high
- Author: pH-T (Nextron Systems), @Kostastsale, TheDFIRReport
- Date: 2022-02-12
- Modified: 2025-11-22
- Source Path: rules/windows/process_creation/proc_creation_win_reg_rdp_keys_tamper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_main_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_main_cli:
  CommandLine|contains|all:
  - ' add '
  - \CurrentControlSet\Control\Terminal Server
  - REG_DWORD
  - ' /f'
selection_values_1:
  CommandLine|contains|all:
  - Licensing Core
  - EnableConcurrentSessions
selection_values_2:
  CommandLine|contains:
  - AllowTSConnections
  - fDenyTSConnections
  - fEnableWinStation
  - fSingleSessionPerUser
  - IdleWinStationPoolCount
  - MaxInstanceCount
  - SecurityLayer
  - TSAdvertise
  - TSAppCompat
  - TSEnabled
  - TSUserEnabled
  - WinStations\RDP-Tcp
filter_main_values_tls:
  CommandLine|contains|all:
  - SecurityLayer
  - '02'
condition: all of selection_main_* and 1 of selection_values_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/02/21/qbot-and-zerologon-lead-to-full-domain-compromise/
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_rdp_keys_tamper.yml)
