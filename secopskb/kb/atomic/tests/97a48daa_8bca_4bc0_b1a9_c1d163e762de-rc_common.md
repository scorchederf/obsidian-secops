---
atomic_guid: "97a48daa-8bca-4bc0-b1a9-c1d163e762de"
title: "rc.common"
framework: "atomic"
generated: "true"
attack_technique_id: "T1037.004"
attack_technique_name: "Boot or Logon Initialization Scripts: Rc.common"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.004/T1037.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "97a48daa-8bca-4bc0-b1a9-c1d163e762de"
  - "rc.common"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# rc.common

Modify rc.common

[Reference](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html)

## Metadata

- Atomic GUID: 97a48daa-8bca-4bc0-b1a9-c1d163e762de
- Technique: T1037.004: Boot or Logon Initialization Scripts: Rc.common
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1037.004/T1037.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.004]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo echo osascript -e 'tell app "Finder" to display dialog "Hello World"' >> /etc/rc.common
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.004/T1037.004.yaml)
