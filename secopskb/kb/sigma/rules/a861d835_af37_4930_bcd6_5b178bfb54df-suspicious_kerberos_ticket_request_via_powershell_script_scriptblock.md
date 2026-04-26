---
sigma_id: "a861d835-af37-4930-bcd6-5b178bfb54df"
title: "Suspicious Kerberos Ticket Request via PowerShell Script - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_request_kerberos_ticket.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_request_kerberos_ticket.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "a861d835-af37-4930-bcd6-5b178bfb54df"
  - "Suspicious Kerberos Ticket Request via PowerShell Script - ScriptBlock"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Kerberos Ticket Request via PowerShell Script - ScriptBlock

Detects PowerShell scripts that utilize native PowerShell Identity modules to request Kerberos tickets.
This behavior is typically seen during a Kerberos or silver ticket attack. A successful execution will output the SPNs for the endpoint in question.

## Metadata

- Rule ID: a861d835-af37-4930-bcd6-5b178bfb54df
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-28
- Modified: 2025-11-18
- Source Path: rules/windows/powershell/powershell_script/posh_ps_request_kerberos_ticket.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - System.IdentityModel.Tokens.KerberosRequestorSecurityToken
  - .GetRequest()
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1558.003/T1558.003.md#atomic-test-4---request-a-single-ticket-via-powershell
- https://learn.microsoft.com/en-us/dotnet/api/system.identitymodel.tokens.kerberosrequestorsecuritytoken?view=netframework-4.8.1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_request_kerberos_ticket.yml)
