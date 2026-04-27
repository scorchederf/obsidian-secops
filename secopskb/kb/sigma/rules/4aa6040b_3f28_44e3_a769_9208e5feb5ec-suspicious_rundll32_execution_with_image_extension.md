---
sigma_id: "4aa6040b-3f28-44e3-a769-9208e5feb5ec"
title: "Suspicious Rundll32 Execution With Image Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_susp_execution_with_image_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_execution_with_image_extension.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4aa6040b-3f28-44e3-a769-9208e5feb5ec"
  - "Suspicious Rundll32 Execution With Image Extension"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of Rundll32.exe with DLL files masquerading as image files

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.exe
selection_cli:
  CommandLine|contains:
  - .bmp
  - .cr2
  - .eps
  - .gif
  - .ico
  - .jpeg
  - .jpg
  - .nef
  - .orf
  - .png
  - .raw
  - .sr2
  - .tif
  - .tiff
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.zscaler.com/blogs/security-research/onenote-growing-threat-malware-distribution

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_execution_with_image_extension.yml)
