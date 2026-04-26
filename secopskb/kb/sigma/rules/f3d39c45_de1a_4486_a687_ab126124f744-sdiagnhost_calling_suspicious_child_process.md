---
sigma_id: "f3d39c45-de1a-4486-a687-ab126124f744"
title: "Sdiagnhost Calling Suspicious Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sdiagnhost_susp_child.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sdiagnhost_susp_child.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f3d39c45-de1a-4486-a687-ab126124f744"
  - "Sdiagnhost Calling Suspicious Child Process"
attack_technique_ids:
  - "T1036"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sdiagnhost Calling Suspicious Child Process

Detects sdiagnhost.exe calling a suspicious child process (e.g. used in exploits for Follina / CVE-2022-30190)

## Metadata

- Rule ID: f3d39c45-de1a-4486-a687-ab126124f744
- Status: test
- Level: high
- Author: Nextron Systems, @Kostastsale
- Date: 2022-06-01
- Modified: 2024-08-23
- Source Path: rules/windows/process_creation/proc_creation_win_sdiagnhost_susp_child.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \sdiagnhost.exe
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \cmd.exe
  - \mshta.exe
  - \cscript.exe
  - \wscript.exe
  - \taskkill.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \calc.exe
filter_main_cmd_bits:
  Image|endswith: \cmd.exe
  CommandLine|contains: bits
filter_main_powershell_noprofile:
  Image|endswith: \powershell.exe
  CommandLine|endswith:
  - -noprofile -
  - -noprofile
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/nao_sec/status/1530196847679401984
- https://doublepulsar.com/follina-a-microsoft-office-code-execution-vulnerability-1a47fce5629e
- https://app.any.run/tasks/713f05d2-fe78-4b9d-a744-f7c133e3fafb/
- https://app.any.run/tasks/f420d295-0457-4e9b-9b9e-6732be227583/
- https://app.any.run/tasks/c4117d9a-f463-461a-b90f-4cd258746798/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sdiagnhost_susp_child.yml)
