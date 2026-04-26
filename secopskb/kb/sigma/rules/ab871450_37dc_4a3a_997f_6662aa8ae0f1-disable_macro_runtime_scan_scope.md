---
sigma_id: "ab871450-37dc-4a3a-997f-6662aa8ae0f1"
title: "Disable Macro Runtime Scan Scope"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_macroruntimescanscope.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_macroruntimescanscope.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "ab871450-37dc-4a3a-997f-6662aa8ae0f1"
  - "Disable Macro Runtime Scan Scope"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Macro Runtime Scan Scope

Detects tampering with the MacroRuntimeScanScope registry key to disable runtime scanning of enabled macros

## Metadata

- Rule ID: ab871450-37dc-4a3a-997f-6662aa8ae0f1
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-25
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disable_macroruntimescanscope.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \SOFTWARE\
  - \Microsoft\Office\
  - \Common\Security
  TargetObject|endswith: \MacroRuntimeScanScope
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/en-us/security/blog/2018/09/12/office-vba-amsi-parting-the-veil-on-malicious-macros/
- https://admx.help/?Category=Office2016&Policy=office16.Office.Microsoft.Policies.Windows::L_MacroRuntimeScanScope
- https://github.com/S3cur3Th1sSh1t/OffensiveVBA/blob/28cc6a2802d8176195ac19b3c8e9a749009a82a3/src/AMSIbypasses.vba

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_macroruntimescanscope.yml)
