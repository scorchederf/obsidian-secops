---
sigma_id: "f17211f1-1f24-4d0c-829f-31e28dc93cdd"
title: "Uncommon Svchost Command Line Parameter"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_svchost_uncommon_command_line_flags.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_uncommon_command_line_flags.yml"
build_date: "2026-04-27 19:13:58"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f17211f1-1f24-4d0c-829f-31e28dc93cdd"
  - "Uncommon Svchost Command Line Parameter"
attack_technique_ids:
  - "T1036.005"
  - "T1055"
  - "T1055.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects instances of svchost.exe running with an unusual or uncommon command line parameter by excluding known legitimate or common patterns.
This could point at a file masquerading as svchost, a process injection, or hollowing of a legitimate svchost instance.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]
- [[kb/attack/techniques/T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]

## Detection

```yaml
selection:
  Image|endswith: \svchost.exe
filter_main_flags:
  CommandLine|re: -k\s\w{1,64}(\s?(-p|-s))?
filter_main_empty:
  CommandLine: ''
filter_main_null:
  CommandLine: null
filter_optional_defender:
  ParentImage|endswith: \MsMpEng.exe
  CommandLine|contains: svchost.exe
filter_optional_mrt:
  ParentImage|endswith: \MRT.exe
  CommandLine: svchost.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unlikely

## References

- https://cardinalops.com/blog/the-art-of-anomaly-hunting-patterns-detection/
- https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware
- https://cloud.google.com/blog/topics/threat-intelligence/apt41-initiates-global-intrusion-campaign-using-multiple-exploits/
- https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_uncommon_command_line_flags.yml)
