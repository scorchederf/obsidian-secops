---
sigma_id: "7892ec59-c5bb-496d-8968-e5d210ca3ac4"
title: "DPAPI Backup Keys And Certificate Export Activity IOC"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_dpapi_backup_and_cert_export_ioc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_dpapi_backup_and_cert_export_ioc.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "7892ec59-c5bb-496d-8968-e5d210ca3ac4"
  - "DPAPI Backup Keys And Certificate Export Activity IOC"
attack_technique_ids:
  - "T1555"
  - "T1552.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DPAPI Backup Keys And Certificate Export Activity IOC

Detects file names with specific patterns seen generated and used by tools such as Mimikatz and DSInternals related to exported or stolen DPAPI backup keys and certificates.

## Metadata

- Rule ID: 7892ec59-c5bb-496d-8968-e5d210ca3ac4
- Status: test
- Level: high
- Author: Nounou Mbeiri, Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-06-26
- Source Path: rules/windows/file/file_event/file_event_win_susp_dpapi_backup_and_cert_export_ioc.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Detection

```yaml
selection:
  TargetFilename|contains:
  - ntds_capi_
  - ntds_legacy_
  - ntds_unknown_
  TargetFilename|endswith:
  - .cer
  - .key
  - .pfx
  - .pvk
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.dsinternals.com/en/dpapi-backup-key-theft-auditing/
- https://github.com/MichaelGrafnetter/DSInternals/blob/39ee8a69bbdc1cfd12c9afdd7513b4788c4895d4/Src/DSInternals.Common/Data/DPAPI/DPAPIBackupKey.cs#L28-L32

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_dpapi_backup_and_cert_export_ioc.yml)
