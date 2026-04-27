---
sigma_id: "68d37776-61db-42f5-bf54-27e87072d17e"
title: "PUA - NPS Tunneling Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_nps.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nps.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "68d37776-61db-42f5-bf54-27e87072d17e"
  - "PUA - NPS Tunneling Tool Execution"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of NPS, a port forwarding and intranet penetration proxy server

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090: Proxy]]

## Detection

```yaml
selection_img:
  Image|endswith: \npc.exe
selection_cli_1:
  CommandLine|contains|all:
  - ' -server='
  - ' -vkey='
  - ' -password='
selection_cli_2:
  CommandLine|contains: ' -config=npc'
selection_hashes:
  Hashes|contains:
  - MD5=AE8ACF66BFE3A44148964048B826D005
  - SHA1=CEA49E9B9B67F3A13AD0BE1C2655293EA3C18181
  - SHA256=5A456283392FFCEEEACA3D3426C306EB470304637520D72FED1CC1FEBBBD6856
condition: 1 of selection_*
```

## False Positives

- Legitimate use

## References

- https://github.com/ehang-io/nps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nps.yml)
