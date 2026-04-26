---
mitre_id: "T1669"
mitre_name: "Wi-Fi Networks"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--fde016f6-211a-41c8-a4ab-301f1e419c62"
mitre_created: "2025-02-25T15:49:33.963Z"
mitre_modified: "2025-04-15T19:59:24.690Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1669/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Network Devices"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0001"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may gain initial access to target systems by connecting to wireless networks. They may accomplish this by exploiting open Wi-Fi networks used by target devices or by accessing secured Wi-Fi networks — requiring [[T1078-valid_accounts|T1078: Valid Accounts]] — belonging to a target organization.(Citation: DOJ GRU Charges 2018)(Citation: Nearest Neighbor Volexity) Establishing a connection to a Wi-Fi access point requires a certain level of proximity to both discover and maintain a stable network connection. 

Adversaries may establish a wireless connection through various methods, such as by physically positioning themselves near a Wi-Fi network to conduct close access operations. To bypass the need for physical proximity, adversaries may attempt to remotely compromise nearby third-party systems that have both wired and wireless network connections available (i.e., dual-homed systems). These third-party compromised devices can then serve as a bridge to connect to a target’s Wi-Fi network.(Citation: Nearest Neighbor Volexity)

Once an initial wireless connection is achieved, adversaries may leverage this access for follow-on activities in the victim network or further targeting of specific devices on the network. Adversaries may perform [[T1040-network_sniffing|T1040: Network Sniffing]] or [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]] activities for [[TA0006-credential_access|TA0006: Credential Access]] or [[TA0007-discovery|TA0007: Discovery]].

## Workspace

- [[workspaces/attack/techniques/T1669-wi-fi_networks-note|Open workspace note]]

![[workspaces/attack/techniques/T1669-wi-fi_networks-note]]

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]

## Platforms

- Linux
- Network Devices
- Windows
- macOS

