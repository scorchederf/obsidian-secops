---
sigma_id: "84b14121-9d14-416e-800b-f3b829c5a14d"
title: "Suspicious CustomShellHost Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_customshellhost_susp_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_customshellhost_susp_exec.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "84b14121-9d14-416e-800b-f3b829c5a14d"
  - "Suspicious CustomShellHost Execution"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of CustomShellHost.exe where the child isn't located in 'C:\Windows\explorer.exe'. CustomShellHost is a known LOLBin that can be abused by attackers for defense evasion techniques.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

## Detection

```yaml
selection:
  ParentImage|endswith: \CustomShellHost.exe
filter_main_explorer:
  Image: C:\Windows\explorer.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- False positives are unlikely, investigate matches carefully.

## References

- https://github.com/LOLBAS-Project/LOLBAS/pull/180
- https://lolbas-project.github.io/lolbas/Binaries/CustomShellHost/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_customshellhost_susp_exec.yml)
