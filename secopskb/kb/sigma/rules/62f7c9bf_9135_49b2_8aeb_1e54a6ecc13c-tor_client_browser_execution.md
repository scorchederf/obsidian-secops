---
sigma_id: "62f7c9bf-9135-49b2-8aeb-1e54a6ecc13c"
title: "Tor Client/Browser Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_tor_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_tor_execution.yml"
build_date: "2026-04-26 15:01:53"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tor Client/Browser Execution

Detects the use of Tor or Tor-Browser to connect to onion routing networks

## Metadata

- Rule ID: 62f7c9bf-9135-49b2-8aeb-1e54a6ecc13c
- Status: test
- Level: high
- Author: frack113
- Date: 2022-02-20
- Modified: 2025-10-27
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_tor_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090.003]]

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
