---
sigma_id: "4782eb5a-a513-4523-a0ac-f3082b26ac5c"
title: "Mshtml.DLL RunHTMLApplication Suspicious Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_mshtml_runhtmlapplication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_mshtml_runhtmlapplication.yml"
build_date: "2026-04-27 19:13:53"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of commands that leverage the "mshtml.dll" RunHTMLApplication export to run arbitrary code via different protocol handlers (vbscript, javascript, file, http...)

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
