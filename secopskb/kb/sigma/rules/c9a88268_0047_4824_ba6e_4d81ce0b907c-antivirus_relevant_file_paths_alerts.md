---
sigma_id: "c9a88268-0047-4824-ba6e-4d81ce0b907c"
title: "Antivirus Relevant File Paths Alerts"
framework: "sigma"
generated: "true"
source_path: "rules/category/antivirus/av_relevant_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_relevant_files.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "antivirus"
aliases:
  - "c9a88268-0047-4824-ba6e-4d81ce0b907c"
  - "Antivirus Relevant File Paths Alerts"
attack_technique_ids:
  - "T1588"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Antivirus Relevant File Paths Alerts

Detects an Antivirus alert in a highly relevant file path or with a relevant file name.
This event must not be ignored just because the AV has blocked the malware but investigate, how it came there in the first place.

## Metadata

- Rule ID: c9a88268-0047-4824-ba6e-4d81ce0b907c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Arnim Rupp
- Date: 2018-09-09
- Modified: 2024-11-02
- Source Path: rules/category/antivirus/av_relevant_files.yml

## Logsource

- category: antivirus

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities|T1588]]

## Detection

```yaml
selection_path:
  Filename|contains:
  - :\PerfLogs\
  - :\Temp\
  - :\Users\Default\
  - :\Users\Public\
  - :\Windows\
  - /www/
  - \inetpub\
  - \tsclient\
  - apache
  - nginx
  - tomcat
  - weblogic
selection_ext:
  Filename|endswith:
  - .asax
  - .ashx
  - .asmx
  - .asp
  - .aspx
  - .bat
  - .cfm
  - .cgi
  - .chm
  - .cmd
  - .dat
  - .ear
  - .gif
  - .hta
  - .jpeg
  - .jpg
  - .jsp
  - .jspx
  - .lnk
  - .msc
  - .php
  - .pl
  - .png
  - .ps1
  - .psm1
  - .py
  - .pyc
  - .rb
  - .scf
  - .sct
  - .sh
  - .svg
  - .txt
  - .vbe
  - .vbs
  - .war
  - .wll
  - .wsf
  - .wsh
  - .xll
  - .xml
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://www.nextron-systems.com/?s=antivirus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_relevant_files.yml)
