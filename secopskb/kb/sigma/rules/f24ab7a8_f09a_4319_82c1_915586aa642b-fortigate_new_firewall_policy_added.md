---
sigma_id: "f24ab7a8-f09a-4319-82c1-915586aa642b"
title: "FortiGate - New Firewall Policy Added"
framework: "sigma"
generated: "true"
source_path: "rules/network/fortinet/fortigate/fortinet_fortigate_new_firewall_policy_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_firewall_policy_added.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "medium"
logsource: "fortigate / event"
aliases:
  - "f24ab7a8-f09a-4319-82c1-915586aa642b"
  - "FortiGate - New Firewall Policy Added"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# FortiGate - New Firewall Policy Added

Detects the addition of a new firewall policy on a Fortinet FortiGate Firewall.

## Metadata

- Rule ID: f24ab7a8-f09a-4319-82c1-915586aa642b
- Status: experimental
- Level: medium
- Author: Marco Pedrinazzi @pedrinazziM (InTheCyber)
- Date: 2025-11-01
- Source Path: rules/network/fortinet/fortigate/fortinet_fortigate_new_firewall_policy_added.yml

## Logsource

- product: fortigate
- service: event

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  action: Add
  cfgpath: firewall.policy
condition: selection
```

## False Positives

- A firewall policy can be added for legitimate purposes.

## References

- https://www.fortiguard.com/psirt/FG-IR-24-535
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/398/event
- https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/333889629/config-firewall-policy
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/44547/44547-logid-event-config-objattr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_firewall_policy_added.yml)
