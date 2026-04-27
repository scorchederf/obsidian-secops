---
sigma_id: "1228c958-e64e-4e71-92ad-7d429f4138ba"
title: "Script Interpreter Execution From Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_script_exec_from_env_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_script_exec_from_env_folder.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1228c958-e64e-4e71-92ad-7d429f4138ba"
  - "Script Interpreter Execution From Suspicious Folder"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious script execution in temporary folders or folders accessible by environment variables

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection_proc_image:
  Image|endswith:
  - \cscript.exe
  - \mshta.exe
  - \wscript.exe
selection_proc_flags:
  CommandLine|contains:
  - ' -ep bypass '
  - ' -ExecutionPolicy bypass '
  - ' -w hidden '
  - '/e:javascript '
  - '/e:Jscript '
  - '/e:vbscript '
selection_proc_original:
  OriginalFileName:
  - cscript.exe
  - mshta.exe
  - wscript.exe
selection_folders_1:
  CommandLine|contains:
  - :\Perflogs\
  - :\Users\Public\
  - \AppData\Local\Temp
  - \AppData\Roaming\Temp
  - \Temporary Internet
  - \Windows\Temp
selection_folders_2:
- CommandLine|contains|all:
  - :\Users\
  - \Favorites\
- CommandLine|contains|all:
  - :\Users\
  - \Favourites\
- CommandLine|contains|all:
  - :\Users\
  - \Contacts\
condition: 1 of selection_proc_* and 1 of selection_folders_*
```

## False Positives

- Unknown

## References

- https://www.virustotal.com/gui/file/91ba814a86ddedc7a9d546e26f912c541205b47a853d227756ab1334ade92c3f
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-russia-ukraine-military
- https://learn.microsoft.com/en-us/windows/win32/shell/csidl

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_script_exec_from_env_folder.yml)
