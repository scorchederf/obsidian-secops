---
sigma_id: "0d34ed8b-1c12-4ff2-828c-16fc860b766d"
title: "Suspicious Processes Spawned by Java.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_java_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_susp_child_process.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0d34ed8b-1c12-4ff2-828c-16fc860b766d"
  - "Suspicious Processes Spawned by Java.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Processes Spawned by Java.EXE

Detects suspicious processes spawned from a Java host process which could indicate a sign of exploitation (e.g. log4j)

## Metadata

- Rule ID: 0d34ed8b-1c12-4ff2-828c-16fc860b766d
- Status: test
- Level: high
- Author: Andreas Hunkeler (@Karneades), Florian Roth
- Date: 2021-12-17
- Modified: 2024-01-18
- Source Path: rules/windows/process_creation/proc_creation_win_java_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage|endswith: \java.exe
  Image|endswith:
  - \AppVLP.exe
  - \bitsadmin.exe
  - \certutil.exe
  - \cscript.exe
  - \curl.exe
  - \forfiles.exe
  - \hh.exe
  - \mftrace.exe
  - \mshta.exe
  - \net.exe
  - \net1.exe
  - \query.exe
  - \reg.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \schtasks.exe
  - \scrcons.exe
  - \scriptrunner.exe
  - \sh.exe
  - \systeminfo.exe
  - \whoami.exe
  - \wmic.exe
  - \wscript.exe
condition: selection
```

## False Positives

- Legitimate calls to system binaries
- Company specific internal usage

## References

- https://web.archive.org/web/20231230220738/https://www.lunasec.io/docs/blog/log4j-zero-day/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_susp_child_process.yml)
