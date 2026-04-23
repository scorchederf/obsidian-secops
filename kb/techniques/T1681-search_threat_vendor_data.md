---
mitre_id: "T1681"
mitre_name: "Search Threat Vendor Data"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--63b24abc-5702-4745-b1e4-ac70b20a43f2"
mitre_created: "2025-09-26T15:42:30.468Z"
mitre_modified: "2025-10-24T17:48:51.996Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1681/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0043"
---

# T1681: Search Threat Vendor Data

Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives, or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their behavior when planning their future operations. 

Adversaries have been observed replacing atomic indicators mentioned in blog posts in under a week.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) Adversaries have also been seen searching for their own domain names in threat vendor data and then taking them down, likely to avoid seizure or further investigation.(Citation: Sentinel One Contagious Interview ClickFix September 2025)

This technique is distinct from [[T1597-search_closed_sources#^t1597001-threat-intel-vendors|T1597.001: Threat Intel Vendors]] in that it describes threat actors performing reconnaissance on their own activity, not in search of victim information. 

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

