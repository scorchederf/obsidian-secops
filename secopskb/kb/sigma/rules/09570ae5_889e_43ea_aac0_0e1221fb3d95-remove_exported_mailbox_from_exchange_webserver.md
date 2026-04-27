---
sigma_id: "09570ae5-889e-43ea-aac0-0e1221fb3d95"
title: "Remove Exported Mailbox from Exchange Webserver"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/msexchange/win_exchange_proxyshell_remove_mailbox_export.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxyshell_remove_mailbox_export.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / msexchange-management"
aliases:
  - "09570ae5-889e-43ea-aac0-0e1221fb3d95"
  - "Remove Exported Mailbox from Exchange Webserver"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remove Exported Mailbox from Exchange Webserver

Detects removal of an exported Exchange mailbox which could be to cover tracks from ProxyShell exploit

## Metadata

- Rule ID: 09570ae5-889e-43ea-aac0-0e1221fb3d95
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-27
- Modified: 2023-01-23
- Source Path: rules/windows/builtin/msexchange/win_exchange_proxyshell_remove_mailbox_export.yml

## Logsource

- product: windows
- service: msexchange-management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
keywords:
  '|all':
  - Remove-MailboxExportRequest
  - ' -Identity '
  - ' -Confirm "False"'
condition: keywords
```

## False Positives

- Unknown

## References

- https://github.com/rapid7/metasploit-framework/blob/1416b5776d963f21b7b5b45d19f3e961201e0aed/modules/exploits/windows/http/exchange_proxyshell_rce.rb#L430

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxyshell_remove_mailbox_export.yml)
