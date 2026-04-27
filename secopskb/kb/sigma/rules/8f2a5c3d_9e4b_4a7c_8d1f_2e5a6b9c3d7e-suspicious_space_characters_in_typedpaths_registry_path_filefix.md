---
sigma_id: "8f2a5c3d-9e4b-4a7c-8d1f-2e5a6b9c3d7e"
title: "Suspicious Space Characters in TypedPaths Registry Path - FileFix"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_typedpaths_space_characters.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_typedpaths_space_characters.yml"
build_date: "2026-04-27 19:13:57"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "8f2a5c3d-9e4b-4a7c-8d1f-2e5a6b9c3d7e"
  - "Suspicious Space Characters in TypedPaths Registry Path - FileFix"
attack_technique_ids:
  - "T1204.004"
  - "T1027.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the occurrence of numerous space characters in TypedPaths registry paths, which may indicate execution via phishing lures using file-fix techniques to hide malicious commands.

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
  TargetObject|endswith: \Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths\url1
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
- https://mrd0x.com/filefix-clickfix-alternative/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_typedpaths_space_characters.yml)
