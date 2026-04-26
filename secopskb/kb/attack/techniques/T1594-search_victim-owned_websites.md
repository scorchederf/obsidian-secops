---
mitre_id: "T1594"
mitre_name: "Search Victim-Owned Websites"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--16cdd21f-da65-4e4f-bc04-dd7d198c7b26"
mitre_created: "2020-10-02T16:51:50.306Z"
mitre_modified: "2025-10-24T17:48:26.799Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1594/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0043"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain a variety of details, including names of departments/divisions, physical locations, and data about key employees such as names, roles, and contact info (ex: [[T1589-gather_victim_identity_information#^t1589002-email-addresses|T1589.002: Email Addresses]]). These sites may also have details highlighting business operations and relationships.(Citation: Comparitech Leak)

Adversaries may search victim-owned websites to gather actionable information. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1199-trusted_relationship|T1199: Trusted Relationship]] or [[T1566-phishing|T1566: Phishing]]).

In addition to manually browsing the website, adversaries may attempt to identify hidden directories or files that could contain additional sensitive information or vulnerable functionality. They may do this through automated activities such as [[T1595-active_scanning#^t1595003-wordlist-scanning|T1595.003: Wordlist Scanning]], as well as by leveraging files such as sitemap.xml and robots.txt.(Citation: Perez Sitemap XML 2023)(Citation: Register Robots TXT 2015) 

## Workspace

- [[workspaces/attack/techniques/T1594-search_victim-owned_websites-note|Open workspace note]]

![[workspaces/attack/techniques/T1594-search_victim-owned_websites-note]]

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

