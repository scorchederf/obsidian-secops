---
sigma_id: "2dd2c217-bf68-437a-b57c-fe9fd01d5de8"
title: "Potentially Suspicious Regsvr32 HTTP IP Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_http_ip_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_http_ip_pattern.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2dd2c217-bf68-437a-b57c-fe9fd01d5de8"
  - "Potentially Suspicious Regsvr32 HTTP IP Pattern"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects regsvr32 execution to download and install DLLs located remotely where the address is an IP address.

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
selection_ip:
  CommandLine|contains:
  - ' /i:http://1'
  - ' /i:http://2'
  - ' /i:http://3'
  - ' /i:http://4'
  - ' /i:http://5'
  - ' /i:http://6'
  - ' /i:http://7'
  - ' /i:http://8'
  - ' /i:http://9'
  - ' /i:https://1'
  - ' /i:https://2'
  - ' /i:https://3'
  - ' /i:https://4'
  - ' /i:https://5'
  - ' /i:https://6'
  - ' /i:https://7'
  - ' /i:https://8'
  - ' /i:https://9'
  - ' -i:http://1'
  - ' -i:http://2'
  - ' -i:http://3'
  - ' -i:http://4'
  - ' -i:http://5'
  - ' -i:http://6'
  - ' -i:http://7'
  - ' -i:http://8'
  - ' -i:http://9'
  - ' -i:https://1'
  - ' -i:https://2'
  - ' -i:https://3'
  - ' -i:https://4'
  - ' -i:https://5'
  - ' -i:https://6'
  - ' -i:https://7'
  - ' -i:https://8'
  - ' -i:https://9'
condition: all of selection_*
```

## False Positives

- FQDNs that start with a number such as "7-Zip"

## References

- https://twitter.com/mrd0x/status/1461041276514623491
- https://twitter.com/tccontre18/status/1480950986650832903
- https://lolbas-project.github.io/lolbas/Binaries/Regsvr32/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_http_ip_pattern.yml)
