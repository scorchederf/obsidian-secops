---
sigma_id: "06ce37c2-61ab-4f05-9ff5-b1a96d18ae32"
title: "WMIC Loading Scripting Libraries"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_wmic_remote_xsl_scripting_dlls.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wmic_remote_xsl_scripting_dlls.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "06ce37c2-61ab-4f05-9ff5-b1a96d18ae32"
  - "WMIC Loading Scripting Libraries"
attack_technique_ids:
  - "T1220"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMIC Loading Scripting Libraries

Detects threat actors proxy executing code and bypassing application controls by leveraging wmic and the `/FORMAT` argument switch to download and execute an XSL file (i.e js, vbs, etc).
It could be an indicator of SquiblyTwo technique, which uses Windows Management Instrumentation (WMI) to execute malicious code.

## Metadata

- Rule ID: 06ce37c2-61ab-4f05-9ff5-b1a96d18ae32
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-10-17
- Modified: 2022-10-13
- Source Path: rules/windows/image_load/image_load_wmic_remote_xsl_scripting_dlls.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

## Detection

```yaml
selection:
  Image|endswith: \wmic.exe
  ImageLoaded|endswith:
  - \jscript.dll
  - \vbscript.dll
condition: selection
```

## False Positives

- The command wmic os get lastbootuptime loads vbscript.dll
- The command wmic os get locale loads vbscript.dll
- Since the ImageLoad event doesn't have enough information in this case. It's better to look at the recent process creation events that spawned the WMIC process and investigate the command line and parent/child processes to get more insights
- The command `wmic ntevent` loads vbscript.dll

## References

- https://securitydatasets.com/notebooks/atomic/windows/defense_evasion/SDWIN-201017061100.html
- https://twitter.com/dez_/status/986614411711442944
- https://lolbas-project.github.io/lolbas/Binaries/Wmic/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wmic_remote_xsl_scripting_dlls.yml)
