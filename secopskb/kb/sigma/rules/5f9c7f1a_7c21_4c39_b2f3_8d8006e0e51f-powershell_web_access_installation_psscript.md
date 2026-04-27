---
sigma_id: "5f9c7f1a-7c21-4c39-b2f3-8d8006e0e51f"
title: "PowerShell Web Access Installation - PsScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_powershell_web_access_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_powershell_web_access_installation.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "5f9c7f1a-7c21-4c39-b2f3-8d8006e0e51f"
  - "PowerShell Web Access Installation - PsScript"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Web Access Installation - PsScript

Detects the installation and configuration of PowerShell Web Access, which could be used for remote access and potential abuse

## Metadata

- Rule ID: 5f9c7f1a-7c21-4c39-b2f3-8d8006e0e51f
- Status: test
- Level: high
- Author: Michael Haag
- Date: 2024-09-03
- Source Path: rules/windows/powershell/powershell_script/posh_ps_powershell_web_access_installation.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_install:
  ScriptBlockText|contains: Install-WindowsFeature WindowsPowerShellWebAccess
selection_config:
  ScriptBlockText|contains: Install-PswaWebApplication
selection_auth:
  ScriptBlockText|contains|all:
  - Add-PswaAuthorizationRule
  - -UserName *
  - -ComputerName *
condition: 1 of selection_*
```

## False Positives

- Legitimate PowerShell Web Access installations by administrators

## References

- https://docs.microsoft.com/en-us/powershell/module/powershellwebaccess/install-pswawebapplication
- https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-241a
- https://gist.github.com/MHaggis/7e67b659af9148fa593cf2402edebb41

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_powershell_web_access_installation.yml)
