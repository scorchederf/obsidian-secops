---
sigma_id: "8b5dacf2-aeb7-459d-b133-678eb696d410"
title: "FortiGate - VPN SSL Settings Modified"
framework: "sigma"
generated: "true"
source_path: "rules/network/fortinet/fortigate/fortinet_fortigate_vpn_ssl_settings_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_vpn_ssl_settings_modified.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "medium"
logsource: "fortigate / event"
aliases:
  - "8b5dacf2-aeb7-459d-b133-678eb696d410"
  - "FortiGate - VPN SSL Settings Modified"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# FortiGate - VPN SSL Settings Modified

Detects the modification of VPN SSL Settings (for example, the modification of authentication rules).
This behavior was observed in pair with the addition of a VPN SSL Web Portal.

## Metadata

- Rule ID: 8b5dacf2-aeb7-459d-b133-678eb696d410
- Status: experimental
- Level: medium
- Author: Marco Pedrinazzi @pedrinazziM (InTheCyber)
- Date: 2025-11-01
- Source Path: rules/network/fortinet/fortigate/fortinet_fortigate_vpn_ssl_settings_modified.yml

## Logsource

- product: fortigate
- service: event

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  action: Edit
  cfgpath: vpn.ssl.settings
condition: selection
```

## False Positives

- VPN SSL settings can be changed for legitimate purposes.

## References

- https://www.fortiguard.com/psirt/FG-IR-24-535
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/398/event
- https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/114404382/config-vpn-ssl-settings
- https://docs.fortinet.com/document/fortigate/7.6.4/fortios-log-message-reference/44546/44546-logid-event-config-attr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/fortinet/fortigate/fortinet_fortigate_vpn_ssl_settings_modified.yml)
