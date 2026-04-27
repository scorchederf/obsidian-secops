---
atomic_guid: "ff1d8c25-2aa4-4f18-a425-fede4a41ee88"
title: "List macOS Firewall Rules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "ff1d8c25-2aa4-4f18-a425-fede4a41ee88"
  - "List macOS Firewall Rules"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# List macOS Firewall Rules

"This will test if the macOS firewall is enabled and/or show what rules are configured. Must be run with elevated privileges. Upon successful execution, these commands will output various information about the firewall configuration, including status and specific port/protocol blocks or allows. 

Using `defaults`, additional arguments can be added to see filtered details, such as `globalstate` for global configuration (\"Is it on or off?\"), `firewall` for common application allow rules, and `explicitauths` for specific rules configured by the user. 

Using `socketfilterfw`, flags such as --getglobalstate or --listapps can be used for similar filtering. At least one flag is required to send parseable output to standard out.

## Metadata

- Atomic GUID: ff1d8c25-2aa4-4f18-a425-fede4a41ee88
- Technique: T1016: System Network Configuration Discovery
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1016/T1016.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo defaults read /Library/Preferences/com.apple.alf
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
