---
sigma_id: "69ffc84e-8b1a-4024-8351-e018f66b8275"
title: "FortiGate - User Group Modified"
framework: "sigma"
generated: "true"
source_path: "rules/network/fortinet/fortigate/fortinet_fortigate_user_group_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_user_group_modified.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "medium"
logsource: "fortigate / event"
aliases:
  - "69ffc84e-8b1a-4024-8351-e018f66b8275"
  - "FortiGate - User Group Modified"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# FortiGate - User Group Modified

Detects the modification of a user group on a Fortinet FortiGate Firewall.
The group could be used to grant VPN access to a network.

## Metadata

- Rule ID: 69ffc84e-8b1a-4024-8351-e018f66b8275
- Status: experimental
- Level: medium
- Author: Marco Pedrinazzi @pedrinazziM (InTheCyber)
- Date: 2025-11-01
- Source Path: rules/network/fortinet/fortigate/fortinet_fortigate_user_group_modified.yml

## Logsource

- product: fortigate
- service: event

## Detection

```yaml
selection:
  action: Edit
  cfgpath: user.group
condition: selection
```

## False Positives

- A group can be modified for legitimate purposes.

## References

- https://www.fortiguard.com/psirt/FG-IR-24-535
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/398/event
- https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/328136827/config-user-group
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/44547/44547-logid-event-config-objattr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_user_group_modified.yml)
