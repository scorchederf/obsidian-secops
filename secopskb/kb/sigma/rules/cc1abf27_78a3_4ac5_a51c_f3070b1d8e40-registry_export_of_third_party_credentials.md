---
sigma_id: "cc1abf27-78a3-4ac5-a51c-f3070b1d8e40"
title: "Registry Export of Third-Party Credentials"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_export_of_thirdparty_creds.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_export_of_thirdparty_creds.yml"
build_date: "2026-04-26 15:01:50"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cc1abf27-78a3-4ac5-a51c-f3070b1d8e40"
  - "Registry Export of Third-Party Credentials"
attack_technique_ids:
  - "T1552.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry Export of Third-Party Credentials

Detects the use of reg.exe to export registry paths associated with third-party credentials.
Credential stealers have been known to use this technique to extract sensitive information from the registry.

## Metadata

- Rule ID: cc1abf27-78a3-4ac5-a51c-f3070b1d8e40
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-05-22
- Source Path: rules/windows/process_creation/proc_creation_win_registry_export_of_thirdparty_creds.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_cli_save:
  CommandLine|contains:
  - save
  - export
selection_cli_path:
  CommandLine|contains:
  - \Software\Aerofox\Foxmail\V3.1
  - \Software\Aerofox\FoxmailPreview
  - \Software\DownloadManager\Passwords
  - \Software\FTPWare\COREFTP\Sites
  - \Software\IncrediMail\Identities
  - \Software\Martin Prikryl\WinSCP 2\Sessions
  - \Software\Mobatek\MobaXterm
  - \Software\OpenSSH\Agent\Keys
  - \Software\OpenVPN-GUI\configs
  - \Software\ORL\WinVNC3\Password
  - \Software\Qualcomm\Eudora\CommandLine
  - \Software\RealVNC\WinVNC4
  - \Software\RimArts\B2\Settings
  - \Software\SimonTatham\PuTTY\Sessions
  - \Software\SimonTatham\PuTTY\SshHostKeys
  - \Software\Sota\FFFTP
  - \Software\TightVNC\Server
  - \Software\WOW6432Node\Radmin\v3.0\Server\Parameters\Radmin
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.virustotal.com/gui/file/fdc86a5b3d7df37a72c3272836f743747c47bfbc538f05af9ecf78547fa2e789/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_export_of_thirdparty_creds.yml)
