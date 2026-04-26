---
sigma_id: "bd33d2aa-497e-4651-9893-5c5364646595"
title: "Suspicious TCP Tunnel Via PowerShell Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_proxy_scripts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_proxy_scripts.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "bd33d2aa-497e-4651-9893-5c5364646595"
  - "Suspicious TCP Tunnel Via PowerShell Script"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious TCP Tunnel Via PowerShell Script

Detects powershell scripts that creates sockets/listeners which could be indicative of tunneling activity

## Metadata

- Rule ID: bd33d2aa-497e-4651-9893-5c5364646595
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-08
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_proxy_scripts.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - '[System.Net.HttpWebRequest]'
  - System.Net.Sockets.TcpListener
  - AcceptTcpClient
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Arno0x/PowerShellScripts/blob/a6b7d5490fbf0b20f91195838f3a11156724b4f7/proxyTunnel.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_proxy_scripts.yml)
