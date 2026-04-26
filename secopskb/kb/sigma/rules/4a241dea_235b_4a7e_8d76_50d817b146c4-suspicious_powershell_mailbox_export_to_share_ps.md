---
sigma_id: "4a241dea-235b-4a7e-8d76-50d817b146c4"
title: "Suspicious PowerShell Mailbox Export to Share - PS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_mailboxexport_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_mailboxexport_share.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "critical"
logsource: "windows / ps_script"
aliases:
  - "4a241dea-235b-4a7e-8d76-50d817b146c4"
  - "Suspicious PowerShell Mailbox Export to Share - PS"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Mailbox Export to Share - PS

Detects usage of the powerShell New-MailboxExportRequest Cmdlet to exports a mailbox to a remote or local share, as used in ProxyShell exploitations

## Metadata

- Rule ID: 4a241dea-235b-4a7e-8d76-50d817b146c4
- Status: test
- Level: critical
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-26
- Source Path: rules/windows/powershell/powershell_script/posh_ps_mailboxexport_share.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_mailboxexport_share.yml)
