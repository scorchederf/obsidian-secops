---
atomic_guid: "f047c7de-a2d9-406e-a62b-12a09d9516f4"
title: "Logon Scripts - Mac"
framework: "atomic"
generated: "true"
attack_technique_id: "T1037.002"
attack_technique_name: "Boot or Logon Initialization Scripts: Logon Script (Mac)"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.002/T1037.002.yaml"
build_date: "2026-04-27 19:12:25"
executor: "manual"
aliases:
  - "f047c7de-a2d9-406e-a62b-12a09d9516f4"
  - "Logon Scripts - Mac"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Mac logon script

## ATT&CK Mapping

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts#^t1037002-login-hook|T1037.002: Login Hook]]

## Executor

- name: manual
- steps: 1. Create the required plist file

    sudo touch /private/var/root/Library/Preferences/com.apple.loginwindow.plist

2. Populate the plist with the location of your shell script

    sudo defaults write com.apple.loginwindow LoginHook /Library/Scripts/AtomicRedTeam.sh

3. Create the required plist file in the target user's Preferences directory

	  touch /Users/$USER/Library/Preferences/com.apple.loginwindow.plist

4. Populate the plist with the location of your shell script

	  defaults write com.apple.loginwindow LoginHook /Library/Scripts/AtomicRedTeam.sh


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.002/T1037.002.yaml)
