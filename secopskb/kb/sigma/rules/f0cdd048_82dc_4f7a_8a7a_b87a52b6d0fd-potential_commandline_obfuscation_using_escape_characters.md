---
sigma_id: "f0cdd048-82dc-4f7a-8a7a-b87a52b6d0fd"
title: "Potential Commandline Obfuscation Using Escape Characters"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_escape_char.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_escape_char.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f0cdd048-82dc-4f7a-8a7a-b87a52b6d0fd"
  - "Potential Commandline Obfuscation Using Escape Characters"
attack_technique_ids:
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Commandline Obfuscation Using Escape Characters

Detects potential commandline obfuscation using known escape characters

## Metadata

- Rule ID: f0cdd048-82dc-4f7a-8a7a-b87a52b6d0fd
- Status: test
- Level: medium
- Author: juju4
- Date: 2018-12-11
- Modified: 2023-03-03
- Source Path: rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_escape_char.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - h^t^t^p
  - h"t"t"p
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/vysecurity/status/885545634958385153
- https://twitter.com/Hexacorn/status/885553465417756673
- https://twitter.com/Hexacorn/status/885570278637678592
- https://www.mandiant.com/resources/blog/obfuscation-wild-targeted-attackers-lead-way-evasion-techniques
- https://web.archive.org/web/20190213114956/http://www.windowsinspired.com/understanding-the-command-line-string-and-arguments-received-by-a-windows-program/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_escape_char.yml)
