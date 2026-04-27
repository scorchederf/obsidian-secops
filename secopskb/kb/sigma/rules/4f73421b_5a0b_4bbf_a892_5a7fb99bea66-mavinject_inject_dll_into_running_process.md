---
sigma_id: "4f73421b-5a0b-4bbf-a892-5a7fb99bea66"
title: "Mavinject Inject DLL Into Running Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml"
build_date: "2026-04-27 19:13:53"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects process injection using the signed Windows tool "Mavinject" via the "INJECTRUNNING" flag

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218013-mavinject|T1218.013: Mavinject]]

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
