---
atomic_guid: "3d456e2b-a7db-4af8-b5b3-720e7c4d9da5"
title: "Edge Chromium Addon - VPN"
framework: "atomic"
generated: "true"
attack_technique_id: "T1176"
attack_technique_name: "Browser Extensions"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1176/T1176.yaml"
build_date: "2026-04-26 14:38:40"
executor: "manual"
aliases:
  - "3d456e2b-a7db-4af8-b5b3-720e7c4d9da5"
  - "Edge Chromium Addon - VPN"
platforms:
  - "windows"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Edge Chromium Addon - VPN

Adversaries may use VPN extensions in an attempt to hide traffic sent from a compromised host. This will install one (of many) available VPNS in the Edge add-on store.

## Metadata

- Atomic GUID: 3d456e2b-a7db-4af8-b5b3-720e7c4d9da5
- Technique: T1176: Browser Extensions
- Platforms: windows, macos
- Executor: manual
- Source Path: atomics/T1176/T1176.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1176-software_extensions|T1176]]

## Executor

- name: manual
- steps: 1. Navigate to https://microsoftedge.microsoft.com/addons/detail/fjnehcbecaggobjholekjijaaekbnlgj
in Edge Chromium

2. Click 'Get'


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1176/T1176.yaml)
