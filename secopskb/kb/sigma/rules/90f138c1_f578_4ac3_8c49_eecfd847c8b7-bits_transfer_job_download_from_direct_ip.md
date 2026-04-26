---
sigma_id: "90f138c1-f578-4ac3-8c49-eecfd847c8b7"
title: "BITS Transfer Job Download From Direct IP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_ip_address.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_ip_address.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / bits-client"
aliases:
  - "90f138c1-f578-4ac3-8c49-eecfd847c8b7"
  - "BITS Transfer Job Download From Direct IP"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# BITS Transfer Job Download From Direct IP

Detects a BITS transfer job downloading file(s) from a direct IP address.

## Metadata

- Rule ID: 90f138c1-f578-4ac3-8c49-eecfd847c8b7
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-11
- Modified: 2023-03-27
- Source Path: rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_ip_address.yml

## Logsource

- product: windows
- service: bits-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Detection

```yaml
selection:
  EventID: 16403
  RemoteName|contains:
  - http://1
  - http://2
  - http://3
  - http://4
  - http://5
  - http://6
  - http://7
  - http://8
  - http://9
  - https://1
  - https://2
  - https://3
  - https://4
  - https://5
  - https://6
  - https://7
  - https://8
  - https://9
filter_optional_local_networks:
  RemoteName|contains:
  - ://10.
  - ://192.168.
  - ://172.16.
  - ://172.17.
  - ://172.18.
  - ://172.19.
  - ://172.20.
  - ://172.21.
  - ://172.22.
  - ://172.23.
  - ://172.24.
  - ://172.25.
  - ://172.26.
  - ://172.27.
  - ://172.28.
  - ://172.29.
  - ://172.30.
  - ://172.31.
  - ://127.
  - ://169.254.
filter_optional_seven_zip:
  RemoteName|contains:
  - https://7-
  - http://7-
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://blog.netspi.com/15-ways-to-download-a-file/#bitsadmin
- https://isc.sans.edu/diary/22264
- https://lolbas-project.github.io/lolbas/Binaries/Bitsadmin/
- https://blog.talosintelligence.com/breaking-the-silence-recent-truebot-activity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_ip_address.yml)
