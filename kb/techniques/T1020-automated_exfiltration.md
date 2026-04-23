---
mitre_id: "T1020"
mitre_name: "Automated Exfiltration"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--774a3188-6ba9-4dc4-879d-d54ee48a5ce9"
mitre_created: "2017-05-31T21:30:29.458Z"
mitre_modified: "2025-10-24T17:48:58.340Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1020/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0010"
---

# T1020: Automated Exfiltration

Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after being gathered during Collection.(Citation: ESET Gamaredon June 2020) 

When automated exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]] and [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]].

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Subtechniques

### T1020.001: Traffic Duplication

^t1020001-traffic-duplication

Adversaries may leverage traffic mirroring in order to automate data exfiltration over compromised infrastructure. Traffic mirroring is a native feature for some devices, often used for network analysis. For example, devices may be configured to forward network traffic to one or more destinations for analysis by a network analyzer or other monitoring device. (Citation: Cisco Traffic Mirroring)(Citation: Juniper Traffic Mirroring)

Adversaries may abuse traffic mirroring to mirror or redirect network traffic through other infrastructure they control. Malicious modifications to network devices to enable traffic redirection may be possible through [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]] or [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]].(Citation: US-CERT-TA18-106A)(Citation: Cisco Blog Legacy Device Attacks)

Many cloud-based environments also support traffic mirroring. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to.(Citation: AWS Traffic Mirroring)(Citation: GCP Packet Mirroring)(Citation: Azure Virtual Network TAP)

Adversaries may use traffic duplication in conjunction with [[T1040-network_sniffing|T1040: Network Sniffing]], [[T1056-input_capture|T1056: Input Capture]], or [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]] depending on the goals and objectives of the adversary.

## Tools

- [[empire|Empire]]
- [[shimratreporter|ShimRatReporter]]

## Platforms

- Linux
- macOS
- Network Devices
- Windows

