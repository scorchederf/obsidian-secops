---
sigma_id: "8d63dadf-b91b-4187-87b6-34a1114577ea"
title: "Potential Remote SquiblyTwo Technique Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_squiblytwo_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_squiblytwo_bypass.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8d63dadf-b91b-4187-87b6-34a1114577ea"
  - "Potential Remote SquiblyTwo Technique Execution"
attack_technique_ids:
  - "T1047"
  - "T1220"
  - "T1059.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Remote SquiblyTwo Technique Execution

Detects potential execution of the SquiblyTwo technique that leverages Windows Management Instrumentation (WMI)
to execute malicious code remotely. This technique bypasses application whitelisting by using wmic.exe to process
malicious XSL (eXtensible Stylesheet Language) scripts that can contain embedded JScript or VBScript.
The attack typically works by fetching XSL content from a remote source (using HTTP/HTTPS) and executing it
with full trust privileges directly in memory, avoiding disk-based detection mechanisms. This is a common
LOLBin (Living Off The Land Binary) technique used for defense evasion and code execution.

## Metadata

- Rule ID: 8d63dadf-b91b-4187-87b6-34a1114577ea
- Status: test
- Level: high
- Author: Markus Neis, Florian Roth, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2019-01-16
- Modified: 2026-01-24
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_squiblytwo_bypass.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection_pe:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
- Hashes|contains:
  - IMPHASH=1B1A3F43BF37B5BFE60751F2EE2F326E
  - IMPHASH=37777A96245A3C74EB217308F3546F4C
  - IMPHASH=9D87C9D67CE724033C0B40CC4CA1B206
  - IMPHASH=B12619881D79C3ACADF45E752A58554A
  - IMPHASH=16A48C3CABF98A9DC1BF02C07FE1EA00
selection_cli:
  CommandLine|contains|windash: '/format:'
  CommandLine|contains:
  - ://
  - \\\\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20190209154607/https://subt0x11.blogspot.com/2018/04/wmicexe-whitelisting-bypass-hacking.html
- https://twitter.com/mattifestation/status/986280382042595328
- https://atomicredteam.io/defense-evasion/T1220/
- https://lolbas-project.github.io/lolbas/Binaries/Wmic/
- https://x.com/byrne_emmy12099/status/1932346420226658668

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_squiblytwo_bypass.yml)
