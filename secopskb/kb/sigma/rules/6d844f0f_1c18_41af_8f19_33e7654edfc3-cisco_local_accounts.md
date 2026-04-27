---
sigma_id: "6d844f0f-1c18-41af-8f19-33e7654edfc3"
title: "Cisco Local Accounts"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_local_accounts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_local_accounts.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "cisco / aaa"
aliases:
  - "6d844f0f-1c18-41af-8f19-33e7654edfc3"
  - "Cisco Local Accounts"
attack_technique_ids:
  - "T1136.001"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Find local accounts being created or modified as well as remote authentication configurations

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098: Account Manipulation]]

## Detection

```yaml
keywords:
- username
- aaa
condition: keywords
```

## False Positives

- When remote authentication is in place, this should not change often

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_local_accounts.yml)
