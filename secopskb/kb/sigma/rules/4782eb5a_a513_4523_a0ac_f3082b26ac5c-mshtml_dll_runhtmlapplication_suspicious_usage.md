---
sigma_id: "4782eb5a-a513-4523-a0ac-f3082b26ac5c"
title: "Mshtml.DLL RunHTMLApplication Suspicious Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_mshtml_runhtmlapplication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_mshtml_runhtmlapplication.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4782eb5a-a513-4523-a0ac-f3082b26ac5c"
  - "Mshtml.DLL RunHTMLApplication Suspicious Usage"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Mshtml.DLL RunHTMLApplication Suspicious Usage

Detects execution of commands that leverage the "mshtml.dll" RunHTMLApplication export to run arbitrary code via different protocol handlers (vbscript, javascript, file, http...)

## Metadata

- Rule ID: 4782eb5a-a513-4523-a0ac-f3082b26ac5c
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems),  Florian Roth (Nextron Systems), Josh Nickels, frack113, Zaw Min Htun (ZETA)
- Date: 2022-08-14
- Modified: 2024-02-23
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_mshtml_runhtmlapplication.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \..\
  - mshtml
  CommandLine|contains:
  - '#135'
  - RunHTMLApplication
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/n1nj4sec/status/1421190238081277959
- https://hyp3rlinx.altervista.org/advisories/MICROSOFT_WINDOWS_DEFENDER_TROJAN.WIN32.POWESSERE.G_MITIGATION_BYPASS_PART2.txt
- http://hyp3rlinx.altervista.org/advisories/MICROSOFT_WINDOWS_DEFENDER_DETECTION_BYPASS.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_mshtml_runhtmlapplication.yml)
