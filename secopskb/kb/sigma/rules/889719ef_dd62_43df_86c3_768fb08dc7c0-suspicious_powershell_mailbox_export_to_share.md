---
sigma_id: "889719ef-dd62-43df-86c3-768fb08dc7c0"
title: "Suspicious PowerShell Mailbox Export to Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_mailboxexport_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_mailboxexport_share.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "889719ef-dd62-43df-86c3-768fb08dc7c0"
  - "Suspicious PowerShell Mailbox Export to Share"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Mailbox Export to Share

Detects usage of the powerShell New-MailboxExportRequest Cmdlet to exports a mailbox to a remote or local share, as used in ProxyShell exploitations

## Metadata

- Rule ID: 889719ef-dd62-43df-86c3-768fb08dc7c0
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-08-07
- Modified: 2022-10-26
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_mailboxexport_share.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - New-MailboxExportRequest
  - ' -Mailbox '
  - ' -FilePath \\\\'
condition: selection
```

## False Positives

- Unknown

## References

- https://youtu.be/5mqid-7zp8k?t=2481
- https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-exchange-part-1.html
- https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1
- https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-server-logs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_mailboxexport_share.yml)
