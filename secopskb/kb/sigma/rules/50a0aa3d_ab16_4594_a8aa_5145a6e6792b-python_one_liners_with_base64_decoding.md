---
sigma_id: "50a0aa3d-ab16-4594-a8aa-5145a6e6792b"
title: "Python One-Liners with Base64 Decoding"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_python_base64_encoded_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_base64_encoded_execution.yml"
build_date: "2026-04-27 19:13:55"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "50a0aa3d-ab16-4594-a8aa-5145a6e6792b"
  - "Python One-Liners with Base64 Decoding"
attack_technique_ids:
  - "T1059.006"
  - "T1027.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Python one-liners that use base64 decoding functions in command line executions.
Malicious scripts or attackers often use python one-liners to decode and execute base64-encoded payloads, which is a common technique for obfuscation and evasion.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027010-command-obfuscation|T1027.010: Command Obfuscation]]

## Detection

```yaml
selection_img:
- Image|contains: \python
- OriginalFileName|contains: python
selection_cli:
  CommandLine|contains|all:
  - import
  - base64
  - ' -c'
  CommandLine|contains:
  - .decode
  - b16decode
  - b32decode
  - b32hexdecode
  - b64decode
  - b85decode
  - z85decode
condition: all of selection_*
```

## False Positives

- Legitimate use of Python for decoding data, which is uncommon in typical enterprise environments but possible in development or data analysis contexts.

## References

- https://docs.python.org/3/library/base64.html
- https://www.virustotal.com/gui/file/bc43e925d7b4b74319f6e74e836a96f1997ba404e14ac566cf12a21e9da463db/behavior
- https://cloud.google.com/blog/topics/threat-intelligence/cybercriminals-weaponize-fake-ai-websites

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_base64_encoded_execution.yml)
