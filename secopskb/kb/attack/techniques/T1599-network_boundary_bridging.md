---
mitre_id: "T1599"
mitre_name: "Network Boundary Bridging"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b8017880-4b1e-42de-ad10-ae7ac6705166"
mitre_created: "2020-10-19T16:08:29.817Z"
mitre_modified: "2025-10-24T17:49:16.493Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1599/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Network Devices"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices responsible for network segmentation. Breaching these devices may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.

Devices such as routers and firewalls can be used to create boundaries between trusted and untrusted networks.  They achieve this by restricting traffic types to enforce organizational policy in an attempt to reduce the risk inherent in such connections.  Restriction of traffic can be achieved by prohibiting IP addresses, layer 4 protocol ports, or through deep packet inspection to identify applications.  To participate with the rest of the network, these devices can be directly addressable or transparent, but their mode of operation has no bearing on how the adversary can bypass them when compromised.

When an adversary takes control of such a boundary device, they can bypass its policy enforcement to pass normally prohibited traffic across the trust boundary between the two separated networks without hinderance.  By achieving sufficient rights on the device, an adversary can reconfigure the device to allow the traffic they want, allowing them to then further achieve goals such as command and control via [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]] or exfiltration of data via [[T1020-automated_exfiltration#^t1020001-traffic-duplication|T1020.001: Traffic Duplication]]. Adversaries may also target internal devices responsible for network segmentation and abuse these in conjunction with [[T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]] to achieve the same goals.(Citation: Kaspersky ThreatNeedle Feb 2021)  In the cases where a border device separates two separate organizations, the adversary can also facilitate lateral movement into new victim environments.

## Workspace

- [[workspaces/attack/techniques/T1599-network_boundary_bridging-note|Open workspace note]]

![[workspaces/attack/techniques/T1599-network_boundary_bridging-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Subtechniques

### T1599.001: Network Address Translation Traversal

^t1599001-network-address-translation-traversal

Adversaries may bridge network boundaries by modifying a network device’s Network Address Translation (NAT) configuration. Malicious modifications to NAT may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.

Network devices such as routers and firewalls that connect multiple networks together may implement NAT during the process of passing packets between networks. When performing NAT, the network device will rewrite the source and/or destination addresses of the IP address header. Some network designs require NAT for the packets to cross the border device.  A typical example of this is environments where internal networks make use of non-Internet routable addresses.(Citation: RFC1918)

When an adversary gains control of a network boundary device, they may modify NAT configurations to send traffic between two separated networks, or to obscure their activities.  In network designs that require NAT to function, such modifications enable the adversary to overcome inherent routing limitations that would normally prevent them from accessing protected systems behind the border device.  In network designs that do not require NAT, adversaries may use address translation to further obscure their activities, as changing the addresses of packets that traverse a network boundary device can make monitoring data transmissions more challenging for defenders.  

Adversaries may use [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]] to change the operating system of a network device, implementing their own custom NAT mechanisms to further obscure their activities.

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1043-credential_access_protection|M1043: Credential Access Protection]]

## Platforms

- Network Devices

