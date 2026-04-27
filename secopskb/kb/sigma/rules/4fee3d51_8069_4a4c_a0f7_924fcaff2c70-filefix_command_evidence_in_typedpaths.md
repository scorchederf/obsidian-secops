---
sigma_id: "4fee3d51-8069-4a4c-a0f7-924fcaff2c70"
title: "FileFix - Command Evidence in TypedPaths"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_filefix_typedpath_commands.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_filefix_typedpath_commands.yml"
build_date: "2026-04-27 19:13:51"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "4fee3d51-8069-4a4c-a0f7-924fcaff2c70"
  - "FileFix - Command Evidence in TypedPaths"
attack_technique_ids:
  - "T1204.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects commonly-used chained commands and strings in the most recent 'url' value of the 'TypedPaths' key, which could be indicative of a user being targeted by the FileFix technique.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution#^t1204004-malicious-copy-and-paste|T1204.004: Malicious Copy and Paste]]

## Detection

```yaml
selection_base:
  TargetObject|endswith: \Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths\url1
  Details|contains|all:
  - '#'
  - http
selection_cmd:
- Details|contains:
  - account
  - anti-bot
  - botcheck
  - captcha
  - challenge
  - confirmation
  - fraud
  - human
  - identification
  - identificator
  - identity
  - robot
  - validation
  - verification
  - verify
- Details|contains:
  - '%comspec%'
  - bitsadmin
  - certutil
  - cmd
  - cscript
  - curl
  - finger
  - mshta
  - powershell
  - pwsh
  - regsvr32
  - rundll32
  - schtasks
  - wget
  - wscript
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://x.com/russianpanda9xx/status/1940831134759506029
- https://mrd0x.com/filefix-clickfix-alternative/
- https://www.scpx.com.au/2025/11/16/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_filefix_typedpath_commands.yml)
