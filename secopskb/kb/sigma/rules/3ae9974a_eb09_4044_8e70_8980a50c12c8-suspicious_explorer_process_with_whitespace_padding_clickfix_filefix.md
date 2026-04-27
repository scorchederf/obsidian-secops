---
sigma_id: "3ae9974a-eb09-4044-8e70-8980a50c12c8"
title: "Suspicious Explorer Process with Whitespace Padding - ClickFix/FileFix"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_clickfix_filefix_whitespace_padding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_clickfix_filefix_whitespace_padding.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "3ae9974a-eb09-4044-8e70-8980a50c12c8"
  - "Suspicious Explorer Process with Whitespace Padding - ClickFix/FileFix"
attack_technique_ids:
  - "T1204.004"
  - "T1027.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects process creation with suspicious whitespace padding followed by a '#' character, which may indicate ClickFix or FileFix techniques used to conceal malicious commands from visual inspection.
ClickFix and FileFix are social engineering attack techniques where adversaries distribute phishing documents or malicious links that deceive users into opening the Windows Run dialog box or File Explorer search bar.
The victims are then instructed to paste commands from their clipboard, which contain extensive whitespace padding using various Unicode space characters to push the actual malicious command far to the right, effectively hiding it from immediate view.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution#^t1204004-malicious-copy-and-paste|T1204.004: Malicious Copy and Paste]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027010-command-obfuscation|T1027.010: Command Obfuscation]]

## Detection

```yaml
selection_explorer:
  ParentImage|endswith: \explorer.exe
  CommandLine|contains: '#'
selection_space_variation:
  CommandLine|contains:
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

- Unknown

## References

- https://expel.com/blog/cache-smuggling-when-a-picture-isnt-a-thousand-words/
- https://mrd0x.com/filefix-clickfix-alternative/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_clickfix_filefix_whitespace_padding.yml)
