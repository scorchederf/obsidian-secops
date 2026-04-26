---
sigma_id: "3ceb2083-a27f-449a-be33-14ec1b7cc973"
title: "Silence.EDA Detection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_apt_silence_eda.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_apt_silence_eda.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "critical"
logsource: "windows / ps_script"
aliases:
  - "3ceb2083-a27f-449a-be33-14ec1b7cc973"
  - "Silence.EDA Detection"
attack_technique_ids:
  - "T1059.001"
  - "T1071.004"
  - "T1572"
  - "T1529"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Silence.EDA Detection

Detects Silence EmpireDNSAgent as described in the Group-IP report

## Metadata

- Rule ID: 3ceb2083-a27f-449a-be33-14ec1b7cc973
- Status: test
- Level: critical
- Author: Alina Stepchenkova, Group-IB, oscd.community
- Date: 2019-11-01
- Modified: 2023-04-03
- Source Path: rules/windows/powershell/powershell_script/posh_ps_apt_silence_eda.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.004]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]
- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

### Software Tags

- S0363

## Detection

```yaml
empire:
  ScriptBlockText|contains|all:
  - System.Diagnostics.Process
  - Stop-Computer
  - Restart-Computer
  - Exception in execution
  - $cmdargs
  - Close-Dnscat2Tunnel
dnscat:
  ScriptBlockText|contains|all:
  - set type=$LookupType`nserver
  - $Command | nslookup 2>&1 | Out-String
  - New-RandomDNSField
  - '[Convert]::ToString($SYNOptions, 16)'
  - $Session.Dead = $True
  - $Session["Driver"] -eq
condition: empire and dnscat
```

## False Positives

- Unknown

## References

- https://www.group-ib.com/resources/threat-research/silence_2.0.going_global.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_apt_silence_eda.yml)
