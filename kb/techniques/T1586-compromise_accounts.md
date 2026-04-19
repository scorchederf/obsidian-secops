---
id: T1586
name: Compromise Accounts
created: 2020-10-01 01:17:15.965000+00:00
modified: 2025-10-24 17:49:02.015000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[resource_development|Resource Development]]

Adversaries may compromise accounts with services that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating accounts (i.e. [Establish Accounts](https://attack.mitre.org/techniques/T1585)), adversaries may compromise existing accounts. Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. 

A variety of methods exist for compromising accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, brute forcing credentials (ex: password reuse from breach credential dumps), or paying employees, suppliers or business partners for access to credentials.(Citation: AnonHBGary)(Citation: Microsoft DEV-0537) Prior to compromising accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Personas may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, Google, etc.). Compromised accounts may require additional development, this could include filling out or modifying profile information, further developing social networks, or incorporating photos.

Adversaries may directly leverage compromised email accounts for [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Phishing](https://attack.mitre.org/techniques/T1566).

## Properties

- id: T1586
- name: Compromise Accounts
- created: 2020-10-01 01:17:15.965000+00:00
- modified: 2025-10-24 17:49:02.015000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1586.001: Social Media Accounts

^t1586001-social-media-accounts

**Parent Technique**
- [[T1586-compromise_accounts|T1586: Compromise Accounts]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may compromise social media accounts that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating social media profiles (i.e. [Social Media Accounts](https://attack.mitre.org/techniques/T1585/001)), adversaries may compromise existing social media accounts. Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. 

A variety of methods exist for compromising social media accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, or by brute forcing credentials (ex: password reuse from breach credential dumps).(Citation: AnonHBGary) Prior to compromising social media accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Personas may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, etc.). Compromised social media accounts may require additional development, this could include filling out or modifying profile information, further developing social networks, or incorporating photos.

Adversaries can use a compromised social media profile to create new, or hijack existing, connections to targets of interest. These connections may be direct or may include trying to connect through others.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage) Compromised profiles may be leveraged during other phases of the adversary lifecycle, such as during Initial Access (ex: [Spearphishing via Service](https://attack.mitre.org/techniques/T1566/003)).

#### Properties

- id: T1586.001
- name: Social Media Accounts
- created: 2020-10-01 01:18:35.535000+00:00
- modified: 2025-10-24 17:48:32.696000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1586.002: Email Accounts

^t1586002-email-accounts

**Parent Technique**
- [[T1586-compromise_accounts|T1586: Compromise Accounts]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may compromise email accounts that can be used during targeting. Adversaries can use compromised email accounts to further their operations, such as leveraging them to conduct [Phishing for Information](https://attack.mitre.org/techniques/T1598), [Phishing](https://attack.mitre.org/techniques/T1566), or large-scale spam email campaigns. Utilizing an existing persona with a compromised email account may engender a level of trust in a potential victim if they have a relationship with, or knowledge of, the compromised persona. Compromised email accounts can also be used in the acquisition of infrastructure (ex: [Domains](https://attack.mitre.org/techniques/T1583/001)).

A variety of methods exist for compromising email accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, brute forcing credentials (ex: password reuse from breach credential dumps), or paying employees, suppliers or business partners for access to credentials.(Citation: AnonHBGary)(Citation: Microsoft DEV-0537) Prior to compromising email accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation. Adversaries may target compromising well-known email accounts or domains from which malicious spam or [Phishing](https://attack.mitre.org/techniques/T1566) emails may evade reputation-based email filtering rules.

Adversaries can use a compromised email account to hijack existing email threads with targets of interest.

#### Properties

- id: T1586.002
- name: Email Accounts
- created: 2020-10-01 01:20:53.104000+00:00
- modified: 2025-10-24 17:48:41.309000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1586.003: Cloud Accounts

^t1586003-cloud-accounts

**Parent Technique**
- [[T1586-compromise_accounts|T1586: Compromise Accounts]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may compromise cloud accounts that can be used during targeting. Adversaries can use compromised cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, Microsoft OneDrive, or AWS S3 buckets for [Exfiltration to Cloud Storage](https://attack.mitre.org/techniques/T1567/002) or to [Upload Tool](https://attack.mitre.org/techniques/T1608/002)s. Cloud accounts can also be used in the acquisition of infrastructure, such as [Virtual Private Server](https://attack.mitre.org/techniques/T1583/003)s or [Serverless](https://attack.mitre.org/techniques/T1583/007) infrastructure. Additionally, cloud-based messaging services such as Twilio, SendGrid, AWS End User Messaging, AWS SNS (Simple Notification Service), or AWS SES (Simple Email Service) may be leveraged for spam or [Phishing](https://attack.mitre.org/techniques/T1566).(Citation: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022)(Citation: Netcraft SendGrid 2024) Compromising cloud accounts may allow adversaries to develop sophisticated capabilities without managing their own servers.(Citation: Awake Security C2 Cloud)

A variety of methods exist for compromising cloud accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, conducting [Password Spraying](https://attack.mitre.org/techniques/T1110/003) attacks, or attempting to [Steal Application Access Token](https://attack.mitre.org/techniques/T1528)s.(Citation: MSTIC Nobelium Oct 2021) Prior to compromising cloud accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation. In some cases, adversaries may target privileged service provider accounts with the intent of leveraging a [Trusted Relationship](https://attack.mitre.org/techniques/T1199) between service providers and their customers.(Citation: MSTIC Nobelium Oct 2021)

#### Properties

- id: T1586.003
- name: Cloud Accounts
- created: 2022-05-27 14:30:01.904000+00:00
- modified: 2025-10-24 17:48:41.215000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

