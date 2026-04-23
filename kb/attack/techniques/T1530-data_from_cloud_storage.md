---
mitre_id: "T1530"
mitre_name: "Data from Cloud Storage"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3298ce88-1628-43b1-87d9-0b5336b193d7"
mitre_created: "2019-08-30T18:07:27.741Z"
mitre_modified: "2025-10-24T17:48:37.187Z"
mitre_version: "2.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1530/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "Office Suite"
  - "SaaS"
mitre_tactic_ids:
  - "TA0009"
tags:
  - "attack"
  - "technique"
  - "offense"
---

# T1530: Data from Cloud Storage

Adversaries may access data from cloud storage.

Many IaaS providers offer solutions for online data object storage such as Amazon S3, Azure Storage, and Google Cloud Storage. Similarly, SaaS enterprise platforms such as Office 365 and Google Workspace provide cloud-based document storage to users through services such as OneDrive and Google Drive, while SaaS application providers such as Slack, Confluence, Salesforce, and Dropbox may provide cloud storage solutions as a peripheral or primary use case of their platform. 

In some cases, as with IaaS-based cloud storage, there exists no overarching application (such as SQL or Elasticsearch) with which to interact with the stored objects: instead, data from these solutions is retrieved directly though the [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]]. In SaaS applications, adversaries may be able to collect this data directly from APIs or backend cloud storage objects, rather than through their front-end application or interface (i.e., [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]). 

Adversaries may collect sensitive data from these cloud storage solutions. Providers typically offer security guides to help end users configure systems, though misconfigurations are a common problem.(Citation: Amazon S3 Security, 2019)(Citation: Microsoft Azure Storage Security, 2019)(Citation: Google Cloud Storage Best Practices, 2019) There have been numerous incidents where cloud storage has been improperly secured, typically by unintentionally allowing public access to unauthenticated users, overly-broad access by all users, or even access for any anonymous person outside the control of the Identity Access Management system without even needing basic user permissions.

This open access may expose various types of sensitive data, such as credit cards, personally identifiable information, or medical records.(Citation: Trend Micro S3 Exposed PII, 2017)(Citation: Wired Magecart S3 Buckets, 2019)(Citation: HIPAA Journal S3 Breach, 2017)(Citation: Rclone-mega-extortion_05_2021)

Adversaries may also obtain then abuse leaked credentials from source repositories, logs, or other means as a way to gain access to cloud storage objects.

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[aadinternals|AADInternals]]
- [[peirates|Peirates]]
- [[pacu|Pacu]]

## Platforms

- IaaS
- Office Suite
- SaaS

## Workspace

- [[kb/notes/attack/techniques/t1530-notes|Open workspace note]]

