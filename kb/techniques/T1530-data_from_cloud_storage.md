---
id: T1530
name: Data from Cloud Storage
created: 2019-08-30 18:07:27.741000+00:00
modified: 2025-10-24 17:48:37.187000+00:00
type: attack-pattern
x_mitre_version: 2.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may access data from cloud storage.

Many IaaS providers offer solutions for online data object storage such as Amazon S3, Azure Storage, and Google Cloud Storage. Similarly, SaaS enterprise platforms such as Office 365 and Google Workspace provide cloud-based document storage to users through services such as OneDrive and Google Drive, while SaaS application providers such as Slack, Confluence, Salesforce, and Dropbox may provide cloud storage solutions as a peripheral or primary use case of their platform. 

In some cases, as with IaaS-based cloud storage, there exists no overarching application (such as SQL or Elasticsearch) with which to interact with the stored objects: instead, data from these solutions is retrieved directly though the [Cloud API](https://attack.mitre.org/techniques/T1059/009). In SaaS applications, adversaries may be able to collect this data directly from APIs or backend cloud storage objects, rather than through their front-end application or interface (i.e., [Data from Information Repositories](https://attack.mitre.org/techniques/T1213)). 

Adversaries may collect sensitive data from these cloud storage solutions. Providers typically offer security guides to help end users configure systems, though misconfigurations are a common problem.(Citation: Amazon S3 Security, 2019)(Citation: Microsoft Azure Storage Security, 2019)(Citation: Google Cloud Storage Best Practices, 2019) There have been numerous incidents where cloud storage has been improperly secured, typically by unintentionally allowing public access to unauthenticated users, overly-broad access by all users, or even access for any anonymous person outside the control of the Identity Access Management system without even needing basic user permissions.

This open access may expose various types of sensitive data, such as credit cards, personally identifiable information, or medical records.(Citation: Trend Micro S3 Exposed PII, 2017)(Citation: Wired Magecart S3 Buckets, 2019)(Citation: HIPAA Journal S3 Breach, 2017)(Citation: Rclone-mega-extortion_05_2021)

Adversaries may also obtain then abuse leaked credentials from source repositories, logs, or other means as a way to gain access to cloud storage objects.

## Properties

- id: T1530
- name: Data from Cloud Storage
- created: 2019-08-30 18:07:27.741000+00:00
- modified: 2025-10-24 17:48:37.187000+00:00
- type: attack-pattern
- x_mitre_version: 2.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- IaaS
- Office Suite
- SaaS

## Tools

- [[S0677-aadinternals|S0677: AADInternals]]
- [[S0683-peirates|S0683: Peirates]]
- [[S1091-pacu|S1091: Pacu]]

