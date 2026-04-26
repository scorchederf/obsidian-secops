---
sigma_id: "38a7625e-b2cb-485d-b83d-aff137d859f4"
title: "Potential RemoteFXvGPUDisablement.EXE Abuse - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_remotefxvgpudisablement_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_remotefxvgpudisablement_abuse.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "38a7625e-b2cb-485d-b83d-aff137d859f4"
  - "Potential RemoteFXvGPUDisablement.EXE Abuse - PowerShell Module"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential RemoteFXvGPUDisablement.EXE Abuse - PowerShell Module

Detects PowerShell module creation where the module Contents are set to "function Get-VMRemoteFXPhysicalVideoAdapter". This could be a sign of potential abuse of the "RemoteFXvGPUDisablement.exe" binary which is known to be vulnerable to module load-order hijacking.

## Metadata

- Rule ID: 38a7625e-b2cb-485d-b83d-aff137d859f4
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2021-07-13
- Modified: 2023-05-09
- Source Path: rules/windows/powershell/powershell_module/posh_pm_remotefxvgpudisablement_abuse.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Payload|contains: ModuleContents=function Get-VMRemoteFXPhysicalVideoAdapter {
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://github.com/redcanaryco/AtomicTestHarnesses/blob/7e1e4da116801e3d6fcc6bedb207064577e40572/TestHarnesses/T1218_SignedBinaryProxyExecution/InvokeRemoteFXvGPUDisablementCommand.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_remotefxvgpudisablement_abuse.yml)
