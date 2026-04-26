---
sigma_id: "4f73421b-5a0b-4bbf-a892-5a7fb99bea66"
title: "Mavinject Inject DLL Into Running Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4f73421b-5a0b-4bbf-a892-5a7fb99bea66"
  - "Mavinject Inject DLL Into Running Process"
attack_technique_ids:
  - "T1055.001"
  - "T1218.013"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mavinject Inject DLL Into Running Process

Detects process injection using the signed Windows tool "Mavinject" via the "INJECTRUNNING" flag

## Metadata

- Rule ID: 4f73421b-5a0b-4bbf-a892-5a7fb99bea66
- Status: test
- Level: high
- Author: frack113, Florian Roth
- Date: 2021-07-12
- Modified: 2022-12-05
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.001]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.013]]

## Detection

```yaml
selection:
  CommandLine|contains: ' /INJECTRUNNING '
filter:
  ParentImage: C:\Windows\System32\AppVClient.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1056.004/T1056.004.md
- https://posts.specterops.io/mavinject-exe-functionality-deconstructed-c29ab2cf5c0e
- https://twitter.com/gN3mes1s/status/941315826107510784
- https://reaqta.com/2017/12/mavinject-microsoft-injector/
- https://twitter.com/Hexacorn/status/776122138063409152
- https://github.com/SigmaHQ/sigma/issues/3742
- https://github.com/keyboardcrunch/SentinelOne-ATTACK-Queries/blob/6a228d23eefe963ca81f2d52f94b815f61ef5ee0/Tactics/DefenseEvasion.md#t1055-process-injection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml)
