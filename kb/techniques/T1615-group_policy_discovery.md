---
mitre_id: "T1615"
mitre_name: "Group Policy Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1b20efbf-8063-4fc3-a07d-b575318a301b"
mitre_created: "2021-08-06T13:10:12.916Z"
mitre_modified: "2025-10-24T17:48:28.148Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1615/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1615: Group Policy Discovery

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence 2016)

Adversaries may use commands such as `gpresult` or various publicly available PowerShell functions, such as `Get-DomainGPO` and `Get-DomainGPOLocalGroup`, to gather information on Group Policy settings.(Citation: Microsoft gpresult)(Citation: Github PowerShell Empire) Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]) for their benefit.

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[empire|Empire]]
- [[bloodhound|BloodHound]]

## Platforms

- Windows

