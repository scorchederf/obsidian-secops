---
sigma_id: "62b7ccc9-23b4-471e-aa15-6da3663c4d59"
title: "PowerShell Base64 Encoded Reflective Assembly Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_reflection_assembly_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_reflection_assembly_load.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "62b7ccc9-23b4-471e-aa15-6da3663c4d59"
  - "PowerShell Base64 Encoded Reflective Assembly Load"
attack_technique_ids:
  - "T1059.001"
  - "T1027"
  - "T1620"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Base64 Encoded Reflective Assembly Load

Detects base64 encoded .NET reflective loading of Assembly

## Metadata

- Rule ID: 62b7ccc9-23b4-471e-aa15-6da3663c4d59
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems), pH-T (Nextron Systems)
- Date: 2022-03-01
- Modified: 2023-01-30
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_base64_reflection_assembly_load.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1620-reflective_code_loading|T1620]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - WwBSAGUAZgBsAGUAYwB0AGkAbwBuAC4AQQBzAHMAZQBtAGIAbAB5AF0AOgA6AEwAbwBhAGQAKA
  - sAUgBlAGYAbABlAGMAdABpAG8AbgAuAEEAcwBzAGUAbQBiAGwAeQBdADoAOgBMAG8AYQBkACgA
  - bAFIAZQBmAGwAZQBjAHQAaQBvAG4ALgBBAHMAcwBlAG0AYgBsAHkAXQA6ADoATABvAGEAZAAoA
  - AFsAcgBlAGYAbABlAGMAdABpAG8AbgAuAGEAcwBzAGUAbQBiAGwAeQBdADoAOgAoACIATABvAGEAZAAiAC
  - BbAHIAZQBmAGwAZQBjAHQAaQBvAG4ALgBhAHMAcwBlAG0AYgBsAHkAXQA6ADoAKAAiAEwAbwBhAGQAIgAp
  - AWwByAGUAZgBsAGUAYwB0AGkAbwBuAC4AYQBzAHMAZQBtAGIAbAB5AF0AOgA6ACgAIgBMAG8AYQBkACIAK
  - WwBSAGUAZgBsAGUAYwB0AGkAbwBuAC4AQQBzAHMAZQBtAGIAbAB5AF0AOgA6ACgAIgBMAG8AYQBkACIAKQ
  - sAUgBlAGYAbABlAGMAdABpAG8AbgAuAEEAcwBzAGUAbQBiAGwAeQBdADoAOgAoACIATABvAGEAZAAiACkA
  - bAFIAZQBmAGwAZQBjAHQAaQBvAG4ALgBBAHMAcwBlAG0AYgBsAHkAXQA6ADoAKAAiAEwAbwBhAGQAIgApA
  - WwByAGUAZgBsAGUAYwB0AGkAbwBuAC4AYQBzAHMAZQBtAGIAbAB5AF0AOgA6AEwAbwBhAGQAKA
  - sAcgBlAGYAbABlAGMAdABpAG8AbgAuAGEAcwBzAGUAbQBiAGwAeQBdADoAOgBMAG8AYQBkACgA
  - bAHIAZQBmAGwAZQBjAHQAaQBvAG4ALgBhAHMAcwBlAG0AYgBsAHkAXQA6ADoATABvAGEAZAAoA
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb2765d0ea08dcb6/yara/mal_revil.yar
- https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_reflection_assembly_load.yml)
