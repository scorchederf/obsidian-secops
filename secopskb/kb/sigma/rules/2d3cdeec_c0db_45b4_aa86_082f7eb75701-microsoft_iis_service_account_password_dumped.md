---
sigma_id: "2d3cdeec-c0db-45b4-aa86-082f7eb75701"
title: "Microsoft IIS Service Account Password Dumped"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iis_appcmd_service_account_password_dumped.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_service_account_password_dumped.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2d3cdeec-c0db-45b4-aa86-082f7eb75701"
  - "Microsoft IIS Service Account Password Dumped"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the Internet Information Services (IIS) command-line tool, AppCmd, being used to list passwords

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

## Detection

```yaml
selection_base_name:
- Image|endswith: \appcmd.exe
- OriginalFileName: appcmd.exe
selection_base_list:
  CommandLine|contains: 'list '
selection_standalone:
  CommandLine|contains:
  - ' /config'
  - ' /xml'
  - ' -config'
  - ' -xml'
selection_cmd_flags:
  CommandLine|contains:
  - ' /@t'
  - ' /text'
  - ' /show'
  - ' -@t'
  - ' -text'
  - ' -show'
selection_cmd_grep:
  CommandLine|contains:
  - :\*
  - password
condition: all of selection_base_* and (selection_standalone or all of selection_cmd_*)
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/microsoft-iis-service-account-password-dumped.html
- https://twitter.com/0gtweet/status/1588815661085917186?cxt=HHwWhIDUyaDbzYwsAAAA
- https://www.netspi.com/blog/technical/network-penetration-testing/decrypting-iis-passwords-to-break-out-of-the-dmz-part-2/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_service_account_password_dumped.yml)
