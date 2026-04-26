---
sigma_id: "8a582fe2-0882-4b89-a82a-da6b2dc32937"
title: "Suspicious WmiPrvSE Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmiprvse_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmiprvse_susp_child_processes.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8a582fe2-0882-4b89-a82a-da6b2dc32937"
  - "Suspicious WmiPrvSE Child Process"
attack_technique_ids:
  - "T1047"
  - "T1204.002"
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious WmiPrvSE Child Process

Detects suspicious and uncommon child processes of WmiPrvSE

## Metadata

- Rule ID: 8a582fe2-0882-4b89-a82a-da6b2dc32937
- Status: test
- Level: high
- Author: Vadim Khrykov (ThreatIntel), Cyb3rEng, Florian Roth (Nextron Systems)
- Date: 2021-08-23
- Modified: 2023-11-10
- Source Path: rules/windows/process_creation/proc_creation_win_wmiprvse_susp_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \wbem\WmiPrvSE.exe
selection_children_1:
  Image|endswith:
  - \certutil.exe
  - \cscript.exe
  - \mshta.exe
  - \msiexec.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \verclsid.exe
  - \wscript.exe
selection_children_2:
  Image|endswith: \cmd.exe
  CommandLine|contains:
  - cscript
  - mshta
  - powershell
  - pwsh
  - regsvr32
  - rundll32
  - wscript
filter_main_werfault:
  Image|endswith: \WerFault.exe
filter_main_wmiprvse:
  Image|endswith: \WmiPrvSE.exe
filter_main_msiexec:
  Image|endswith: \msiexec.exe
  CommandLine|contains: '/i '
condition: selection_parent and 1 of selection_children_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/
- https://github.com/vadim-hunter/Detection-Ideas-Rules/blob/02bcbfc2bfb8b4da601bb30de0344ae453aa1afe/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sodinokibi_(aka_REvil)_Ransomware.yaml
- https://blog.osarmor.com/319/onenote-attachment-delivers-asyncrat-malware/
- https://twitter.com/ForensicITGuy/status/1334734244120309760

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmiprvse_susp_child_processes.yml)
