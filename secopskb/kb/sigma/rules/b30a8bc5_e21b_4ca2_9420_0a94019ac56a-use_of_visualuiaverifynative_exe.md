---
sigma_id: "b30a8bc5-e21b-4ca2-9420-0a94019ac56a"
title: "Use of VisualUiaVerifyNative.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b30a8bc5-e21b-4ca2-9420-0a94019ac56a"
  - "Use of VisualUiaVerifyNative.exe"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of VisualUiaVerifyNative.exe

VisualUiaVerifyNative.exe is a Windows SDK that can be used for AWL bypass and is listed in Microsoft's recommended block rules.

## Metadata

- Rule ID: b30a8bc5-e21b-4ca2-9420-0a94019ac56a
- Status: test
- Level: medium
- Author: Christopher Peacock @SecurePeacock, SCYTHE @scythe_io
- Date: 2022-06-01
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
- Image|endswith: \VisualUiaVerifyNative.exe
- OriginalFileName: VisualUiaVerifyNative.exe
condition: selection
```

## False Positives

- Legitimate testing of Microsoft UI parts.

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/VisualUiaVerifyNative/
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/design/applications-that-can-bypass-wdac
- https://bohops.com/2020/10/15/exploring-the-wdac-microsoft-recommended-block-rules-visualuiaverifynative/
- https://github.com/MicrosoftDocs/windows-itpro-docs/commit/937db704b9148e9cee7c7010cad4d00ce9c4fdad

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml)
