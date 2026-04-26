---
sigma_id: "e2482f8d-3443-4237-b906-cc145d87a076"
title: "Disable Internal Tools or Feature in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_function_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_function_user.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "e2482f8d-3443-4237-b906-cc145d87a076"
  - "Disable Internal Tools or Feature in Registry"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Internal Tools or Feature in Registry

Detects registry modifications that change features of internal Windows tools (malware like Agent Tesla uses this technique)

## Metadata

- Rule ID: e2482f8d-3443-4237-b906-cc145d87a076
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems), CrimpSec
- Date: 2022-03-18
- Modified: 2025-06-04
- Source Path: rules/windows/registry/registry_set/registry_set_disable_function_user.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_set_1:
  TargetObject|endswith:
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisableCMD
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoControlPanel
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoRun
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\StartMenuLogOff
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\DisableChangePassword
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\DisableLockWorkstation
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\DisableRegistryTools
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\DisableTaskmgr
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\NoDispBackgroundPage
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\NoDispCPL
  - SOFTWARE\Policies\Microsoft\Windows\Explorer\DisableNotificationCenter
  - SOFTWARE\Policies\Microsoft\Windows\System\DisableCMD
  Details: DWORD (0x00000001)
selection_set_0:
  TargetObject|endswith:
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ConsentPromptBehaviorAdmin
  - Software\Microsoft\Windows\CurrentVersion\Policies\System\InactivityTimeoutSecs
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\shutdownwithoutlogon
  - SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications\ToastEnabled
  - SYSTEM\CurrentControlSet\Control\Storage\Write Protection
  - SYSTEM\CurrentControlSet\Control\StorageDevicePolicies\WriteProtect
  Details: DWORD (0x00000000)
condition: 1 of selection_set_*
```

## False Positives

- Legitimate admin script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md
- https://www.mandiant.com/resources/unc2165-shifts-to-evade-sanctions
- https://blogs.vmware.com/security/2022/11/batloader-the-evasive-downloader-malware.html
- https://www.malwarebytes.com/blog/detections/pum-optional-nodispbackgroundpage
- https://www.malwarebytes.com/blog/detections/pum-optional-nodispcpl
- https://bazaar.abuse.ch/sample/7bde840c7e8c36dce4c3bac937bcf39f36a6f118001b406bfbbc25451ce44fb4/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_function_user.yml)
