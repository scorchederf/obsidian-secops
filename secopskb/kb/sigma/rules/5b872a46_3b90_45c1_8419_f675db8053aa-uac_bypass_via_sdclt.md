---
sigma_id: "5b872a46-3b90-45c1-8419-f675db8053aa"
title: "UAC Bypass via Sdclt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_uac_bypass_sdclt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_sdclt.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "5b872a46-3b90-45c1-8419-f675db8053aa"
  - "UAC Bypass via Sdclt"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass via Sdclt

Detects the pattern of UAC Bypass using registry key manipulation of sdclt.exe (e.g. UACMe 53)

## Metadata

- Rule ID: 5b872a46-3b90-45c1-8419-f675db8053aa
- Status: test
- Level: high
- Author: Omer Yampel, Christian Burkard (Nextron Systems)
- Date: 2017-03-17
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_uac_bypass_sdclt.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection1:
  TargetObject|endswith: Software\Classes\exefile\shell\runas\command\isolatedCommand
selection2:
  TargetObject|endswith: Software\Classes\Folder\shell\open\command\SymbolicLinkValue
  Details|re: -1[0-9]{3}\\Software\\Classes\\
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://enigma0x3.net/2017/03/17/fileless-uac-bypass-using-sdclt-exe/
- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_sdclt.yml)
