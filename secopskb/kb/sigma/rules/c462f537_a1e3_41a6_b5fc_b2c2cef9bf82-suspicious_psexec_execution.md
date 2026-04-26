---
sigma_id: "c462f537-a1e3-41a6-b5fc-b2c2cef9bf82"
title: "Suspicious PsExec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_psexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_psexec.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "c462f537-a1e3-41a6-b5fc-b2c2cef9bf82"
  - "Suspicious PsExec Execution"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious PsExec Execution

detects execution of psexec or paexec with renamed service name, this rule helps to filter out the noise if psexec is used for legit purposes or if attacker uses a different psexec client other than sysinternal one

## Metadata

- Rule ID: c462f537-a1e3-41a6-b5fc-b2c2cef9bf82
- Status: test
- Level: high
- Author: Samir Bousseaden
- Date: 2019-04-03
- Modified: 2022-08-11
- Source Path: rules/windows/builtin/security/win_security_susp_psexec.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection1:
  EventID: 5145
  ShareName: \\\\\*\\IPC$
  RelativeTargetName|endswith:
  - -stdin
  - -stdout
  - -stderr
filter:
  RelativeTargetName|startswith: PSEXESVC
condition: selection1 and not filter
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230329171218/https://blog.menasec.net/2019/02/threat-hunting-3-detecting-psexec.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_psexec.yml)
