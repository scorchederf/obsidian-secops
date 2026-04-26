---
sigma_id: "ad691d92-15f2-4181-9aa4-723c74f9ddc3"
title: "Potential Defense Evasion Via Right-to-Left Override"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_right_to_left_override.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_right_to_left_override.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ad691d92-15f2-4181-9aa4-723c74f9ddc3"
  - "Potential Defense Evasion Via Right-to-Left Override"
attack_technique_ids:
  - "T1036.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Defense Evasion Via Right-to-Left Override

Detects the presence of the "u202+E" character, which causes a terminal, browser, or operating system to render text in a right-to-left sequence.
This character is used as an obfuscation and masquerading techniques by adversaries to trick users into opening malicious files.

## Metadata

- Rule ID: ad691d92-15f2-4181-9aa4-723c74f9ddc3
- Status: test
- Level: high
- Author: Micah Babinski, @micahbabinski, Swachchhanda Shrawan Poudel (Nextron Systems), Luc Génaux
- Date: 2023-02-15
- Modified: 2026-03-20
- Source Path: rules/windows/process_creation/proc_creation_win_susp_right_to_left_override.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.002]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - \u202e
  - '[U+202E]'
  - ‮
condition: selection
```

## False Positives

- Commandlines that contains scriptures such as arabic or hebrew might make use of this character

## References

- https://redcanary.com/blog/right-to-left-override/
- https://www.malwarebytes.com/blog/news/2014/01/the-rtlo-method
- https://unicode-explorer.com/c/202E
- https://tria.ge/241015-l98snsyeje/behavioral2
- https://unprotect.it/technique/right-to-left-override-rlo-extension-spoofing/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_right_to_left_override.yml)
