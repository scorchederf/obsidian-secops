---
sigma_id: "87a476dc-0079-4583-a985-dee7a20a03de"
title: "Enumeration for 3rd Party Creds From CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_enumeration_for_credentials_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_enumeration_for_credentials_cli.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "87a476dc-0079-4583-a985-dee7a20a03de"
  - "Enumeration for 3rd Party Creds From CLI"
attack_technique_ids:
  - "T1552.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enumeration for 3rd Party Creds From CLI

Detects processes that query known 3rd party registry keys that holds credentials via commandline

## Metadata

- Rule ID: 87a476dc-0079-4583-a985-dee7a20a03de
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-20
- Modified: 2025-05-22
- Source Path: rules/windows/process_creation/proc_creation_win_registry_enumeration_for_credentials_cli.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.002]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - \Software\Aerofox\Foxmail\V3.1
  - \Software\Aerofox\FoxmailPreview
  - \Software\DownloadManager\Passwords
  - \Software\FTPWare\COREFTP\Sites
  - \Software\IncrediMail\Identities
  - \Software\Martin Prikryl\WinSCP 2\Sessions
  - \Software\Mobatek\MobaXterm\
  - \Software\OpenSSH\Agent\Keys
  - \Software\OpenVPN-GUI\configs
  - \Software\ORL\WinVNC3\Password
  - \Software\Qualcomm\Eudora\CommandLine
  - \Software\RealVNC\WinVNC4
  - \Software\RimArts\B2\Settings
  - \Software\SimonTatham\PuTTY\Sessions
  - \Software\SimonTatham\PuTTY\SshHostKeys\
  - \Software\Sota\FFFTP
  - \Software\TightVNC\Server
  - \Software\WOW6432Node\Radmin\v3.0\Server\Parameters\Radmin
filter_main_other_rule:
  Image|endswith: reg.exe
  CommandLine|contains:
  - export
  - save
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://isc.sans.edu/diary/More+Data+Exfiltration/25698
- https://github.com/synacktiv/Radmin3-Password-Cracker/blob/acfc87393e4b7c06353973a14a6c7126a51f36ac/regkey.txt
- https://github.com/HyperSine/how-does-MobaXterm-encrypt-password
- https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#inside-the-registry

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_enumeration_for_credentials_cli.yml)
