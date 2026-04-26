---
atomic_guid: "3ecd790d-2617-4abf-9a8c-4e8d47da9ee1"
title: "Chrome/Chromium (Developer Mode)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1176"
attack_technique_name: "Browser Extensions"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1176/T1176.yaml"
build_date: "2026-04-26 14:38:40"
executor: "manual"
aliases:
  - "3ecd790d-2617-4abf-9a8c-4e8d47da9ee1"
  - "Chrome/Chromium (Developer Mode)"
platforms:
  - "linux"
  - "windows"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Chrome/Chromium (Developer Mode)

Turn on Chrome/Chromium developer mode and Load Extension found in the src directory

## Metadata

- Atomic GUID: 3ecd790d-2617-4abf-9a8c-4e8d47da9ee1
- Technique: T1176: Browser Extensions
- Platforms: linux, windows, macos
- Executor: manual
- Source Path: atomics/T1176/T1176.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1176-software_extensions|T1176]]

## Executor

- name: manual
- steps: 1. Navigate to [chrome://extensions](chrome://extensions) and
tick 'Developer Mode'.

2. Click 'Load unpacked extension...' and navigate to
[Browser_Extension](../t1176/src/)

3. Click 'Select'


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1176/T1176.yaml)
