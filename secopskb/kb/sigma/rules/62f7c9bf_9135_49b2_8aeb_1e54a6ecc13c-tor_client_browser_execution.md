---
sigma_id: "62f7c9bf-9135-49b2-8aeb-1e54a6ecc13c"
title: "Tor Client/Browser Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_tor_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_tor_execution.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "62f7c9bf-9135-49b2-8aeb-1e54a6ecc13c"
  - "Tor Client/Browser Execution"
attack_technique_ids:
  - "T1090.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of Tor or Tor-Browser to connect to onion routing networks

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]

## Detection

```yaml
selection:
- Description: Tor Browser
- Product: Tor Browser
- Image|endswith:
  - \tor.exe
  - \Tor Browser\Browser\firefox.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.logpoint.com/en/blog/detecting-tor-use-with-logpoint/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_tor_execution.yml)
