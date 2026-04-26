---
sigma_id: "8d85cf08-bf97-4260-ba49-986a2a65129c"
title: "Suspicious PowerShell In Registry Run Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_powershell_in_run_keys.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_in_run_keys.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "8d85cf08-bf97-4260-ba49-986a2a65129c"
  - "Suspicious PowerShell In Registry Run Keys"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell In Registry Run Keys

Detects potential PowerShell commands or code within registry run keys

## Metadata

- Rule ID: 8d85cf08-bf97-4260-ba49-986a2a65129c
- Status: test
- Level: medium
- Author: frack113, Florian Roth (Nextron Systems)
- Date: 2022-03-17
- Modified: 2025-07-18
- Source Path: rules/windows/registry/registry_set/registry_set_powershell_in_run_keys.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Software\Microsoft\Windows\CurrentVersion\Run
  - \Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
  - \Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
  Details|contains:
  - powershell
  - 'pwsh '
  - FromBase64String
  - .DownloadFile(
  - .DownloadString(
  - ' -w hidden '
  - ' -w 1 '
  - -windowstyle hidden
  - -window hidden
  - ' -nop '
  - ' -encodedcommand '
  - -ExecutionPolicy Bypass
  - Invoke-Expression
  - IEX (
  - Invoke-Command
  - ICM -
  - Invoke-WebRequest
  - 'IWR '
  - Invoke-RestMethod
  - 'IRM '
  - ' -noni '
  - ' -noninteractive '
condition: selection
```

## False Positives

- Legitimate admin or third party scripts. Baseline according to your environment

## References

- https://github.com/frack113/atomic-red-team/blob/a9051c38de8a5320b31c7039efcbd3b56cf2d65a/atomics/T1547.001/T1547.001.md#atomic-test-9---systembc-malware-as-a-service-registry
- https://www.trendmicro.com/en_us/research/22/j/lv-ransomware-exploits-proxyshell-in-attack.html
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_in_run_keys.yml)
