---
sigma_id: "ceb407f6-8277-439b-951f-e4210e3ed956"
title: "Cisco Clear Logs"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_clear_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_clear_logs.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "cisco / aaa"
aliases:
  - "ceb407f6-8277-439b-951f-e4210e3ed956"
  - "Cisco Clear Logs"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cisco Clear Logs

Clear command history in network OS which is used for defense evasion

## Metadata

- Rule ID: ceb407f6-8277-439b-951f-e4210e3ed956
- Status: test
- Level: high
- Author: Austin Clark
- Date: 2019-08-12
- Modified: 2023-05-26
- Source Path: rules/network/cisco/aaa/cisco_cli_clear_logs.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
keywords:
- clear logging
- clear archive
condition: keywords
```

## False Positives

- Legitimate administrators may run these commands

## References

- https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5000/sw/command/reference/sysmgmt/n5k-sysmgmt-cr/n5k-sm_cmds_c.html
- https://www.cisco.com/c/en/us/td/docs/ios/12_2sr/12_2sra/feature/guide/srmgtint.html#wp1127609

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_clear_logs.yml)
