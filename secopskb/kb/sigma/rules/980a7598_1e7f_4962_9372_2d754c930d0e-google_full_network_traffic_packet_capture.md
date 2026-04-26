---
sigma_id: "980a7598-1e7f-4962-9372-2d754c930d0e"
title: "Google Full Network Traffic Packet Capture"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_full_network_traffic_packet_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_full_network_traffic_packet_capture.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "980a7598-1e7f-4962-9372-2d754c930d0e"
  - "Google Full Network Traffic Packet Capture"
attack_technique_ids:
  - "T1074"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Full Network Traffic Packet Capture

Identifies potential full network packet capture in gcp. This feature can potentially be abused to read sensitive data from unencrypted internal traffic.

## Metadata

- Rule ID: 980a7598-1e7f-4962-9372-2d754c930d0e
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-13
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_full_network_traffic_packet_capture.yml

## Logsource

- product: gcp
- service: gcp.audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1074-data_staged|T1074]]

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - v*.Compute.PacketMirrorings.Get
  - v*.Compute.PacketMirrorings.Delete
  - v*.Compute.PacketMirrorings.Insert
  - v*.Compute.PacketMirrorings.Patch
  - v*.Compute.PacketMirrorings.List
  - v*.Compute.PacketMirrorings.aggregatedList
condition: selection
```

## False Positives

- Full Network Packet Capture may be done by a system or network administrator.
- If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging
- https://developers.google.com/resources/api-libraries/documentation/compute/v1/java/latest/com/google/api/services/compute/Compute.PacketMirrorings.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_full_network_traffic_packet_capture.yml)
