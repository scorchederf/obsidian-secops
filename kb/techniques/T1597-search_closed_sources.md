---
id: T1597
name: Search Closed Sources
created: 2020-10-02 17:01:42.558000+00:00
modified: 2025-10-24 17:49:11.164000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[reconnaissance|Reconnaissance]]

Adversaries may search and gather information about victims from closed (e.g., paid, private, or otherwise not freely available) sources that can be used during targeting. Information about victims may be available for purchase from reputable private sources and databases, such as paid subscriptions to feeds of technical/threat intelligence data. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.(Citation: ZDNET Selling Data)

Adversaries may search in different closed databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

## Subtechniques

### T1597.001: Threat Intel Vendors
^t1597001-threat-intel-vendors

**Parent Technique**
- [[T1597-search_closed_sources|T1597: Search Closed Sources]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may search private data from threat intelligence vendors for information that can be used during targeting. Threat intelligence vendors may offer paid feeds or portals that offer more data than what is publicly reported. Although sensitive details (such as customer names and other identifiers) may be redacted, this information may contain trends regarding breaches such as target industries, attribution claims, and successful TTPs/countermeasures.(Citation: D3Secutrity CTI Feeds)

Adversaries may search in private threat intelligence vendor data to gather actionable information. If a threat actor is searching for information on their own activities, that falls under [Search Threat Vendor Data](https://attack.mitre.org/techniques/T1681). Information reported by vendors may also reveal opportunities other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190) or [External Remote Services](https://attack.mitre.org/techniques/T1133)).

#### Properties

- id: T1597.001
- name: Threat Intel Vendors
- created: 2020-10-02 17:03:45.918000+00:00
- modified: 2025-10-24 17:48:46.954000+00:00
- type: attack-pattern
- x_mitre_version: 2.0
- x_mitre_domains: enterprise-attack

### T1597.002: Purchase Technical Data
^t1597002-purchase-technical-data

**Parent Technique**
- [[T1597-search_closed_sources|T1597: Search Closed Sources]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may purchase technical information about victims that can be used during targeting. Information about victims may be available for purchase within reputable private sources and databases, such as paid subscriptions to feeds of scan databases or other data aggregation services. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.

Adversaries may purchase information about their already identified targets, or use purchased data to discover opportunities for successful breaches. Threat actors may gather various technical details from purchased data, including but not limited to employee contact information, credentials, or specifics regarding a victim’s infrastructure.(Citation: ZDNET Selling Data) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

#### Properties

- id: T1597.002
- name: Purchase Technical Data
- created: 2020-10-02 17:05:43.562000+00:00
- modified: 2025-10-24 17:48:22.109000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

