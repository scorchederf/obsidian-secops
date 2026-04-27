---
sigma_id: "25cde13e-8e20-4c29-b949-4e795b76f16f"
title: "Suspicious Teams Application Related ObjectAcess Event"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_teams_suspicious_objectaccess.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_teams_suspicious_objectaccess.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "25cde13e-8e20-4c29-b949-4e795b76f16f"
  - "Suspicious Teams Application Related ObjectAcess Event"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Teams Application Related ObjectAcess Event

Detects an access to authentication tokens and accounts of Microsoft Teams desktop application.

## Metadata

- Rule ID: 25cde13e-8e20-4c29-b949-4e795b76f16f
- Status: test
- Level: high
- Author: @SerkinValery
- Date: 2022-09-16
- Source Path: rules/windows/builtin/security/win_security_teams_suspicious_objectaccess.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  EventID: 4663
  ObjectName|contains:
  - \Microsoft\Teams\Cookies
  - \Microsoft\Teams\Local Storage\leveldb
filter:
  ProcessName|contains: \Microsoft\Teams\current\Teams.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-tokens-as-cleartext-in-windows-linux-macs/
- https://www.vectra.ai/blogpost/undermining-microsoft-teams-security-by-mining-tokens

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_teams_suspicious_objectaccess.yml)
