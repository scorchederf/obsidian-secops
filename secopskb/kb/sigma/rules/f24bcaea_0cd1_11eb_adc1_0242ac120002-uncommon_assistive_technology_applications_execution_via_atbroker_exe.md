---
sigma_id: "f24bcaea-0cd1-11eb-adc1-0242ac120002"
title: "Uncommon  Assistive Technology Applications Execution Via AtBroker.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_atbroker_uncommon_ats_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_atbroker_uncommon_ats_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f24bcaea-0cd1-11eb-adc1-0242ac120002"
  - "Uncommon  Assistive Technology Applications Execution Via AtBroker.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon  Assistive Technology Applications Execution Via AtBroker.EXE

Detects the start of a non built-in assistive technology applications via "Atbroker.EXE".

## Metadata

- Rule ID: f24bcaea-0cd1-11eb-adc1-0242ac120002
- Status: test
- Level: medium
- Author: Mateusz Wydra, oscd.community
- Date: 2020-10-12
- Modified: 2024-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_atbroker_uncommon_ats_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \AtBroker.exe
- OriginalFileName: AtBroker.exe
selection_cli:
  CommandLine|contains: start
filter_main_builtin:
  CommandLine|contains:
  - animations
  - audiodescription
  - caretbrowsing
  - caretwidth
  - colorfiltering
  - cursorindicator
  - cursorscheme
  - filterkeys
  - focusborderheight
  - focusborderwidth
  - highcontrast
  - keyboardcues
  - keyboardpref
  - livecaptions
  - magnifierpane
  - messageduration
  - minimumhitradius
  - mousekeys
  - Narrator
  - osk
  - overlappedcontent
  - showsounds
  - soundsentry
  - speechreco
  - stickykeys
  - togglekeys
  - voiceaccess
  - windowarranging
  - windowtracking
  - windowtrackingtimeout
  - windowtrackingzorder
filter_optional_java:
  CommandLine|contains: Oracle_JavaAccessBridge
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate, non-default assistive technology applications execution

## References

- http://www.hexacorn.com/blog/2016/07/22/beyond-good-ol-run-key-part-42/
- https://lolbas-project.github.io/lolbas/Binaries/Atbroker/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_atbroker_uncommon_ats_execution.yml)
