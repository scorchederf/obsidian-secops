---
sigma_id: "f65e22f9-819e-4f96-9c7b-498364ae7a25"
title: "Potential RemoteFXvGPUDisablement.EXE Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_remotefxvgpudisablement_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_remotefxvgpudisablement_abuse.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / powershell-classic"
aliases:
  - "f65e22f9-819e-4f96-9c7b-498364ae7a25"
  - "Potential RemoteFXvGPUDisablement.EXE Abuse"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential RemoteFXvGPUDisablement.EXE Abuse

Detects PowerShell module creation where the module Contents are set to "function Get-VMRemoteFXPhysicalVideoAdapter". This could be a sign of potential abuse of  the "RemoteFXvGPUDisablement.exe" binary which is known to be vulnerable to module load-order hijacking.

## Metadata

- Rule ID: f65e22f9-819e-4f96-9c7b-498364ae7a25
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-07-13
- Modified: 2023-05-09
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_remotefxvgpudisablement_abuse.yml

## Logsource

- definition: fields have to be extract from event
- product: windows
- service: powershell-classic

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Data|contains: ModuleContents=function Get-VMRemoteFXPhysicalVideoAdapter {
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://github.com/redcanaryco/AtomicTestHarnesses/blob/7e1e4da116801e3d6fcc6bedb207064577e40572/TestHarnesses/T1218_SignedBinaryProxyExecution/InvokeRemoteFXvGPUDisablementCommand.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_remotefxvgpudisablement_abuse.yml)
