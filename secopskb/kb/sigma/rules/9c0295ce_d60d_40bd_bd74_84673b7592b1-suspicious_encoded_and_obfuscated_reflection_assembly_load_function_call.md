---
sigma_id: "9c0295ce-d60d-40bd-bd74-84673b7592b1"
title: "Suspicious Encoded And Obfuscated Reflection Assembly Load Function Call"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_reflection_assembly_load_obfusc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_reflection_assembly_load_obfusc.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9c0295ce-d60d-40bd-bd74-84673b7592b1"
  - "Suspicious Encoded And Obfuscated Reflection Assembly Load Function Call"
attack_technique_ids:
  - "T1059.001"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious base64 encoded and obfuscated "LOAD" keyword used in .NET "reflection.assembly"

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - OgA6ACgAIgBMACIAKwAiAG8AYQBkACIAKQ
  - oAOgAoACIATAAiACsAIgBvAGEAZAAiACkA
  - 6ADoAKAAiAEwAIgArACIAbwBhAGQAIgApA
  - OgA6ACgAIgBMAG8AIgArACIAYQBkACIAKQ
  - oAOgAoACIATABvACIAKwAiAGEAZAAiACkA
  - 6ADoAKAAiAEwAbwAiACsAIgBhAGQAIgApA
  - OgA6ACgAIgBMAG8AYQAiACsAIgBkACIAKQ
  - oAOgAoACIATABvAGEAIgArACIAZAAiACkA
  - 6ADoAKAAiAEwAbwBhACIAKwAiAGQAIgApA
  - OgA6ACgAJwBMACcAKwAnAG8AYQBkACcAKQ
  - oAOgAoACcATAAnACsAJwBvAGEAZAAnACkA
  - 6ADoAKAAnAEwAJwArACcAbwBhAGQAJwApA
  - OgA6ACgAJwBMAG8AJwArACcAYQBkACcAKQ
  - oAOgAoACcATABvACcAKwAnAGEAZAAnACkA
  - 6ADoAKAAnAEwAbwAnACsAJwBhAGQAJwApA
  - OgA6ACgAJwBMAG8AYQAnACsAJwBkACcAKQ
  - oAOgAoACcATABvAGEAJwArACcAZAAnACkA
  - 6ADoAKAAnAEwAbwBhACcAKwAnAGQAJwApA
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb2765d0ea08dcb6/yara/mal_revil.yar
- https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/
- https://learn.microsoft.com/en-us/dotnet/api/system.appdomain.load?view=net-7.0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_reflection_assembly_load_obfusc.yml)
