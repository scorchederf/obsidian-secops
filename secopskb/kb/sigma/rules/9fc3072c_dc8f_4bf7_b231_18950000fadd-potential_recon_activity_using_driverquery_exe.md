---
sigma_id: "9fc3072c-dc8f-4bf7-b231-18950000fadd"
title: "Potential Recon Activity Using DriverQuery.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_driverquery_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_driverquery_recon.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9fc3072c-dc8f-4bf7-b231-18950000fadd"
  - "Potential Recon Activity Using DriverQuery.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect usage of the "driverquery" utility to perform reconnaissance on installed drivers

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: driverquery.exe
- OriginalFileName: drvqry.exe
selection_parent:
- ParentImage|endswith:
  - \cscript.exe
  - \mshta.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- ParentImage|contains:
  - \AppData\Local\
  - \Users\Public\
  - \Windows\Temp\
condition: all of selection_*
```

## False Positives

- Legitimate usage by some scripts might trigger this as well

## References

- https://thedfirreport.com/2023/01/09/unwrapping-ursnifs-gifts/
- https://www.vmray.com/cyber-security-blog/analyzing-ursnif-behavior-malware-sandbox/
- https://www.fireeye.com/blog/threat-research/2020/01/saigon-mysterious-ursnif-fork.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_driverquery_recon.yml)
