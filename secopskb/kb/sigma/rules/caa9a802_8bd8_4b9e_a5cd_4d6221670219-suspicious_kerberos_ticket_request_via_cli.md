---
sigma_id: "caa9a802-8bd8-4b9e-a5cd-4d6221670219"
title: "Suspicious Kerberos Ticket Request via CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_kerberos_kerberos_ticket_request_via_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_kerberos_kerberos_ticket_request_via_cli.yml"
build_date: "2026-04-26 17:03:23"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "caa9a802-8bd8-4b9e-a5cd-4d6221670219"
  - "Suspicious Kerberos Ticket Request via CLI"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Kerberos Ticket Request via CLI

Detects suspicious Kerberos ticket requests via command line using System.IdentityModel.Tokens.KerberosRequestorSecurityToken class.
Threat actors may use command line interfaces to request Kerberos tickets for service accounts in order to
perform offline password cracking attacks commonly known as Kerberoasting or other Kerberos ticket abuse
techniques like silver ticket attacks.

## Metadata

- Rule ID: caa9a802-8bd8-4b9e-a5cd-4d6221670219
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-18
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_kerberos_kerberos_ticket_request_via_cli.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - powershell.exe
  - pwsh.dll
selection_cli:
  CommandLine|contains|all:
  - System.IdentityModel.Tokens.KerberosRequestorSecurityToken
  - .GetRequest()
condition: all of selection_*
```

## False Positives

- Legitimate command line usage by administrators or security tools.

## References

- https://www.huntress.com/blog/gootloader-threat-detection-woff2-obfuscation
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1558.003/T1558.003.md#atomic-test-4---request-a-single-ticket-via-powershell
- https://learn.microsoft.com/en-us/dotnet/api/system.identitymodel.tokens.kerberosrequestorsecuritytoken?view=netframework-4.8.1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_kerberos_kerberos_ticket_request_via_cli.yml)
