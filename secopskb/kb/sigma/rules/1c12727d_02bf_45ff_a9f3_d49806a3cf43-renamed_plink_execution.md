---
sigma_id: "1c12727d-02bf-45ff-a9f3-d49806a3cf43"
title: "Renamed Plink Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_plink.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_plink.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1c12727d-02bf-45ff-a9f3-d49806a3cf43"
  - "Renamed Plink Execution"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of a renamed version of the Plink binary

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]

## Detection

```yaml
selection:
- OriginalFileName: Plink
- CommandLine|contains|all:
  - ' -l forward'
  - ' -P '
  - ' -R '
filter:
  Image|endswith: \plink.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/06/06/will-the-real-msiexec-please-stand-up-exploit-leads-to-data-exfiltration/
- https://the.earth.li/~sgtatham/putty/0.58/htmldoc/Chapter7.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_plink.yml)
