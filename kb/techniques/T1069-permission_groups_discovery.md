---
id: T1069
name: Permission Groups Discovery
created: 2017-05-31 21:30:55.471000+00:00
modified: 2025-10-24 17:48:26.378000+00:00
type: attack-pattern
x_mitre_version: 2.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike BloodHound April 2018)

## Properties

- id: T1069
- name: Permission Groups Discovery
- created: 2017-05-31 21:30:55.471000+00:00
- modified: 2025-10-24 17:48:26.378000+00:00
- type: attack-pattern
- x_mitre_version: 2.6
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1069.001: Local Groups

^t1069001-local-groups

**Parent Technique**
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to find local system groups and permission settings. The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as the users found within the local administrators group.

Commands such as <code>net localgroup</code> of the [Net](https://attack.mitre.org/software/S0039) utility, <code>dscl . -list /Groups</code> on macOS, and <code>groups</code> on Linux can list local groups.

#### Properties

- id: T1069.001
- name: Local Groups
- created: 2020-03-12 19:29:21.013000+00:00
- modified: 2025-10-24 17:49:10.014000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1069.002: Domain Groups

^t1069002-domain-groups

**Parent Technique**
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

Commands such as <code>net group /domain</code> of the [Net](https://attack.mitre.org/software/S0039) utility,  <code>dscacheutil -q group</code> on macOS, and <code>ldapsearch</code> on Linux can list domain-level groups.

#### Properties

- id: T1069.002
- name: Domain Groups
- created: 2020-02-21 21:15:06.561000+00:00
- modified: 2025-10-24 17:48:33.946000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1069.003: Cloud Groups

^t1069003-cloud-groups

**Parent Technique**
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group.

With authenticated access there are several tools that can be used to find permissions groups. The <code>Get-MsolRole</code> PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts (Citation: Microsoft Msolrole)(Citation: GitHub Raindance).

Azure CLI (AZ CLI) and the Google Cloud Identity Provider API also provide interfaces to obtain permissions groups. The command <code>az ad user get-member-groups</code> will list groups associated to a user account for Azure while the API endpoint <code>GET https://cloudidentity.googleapis.com/v1/groups</code> lists group resources available to a user for Google.(Citation: Microsoft AZ CLI)(Citation: Black Hills Red Teaming MS AD Azure, 2018)(Citation: Google Cloud Identity API Documentation) In AWS, the commands `ListRolePolicies` and `ListAttachedRolePolicies` allow users to enumerate the policies attached to a role.(Citation: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022)

Adversaries may attempt to list ACLs for objects to determine the owner and other accounts with access to the object, for example, via the AWS <code>GetBucketAcl</code> API (Citation: AWS Get Bucket ACL). Using this information an adversary can target accounts with permissions to a given object or leverage accounts they have already compromised to access the object.

#### Properties

- id: T1069.003
- name: Cloud Groups
- created: 2020-02-21 21:15:33.222000+00:00
- modified: 2025-10-24 17:48:26.982000+00:00
- type: attack-pattern
- x_mitre_version: 1.5
- x_mitre_domains: enterprise-attack

## Platforms

- Containers
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows

## Tools

- [[S0445-shimratreporter|S0445: ShimRatReporter]]

