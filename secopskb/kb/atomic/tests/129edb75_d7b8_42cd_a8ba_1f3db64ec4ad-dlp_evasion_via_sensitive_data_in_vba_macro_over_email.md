---
atomic_guid: "129edb75-d7b8-42cd-a8ba-1f3db64ec4ad"
title: "DLP Evasion via Sensitive Data in VBA Macro over email"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "129edb75-d7b8-42cd-a8ba-1f3db64ec4ad"
  - "DLP Evasion via Sensitive Data in VBA Macro over email"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DLP Evasion via Sensitive Data in VBA Macro over email

Upon successful execution, an excel containing VBA Macro containing sensitive data will be sent outside the network using email.
Sensitive data includes about around 20 odd simulated credit card numbers that passes the LUHN check.

## Metadata

- Atomic GUID: 129edb75-d7b8-42cd-a8ba-1f3db64ec4ad
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Input Arguments

### input_file

- description: Path of the XLSM file
- type: path
- default: PathToAtomicsFolder\T1027\src\T1027-cc-macro.xlsm

### receiver

- description: receiver email
- type: string
- default: test@corp.com

### sender

- description: sender email
- type: string
- default: test@corp.com

### smtp_server

- description: SMTP Server IP Address
- type: string
- default: 127.0.0.1

## Executor

- name: powershell

### Command

```powershell
Send-MailMessage -From #{sender} -To #{receiver} -Subject 'T1027_Atomic_Test' -Attachments "#{input_file}" -SmtpServer #{smtp_server}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
