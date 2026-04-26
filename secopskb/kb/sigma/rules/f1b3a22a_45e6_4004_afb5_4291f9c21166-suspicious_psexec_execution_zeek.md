---
sigma_id: "f1b3a22a-45e6-4004-afb5-4291f9c21166"
title: "Suspicious PsExec Execution - Zeek"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_smb_converted_win_susp_psexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_susp_psexec.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "zeek / smb_files"
aliases:
  - "f1b3a22a-45e6-4004-afb5-4291f9c21166"
  - "Suspicious PsExec Execution - Zeek"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious PsExec Execution - Zeek

detects execution of psexec or paexec with renamed service name, this rule helps to filter out the noise if psexec is used for legit purposes or if attacker uses a different psexec client other than sysinternal one

## Metadata

- Rule ID: f1b3a22a-45e6-4004-afb5-4291f9c21166
- Status: test
- Level: high
- Author: Samir Bousseaden, @neu5ron, Tim Shelton
- Date: 2020-04-02
- Modified: 2022-12-27
- Source Path: rules/network/zeek/zeek_smb_converted_win_susp_psexec.yml

## Logsource

- product: zeek
- service: smb_files

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  path|contains|all:
  - \\
  - \IPC$
  name|endswith:
  - -stdin
  - -stdout
  - -stderr
filter:
  name|startswith: PSEXESVC
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230329171218/https://blog.menasec.net/2019/02/threat-hunting-3-detecting-psexec.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_susp_psexec.yml)
