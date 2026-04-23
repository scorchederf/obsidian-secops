---
mitre_id: "S0105"
mitre_name: "dsquery"
mitre_type: "tool"
mitre_stix_id: "tool--38952eac-cb1b-4a71-bad2-ee8223a1c8fe"
mitre_created: "2017-05-31T21:33:04.937Z"
mitre_modified: "2025-04-16T20:38:51.407Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0105/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_aliases:
  - "dsquery"
  - "dsquery.exe"
---

# dsquery

[dsquery](https://attack.mitre.org/software/S0105) is a command-line utility that can be used to query Active Directory for information from a system within a domain. (Citation: TechNet Dsquery) It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle.

## Uses Techniques

- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
- [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
- [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]

