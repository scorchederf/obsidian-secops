---
sigma_id: "867356ee-9352-41c9-a8f2-1be690d78216"
title: "Potentially Suspicious Regsvr32 HTTP/FTP Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "867356ee-9352-41c9-a8f2-1be690d78216"
  - "Potentially Suspicious Regsvr32 HTTP/FTP Pattern"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Regsvr32 HTTP/FTP Pattern

Detects regsvr32 execution to download/install/register new DLLs that are hosted on Web or FTP servers.

## Metadata

- Rule ID: 867356ee-9352-41c9-a8f2-1be690d78216
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2023-05-24
- Modified: 2023-05-26
- Source Path: rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection_img:
- Image|endswith: \regsvr32.exe
- OriginalFileName: REGSVR32.EXE
selection_flag:
  CommandLine|contains:
  - ' /i'
  - ' -i'
selection_protocol:
  CommandLine|contains:
  - ftp
  - http
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1461041276514623491
- https://twitter.com/tccontre18/status/1480950986650832903
- https://lolbas-project.github.io/lolbas/Binaries/Regsvr32/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml)
