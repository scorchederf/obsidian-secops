---
atomic_guid: "b2698b33-984c-4a1c-93bb-e4ba72a0babb"
title: "Enumerate Active Directory Password Policy with get-addefaultdomainpasswordpolicy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "b2698b33-984c-4a1c-93bb-e4ba72a0babb"
  - "Enumerate Active Directory Password Policy with get-addefaultdomainpasswordpolicy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Active Directory Password Policy with get-addefaultdomainpasswordpolicy

The following Atomic test will utilize get-addefaultdomainpasswordpolicy to enumerate domain password policy.
Upon successful execution a listing of the policy implemented will display.
Reference: https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-addefaultdomainpasswordpolicy?view=windowsserver2022-ps

## Metadata

- Atomic GUID: b2698b33-984c-4a1c-93bb-e4ba72a0babb
- Technique: T1201: Password Policy Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
get-addefaultdomainpasswordpolicy
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
