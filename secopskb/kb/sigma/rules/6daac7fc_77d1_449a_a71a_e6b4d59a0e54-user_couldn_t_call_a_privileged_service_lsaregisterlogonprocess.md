---
sigma_id: "6daac7fc-77d1-449a-a71a-e6b4d59a0e54"
title: "User Couldn't Call a Privileged Service 'LsaRegisterLogonProcess'"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_user_couldnt_call_priv_service_lsaregisterlogonprocess.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_couldnt_call_priv_service_lsaregisterlogonprocess.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "6daac7fc-77d1-449a-a71a-e6b4d59a0e54"
  - "User Couldn't Call a Privileged Service 'LsaRegisterLogonProcess'"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# User Couldn't Call a Privileged Service 'LsaRegisterLogonProcess'

The 'LsaRegisterLogonProcess' function verifies that the application making the function call is a logon process by checking that it has the SeTcbPrivilege privilege set. Possible Rubeus tries to get a handle to LSA.

## Metadata

- Rule ID: 6daac7fc-77d1-449a-a71a-e6b4d59a0e54
- Status: test
- Level: high
- Author: Roberto Rodriguez (source), Ilyas Ochkov (rule), oscd.community
- Date: 2019-10-24
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/security/win_security_user_couldnt_call_priv_service_lsaregisterlogonprocess.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection:
  EventID: 4673
  Service: LsaRegisterLogonProcess()
  Keywords: '0x8010000000000000'
condition: selection
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-trusts-71f2b33688e1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_couldnt_call_priv_service_lsaregisterlogonprocess.yml)
