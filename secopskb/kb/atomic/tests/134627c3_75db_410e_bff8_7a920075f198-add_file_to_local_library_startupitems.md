---
atomic_guid: "134627c3-75db-410e-bff8-7a920075f198"
title: "Add file to Local Library StartupItems"
framework: "atomic"
generated: "true"
attack_technique_id: "T1037.005"
attack_technique_name: "Boot or Logon Initialization Scripts: Startup Items"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.005/T1037.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "134627c3-75db-410e-bff8-7a920075f198"
  - "Add file to Local Library StartupItems"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Add file to Local Library StartupItems

Modify or create an file in /Library/StartupItems
[Reference](https://www.alienvault.com/blogs/labs-research/diversity-in-recent-mac-malware)

## Metadata

- Atomic GUID: 134627c3-75db-410e-bff8-7a920075f198
- Technique: T1037.005: Boot or Logon Initialization Scripts: Startup Items
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1037.005/T1037.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.005]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo touch /Library/StartupItems/EvilStartup.plist
```

### Cleanup

```bash
sudo rm /Library/StartupItems/EvilStartup.plist
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.005/T1037.005.yaml)
