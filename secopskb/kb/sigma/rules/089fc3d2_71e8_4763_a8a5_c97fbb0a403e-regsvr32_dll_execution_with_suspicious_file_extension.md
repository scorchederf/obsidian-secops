---
sigma_id: "089fc3d2-71e8-4763-a8a5-c97fbb0a403e"
title: "Regsvr32 DLL Execution With Suspicious File Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_susp_extensions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_extensions.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "089fc3d2-71e8-4763-a8a5-c97fbb0a403e"
  - "Regsvr32 DLL Execution With Suspicious File Extension"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of REGSVR32.exe with DLL files masquerading as other files

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218010-regsvr32|T1218.010: Regsvr32]]

## Detection

```yaml
selection_img:
- Image|endswith: \regsvr32.exe
- OriginalFileName: REGSVR32.EXE
selection_cli:
  CommandLine|endswith:
  - .bin
  - .bmp
  - .cr2
  - .dat
  - .eps
  - .gif
  - .ico
  - .jpeg
  - .jpg
  - .log
  - .nef
  - .orf
  - .png
  - .raw
  - .rtf
  - .sr2
  - .temp
  - .tif
  - .tiff
  - .tmp
  - .txt
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/
- https://blog.talosintelligence.com/2021/10/threat-hunting-in-large-datasets-by.html
- https://guides.lib.umich.edu/c.php?g=282942&p=1885348
- https://harfanglab.io/insidethelab/uac-0057-pressure-ukraine-poland/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_extensions.yml)
