---
sigma_id: "488b44e7-3781-4a71-888d-c95abfacf44d"
title: "Windows Firewall Profile Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_windows_firewall_profile_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_windows_firewall_profile_disabled.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "488b44e7-3781-4a71-888d-c95abfacf44d"
  - "Windows Firewall Profile Disabled"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Firewall Profile Disabled

Detects when a user disables the Windows Firewall via a Profile to help evade defense.

## Metadata

- Rule ID: 488b44e7-3781-4a71-888d-c95abfacf44d
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-10-12
- Modified: 2022-12-30
- Source Path: rules/windows/powershell/powershell_script/posh_ps_windows_firewall_profile_disabled.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection_args:
  ScriptBlockText|contains|all:
  - 'Set-NetFirewallProfile '
  - ' -Enabled '
  - ' False'
selection_opt:
  ScriptBlockText|contains:
  - ' -All '
  - Public
  - Domain
  - Private
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/powershell/module/netsecurity/set-netfirewallprofile?view=windowsserver2022-ps
- https://www.tutorialspoint.com/how-to-get-windows-firewall-profile-settings-using-powershell
- https://web.archive.org/web/20230929023836/http://powershellhelp.space/commands/set-netfirewallrule-psv5.php
- http://woshub.com/manage-windows-firewall-powershell/
- https://www.elastic.co/guide/en/security/current/windows-firewall-disabled-via-powershell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_windows_firewall_profile_disabled.yml)
