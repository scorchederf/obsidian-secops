---
id: S1071
name: Rubeus
created: 2023-03-29 20:19:26.940000+00:00
modified: 2025-04-16 20:38:56.949000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Rubeus

[Rubeus](https://attack.mitre.org/software/S1071) is a C# toolset designed for raw Kerberos interaction that has been used since at least 2020, including in ransomware operations.(Citation: GitHub Rubeus March 2023)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)

## Properties

- id: S1071
- name: Rubeus
- created: 2023-03-29 20:19:26.940000+00:00
- modified: 2025-04-16 20:38:56.949000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558002-silver-ticket|T1558.002: Silver Ticket]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558004-as-rep-roasting|T1558.004: AS-REP Roasting]]

