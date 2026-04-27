---
sigma_id: "90fb5e62-ca1f-4e22-b42e-cc521874c938"
title: "Suspicious Shells Spawn by Java Utility Keytool"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_java_keytool_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_keytool_susp_child_process.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "90fb5e62-ca1f-4e22-b42e-cc521874c938"
  - "Suspicious Shells Spawn by Java Utility Keytool"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious shell spawn from Java utility keytool process (e.g. adselfservice plus exploitation)

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage|endswith: \keytool.exe
  Image|endswith:
  - \cmd.exe
  - \sh.exe
  - \bash.exe
  - \powershell.exe
  - \pwsh.exe
  - \schtasks.exe
  - \certutil.exe
  - \whoami.exe
  - \bitsadmin.exe
  - \wscript.exe
  - \cscript.exe
  - \scrcons.exe
  - \regsvr32.exe
  - \hh.exe
  - \wmic.exe
  - \mshta.exe
  - \rundll32.exe
  - \forfiles.exe
  - \scriptrunner.exe
  - \mftrace.exe
  - \AppVLP.exe
  - \systeminfo.exe
  - \reg.exe
  - \query.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/intelligence-insights-december-2021
- https://www.synacktiv.com/en/publications/how-to-exploit-cve-2021-40539-on-manageengine-adselfservice-plus.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_keytool_susp_child_process.yml)
