---
sigma_id: "cacef8fc-9d3d-41f7-956d-455c6e881bc5"
title: "Potential RemoteFXvGPUDisablement.EXE Abuse - PowerShell ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_remotefxvgpudisablement_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_remotefxvgpudisablement_abuse.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "cacef8fc-9d3d-41f7-956d-455c6e881bc5"
  - "Potential RemoteFXvGPUDisablement.EXE Abuse - PowerShell ScriptBlock"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential RemoteFXvGPUDisablement.EXE Abuse - PowerShell ScriptBlock

Detects PowerShell module creation where the module Contents are set to "function Get-VMRemoteFXPhysicalVideoAdapter". This could be a sign of potential abuse of the "RemoteFXvGPUDisablement.exe" binary which is known to be vulnerable to module load-order hijacking.

## Metadata

- Rule ID: cacef8fc-9d3d-41f7-956d-455c6e881bc5
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-09
- Source Path: rules/windows/powershell/powershell_script/posh_ps_remotefxvgpudisablement_abuse.yml

## Logsource

- category: ps_script
- definition: bade5735-5ab0-4aa7-a642-a11be0e40872
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ScriptBlockText|startswith: function Get-VMRemoteFXPhysicalVideoAdapter {
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://github.com/redcanaryco/AtomicTestHarnesses/blob/7e1e4da116801e3d6fcc6bedb207064577e40572/TestHarnesses/T1218_SignedBinaryProxyExecution/InvokeRemoteFXvGPUDisablementCommand.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_remotefxvgpudisablement_abuse.yml)
