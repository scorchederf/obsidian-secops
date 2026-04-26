---
sigma_id: "552b6b65-df37-4d3e-a258-f2fc4771ae54"
title: "Potential Antivirus Software DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_antivirus.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_antivirus.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "552b6b65-df37-4d3e-a258-f2fc4771ae54"
  - "Potential Antivirus Software DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Antivirus Software DLL Sideloading

Detects potential DLL sideloading of DLLs that are part of antivirus software suchas McAfee, Symantec...etc

## Metadata

- Rule ID: 552b6b65-df37-4d3e-a258-f2fc4771ae54
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Wietze Beukema (project and research)
- Date: 2022-08-17
- Modified: 2025-10-07
- Source Path: rules/windows/image_load/image_load_side_load_antivirus.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection_bitdefender:
  ImageLoaded|endswith: \log.dll
filter_log_dll_bitdefender:
  ImageLoaded|startswith:
  - C:\Program Files\Bitdefender Antivirus Free\
  - C:\Program Files (x86)\Bitdefender Antivirus Free\
filter_log_dll_dell_sar:
  Image: C:\Program Files\Dell\SARemediation\audit\TelemetryUtility.exe
  ImageLoaded:
  - C:\Program Files\Dell\SARemediation\plugin\log.dll
  - C:\Program Files\Dell\SARemediation\audit\log.dll
filter_log_dll_canon:
  ImageLoaded|startswith: C:\Program Files\Canon\MyPrinter\
filter_log_dll_avast:
  ImageLoaded:
  - C:\Program Files\AVAST Software\Avast\log.dll
  - C:\Program Files (x86)\AVAST Software\Avast\log.dll
filter_log_dll_avg:
  ImageLoaded:
  - C:\Program Files\AVG\Antivirus\log.dll
  - C:\Program Files (x86)\AVG\Antivirus\log.dll
selection_fsecure:
  ImageLoaded|endswith: \qrt.dll
filter_fsecure:
  ImageLoaded|startswith:
  - C:\Program Files\F-Secure\Anti-Virus\
  - C:\Program Files (x86)\F-Secure\Anti-Virus\
selection_mcafee:
  ImageLoaded|endswith:
  - \ashldres.dll
  - \lockdown.dll
  - \vsodscpl.dll
filter_mcafee:
  ImageLoaded|startswith:
  - C:\Program Files\McAfee\
  - C:\Program Files (x86)\McAfee\
selection_cyberark:
  ImageLoaded|endswith: \vftrace.dll
filter_cyberark:
  ImageLoaded|startswith:
  - C:\Program Files\CyberArk\Endpoint Privilege Manager\Agent\x32\
  - C:\Program Files (x86)\CyberArk\Endpoint Privilege Manager\Agent\x32\
selection_avast:
  ImageLoaded|endswith: \wsc.dll
filter_wsc_dll_avast:
  ImageLoaded|startswith:
  - C:\program Files\AVAST Software\Avast\
  - C:\program Files (x86)\AVAST Software\Avast\
filter_wsc_dll_avg:
  ImageLoaded|startswith:
  - C:\Program Files\AVG\Antivirus\
  - C:\Program Files (x86)\AVG\Antivirus\
selection_eset_deslock:
  ImageLoaded|endswith: \DLPPREM32.dll
filter_eset_deslock:
  ImageLoaded|startswith:
  - C:\program Files\ESET
  - C:\program Files (x86)\ESET
selection_titanium:
  ImageLoaded|endswith: \tmdbglog.dll
filter_titanium:
  ImageLoaded|startswith:
  - C:\program Files\Trend Micro\Titanium\
  - C:\program Files (x86)\Trend Micro\Titanium\
condition: (selection_bitdefender and not 1 of filter_log_dll_*) or (selection_fsecure
  and not filter_fsecure) or (selection_mcafee and not filter_mcafee) or (selection_cyberark
  and not filter_cyberark) or (selection_avast and not 1 of filter_wsc_dll_*) or (selection_titanium
  and not filter_titanium) or (selection_eset_deslock and not filter_eset_deslock)
```

## False Positives

- Applications that load the same dlls mentioned in the detection section. Investigate them and filter them out if a lot FPs are caused.
- Dell SARemediation plugin folder (C:\Program Files\Dell\SARemediation\plugin\log.dll) is known to contain the 'log.dll' file.
- The Canon MyPrinter folder 'C:\Program Files\Canon\MyPrinter\' is known to contain the 'log.dll' file

## References

- https://hijacklibs.net/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_antivirus.yml)
