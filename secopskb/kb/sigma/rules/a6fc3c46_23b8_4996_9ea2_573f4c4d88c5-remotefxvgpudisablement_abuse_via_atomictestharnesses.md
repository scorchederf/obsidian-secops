---
sigma_id: "a6fc3c46-23b8-4996-9ea2-573f4c4d88c5"
title: "RemoteFXvGPUDisablement Abuse Via AtomicTestHarnesses"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_remotefxvgpudisablement_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_remotefxvgpudisablement_abuse.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a6fc3c46-23b8-4996-9ea2-573f4c4d88c5"
  - "RemoteFXvGPUDisablement Abuse Via AtomicTestHarnesses"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects calls to the AtomicTestHarnesses "Invoke-ATHRemoteFXvGPUDisablementCommand" which is designed to abuse the "RemoteFXvGPUDisablement.exe" binary to run custom PowerShell code via module load-order hijacking.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - Invoke-ATHRemoteFXvGPUDisablementCommand
  - Invoke-ATHRemoteFXvGPUDisableme
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://github.com/redcanaryco/AtomicTestHarnesses/blob/7e1e4da116801e3d6fcc6bedb207064577e40572/TestHarnesses/T1218_SignedBinaryProxyExecution/InvokeRemoteFXvGPUDisablementCommand.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_remotefxvgpudisablement_abuse.yml)
