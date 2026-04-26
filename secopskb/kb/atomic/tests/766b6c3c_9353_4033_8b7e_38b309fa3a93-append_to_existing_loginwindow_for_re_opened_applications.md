---
atomic_guid: "766b6c3c-9353-4033-8b7e-38b309fa3a93"
title: "Append to existing loginwindow for Re-Opened Applications"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.007"
attack_technique_name: "Boot or Logon Autostart Execution: Re-opened Applications"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.007/T1547.007.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "766b6c3c-9353-4033-8b7e-38b309fa3a93"
  - "Append to existing loginwindow for Re-Opened Applications"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Append to existing loginwindow for Re-Opened Applications

Appends an entry to launch Calculator hidden loginwindow.*.plist for next login.
Note that the change may not result in the added Calculator program launching on next user login.
It may depend on which version of macOS you are running on.

## Metadata

- Atomic GUID: 766b6c3c-9353-4033-8b7e-38b309fa3a93
- Technique: T1547.007: Boot or Logon Autostart Execution: Re-opened Applications
- Platforms: macos
- Executor: sh
- Dependency Executor: bash
- Source Path: atomics/T1547.007/T1547.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.007]]

## Input Arguments

### exe_path

- description: path to compiled program
- type: path
- default: /tmp/t1547007_append_exe

### objc_source_path

- description: path to objective C program
- type: path
- default: PathToAtomicsFolder/T1547.007/src/append_reopen_loginwindow.m

## Dependencies

compile C program

### Prerequisite Check

```text
if [ -f "#{exe_path}" ]; then exit 0 ; else exit 1; fi
```

### Get Prerequisite

```text
cc #{objc_source_path} -o #{exe_path} -framework Cocoa
```

## Executor

- name: sh

### Command

```sh
FILE=`find ~/Library/Preferences/ByHost/com.apple.loginwindow.*.plist -type f | head -1`
if [ -z "${FILE}" ] ; then echo "No loginwindow plist file found" && exit 1 ; fi
echo save backup copy to /tmp/
cp ${FILE} /tmp/t1547007_loginwindow-backup.plist
echo before
plutil -p ${FILE}
echo overwriting...
#{exe_path} ${FILE} && echo after && plutil -p ${FILE}
```

### Cleanup

```sh
rm -f #{exe_path}
# revert to backup copy
FILE=`find ~/Library/Preferences/ByHost/com.apple.loginwindow.*.plist -type f | head -1`
if [ -z "${FILE}" ] ; then
   exit 0
fi
mv /tmp/t1547007_loginwindow-backup.plist ${FILE}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.007/T1547.007.yaml)
