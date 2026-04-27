---
sigma_id: "32d56ea1-417f-44ff-822b-882873f5f43b"
title: "Impacket PsExec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_impacket_psexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_impacket_psexec.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "32d56ea1-417f-44ff-822b-882873f5f43b"
  - "Impacket PsExec Execution"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Impacket PsExec Execution

Detects execution of Impacket's psexec.py.

## Metadata

- Rule ID: 32d56ea1-417f-44ff-822b-882873f5f43b
- Status: test
- Level: high
- Author: Bhabesh Raj
- Date: 2020-12-14
- Modified: 2022-09-22
- Source Path: rules/windows/builtin/security/win_security_impacket_psexec.yml

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
  RelativeTargetName|contains:
  - RemCom_stdin
  - RemCom_stdout
  - RemCom_stderr
condition: selection1
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230329171218/https://blog.menasec.net/2019/02/threat-hunting-3-detecting-psexec.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_impacket_psexec.yml)
