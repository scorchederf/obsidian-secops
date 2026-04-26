---
sigma_id: "2bfb6216-0c31-4d20-8501-2629b29a3fa2"
title: "FortiGate - New VPN SSL Web Portal Added"
framework: "sigma"
generated: "true"
source_path: "rules/network/fortinet/fortigate/fortinet_fortigate_new_vpn_ssl_web_portal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_vpn_ssl_web_portal.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "medium"
logsource: "fortigate / event"
aliases:
  - "2bfb6216-0c31-4d20-8501-2629b29a3fa2"
  - "FortiGate - New VPN SSL Web Portal Added"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# FortiGate - New VPN SSL Web Portal Added

Detects the addition of a VPN SSL Web Portal on a Fortinet FortiGate Firewall.
This behavior was observed in pair with modification of VPN SSL settings.

## Metadata

- Rule ID: 2bfb6216-0c31-4d20-8501-2629b29a3fa2
- Status: experimental
- Level: medium
- Author: Marco Pedrinazzi @pedrinazziM (InTheCyber)
- Date: 2025-11-01
- Source Path: rules/network/fortinet/fortigate/fortinet_fortigate_new_vpn_ssl_web_portal.yml

## Logsource

- product: fortigate
- service: event

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  action: Add
  cfgpath: vpn.ssl.web.portal
condition: selection
```

## False Positives

- A VPN SSL Web Portal can be added for legitimate purposes.

## References

- https://www.fortiguard.com/psirt/FG-IR-24-535
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/398/event
- https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/113121765/config-vpn-ssl-web-portal
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/44547/44547-logid-event-config-objattr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_new_vpn_ssl_web_portal.yml)
