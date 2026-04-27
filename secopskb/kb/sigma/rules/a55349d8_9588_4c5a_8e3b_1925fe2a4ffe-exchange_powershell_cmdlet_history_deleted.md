---
sigma_id: "a55349d8-9588-4c5a-8e3b-1925fe2a4ffe"
title: "Exchange PowerShell Cmdlet History Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_exchange_powershell_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_exchange_powershell_logs.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / file_delete"
aliases:
  - "a55349d8-9588-4c5a-8e3b-1925fe2a4ffe"
  - "Exchange PowerShell Cmdlet History Deleted"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the deletion of the Exchange PowerShell cmdlet History logs which may indicate an attempt to destroy forensic evidence

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070: Indicator Removal]]

## Detection

```yaml
selection:
  TargetFilename|startswith: \Logging\CmdletInfra\LocalPowerShell\Cmdlet\
  TargetFilename|contains: _Cmdlet_
condition: selection
```

## False Positives

- Possible FP during log rotation

## References

- https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-server-logs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_exchange_powershell_logs.yml)
