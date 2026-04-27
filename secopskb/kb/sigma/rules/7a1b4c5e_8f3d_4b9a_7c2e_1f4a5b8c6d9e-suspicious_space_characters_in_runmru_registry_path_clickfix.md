---
sigma_id: "7a1b4c5e-8f3d-4b9a-7c2e-1f4a5b8c6d9e"
title: "Suspicious Space Characters in RunMRU Registry Path - ClickFix"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_runmru_space_character.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_runmru_space_character.yml"
build_date: "2026-04-27 19:13:57"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "7a1b4c5e-8f3d-4b9a-7c2e-1f4a5b8c6d9e"
  - "Suspicious Space Characters in RunMRU Registry Path - ClickFix"
attack_technique_ids:
  - "T1204.004"
  - "T1027.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the occurrence of numerous space characters in RunMRU registry paths, which may indicate execution via phishing lures using clickfix techniques to hide malicious commands in the Windows Run dialog box from naked eyes.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution#^t1204004-malicious-copy-and-paste|T1204.004: Malicious Copy and Paste]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027010-command-obfuscation|T1027.010: Command Obfuscation]]

## Detection

```yaml
selection_key:
  TargetObject|contains: \Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU\
  Details|contains: '#'
selection_space_variation:
  Details|contains:
  -             
  -             
  -             
  -             
  -             
  -             
  -             
  -             
  -             
  -             
  -             
  -             
  - '            '
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://expel.com/blog/cache-smuggling-when-a-picture-isnt-a-thousand-words/
- https://github.com/JohnHammond/recaptcha-phish

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_runmru_space_character.yml)
