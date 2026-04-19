---
id: S1131
name: NPPSPY
created: 2024-05-17 18:49:15.318000+00:00
modified: 2024-10-28 19:00:14.732000+00:00
type: tool
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# NPPSPY

NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them to a file on the victim system for follow-on exfiltration.(Citation: Huntress NPPSPY 2022)(Citation: Polak NPPSPY 2004)

## Properties

- id: S1131
- name: NPPSPY
- created: 2024-05-17 18:49:15.318000+00:00
- modified: 2024-10-28 19:00:14.732000+00:00
- type: tool
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1656-impersonation|T1656: Impersonation]]

