---
sigma_id: "f674e36a-4b91-431e-8aef-f8a96c2aca35"
title: "CurrentControlSet Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentcontrolset.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentcontrolset.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "f674e36a-4b91-431e-8aef-f8a96c2aca35"
  - "CurrentControlSet Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CurrentControlSet Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: f674e36a-4b91-431e-8aef-f8a96c2aca35
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentcontrolset.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
system_control_base:
  TargetObject|contains: \SYSTEM\CurrentControlSet\Control
system_control_keys:
  TargetObject|contains:
  - \Terminal Server\WinStations\RDP-Tcp\InitialProgram
  - \Terminal Server\Wds\rdpwd\StartupPrograms
  - \SecurityProviders\SecurityProviders
  - \SafeBoot\AlternateShell
  - \Print\Providers
  - \Print\Monitors
  - \NetworkProvider\Order
  - \Lsa\Notification Packages
  - \Lsa\Authentication Packages
  - \BootVerificationProgram\ImagePath
filter_empty:
  Details: (Empty)
filter_cutepdf:
  Image: C:\Windows\System32\spoolsv.exe
  TargetObject|contains: \Print\Monitors\CutePDF Writer Monitor
  Details:
  - cpwmon64_v40.dll
  - CutePDF Writer
filter_onenote:
  Image: C:\Windows\System32\spoolsv.exe
  TargetObject|contains: Print\Monitors\Appmon\Ports\Microsoft.Office.OneNote_
  User|contains:
  - AUTHORI
  - AUTORI
filter_poqexec:
  Image: C:\Windows\System32\poqexec.exe
  TargetObject|endswith: \NetworkProvider\Order\ProviderOrder
filter_realvnc:
  Image: C:\Windows\System32\spoolsv.exe
  TargetObject|endswith: \Print\Monitors\MONVNC\Driver
  Details: VNCpm.dll
condition: all of system_control_* and not 1 of filter_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentcontrolset.yml)
