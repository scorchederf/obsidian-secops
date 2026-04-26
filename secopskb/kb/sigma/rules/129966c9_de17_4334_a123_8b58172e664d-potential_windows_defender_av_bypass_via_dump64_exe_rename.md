---
sigma_id: "129966c9-de17-4334-a123-8b58172e664d"
title: "Potential Windows Defender AV Bypass Via Dump64.EXE Rename"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dump64_defender_av_bypass_rename.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dump64_defender_av_bypass_rename.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "129966c9-de17-4334-a123-8b58172e664d"
  - "Potential Windows Defender AV Bypass Via Dump64.EXE Rename"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Windows Defender AV Bypass Via Dump64.EXE Rename

Detects when a user is potentially trying to bypass the Windows Defender AV by renaming a tool to dump64.exe and placing it in the Visual Studio folder.
Currently the rule is covering only usage of procdump but other utilities can be added in order to increase coverage.

## Metadata

- Rule ID: 129966c9-de17-4334-a123-8b58172e664d
- Status: test
- Level: high
- Author: Austin Songer @austinsonger, Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-11-26
- Modified: 2024-06-21
- Source Path: rules/windows/process_creation/proc_creation_win_dump64_defender_av_bypass_rename.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_dump:
  Image|startswith: :\Program Files
  Image|contains: \Microsoft Visual Studio\
  Image|endswith: \dump64.exe
selection_tools_procdump:
- OriginalFileName: procdump
- CommandLine|contains:
  - ' -ma '
  - ' -mp '
condition: selection_dump and 1 of selection_tools_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1460597833917251595

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dump64_defender_av_bypass_rename.yml)
