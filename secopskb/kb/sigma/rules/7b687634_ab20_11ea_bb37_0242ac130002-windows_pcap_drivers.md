---
sigma_id: "7b687634-ab20-11ea-bb37-0242ac130002"
title: "Windows Pcap Drivers"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_pcap_drivers.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_pcap_drivers.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "7b687634-ab20-11ea-bb37-0242ac130002"
  - "Windows Pcap Drivers"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Pcap Drivers

Detects Windows Pcap driver installation based on a list of associated .sys files.

## Metadata

- Rule ID: 7b687634-ab20-11ea-bb37-0242ac130002
- Status: test
- Level: medium
- Author: Cian Heasley
- Date: 2020-06-10
- Modified: 2023-04-14
- Source Path: rules/windows/builtin/security/win_security_pcap_drivers.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Detection

```yaml
selection:
  EventID: 4697
  ServiceFileName|contains:
  - pcap
  - npcap
  - npf
  - nm3
  - ndiscap
  - nmnt
  - windivert
  - USBPcap
  - pktmon
condition: selection
```

## False Positives

- Unknown

## References

- https://ragged-lab.blogspot.com/2020/06/capturing-pcap-driver-installations.html#more

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_pcap_drivers.yml)
