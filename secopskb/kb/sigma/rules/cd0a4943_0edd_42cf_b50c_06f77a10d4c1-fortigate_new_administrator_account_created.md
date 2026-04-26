---
sigma_id: "cd0a4943-0edd-42cf-b50c-06f77a10d4c1"
title: "FortiGate - New Administrator Account Created"
framework: "sigma"
generated: "true"
source_path: "rules/network/fortinet/fortigate/fortinet_fortigate_new_admin_account_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_admin_account_created.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "medium"
logsource: "fortigate / event"
aliases:
  - "cd0a4943-0edd-42cf-b50c-06f77a10d4c1"
  - "FortiGate - New Administrator Account Created"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# FortiGate - New Administrator Account Created

Detects the creation of an administrator account on a Fortinet FortiGate Firewall.

## Metadata

- Rule ID: cd0a4943-0edd-42cf-b50c-06f77a10d4c1
- Status: experimental
- Level: medium
- Author: Marco Pedrinazzi @pedrinazziM (InTheCyber)
- Date: 2025-11-01
- Source Path: rules/network/fortinet/fortigate/fortinet_fortigate_new_admin_account_created.yml

## Logsource

- product: fortigate
- service: event

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection:
  action: Add
  cfgpath: system.admin
condition: selection
```

## False Positives

- An administrator account can be created for legitimate purposes. Investigate the account details to determine if it is authorized.

## References

- https://www.fortiguard.com/psirt/FG-IR-24-535
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/398/event
- https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/390485493/config-system-admin
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/44547/44547-logid-event-config-objattr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_admin_account_created.yml)
