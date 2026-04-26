---
sigma_id: "af5732ed-764e-489d-826d-0447c8b36242"
title: "Windows MSIX Package Support Framework AI_STUBS Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msix_ai_stub_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msix_ai_stub_execution.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "af5732ed-764e-489d-826d-0447c8b36242"
  - "Windows MSIX Package Support Framework AI_STUBS Execution"
attack_technique_ids:
  - "T1218"
  - "T1553.005"
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows MSIX Package Support Framework AI_STUBS Execution

Detects execution of Advanced Installer MSIX Package Support Framework (PSF) components, specifically AI_STUBS executables with original filename 'popupwrapper.exe'.
This activity may indicate malicious MSIX packages build with Advanced Installer leveraging the Package Support Framework to bypass application control restrictions.

## Metadata

- Rule ID: af5732ed-764e-489d-826d-0447c8b36242
- Status: experimental
- Level: low
- Author: Michael Haag, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-03
- Source Path: rules/windows/process_creation/proc_creation_win_msix_ai_stub_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.005]]
- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  Image|endswith:
  - \AI_STUBS\AiStubX64Elevated.exe
  - \AI_STUBS\AiStubX86Elevated.exe
  - \AI_STUBS\AiStubX64.exe
  - \AI_STUBS\AiStubX86.exe
  OriginalFileName: popupwrapper.exe
condition: selection
```

## False Positives

- Legitimate applications packaged with Advanced Installer using Package Support Framework

## References

- https://redcanary.com/blog/threat-intelligence/msix-installers/
- https://redcanary.com/threat-detection-report/techniques/installer-packages/
- https://learn.microsoft.com/en-us/windows/msix/package/package-support-framework
- https://www.splunk.com/en_us/blog/security/msix-weaponization-threat-detection-splunk.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msix_ai_stub_execution.yml)
