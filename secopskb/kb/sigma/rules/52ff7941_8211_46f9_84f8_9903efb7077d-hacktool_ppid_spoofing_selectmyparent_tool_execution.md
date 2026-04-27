---
sigma_id: "52ff7941-8211-46f9-84f8-9903efb7077d"
title: "HackTool - PPID Spoofing SelectMyParent Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_selectmyparent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_selectmyparent.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "52ff7941-8211-46f9-84f8-9903efb7077d"
  - "HackTool - PPID Spoofing SelectMyParent Tool Execution"
attack_technique_ids:
  - "T1134.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of parent process ID spoofing tools like Didier Stevens tool SelectMyParent

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation#^t1134004-parent-pid-spoofing|T1134.004: Parent PID Spoofing]]

## Detection

```yaml
selection:
- Image|endswith: \SelectMyParent.exe
- CommandLine|contains:
  - PPID-spoof
  - ppid_spoof
  - spoof-ppid
  - spoof_ppid
  - ppidspoof
  - spoofppid
  - spoofedppid
  - ' -spawnto '
- OriginalFileName|contains:
  - PPID-spoof
  - ppid_spoof
  - spoof-ppid
  - spoof_ppid
  - ppidspoof
  - spoofppid
  - spoofedppid
- Description: SelectMyParent
- Hashes|contains:
  - IMPHASH=04D974875BD225F00902B4CAD9AF3FBC
  - IMPHASH=A782AF154C9E743DDF3F3EB2B8F3D16E
  - IMPHASH=89059503D7FBF470E68F7E63313DA3AD
  - IMPHASH=CA28337632625C8281AB8A130B3D6BAD
condition: selection
```

## False Positives

- Unlikely

## References

- https://pentestlab.blog/2020/02/24/parent-pid-spoofing/
- https://www.picussecurity.com/resource/blog/how-to-detect-parent-pid-ppid-spoofing-attacks
- https://www.ired.team/offensive-security/defense-evasion/parent-process-id-ppid-spoofing
- https://www.virustotal.com/gui/search/filename%253A*spoof*%2520filename%253A*ppid*/files

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_selectmyparent.yml)
