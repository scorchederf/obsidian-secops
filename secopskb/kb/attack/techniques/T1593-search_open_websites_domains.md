---
mitre_id: "T1593"
mitre_name: "Search Open Websites/Domains"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--a0e6614a-7740-4b24-bd65-f1bde09fc365"
mitre_created: "2020-10-02T16:48:04.509Z"
mitre_modified: "2025-10-24T17:49:10.188Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1593/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may search freely available websites and/or domains for information about victims that can be used during targeting. Information about victims may be available in various online sites, such as social media, new sites, or those hosting information about business operations such as hiring or requested/rewarded contracts.(Citation: Cyware Social Media)(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)

Adversaries may search in different online sites depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1566-phishing|T1566: Phishing]]).

## Workspace

- [[workspaces/attack/techniques/T1593-search_open_websites_domains-note|Open workspace note]]

![[workspaces/attack/techniques/T1593-search_open_websites_domains-note]]

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1593.001: Social Media

^t1593001-social-media

Adversaries may search social media for information about victims that can be used during targeting. Social media sites may contain various information about a victim organization, such as business announcements as well as information about the roles, locations, and interests of staff.

Adversaries may search in different social media sites depending on what information they seek to gather. Threat actors may passively harvest data from these sites, as well as use information gathered to create fake profiles/groups to elicit victim’s into revealing specific information (i.e. [[T1598-phishing_for_information#^t1598001-spearphishing-service|T1598.001: Spearphishing Service]]).(Citation: Cyware Social Media) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]).

### T1593.002: Search Engines

^t1593002-search-engines

Adversaries may use search engines to collect information about victims that can be used during targeting. Search engine services typical crawl online sites to index context and may provide users with specialized syntax to search for specific keywords or specific types of content (i.e. filetypes).(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)

Adversaries may craft various search engine queries depending on what information they seek to gather. Threat actors may use search engines to harvest general information about victims, as well as use specialized queries to look for spillages/leaks of sensitive information such as network details or credentials. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1078-valid_accounts|T1078: Valid Accounts]] or [[T1566-phishing|T1566: Phishing]]).

### T1593.003: Code Repositories

^t1593003-code-repositories

Adversaries may search public code repositories for information about victims that can be used during targeting. Victims may store code in repositories on various third-party websites such as GitHub, GitLab, SourceForge, and BitBucket. Users typically interact with code repositories through a web application or command-line utilities such as git.  

Adversaries may search various public code repositories for various information about a victim. Public code repositories can often be a source of various general information about victims, such as commonly used programming languages and libraries as well as the names of employees. Adversaries may also identify more sensitive data, including accidentally leaked credentials or API keys.(Citation: GitHub Cloud Service Credentials) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1586-compromise_accounts|T1586: Compromise Accounts]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1078-valid_accounts|T1078: Valid Accounts]] or [[T1566-phishing|T1566: Phishing]]). 

**Note:** This is distinct from [[T1213-data_from_information_repositories#^t1213003-code-repositories|T1213.003: Code Repositories]], which focuses on [[TA0009-collection|TA0009: Collection]] from private and internally hosted code repositories. 

## Mitigations

- [[M1013-application_developer_guidance|M1013: Application Developer Guidance]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- PRE

