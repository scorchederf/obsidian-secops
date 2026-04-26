---
sigma_id: "5df86130-4e95-4a54-90f7-26541b40aec2"
title: "Registry Modification to Hidden File Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_hidden_extention.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hidden_extention.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "5df86130-4e95-4a54-90f7-26541b40aec2"
  - "Registry Modification to Hidden File Extension"
attack_technique_ids:
  - "T1137"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Modification to Hidden File Extension

Hides the file extension through modification of the registry

## Metadata

- Rule ID: 5df86130-4e95-4a54-90f7-26541b40aec2
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-22
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_hidden_extention.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137]]

## Detection

```yaml
selection_HideFileExt:
  TargetObject|endswith: \SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\HideFileExt
  Details: DWORD (0x00000001)
selection_Hidden:
  TargetObject|endswith: \SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Hidden
  Details: DWORD (0x00000002)
condition: 1 of selection_*
```

## False Positives

- Administrative scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md#atomic-test-1---modify-registry-of-current-user-profile---cmd
- https://unit42.paloaltonetworks.com/ransomware-families/
- https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=TrojanSpy%3aMSIL%2fHakey.A

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hidden_extention.yml)
