---
sigma_id: "377f33a1-4b36-4ee1-acee-1dbe4b43cfbe"
title: "Suspicious VSFTPD Error Messages"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/vsftpd/lnx_vsftpd_susp_error_messages.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/vsftpd/lnx_vsftpd_susp_error_messages.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "linux / vsftpd"
aliases:
  - "377f33a1-4b36-4ee1-acee-1dbe4b43cfbe"
  - "Suspicious VSFTPD Error Messages"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious VSFTPD Error Messages

Detects suspicious VSFTPD error messages that indicate a fatal or suspicious error that could be caused by exploiting attempts

## Metadata

- Rule ID: 377f33a1-4b36-4ee1-acee-1dbe4b43cfbe
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-07-05
- Modified: 2021-11-27
- Source Path: rules/linux/builtin/vsftpd/lnx_vsftpd_susp_error_messages.yml

## Logsource

- product: linux
- service: vsftpd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- 'Connection refused: too many sessions for this address.'
- 'Connection refused: tcp_wrappers denial.'
- Bad HTTP verb.
- port and pasv both active
- pasv and port both active
- Transfer done (but failed to open directory).
- Could not set file modification time.
- 'bug: pid active in ptrace_sandbox_free'
- PTRACE_SETOPTIONS failure
- 'weird status:'
- couldn't handle sandbox event
- syscall * out of bounds
- 'syscall not permitted:'
- 'syscall validate failed:'
- Input line too long.
- poor buffer accounting in str_netfd_alloc
- vsf_sysutil_read_loop
condition: keywords
```

## False Positives

- Unknown

## References

- https://github.com/dagwieers/vsftpd/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/vsftpd/lnx_vsftpd_susp_error_messages.yml)
