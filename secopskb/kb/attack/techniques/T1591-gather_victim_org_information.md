---
mitre_id: "T1591"
mitre_name: "Gather Victim Org Information"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--937e4772-8441-4e4a-8bf0-8d447d667e23"
mitre_created: "2020-10-02T16:27:02.339Z"
mitre_modified: "2025-10-24T17:49:06.846Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1591/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about an organization may also be exposed to adversaries via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: ThreatPost Broadvoice Leak)(Citation: SEC EDGAR Search) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1566-phishing|T1566: Phishing]] or [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

## Workspace

- [[notes/attack/techniques/T1591-gather_victim_org_information-note|Open workspace note]]

![[notes/attack/techniques/T1591-gather_victim_org_information-note]]

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1591.001: Determine Physical Locations

^t1591001-determine-physical-locations

Adversaries may gather the victim's physical location(s) that can be used during targeting. Information about physical locations of a target organization may include a variety of details, including where key resources and infrastructure are housed. Physical locations may also indicate what legal jurisdiction and/or authorities the victim operates within.

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Physical locations of a target organization may also be exposed to adversaries via online or other accessible data sets (ex: [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]] or [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]]).(Citation: ThreatPost Broadvoice Leak)(Citation: SEC EDGAR Search) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1566-phishing|T1566: Phishing]] or [[T1200-hardware_additions|T1200: Hardware Additions]]).

### T1591.002: Business Relationships

^t1591002-business-relationships

Adversaries may gather information about the victim's business relationships that can be used during targeting. Information about an organization’s business relationships may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access. This information may also reveal supply chains and shipment paths for the victim’s hardware and software resources.

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about business relationships may also be exposed to adversaries via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: ThreatPost Broadvoice Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]], [[T1189-drive-by_compromise|T1189: Drive-by Compromise]], or [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

### T1591.003: Identify Business Tempo

^t1591003-identify-business-tempo

Adversaries may gather information about the victim's business tempo that can be used during targeting. Information about an organization’s business tempo may include a variety of details, including operational hours/days of the week. This information may also reveal times/dates of purchases and shipments of the victim’s hardware and software resources.

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about business tempo may also be exposed to adversaries via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: ThreatPost Broadvoice Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]] or [[T1199-trusted_relationship|T1199: Trusted Relationship]])

### T1591.004: Identify Roles

^t1591004-identify-roles

Adversaries may gather information about identities and roles within the victim organization that can be used during targeting. Information about business roles may reveal a variety of targetable details, including identifiable information for key personnel as well as what data/resources they have access to.

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about business roles may also be exposed to adversaries via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: ThreatPost Broadvoice Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1566-phishing|T1566: Phishing]]).

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

