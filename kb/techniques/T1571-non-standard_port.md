---
mitre_id: "T1571"
mitre_name: "Non-Standard Port"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b18eae87-b469-4e14-b454-b171b416bc18"
mitre_created: "2020-03-14T18:18:32.443Z"
mitre_modified: "2025-10-24T17:49:14.187Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1571/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0011"
---

# T1571: Non-Standard Port

Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration settings can be used to modify protocol and port pairings.(Citation: change_rdp_port_conti)

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Tools

- [[quasarrat|QuasarRAT]]
- [[covenant|Covenant]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

