---
sigma_id: "66b6be3d-55d0-4f47-9855-d69df21740ea"
title: "Local User Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_user_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_creation.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "66b6be3d-55d0-4f47-9855-d69df21740ea"
  - "Local User Creation"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local User Creation

Detects local user creation on Windows servers, which shouldn't happen in an Active Directory environment. Apply this Sigma Use Case on your Windows server logs and not on your DC logs.

## Metadata

- Rule ID: 66b6be3d-55d0-4f47-9855-d69df21740ea
- Status: test
- Level: low
- Author: Patrick Bareiss
- Date: 2019-04-18
- Modified: 2021-01-17
- Source Path: rules/windows/builtin/security/win_security_user_creation.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection:
  EventID: 4720
condition: selection
```

## False Positives

- Domain Controller Logs
- Local accounts managed by privileged account management tools

## References

- https://patrick-bareiss.com/detecting-local-user-creation-in-ad-with-sigma/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_creation.yml)
