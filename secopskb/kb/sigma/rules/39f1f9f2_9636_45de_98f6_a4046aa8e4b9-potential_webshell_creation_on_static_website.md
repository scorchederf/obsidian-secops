---
sigma_id: "39f1f9f2-9636-45de-98f6-a4046aa8e4b9"
title: "Potential Webshell Creation On Static Website"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_webshell_creation_detect.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_webshell_creation_detect.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "39f1f9f2-9636-45de-98f6-a4046aa8e4b9"
  - "Potential Webshell Creation On Static Website"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Webshell Creation On Static Website

Detects the creation of files with certain extensions on a static web site. This can be indicative of potential uploads of a web shell.

## Metadata

- Rule ID: 39f1f9f2-9636-45de-98f6-a4046aa8e4b9
- Status: test
- Level: medium
- Author: Beyu Denis, oscd.community, Tim Shelton, Thurein Oo
- Date: 2019-10-22
- Modified: 2023-10-15
- Source Path: rules/windows/file/file_event/file_event_win_webshell_creation_detect.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection_wwwroot_path:
  TargetFilename|contains: \inetpub\wwwroot\
selection_wwwroot_ext:
  TargetFilename|contains:
  - .ashx
  - .asp
  - .ph
  - .soap
selection_htdocs_path:
  TargetFilename|contains:
  - \www\
  - \htdocs\
  - \html\
selection_htdocs_ext:
  TargetFilename|contains: .ph
filter_main_temp:
  TargetFilename|contains:
  - \AppData\Local\Temp\
  - \Windows\Temp\
filter_main_system:
  Image: System
filter_main_legitimate:
  TargetFilename|contains: \xampp
condition: (all of selection_wwwroot_* or all of selection_htdocs_*) and not 1 of
  filter_main_*
```

## False Positives

- Legitimate administrator or developer creating legitimate executable files in a web application folder

## References

- PT ESC rule and personal experience
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/c95a0a1a2855dc0cd7f7327614545fe30482a636/Upload%20Insecure%20Files/README.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_webshell_creation_detect.yml)
