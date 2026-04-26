---
sigma_id: "d04ae2b8-ad54-4de0-bd87-4bc1da66aa59"
title: "Kerberoasting Activity - Initial Query"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_kerberoasting_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_kerberoasting_activity.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "d04ae2b8-ad54-4de0-bd87-4bc1da66aa59"
  - "Kerberoasting Activity - Initial Query"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kerberoasting Activity - Initial Query

This rule will collect the data needed to start looking into possible kerberoasting activity.
Further analysis or computation within the query is needed focusing on requests from one specific host/IP towards multiple service names within a time period of 5 seconds.
You can then set a threshold for the number of requests and time between the requests to turn this into an alert.

## Metadata

- Rule ID: d04ae2b8-ad54-4de0-bd87-4bc1da66aa59
- Status: test
- Level: medium
- Author: @kostastsale
- Date: 2022-01-21
- Modified: 2025-10-19
- Source Path: rules/windows/builtin/security/win_security_kerberoasting_activity.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection:
  EventID: 4769
  Status: '0x0'
  TicketEncryptionType: '0x17'
filter_main_krbtgt:
  ServiceName|endswith:
  - krbtgt
  - $
filter_main_machine_accounts:
  TargetUserName|contains: $@
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legacy applications.

## References

- https://www.trustedsec.com/blog/art_of_kerberoast/
- https://adsecurity.org/?p=3513

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_kerberoasting_activity.yml)
