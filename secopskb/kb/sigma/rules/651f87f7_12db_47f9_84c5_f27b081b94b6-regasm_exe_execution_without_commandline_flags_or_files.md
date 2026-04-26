---
sigma_id: "651f87f7-12db-47f9-84c5-f27b081b94b6"
title: "RegAsm.EXE Execution Without CommandLine Flags or Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regasm_no_flag_or_dll_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regasm_no_flag_or_dll_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "651f87f7-12db-47f9-84c5-f27b081b94b6"
  - "RegAsm.EXE Execution Without CommandLine Flags or Files"
attack_technique_ids:
  - "T1218.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RegAsm.EXE Execution Without CommandLine Flags or Files

Detects the execution of "RegAsm.exe" without a commandline flag or file, which might indicate potential process injection activity.
Usually "RegAsm.exe" should point to a dedicated DLL file or call the help with the "/?" flag.

## Metadata

- Rule ID: 651f87f7-12db-47f9-84c5-f27b081b94b6
- Status: experimental
- Level: low
- Author: frack113
- Date: 2025-06-04
- Source Path: rules/windows/process_creation/proc_creation_win_regasm_no_flag_or_dll_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.009]]

## Detection

```yaml
selection_img:
- Image|endswith: \RegAsm.exe
- OriginalFileName: RegAsm.exe
selection_cli:
  CommandLine|endswith:
  - RegAsm
  - RegAsm.exe
  - RegAsm.exe"
  - RegAsm.exe'
condition: all of selection_*
```

## False Positives

- Legitimate use of Regasm by developers.

## References

- https://www.mcafee.com/blogs/other-blogs/mcafee-labs/agent-teslas-unique-approach-vbs-and-steganography-for-delivery-and-intrusion/
- https://www.zscaler.fr/blogs/security-research/threat-actors-exploit-cve-2017-11882-deliver-agent-tesla
- https://learn.microsoft.com/en-us/dotnet/framework/tools/regasm-exe-assembly-registration-tool
- https://app.any.run/tasks/ea944b89-69d8-49c8-ac1f-5c76ad300db2
- https://www.joesandbox.com/analysis/1467354/0/html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regasm_no_flag_or_dll_execution.yml)
