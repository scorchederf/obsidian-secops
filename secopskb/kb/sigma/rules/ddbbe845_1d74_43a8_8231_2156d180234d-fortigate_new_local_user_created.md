---
sigma_id: "ddbbe845-1d74-43a8-8231-2156d180234d"
title: "FortiGate - New Local User Created"
framework: "sigma"
generated: "true"
source_path: "rules/network/fortinet/fortigate/fortinet_fortigate_new_local_user_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_local_user_created.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "medium"
logsource: "fortigate / event"
aliases:
  - "ddbbe845-1d74-43a8-8231-2156d180234d"
  - "FortiGate - New Local User Created"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# FortiGate - New Local User Created

Detects the creation of a new local user on a Fortinet FortiGate Firewall.
The new local user could be used for VPN connections.

## Metadata

- Rule ID: ddbbe845-1d74-43a8-8231-2156d180234d
- Status: experimental
- Level: medium
- Author: Marco Pedrinazzi @pedrinazziM (InTheCyber)
- Date: 2025-11-01
- Source Path: rules/network/fortinet/fortigate/fortinet_fortigate_new_local_user_created.yml

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
  cfgpath: user.local
condition: selection
```

## False Positives

- A local user can be created for legitimate purposes. Investigate the user details to determine if it is authorized.

## References

- https://www.fortiguard.com/psirt/FG-IR-24-535
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/398/event
- https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/109120963/config-user-local
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/44547/44547-logid-event-config-objattr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_local_user_created.yml)
