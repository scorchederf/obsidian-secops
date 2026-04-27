---
sigma_id: "b86f6dea-0b2f-41f5-bdcc-a057bd19cd6a"
title: "File Download From IP Based URL Via CertOC.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certoc_download_direct_ip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certoc_download_direct_ip.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b86f6dea-0b2f-41f5-bdcc-a057bd19cd6a"
  - "File Download From IP Based URL Via CertOC.EXE"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a user downloads a file from an IP based URL using CertOC.exe

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection_img:
- Image|endswith: \certoc.exe
- OriginalFileName: CertOC.exe
selection_ip:
  CommandLine|re: ://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
selection_cli:
  CommandLine|contains: -GetCACAPS
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Certoc/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certoc_download_direct_ip.yml)
