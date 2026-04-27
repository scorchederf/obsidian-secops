---
sigma_id: "32410e29-5f94-4568-b6a3-d91a8adad863"
title: "PUA - Fast Reverse Proxy (FRP) Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_frp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_frp.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "32410e29-5f94-4568-b6a3-d91a8adad863"
  - "PUA - Fast Reverse Proxy (FRP) Execution"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of Fast Reverse Proxy. frp is a fast reverse proxy to help you expose a local server behind a NAT or firewall to the Internet.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090: Proxy]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - \frpc.exe
  - \frps.exe
selection_cli:
  CommandLine|contains: \frpc.ini
selection_hashes:
  Hashes|contains:
  - MD5=7D9C233B8C9E3F0EA290D2B84593C842
  - SHA1=06DDC9280E1F1810677935A2477012960905942F
  - SHA256=57B0936B8D336D8E981C169466A15A5FD21A7D5A2C7DAF62D5E142EE860E387C
condition: 1 of selection_*
```

## False Positives

- Legitimate use

## References

- https://asec.ahnlab.com/en/38156/
- https://github.com/fatedier/frp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_frp.yml)
