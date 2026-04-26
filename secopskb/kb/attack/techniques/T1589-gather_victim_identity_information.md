---
mitre_id: "T1589"
mitre_name: "Gather Victim Identity Information"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--5282dd9a-d26d-4e16-88b7-7c0f4553daf4"
mitre_created: "2020-10-02T14:54:59.263Z"
mitre_modified: "2025-10-24T17:48:47.303Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1589/"
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

Adversaries may gather information about the victim's identity that can be used during targeting. Information about identities may include a variety of details, including personal data (ex: employee names, email addresses, security question responses, etc.) as well as sensitive details such as credentials or multi-factor authentication (MFA) configurations.

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about users could also be enumerated via other active means (i.e. [[T1595-active_scanning|T1595: Active Scanning]]) such as probing and analyzing responses from authentication services that may reveal valid usernames in a system or permitted MFA /methods associated with those usernames.(Citation: GrimBlog UsernameEnum)(Citation: Obsidian SSPR Abuse 2023) Information about victims may also be exposed to adversaries via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: OPM Leak)(Citation: Register Deloitte)(Citation: Register Uber)(Citation: Detectify Slack Tokens)(Citation: Forbes GitHub Creds)(Citation: GitHub truffleHog)(Citation: GitHub Gitrob)(Citation: CNET Leaks)

Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1566-phishing|T1566: Phishing]] or [[T1078-valid_accounts|T1078: Valid Accounts]]).

## Workspace

- [[workspaces/attack/techniques/T1589-gather_victim_identity_information-note|Open workspace note]]

![[workspaces/attack/techniques/T1589-gather_victim_identity_information-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/19128e5e_4743_48dc_bd97_52e5775af817-azure_ad_account_credential_leaked|Azure AD Account Credential Leaked (high; azure / riskdetection)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1589.001: Credentials

^t1589001-credentials

Adversaries may gather credentials that can be used during targeting. Account credentials gathered by adversaries may be those directly associated with the target victim organization or attempt to take advantage of the tendency for users to use the same passwords across personal and business accounts.

Adversaries may gather credentials from potential victims in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Adversaries may also compromise sites then add malicious content designed to collect website authentication cookies from visitors.(Citation: ATT ScanBox) (Citation: Register Deloitte)(Citation: Register Uber)(Citation: Detectify Slack Tokens)(Citation: Forbes GitHub Creds)(Citation: GitHub truffleHog)(Citation: GitHub Gitrob)(Citation: CNET Leaks) Where multi-factor authentication (MFA) based on out-of-band communications is in use, adversaries may compromise a service provider to gain access to MFA codes and one-time passwords (OTP).(Citation: Okta Scatter Swine 2022)

Credential information may also be exposed to adversaries via leaks to online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593002-search-engines|T1593.002: Search Engines]], breach dumps, code repositories, etc.). Adversaries may purchase credentials from dark web markets, such as Russian Market and 2easy, or through access to Telegram channels that distribute logs from infostealer malware.(Citation: Bleeping Computer 2easy 2021)(Citation: SecureWorks Infostealers 2023)(Citation: Bleeping Computer Stealer Logs 2023)

Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1078-valid_accounts|T1078: Valid Accounts]]). 

### T1589.002: Email Addresses

^t1589002-email-addresses

Adversaries may gather email addresses that can be used during targeting. Even if internal instances exist, organizations may have public-facing email infrastructure and addresses for employees.

Adversaries may easily gather email addresses, since they may be readily available and exposed via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: HackersArise Email)(Citation: CNET Leaks) Email addresses could also be enumerated via more active means (i.e. [[T1595-active_scanning|T1595: Active Scanning]]), such as probing and analyzing responses from authentication services that may reveal valid usernames in a system.(Citation: GrimBlog UsernameEnum) For example, adversaries may be able to enumerate email addresses in Office 365 environments by querying a variety of publicly available API endpoints, such as autodiscover and GetCredentialType.(Citation: GitHub Office 365 User Enumeration)(Citation: Azure Active Directory Reconnaisance)

Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1586-compromise_accounts#^t1586002-email-accounts|T1586.002: Email Accounts]]), and/or initial access (ex: [[T1566-phishing|T1566: Phishing]] or [[T1110-brute_force|T1110: Brute Force]] via [[T1133-external_remote_services|T1133: External Remote Services]]).

### T1589.003: Employee Names

^t1589003-employee-names

Adversaries may gather employee names that can be used during targeting. Employee names be used to derive email addresses as well as to help guide other reconnaissance efforts and/or craft more-believable lures.

Adversaries may easily gather employee names, since they may be readily available and exposed via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: OPM Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1586-compromise_accounts|T1586: Compromise Accounts]]), and/or initial access (ex: [[T1566-phishing|T1566: Phishing]] or [[T1078-valid_accounts|T1078: Valid Accounts]]).

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

