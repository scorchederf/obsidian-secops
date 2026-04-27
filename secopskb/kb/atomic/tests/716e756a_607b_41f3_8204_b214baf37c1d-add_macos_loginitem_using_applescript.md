---
atomic_guid: "716e756a-607b-41f3-8204-b214baf37c1d"
title: "Add macOS LoginItem using Applescript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.015"
attack_technique_name: "Boot or Logon Autostart Execution: Login Items"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.015/T1547.015.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "716e756a-607b-41f3-8204-b214baf37c1d"
  - "Add macOS LoginItem using Applescript"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Runs osascript on a file to create new LoginItem for current user.
NOTE: Will popup dialog prompting user to Allow or Deny Terminal.app to control "System Events"
Therefore, it can't be automated until the TCC is granted.
The login item launches Safari.app when user logs in, but there is a cleanup script to remove it as well.
In addition to the `osascript` Process Events, file modification events to
`/Users/*/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm` should be seen.

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547015-login-items|T1547.015: Login Items]]

## Input Arguments

### cleanup_script

- description: path to Applescript source to delete Safari LoginItem.
- type: string
- default: PathToAtomicsFolder/T1547.015/src/remove_login_item.osa

### scriptfile

- description: path to Applescript source to add Safari LoginItem.
- type: string
- default: PathToAtomicsFolder/T1547.015/src/add_login_item.osa

## Executor

- name: bash

### Command

```bash
osascript #{scriptfile}
```

### Cleanup

```bash
osascript #{cleanup_script}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.015/T1547.015.yaml)
