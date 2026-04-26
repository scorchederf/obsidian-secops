---
sigma_id: "8eef149c-bd26-49f2-9e5a-9b00e3af499b"
title: "Pass the Hash Activity 2"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_pass_the_hash_2.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_pass_the_hash_2.yml"
build_date: "2026-04-26 14:14:30"
status: "stable"
level: "medium"
logsource: "windows / security"
aliases:
  - "8eef149c-bd26-49f2-9e5a-9b00e3af499b"
  - "Pass the Hash Activity 2"
attack_technique_ids:
  - "T1550.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Pass the Hash Activity 2

Detects the attack technique pass the hash which is used to move laterally inside the network

## Metadata

- Rule ID: 8eef149c-bd26-49f2-9e5a-9b00e3af499b
- Status: stable
- Level: medium
- Author: Dave Kennedy, Jeff Warren (method) / David Vassallo (rule)
- Date: 2019-06-14
- Modified: 2022-10-05
- Source Path: rules/windows/builtin/security/account_management/win_security_pass_the_hash_2.yml

## Logsource

- definition: The successful use of PtH for lateral movement between workstations would trigger event ID 4624
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

## Detection

```yaml
selection_logon3:
  EventID: 4624
  SubjectUserSid: S-1-0-0
  LogonType: 3
  LogonProcessName: NtLmSsp
  KeyLength: 0
selection_logon9:
  EventID: 4624
  LogonType: 9
  LogonProcessName: seclogo
filter:
  TargetUserName: ANONYMOUS LOGON
condition: 1 of selection_* and not filter
```

## False Positives

- Administrator activity

## References

- https://github.com/iadgov/Event-Forwarding-Guidance/tree/master/Events
- https://web.archive.org/web/20170909091934/https://blog.binarydefense.com/reliably-detecting-pass-the-hash-through-event-log-analysis
- https://blog.stealthbits.com/how-to-detect-pass-the-hash-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_pass_the_hash_2.yml)
