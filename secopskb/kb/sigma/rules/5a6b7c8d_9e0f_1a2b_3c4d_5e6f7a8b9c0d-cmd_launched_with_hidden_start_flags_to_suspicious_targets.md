---
sigma_id: "5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d"
title: "Cmd Launched with Hidden Start Flags to Suspicious Targets"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_launched_with_hidden_start_flag.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_launched_with_hidden_start_flag.yml"
build_date: "2026-04-26 14:14:22"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d"
  - "Cmd Launched with Hidden Start Flags to Suspicious Targets"
attack_technique_ids:
  - "T1564.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cmd Launched with Hidden Start Flags to Suspicious Targets

Detects cmd.exe executing commands with the "start" utility using "/b" (no window) or "/min" (minimized) flags.
To reduce false positives from standard background tasks, detection is restricted to scenarios where the target is a known script extension or located in suspicious temporary/public directories.
This technique was observed in Chaos, DarkSide, and Emotet malware campaigns.

## Metadata

- Rule ID: 5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d
- Status: experimental
- Level: medium
- Author: Vladan Sekulic, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-01-24
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_launched_with_hidden_start_flag.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

## Detection

```yaml
selection_cmd_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cmd_hidden_start_1:
  CommandLine|contains|windash:
  - 'start '
  - start/b
  - start/min
selection_cmd_hidden_start_2:
  CommandLine|contains|windash:
  - '/b '
  - /b"
  - '/min '
  - /min"
selection_cli_uncommon_location:
  CommandLine|contains:
  - :\Perflogs\
  - :\Temp\
  - :\Users\Default\
  - :\Windows\Temp\
  - \AppData\Roaming\
  - \Contacts\
  - \Documents\
  - \Downloads\
  - \Favorites\
  - \Favourites\
  - \inetpub\
  - \Music\
  - \Photos\
  - \Temporary Internet\
  - \Users\Public\
  - \Videos\
selection_cli_susp_extension:
  CommandLine|contains:
  - .bat
  - .cmd
  - .cpl
  - .hta
  - .js
  - .ps1
  - .scr
  - .vbe
  - .vbs
selection_cli_susp_pattern:
  CommandLine|contains:
  - ' -nop '
  - ' -sta '
  - .downloadfile(
  - .downloadstring(
  - '-noni '
  - '-w hidden '
condition: all of selection_cmd_* and 1 of selection_cli_*
```

## False Positives

- Legitimate administrative scripts running from temporary folders.
- Niche software updaters utilizing hidden batch files in ProgramData.

## References

- https://www.fortinet.com/blog/threat-research/evolution-of-chaos-ransomware-faster-smarter-and-more-dangerous
- https://www.fortinet.com/blog/threat-research/newly-discovered-function-in-darkside-ransomware-variant-targets-disk-partitions
- https://www.fortinet.com/blog/threat-research/ms-office-files-involved-in-emotet-trojan-campaign-pt-one
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_launched_with_hidden_start_flag.yml)
