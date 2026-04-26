---
sigma_id: "516376b4-05cd-4122-bae0-ad7641c38d48"
title: "Mailbox Export to Exchange Webserver"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/msexchange/win_exchange_proxyshell_mailbox_export.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxyshell_mailbox_export.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "critical"
logsource: "windows / msexchange-management"
aliases:
  - "516376b4-05cd-4122-bae0-ad7641c38d48"
  - "Mailbox Export to Exchange Webserver"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mailbox Export to Exchange Webserver

Detects a successful export of an Exchange mailbox to untypical directory or with aspx name suffix which can be used to place a webshell or the needed role assignment for it

## Metadata

- Rule ID: 516376b4-05cd-4122-bae0-ad7641c38d48
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems), Rich Warren, Christian Burkard (Nextron Systems)
- Date: 2021-08-09
- Modified: 2023-04-30
- Source Path: rules/windows/builtin/msexchange/win_exchange_proxyshell_mailbox_export.yml

## Logsource

- product: windows
- service: msexchange-management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
export_command:
  '|all':
  - New-MailboxExportRequest
  - ' -Mailbox '
export_params:
- -FilePath "\\\\
- .aspx
role_assignment:
  '|all':
  - New-ManagementRoleAssignment
  - ' -Role "Mailbox Import Export"'
  - ' -User '
condition: (export_command and export_params) or role_assignment
```

## False Positives

- Unlikely

## References

- https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-exchange-part-1.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxyshell_mailbox_export.yml)
