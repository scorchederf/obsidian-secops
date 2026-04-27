---
sigma_id: "50cb47b8-2c33-4b23-a2e9-4600657d9746"
title: "Loading Diagcab Package From Remote Path"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/diagnosis/scripted/win_diagnosis_scripted_load_remote_diagcab.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/diagnosis/scripted/win_diagnosis_scripted_load_remote_diagcab.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / diagnosis-scripted"
aliases:
  - "50cb47b8-2c33-4b23-a2e9-4600657d9746"
  - "Loading Diagcab Package From Remote Path"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects loading of diagcab packages from a remote path, as seen in DogWalk vulnerability

## Logsource

- product: windows
- service: diagnosis-scripted

## Detection

```yaml
selection:
  EventID: 101
  PackagePath|contains: \\\\
condition: selection
```

## False Positives

- Legitimate package hosted on a known and authorized remote location

## References

- https://twitter.com/nas_bench/status/1539679555908141061
- https://twitter.com/j00sean/status/1537750439701225472

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/diagnosis/scripted/win_diagnosis_scripted_load_remote_diagcab.yml)
