---
mitre_id: "T1069"
mitre_name: "Permission Groups Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--15dbf668-795c-41e6-8219-f0447c0e64ce"
mitre_created: "2017-05-31T21:30:55.471Z"
mitre_modified: "2025-10-24T17:48:26.378Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1069/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "IaaS"
  - "Identity Provider"
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

# T1069: Permission Groups Discovery

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike BloodHound April 2018)

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Subtechniques

### T1069.001: Local Groups

^t1069001-local-groups

Adversaries may attempt to find local system groups and permission settings. The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as the users found within the local administrators group.

Commands such as `net localgroup` of the [[net|Net]] utility, `dscl . -list /Groups` on macOS, and `groups` on Linux can list local groups.

### T1069.002: Domain Groups

^t1069002-domain-groups

Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

Commands such as `net group /domain` of the [[net|Net]] utility,  `dscacheutil -q group` on macOS, and `ldapsearch` on Linux can list domain-level groups.

### T1069.003: Cloud Groups

^t1069003-cloud-groups

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group.

With authenticated access there are several tools that can be used to find permissions groups. The `Get-MsolRole` PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts (Citation: Microsoft Msolrole)(Citation: GitHub Raindance).

Azure CLI (AZ CLI) and the Google Cloud Identity Provider API also provide interfaces to obtain permissions groups. The command `az ad user get-member-groups` will list groups associated to a user account for Azure while the API endpoint `GET https://cloudidentity.googleapis.com/v1/groups` lists group resources available to a user for Google.(Citation: Microsoft AZ CLI)(Citation: Black Hills Red Teaming MS AD Azure, 2018)(Citation: Google Cloud Identity API Documentation) In AWS, the commands `ListRolePolicies` and `ListAttachedRolePolicies` allow users to enumerate the policies attached to a role.(Citation: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022)

Adversaries may attempt to list ACLs for objects to determine the owner and other accounts with access to the object, for example, via the AWS `GetBucketAcl` API (Citation: AWS Get Bucket ACL). Using this information an adversary can target accounts with permissions to a given object or leverage accounts they have already compromised to access the object.

## Tools

- [[shimratreporter|ShimRatReporter]]

## Platforms

- Containers
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows

## Workspace

- [[kb/notes/attack/techniques/t1069-notes|Open workspace note]]

