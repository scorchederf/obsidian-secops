---
sigma_id: "941e5c45-cda7-4864-8cea-bbb7458d194a"
title: "Suspicious Remote Logon with Explicit Credentials"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_logon_explicit_credentials.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_logon_explicit_credentials.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "941e5c45-cda7-4864-8cea-bbb7458d194a"
  - "Suspicious Remote Logon with Explicit Credentials"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Remote Logon with Explicit Credentials

Detects suspicious processes logging on with explicit credentials

## Metadata

- Rule ID: 941e5c45-cda7-4864-8cea-bbb7458d194a
- Status: test
- Level: medium
- Author: oscd.community, Teymur Kheirkhabarov @HeirhabarovT, Zach Stanford @svch0st, Tim Shelton
- Date: 2020-10-05
- Modified: 2022-08-03
- Source Path: rules/windows/builtin/security/win_security_susp_logon_explicit_credentials.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  EventID: 4648
  ProcessName|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \winrs.exe
  - \wmic.exe
  - \net.exe
  - \net1.exe
  - \reg.exe
filter1:
  TargetServerName: localhost
filter2:
  SubjectUserName|endswith: $
  TargetUserName|endswith: $
condition: selection and not 1 of filter*
```

## False Positives

- Administrators that use the RunAS command or scheduled tasks

## References

- https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_logon_explicit_credentials.yml)
