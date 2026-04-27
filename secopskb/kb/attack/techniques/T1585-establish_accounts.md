---
mitre_id: "T1585"
mitre_name: "Establish Accounts"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--cdfc5f0a-9bb9-4352-b896-553cfa2d8fd8"
mitre_created: "2020-10-01T01:05:42.216Z"
mitre_modified: "2025-10-24T17:49:24.456Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1585/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may create and cultivate accounts with services that can be used during targeting. Adversaries can create accounts that can be used to build a persona to further operations. Persona development consists of the development of public information, presence, history and appropriate affiliations. This development could be applied to social media, website, or other publicly available information that could be referenced and scrutinized for legitimacy over the course of an operation using that persona or identity.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage)

For operations incorporating social engineering, the utilization of an online persona may be important. These personas may be fictitious or impersonate real people. The persona may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, Google, GitHub, Docker Hub, etc.). Establishing a persona may require development of additional documentation to make them seem real. This could include filling out profile information, developing social networks, or incorporating photos.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage)

Establishing accounts can also include the creation of accounts with email providers, which may be directly leveraged for [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1566-phishing|T1566: Phishing]].(Citation: Mandiant APT1) In addition, establishing accounts may allow adversaries to abuse free services, such as registering for trial periods to [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] for malicious purposes.(Citation: Free Trial PurpleUrchin)


## Workspace

- [[workspaces/attack/techniques/T1585-establish_accounts-note|Open workspace note]]

![[workspaces/attack/techniques/T1585-establish_accounts-note]]

## Tactics

- [[TA0042-resource_development|TA0042: Resource Development]]

## Subtechniques

### T1585.001: Social Media Accounts

^t1585001-social-media-accounts

Adversaries may create and cultivate social media accounts that can be used during targeting. Adversaries can create social media accounts that can be used to build a persona to further operations. Persona development consists of the development of public information, presence, history and appropriate affiliations.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage)

For operations incorporating social engineering, the utilization of a persona on social media may be important. These personas may be fictitious or impersonate real people. The persona may exist on a single social media site or across multiple sites (ex: Facebook, LinkedIn, Twitter, etc.). Establishing a persona  on social media may require development of additional documentation to make them seem real. This could include filling out profile information, developing social networks, or incorporating photos. 

Once a persona has been developed an adversary can use it to create connections to targets of interest. These connections may be direct or may include trying to connect through others.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage) These accounts may be leveraged during other phases of the adversary lifecycle, such as during Initial Access (ex: [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]).

### T1585.002: Email Accounts

^t1585002-email-accounts

Adversaries may create email accounts that can be used during targeting. Adversaries can use accounts created with email providers to further their operations, such as leveraging them to conduct [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1566-phishing|T1566: Phishing]].(Citation: Mandiant APT1) Establishing email accounts may also allow adversaries to abuse free services – such as trial periods – to [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] for follow-on purposes.(Citation: Free Trial PurpleUrchin)

Adversaries may also take steps to cultivate a persona around the email account, such as through use of [[T1585-establish_accounts#^t1585001-social-media-accounts|T1585.001: Social Media Accounts]], to increase the chance of success of follow-on behaviors. Created email accounts can also be used in the acquisition of infrastructure (ex: [[T1583-acquire_infrastructure#^t1583001-domains|T1583.001: Domains]]).(Citation: Mandiant APT1)

To decrease the chance of physically tying back operations to themselves, adversaries may make use of disposable email services.(Citation: Trend Micro R980 2016) 

### T1585.003: Cloud Accounts

^t1585003-cloud-accounts

Adversaries may create accounts with cloud providers that can be used during targeting. Adversaries can use cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, MEGA, Microsoft OneDrive, or AWS S3 buckets for [[T1567-exfiltration_over_web_service#^t1567002-exfiltration-to-cloud-storage|T1567.002: Exfiltration to Cloud Storage]] or to [[T1608-stage_capabilities#^t1608002-upload-tool|T1608.002: Upload Tool]]s. Cloud accounts can also be used in the acquisition of infrastructure, such as [[T1583-acquire_infrastructure#^t1583003-virtual-private-server|T1583.003: Virtual Private Server]]s or [[T1583-acquire_infrastructure#^t1583007-serverless|T1583.007: Serverless]] infrastructure. Establishing cloud accounts may allow adversaries to develop sophisticated capabilities without managing their own servers.(Citation: Awake Security C2 Cloud)

Creating [[T1585-establish_accounts#^t1585003-cloud-accounts|T1585.003: Cloud Accounts]] may also require adversaries to establish [[T1585-establish_accounts#^t1585002-email-accounts|T1585.002: Email Accounts]] to register with the cloud provider. 

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

