---
atomic_guid: "a4420f93-5386-4290-b780-f4f66abc7070"
title: "Modify VSS Service Permissions"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "a4420f93-5386-4290-b780-f4f66abc7070"
  - "Modify VSS Service Permissions"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify VSS Service Permissions

This atomic test alters the security settings of the Volume Shadow Copy Service (VSS) by modifying its permissions, potentially impacting system recovery operations. The specific permissions set by the command are as follows:
- Deny Generic All (GA) permissions to Network Users (NU)
- Deny GA permissions to Everyone (WD)
- Deny GA permissions to Anonymous (AN)
- Allow Full Access (FA) and Generic All (GA) permissions to Everyone (WD) in System ACL (SACL)
- Allow Object Inherit and Inherit Only (OIIO) Full Access (FA) and GA permissions to Everyone (WD) in SACL
These permissions can significantly restrict VSS functionalities, including backup and restore operations. As such, it is essential to run this test only in a controlled environment with administrative privileges.
A cleanup command is provided to reset VSS permissions to a common default configuration, which should be verified against your specific system's configuration. It's crucial to use this cleanup command after testing to ensure the system's backup and recovery capabilities remain functional. Running this test on a production system or critical environment is not recommended without proper precautions and a robust recovery plan.

## Metadata

- Atomic GUID: a4420f93-5386-4290-b780-f4f66abc7070
- Technique: T1490: Inhibit System Recovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc sdset VSS D:(D;;GA;;;NU)(D;;GA;;;WD)(D;;GA;;;AN)S:(AU;FA;GA;;;WD)(AU;OIIOFA;GA;;;WD)
```

### Cleanup

```cmd
sc sdset VSS D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;LC;;;BU)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
