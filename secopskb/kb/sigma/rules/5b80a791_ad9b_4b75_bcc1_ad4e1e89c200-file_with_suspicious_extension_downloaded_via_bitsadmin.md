---
sigma_id: "5b80a791-ad9b-4b75-bcc1-ad4e1e89c200"
title: "File With Suspicious Extension Downloaded Via Bitsadmin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bitsadmin_download_susp_extensions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_susp_extensions.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5b80a791-ad9b-4b75-bcc1-ad4e1e89c200"
  - "File With Suspicious Extension Downloaded Via Bitsadmin"
attack_technique_ids:
  - "T1197"
  - "T1036.003"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of bitsadmin downloading a file with a suspicious extension

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197: BITS Jobs]]
- [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### Software Tags

- S0190

## Detection

```yaml
selection_img:
- Image|endswith: \bitsadmin.exe
- OriginalFileName: bitsadmin.exe
selection_flags:
  CommandLine|contains:
  - ' /transfer '
  - ' /create '
  - ' /addfile '
selection_extension:
  CommandLine|contains:
  - .7z
  - .asax
  - .ashx
  - .asmx
  - .asp
  - .aspx
  - .bat
  - .cfm
  - .cgi
  - .chm
  - .cmd
  - .dll
  - .gif
  - .jpeg
  - .jpg
  - .jsp
  - .jspx
  - .log
  - .png
  - .ps1
  - .psm1
  - .rar
  - .scf
  - .sct
  - .txt
  - .vbe
  - .vbs
  - .war
  - .wsf
  - .wsh
  - .xll
  - .zip
condition: all of selection_*
```

## False Positives

- Unknown

## Simulation

### Windows - BITSAdmin BITS Download

- Atomic Test: [[kb/atomic/tests/a1921cd3_9a2d_47d5_a891_f1d0f2a7a31b-windows_bitsadmin_bits_download|a1921cd3-9a2d-47d5-a891-f1d0f2a7a31b]]
- atomic_guid: a1921cd3-9a2d-47d5-a891-f1d0f2a7a31b
- name: Windows - BITSAdmin BITS Download
- technique: T1105
- type: atomic-red-team

## References

- https://blog.netspi.com/15-ways-to-download-a-file/#bitsadmin
- https://isc.sans.edu/diary/22264
- https://lolbas-project.github.io/lolbas/Binaries/Bitsadmin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_susp_extensions.yml)
