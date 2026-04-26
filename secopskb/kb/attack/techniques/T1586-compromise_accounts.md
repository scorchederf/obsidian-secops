---
mitre_id: "T1586"
mitre_name: "Compromise Accounts"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--81033c3b-16a4-46e4-8fed-9b030dd03c4a"
mitre_created: "2020-10-01T01:17:15.965Z"
mitre_modified: "2025-10-24T17:49:02.015Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1586/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0042"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may compromise accounts with services that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating accounts (i.e. [[T1585-establish_accounts|T1585: Establish Accounts]]), adversaries may compromise existing accounts. Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. 

A variety of methods exist for compromising accounts, such as gathering credentials via [[T1598-phishing_for_information|T1598: Phishing for Information]], purchasing credentials from third-party sites, brute forcing credentials (ex: password reuse from breach credential dumps), or paying employees, suppliers or business partners for access to credentials.(Citation: AnonHBGary)(Citation: Microsoft DEV-0537) Prior to compromising accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Personas may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, Google, etc.). Compromised accounts may require additional development, this could include filling out or modifying profile information, further developing social networks, or incorporating photos.

Adversaries may directly leverage compromised email accounts for [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1566-phishing|T1566: Phishing]].

## Workspace

- [[workspaces/attack/techniques/T1586-compromise_accounts-note|Open workspace note]]

![[workspaces/attack/techniques/T1586-compromise_accounts-note]]

## Tactics

- [[TA0042-resource_development|TA0042: Resource Development]]

## Subtechniques

### T1586.001: Social Media Accounts

^t1586001-social-media-accounts

Adversaries may compromise social media accounts that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating social media profiles (i.e. [[T1585-establish_accounts#^t1585001-social-media-accounts|T1585.001: Social Media Accounts]]), adversaries may compromise existing social media accounts. Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. 

A variety of methods exist for compromising social media accounts, such as gathering credentials via [[T1598-phishing_for_information|T1598: Phishing for Information]], purchasing credentials from third-party sites, or by brute forcing credentials (ex: password reuse from breach credential dumps).(Citation: AnonHBGary) Prior to compromising social media accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Personas may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, etc.). Compromised social media accounts may require additional development, this could include filling out or modifying profile information, further developing social networks, or incorporating photos.

Adversaries can use a compromised social media profile to create new, or hijack existing, connections to targets of interest. These connections may be direct or may include trying to connect through others.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage) Compromised profiles may be leveraged during other phases of the adversary lifecycle, such as during Initial Access (ex: [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]).

### T1586.002: Email Accounts

^t1586002-email-accounts

Adversaries may compromise email accounts that can be used during targeting. Adversaries can use compromised email accounts to further their operations, such as leveraging them to conduct [[T1598-phishing_for_information|T1598: Phishing for Information]], [[T1566-phishing|T1566: Phishing]], or large-scale spam email campaigns. Utilizing an existing persona with a compromised email account may engender a level of trust in a potential victim if they have a relationship with, or knowledge of, the compromised persona. Compromised email accounts can also be used in the acquisition of infrastructure (ex: [[T1583-acquire_infrastructure#^t1583001-domains|T1583.001: Domains]]).

A variety of methods exist for compromising email accounts, such as gathering credentials via [[T1598-phishing_for_information|T1598: Phishing for Information]], purchasing credentials from third-party sites, brute forcing credentials (ex: password reuse from breach credential dumps), or paying employees, suppliers or business partners for access to credentials.(Citation: AnonHBGary)(Citation: Microsoft DEV-0537) Prior to compromising email accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation. Adversaries may target compromising well-known email accounts or domains from which malicious spam or [[T1566-phishing|T1566: Phishing]] emails may evade reputation-based email filtering rules.

Adversaries can use a compromised email account to hijack existing email threads with targets of interest.

### T1586.003: Cloud Accounts

^t1586003-cloud-accounts

Adversaries may compromise cloud accounts that can be used during targeting. Adversaries can use compromised cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, Microsoft OneDrive, or AWS S3 buckets for [[T1567-exfiltration_over_web_service#^t1567002-exfiltration-to-cloud-storage|T1567.002: Exfiltration to Cloud Storage]] or to [[T1608-stage_capabilities#^t1608002-upload-tool|T1608.002: Upload Tool]]s. Cloud accounts can also be used in the acquisition of infrastructure, such as [[T1583-acquire_infrastructure#^t1583003-virtual-private-server|T1583.003: Virtual Private Server]]s or [[T1583-acquire_infrastructure#^t1583007-serverless|T1583.007: Serverless]] infrastructure. Additionally, cloud-based messaging services such as Twilio, SendGrid, AWS End User Messaging, AWS SNS (Simple Notification Service), or AWS SES (Simple Email Service) may be leveraged for spam or [[T1566-phishing|T1566: Phishing]].(Citation: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022)(Citation: Netcraft SendGrid 2024) Compromising cloud accounts may allow adversaries to develop sophisticated capabilities without managing their own servers.(Citation: Awake Security C2 Cloud)

A variety of methods exist for compromising cloud accounts, such as gathering credentials via [[T1598-phishing_for_information|T1598: Phishing for Information]], purchasing credentials from third-party sites, conducting [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]] attacks, or attempting to [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]s.(Citation: MSTIC Nobelium Oct 2021) Prior to compromising cloud accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation. In some cases, adversaries may target privileged service provider accounts with the intent of leveraging a [[T1199-trusted_relationship|T1199: Trusted Relationship]] between service providers and their customers.(Citation: MSTIC Nobelium Oct 2021)

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

