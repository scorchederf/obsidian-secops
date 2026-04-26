---
sigma_id: "a77c1610-fc73-4019-8e29-0f51efc04a51"
title: "Potential Dosfuscation Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_dosfuscation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_dosfuscation.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a77c1610-fc73-4019-8e29-0f51efc04a51"
  - "Potential Dosfuscation Activity"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Dosfuscation Activity

Detects possible payload obfuscation via the commandline

## Metadata

- Rule ID: a77c1610-fc73-4019-8e29-0f51efc04a51
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-02-15
- Modified: 2023-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_dosfuscation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ^^
  - ^|^
  - ',;,'
  - ;;;;
  - ;; ;;
  - (,(,
  - '%COMSPEC:~'
  - ' c^m^d'
  - ^c^m^d
  - ' c^md'
  - ' cm^d'
  - ^cm^d
  - ' s^et '
  - ' s^e^t '
  - ' se^t '
condition: selection
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/dosfuscation-report.pdf
- https://github.com/danielbohannon/Invoke-DOSfuscation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_dosfuscation.yml)
