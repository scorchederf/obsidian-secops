---
sigma_id: "c363385c-f75d-4753-a108-c1a8e28bdbda"
title: "Potential Manage-bde.wsf Abuse To Proxy Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c363385c-f75d-4753-a108-c1a8e28bdbda"
  - "Potential Manage-bde.wsf Abuse To Proxy Execution"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential abuse of the "manage-bde.wsf" script as a LOLBIN to proxy execution

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

## Detection

```yaml
selection_wscript_img:
- Image|endswith: \wscript.exe
- OriginalFileName: wscript.exe
selection_wscript_cli:
  CommandLine|contains: manage-bde.wsf
selection_parent:
  ParentImage|endswith:
  - \cscript.exe
  - \wscript.exe
  ParentCommandLine|contains: manage-bde.wsf
selection_filter_cmd:
  Image|endswith: \cmd.exe
condition: all of selection_wscript_* or (selection_parent and not selection_filter_cmd)
```

## False Positives

- Unlikely

## References

- https://lolbas-project.github.io/lolbas/Scripts/Manage-bde/
- https://gist.github.com/bohops/735edb7494fe1bd1010d67823842b712
- https://twitter.com/bohops/status/980659399495741441
- https://twitter.com/JohnLaTwC/status/1223292479270600706
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1216/T1216.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml)
