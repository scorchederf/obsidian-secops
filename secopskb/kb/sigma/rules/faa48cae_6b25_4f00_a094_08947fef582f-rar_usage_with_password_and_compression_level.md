---
sigma_id: "faa48cae-6b25-4f00-a094-08947fef582f"
title: "Rar Usage with Password and Compression Level"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rar_compression_with_password.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rar_compression_with_password.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "faa48cae-6b25-4f00-a094-08947fef582f"
  - "Rar Usage with Password and Compression Level"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of rar.exe, on the command line, to create an archive with password protection or with a specific compression level. This is pretty indicative of malicious actions.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

## Detection

```yaml
selection_password:
  CommandLine|contains: ' -hp'
selection_other:
  CommandLine|contains:
  - ' -m'
  - ' a '
condition: selection_password and selection_other
```

## False Positives

- Legitimate use of Winrar command line version
- Other command line tools, that use these flags

## References

- https://labs.sentinelone.com/the-anatomy-of-an-apt-attack-and-cobaltstrike-beacons-encoded-configuration/
- https://ss64.com/bash/rar.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rar_compression_with_password.yml)
