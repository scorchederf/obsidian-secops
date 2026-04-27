---
sigma_id: "7a74da6b-ea76-47db-92cc-874ad90df734"
title: "Suspicious MSDT Parent Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msdt_susp_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_susp_parent.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7a74da6b-ea76-47db-92cc-874ad90df734"
  - "Suspicious MSDT Parent Process"
attack_technique_ids:
  - "T1036"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects msdt.exe executed by a suspicious parent as seen in CVE-2022-30190 / Follina exploitation

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \schtasks.exe
  - \wmic.exe
  - \wscript.exe
  - \wsl.exe
selection_msdt:
- Image|endswith: \msdt.exe
- OriginalFileName: msdt.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/nao_sec/status/1530196847679401984
- https://app.any.run/tasks/713f05d2-fe78-4b9d-a744-f7c133e3fafb/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_susp_parent.yml)
