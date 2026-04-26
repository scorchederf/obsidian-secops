---
sigma_id: "e76b413a-83d0-4b94-8e4c-85db4a5b8bdc"
title: "Suspicious OpenSSH Daemon Error"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/sshd/lnx_sshd_susp_ssh.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/sshd/lnx_sshd_susp_ssh.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux / sshd"
aliases:
  - "e76b413a-83d0-4b94-8e4c-85db4a5b8bdc"
  - "Suspicious OpenSSH Daemon Error"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious OpenSSH Daemon Error

Detects suspicious SSH / SSHD error messages that indicate a fatal or suspicious error that could be caused by exploiting attempts

## Metadata

- Rule ID: e76b413a-83d0-4b94-8e4c-85db4a5b8bdc
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-06-30
- Modified: 2021-11-27
- Source Path: rules/linux/builtin/sshd/lnx_sshd_susp_ssh.yml

## Logsource

- product: linux
- service: sshd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- unexpected internal error
- unknown or unsupported key type
- invalid certificate signing key
- invalid elliptic curve value
- incorrect signature
- error in libcrypto
- unexpected bytes remain after decoding
- 'fatal: buffer_get_string: bad string'
- 'Local: crc32 compensation attack'
- bad client public DH value
- Corrupted MAC on input
condition: keywords
```

## False Positives

- Unknown

## References

- https://github.com/openssh/openssh-portable/blob/c483a5c0fb8e8b8915fad85c5f6113386a4341ca/ssherr.c
- https://github.com/ossec/ossec-hids/blob/1ecffb1b884607cb12e619f9ab3c04f530801083/etc/rules/sshd_rules.xml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/sshd/lnx_sshd_susp_ssh.yml)
