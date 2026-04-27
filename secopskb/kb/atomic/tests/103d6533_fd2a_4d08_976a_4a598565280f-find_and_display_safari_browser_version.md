---
atomic_guid: "103d6533-fd2a-4d08-976a-4a598565280f"
title: "Find and Display Safari Browser Version"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518"
attack_technique_name: "Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "103d6533-fd2a-4d08-976a-4a598565280f"
  - "Find and Display Safari Browser Version"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Find and Display Safari Browser Version

Adversaries may attempt to get a listing of non-security related software that is installed on the system. Adversaries may use the information from Software Discovery during automated discovery to shape follow-on behaviors

## Metadata

- Atomic GUID: 103d6533-fd2a-4d08-976a-4a598565280f
- Technique: T1518: Software Discovery
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1518/T1518.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
/usr/libexec/PlistBuddy -c "print :CFBundleShortVersionString" /Applications/Safari.app/Contents/Info.plist
/usr/libexec/PlistBuddy -c "print :CFBundleVersion" /Applications/Safari.app/Contents/Info.plist
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml)
