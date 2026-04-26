---
sigma_id: "75e508f7-932d-4ebc-af77-269237a84ce1"
title: "DLL Loaded From Suspicious Location Via Cmspt.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_cmstp_load_dll_from_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_cmstp_load_dll_from_susp_location.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "75e508f7-932d-4ebc-af77-269237a84ce1"
  - "DLL Loaded From Suspicious Location Via Cmspt.EXE"
attack_technique_ids:
  - "T1218.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DLL Loaded From Suspicious Location Via Cmspt.EXE

Detects cmstp loading "dll" or "ocx" files from suspicious locations

## Metadata

- Rule ID: 75e508f7-932d-4ebc-af77-269237a84ce1
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-30
- Modified: 2023-02-17
- Source Path: rules/windows/image_load/image_load_cmstp_load_dll_from_susp_location.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

## Detection

```yaml
selection:
  Image|endswith: \cmstp.exe
  ImageLoaded|contains:
  - \PerfLogs\
  - \ProgramData\
  - \Users\
  - \Windows\Temp\
  - C:\Temp\
  ImageLoaded|endswith:
  - .dll
  - .ocx
condition: selection
```

## False Positives

- Unikely

## References

- https://github.com/vadim-hunter/Detection-Ideas-Rules/blob/02bcbfc2bfb8b4da601bb30de0344ae453aa1afe/TTPs/Defense%20Evasion/T1218%20-%20Signed%20Binary%20Proxy%20Execution/T1218.003%20-%20CMSTP/Procedures.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_cmstp_load_dll_from_susp_location.yml)
