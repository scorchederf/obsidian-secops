---
sigma_id: "cb0fe7c5-f3a3-484d-aa25-d350a7912729"
title: "Suspicious Driver/DLL Installation Via Odbcconf.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_driver_install_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_driver_install_susp.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cb0fe7c5-f3a3-484d-aa25-d350a7912729"
  - "Suspicious Driver/DLL Installation Via Odbcconf.EXE"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Driver/DLL Installation Via Odbcconf.EXE

Detects execution of "odbcconf" with the "INSTALLDRIVER" action where the driver doesn't contain a ".dll" extension. This is often used as a defense evasion method.

## Metadata

- Rule ID: cb0fe7c5-f3a3-484d-aa25-d350a7912729
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-23
- Source Path: rules/windows/process_creation/proc_creation_win_odbcconf_driver_install_susp.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.008]]

## Detection

```yaml
selection_img:
- Image|endswith: \odbcconf.exe
- OriginalFileName: odbcconf.exe
selection_cli:
  CommandLine|contains: 'INSTALLDRIVER '
filter_main_dll_ext:
  CommandLine|contains: .dll
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/
- https://web.archive.org/web/20191023232753/https://twitter.com/Hexacorn/status/1187143326673330176
- https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_driver_install_susp.yml)
