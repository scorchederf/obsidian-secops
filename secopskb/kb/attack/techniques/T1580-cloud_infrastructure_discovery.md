---
mitre_id: "T1580"
mitre_name: "Cloud Infrastructure Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--57a3d31a-d04f-4663-b2da-7df8ec3f8c9d"
mitre_created: "2020-08-20T17:51:25.671Z"
mitre_modified: "2025-10-24T17:48:49.479Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1580/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-as-a-service (IaaS) environment. This includes compute service resources such as instances, virtual machines, and snapshots as well as resources of other services including the storage and database services.

Cloud providers offer methods such as APIs and commands issued through CLIs to serve information about infrastructure. For example, AWS provides a `DescribeInstances` API within the Amazon EC2 API that can return information about one or more instances within an account, the `ListBuckets` API that returns a list of all buckets owned by the authenticated sender of the request, the `HeadBucket` API to determine a bucket’s existence along with access permissions of the request sender, or the `GetPublicAccessBlock` API to retrieve access block configuration for a bucket.(Citation: Amazon Describe Instance)(Citation: Amazon Describe Instances API)(Citation: AWS Get Public Access Block)(Citation: AWS Head Bucket) Similarly, GCP's Cloud SDK CLI provides the `gcloud compute instances list` command to list all Google Compute Engine instances in a project (Citation: Google Compute Instances), and Azure's CLI command `az vm list` lists details of virtual machines.(Citation: Microsoft AZ CLI) In addition to API commands, adversaries can utilize open source tools to discover cloud storage infrastructure through [[T1595-active_scanning#^t1595003-wordlist-scanning|T1595.003: Wordlist Scanning]].(Citation: Malwarebytes OSINT Leaky Buckets - Hioureas)

An adversary may enumerate resources using a compromised user's access keys to determine which are available to that user.(Citation: Expel IO Evil in AWS) The discovery of these available resources may help adversaries determine their next steps in the Cloud environment, such as establishing Persistence.(Citation: Mandiant M-Trends 2020)An adversary may also use this information to change the configuration to make the bucket publicly accessible, allowing data to be accessed without authentication. Adversaries have also may use infrastructure discovery APIs such as `DescribeDBInstances` to determine size, owner, permissions, and network ACLs of database resources. (Citation: AWS Describe DB Instances) Adversaries can use this information to determine the potential value of databases and discover the requirements to access them. Unlike in [[T1526-cloud_service_discovery|T1526: Cloud Service Discovery]], this technique focuses on the discovery of components of the provided services rather than the services themselves.

## Workspace

- [[workspaces/attack/techniques/T1580-cloud_infrastructure_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1580-cloud_infrastructure_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Tools

- [[pacu|Pacu (S1091)]]

## Platforms

- IaaS

