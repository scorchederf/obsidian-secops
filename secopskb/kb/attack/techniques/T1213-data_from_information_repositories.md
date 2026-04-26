---
mitre_id: "T1213"
mitre_name: "Data from Information Repositories"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d28ef391-8ed4-45dc-bc4a-2f43abf54416"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:26.262Z"
mitre_version: "3.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1213/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
  - "SaaS"
  - "IaaS"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0009"
d3fend_ids:
  - "D3-DI"
  - "D3-DNR"
  - "D3-NRAM"
  - "D3-RD"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing features to share sensitive documents with recipients outside of the organization (i.e., [[T1537-transfer_data_to_cloud_account|T1537: Transfer Data to Cloud Account]]). 

The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials (i.e., [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]) 
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources
* Contact or other sensitive information about business partners and customers, including personally identifiable information (PII) 

Information stored in a repository may vary based on the specific instance or environment. Specific common information repositories include the following:

* Storage services such as IaaS databases, enterprise databases, and more specialized platforms such as customer relationship management (CRM) databases 
* Collaboration platforms such as SharePoint, Confluence, and code repositories
* Messaging platforms such as Slack and Microsoft Teams 

In some cases, information repositories have been improperly secured, typically by unintentionally allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch.(Citation: Mitiga)(Citation: TrendMicro Exposed Redis 2020)(Citation: Cybernews Reuters Leak 2022)

## Workspace

- [[workspaces/attack/techniques/T1213-data_from_information_repositories-note|Open workspace note]]

![[workspaces/attack/techniques/T1213-data_from_information_repositories-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/195e1b9d_bfc2_4ffa_ab4e_35aef69815f8-bitbucket_full_data_export_triggered|Bitbucket Full Data Export Triggered (high; bitbucket / audit)]]
- [[kb/sigma/rules/34d81081_03c9_4a7f_91c9_5e46af625cde-bitbucket_unauthorized_full_data_export_triggered|Bitbucket Unauthorized Full Data Export Triggered (critical; bitbucket / audit)]]
- [[kb/sigma/rules/3ec9a16d_0b4f_4967_9542_ebf38ceac7dd-opencanary_mssql_login_attempt_via_sqlauth|OpenCanary - MSSQL Login Attempt Via SQLAuth (high; opencanary / application)]]
- [[kb/sigma/rules/4fe17521_aef3_4e6a_9d6b_4a7c8de155a8-opencanary_git_clone_request|OpenCanary - GIT Clone Request (high; opencanary / application)]]
- [[kb/sigma/rules/547dfc53_ebf6_4afe_8d2e_793d9574975d-opencanary_redis_action_command_attempt|OpenCanary - REDIS Action Command Attempt (high; opencanary / application)]]
- [[kb/sigma/rules/6e78f90f_0043_4a01_ac41_f97681613a66-opencanary_mssql_login_attempt_via_windows_authentication|OpenCanary - MSSQL Login Attempt Via Windows Authentication (high; opencanary / application)]]
- [[kb/sigma/rules/e7d79a1b_25ed_4956_bd56_bd344fa8fd06-opencanary_mysql_login_attempt|OpenCanary - MySQL Login Attempt (high; opencanary / application)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]

## Subtechniques

### T1213.001: Confluence

^t1213001-confluence


Adversaries may leverage Confluence repositories to mine valuable information. Often found in development environments alongside Atlassian JIRA, Confluence is generally used to store development-related documentation, however, in general may contain more diverse categories of useful information, such as:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials (i.e., [[T1552-unsecured_credentials|T1552: Unsecured Credentials]])
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources


### T1213.002: Sharepoint

^t1213002-sharepoint

Adversaries may leverage the SharePoint repository as a source to mine valuable information. SharePoint will often contain useful information for an adversary to learn about the structure and functionality of the internal network and systems. For example, the following is a list of example information that may hold potential value to an adversary and may also be found on SharePoint:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials (i.e., [[T1552-unsecured_credentials|T1552: Unsecured Credentials]])
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources


### T1213.003: Code Repositories

^t1213003-code-repositories

Adversaries may leverage code repositories to collect valuable information. Code repositories are tools/services that store source code and automate software builds. They may be hosted internally or privately on third party sites such as Github, GitLab, SourceForge, and BitBucket. Users typically interact with code repositories through a web application or command-line utilities such as git.

Once adversaries gain access to a victim network or a private code repository, they may collect sensitive information such as proprietary source code or [[T1552-unsecured_credentials|T1552: Unsecured Credentials]] contained within software's source code.  Having access to software's source code may allow adversaries to develop [[T1587-develop_capabilities#^t1587004-exploits|T1587.004: Exploits]], while credentials may provide access to additional resources using [[T1078-valid_accounts|T1078: Valid Accounts]].(Citation: Wired Uber Breach)(Citation: Krebs Adobe)

**Note:** This is distinct from [[T1593-search_open_websites_domains#^t1593003-code-repositories|T1593.003: Code Repositories]], which focuses on conducting [[TA0043-reconnaissance|TA0043: Reconnaissance]] via public code repositories.

### T1213.004: Customer Relationship Management Software

^t1213004-customer-relationship-management-software

Adversaries may leverage Customer Relationship Management (CRM) software to mine valuable information. CRM software is used to assist organizations in tracking and managing customer interactions, as well as storing customer data.

Once adversaries gain access to a victim organization, they may mine CRM software for customer data. This may include personally identifiable information (PII) such as full names, emails, phone numbers, and addresses, as well as additional details such as purchase histories and IT support interactions. By collecting this data, an adversary may be able to send personalized [[T1566-phishing|T1566: Phishing]] emails, engage in SIM swapping, or otherwise target the organization’s customers in ways that enable financial gain or the compromise of additional organizations.(Citation: Bleeping Computer US Cellular Hack 2022)(Citation: Bleeping Computer Mint Mobile Hack 2021)(Citation: Bleeping Computer Bank Hack 2020)

CRM software may be hosted on-premises or in the cloud. Information stored in these solutions may vary based on the specific instance or environment. Examples of CRM software include Microsoft Dynamics 365, Salesforce, Zoho, Zendesk, and HubSpot.

### T1213.005: Messaging Applications

^t1213005-messaging-applications

Adversaries may leverage chat and messaging applications, such as Microsoft Teams, Google Chat, and Slack, to mine valuable information.  

The following is a brief list of example information that may hold potential value to an adversary and may also be found on messaging applications: 

* Testing / development credentials (i.e., [[T1552-unsecured_credentials#^t1552008-chat-messages|T1552.008: Chat Messages]]) 
* Source code snippets 
* Links to network shares and other internal resources 
* Proprietary data(Citation: Guardian Grand Theft Auto Leak 2022)
* Discussions about ongoing incident response efforts(Citation: SC Magazine Ragnar Locker 2021)(Citation: Microsoft DEV-0537)

In addition to exfiltrating data from messaging applications, adversaries may leverage data from chat messages in order to improve their targeting - for example, by learning more about an environment or evading ongoing incident response efforts.(Citation: Sentinel Labs NullBulge 2024)(Citation: Permiso Scattered Spider 2023)

### T1213.006: Databases

^t1213006-databases

Adversaries may leverage databases to mine valuable information. These databases may be hosted on-premises or in the cloud (both in platform-as-a-service and software-as-a-service environments). 

Examples of databases from which information may be collected include MySQL, PostgreSQL, MongoDB, Amazon Relational Database Service, Azure SQL Database, Google Firebase, and Snowflake. Databases may include a variety of information of interest to adversaries, such as usernames, hashed passwords, personally identifiable information, and financial data. Data collected from databases may be used for [[TA0008-lateral_movement|TA0008: Lateral Movement]], [[TA0011-command_and_control|TA0011: Command and Control]], or [[TA0010-exfiltration|TA0010: Exfiltration]]. Data exfiltrated from databases may also be used to extort victims or may be sold for profit.(Citation: Google Cloud Threat Intelligence UNC5537 Snowflake 2024)

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1047-audit|M1047: Audit]]
- [[M1054-software_configuration|M1054: Software Configuration]]
- [[M1060-out-of-band_communications_channel|M1060: Out-of-Band Communications Channel]]

## Platforms

- Linux
- Windows
- macOS
- SaaS
- IaaS
- Office Suite

