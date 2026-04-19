---
id: T1566
name: Phishing
created: 2020-03-02 18:45:07.892000+00:00
modified: 2025-10-24 17:49:11.351000+00:00
type: attack-pattern
x_mitre_version: 2.7
x_mitre_domains: enterprise-attack
---

## Tactic

- [[initial_access|Initial Access]]

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns.

Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services, like social media platforms. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., [Email Hiding Rules](https://attack.mitre.org/techniques/T1564/008)).(Citation: Microsoft OAuth Spam 2022)(Citation: Palo Alto Unit 42 VBA Infostealer 2014) Another way to accomplish this is by [Email Spoofing](https://attack.mitre.org/techniques/T1672)(Citation: Proofpoint-spoof) the identity of the sender, which can be used to fool both the human recipient as well as automated security tools,(Citation: cyberproof-double-bounce) or by including the intended target as a party to an existing email thread that includes malicious files or links (i.e., "thread hijacking").(Citation: phishing-krebs)

Victims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,(Citation: sygnia Luna Month)(Citation: CISA Remote Monitoring and Management Software) or install adversary-accessible remote management tools onto their computer (i.e., [User Execution](https://attack.mitre.org/techniques/T1204)).(Citation: Unit42 Luna Moth)

## Subtechniques

### T1566.001: Spearphishing Attachment
^t1566001-spearphishing-attachment

**Parent Technique**
- [[T1566-phishing|T1566: Phishing]]

**Tactic**
- [[initial_access|Initial Access]]

Adversaries may send spearphishing emails with a malicious attachment in an attempt to gain access to victim systems. Spearphishing attachment is a specific variant of spearphishing. Spearphishing attachment is different from other forms of spearphishing in that it employs the use of malware attached to an email. All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon [User Execution](https://attack.mitre.org/techniques/T1204) to gain execution.(Citation: Unit 42 DarkHydrus July 2018) Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

There are many options for the attachment such as Microsoft Office documents, executables, PDFs, or archived files. Upon opening the attachment (and potentially clicking past protections), the adversary's payload exploits a vulnerability or directly executes on the user's system. The text of the spearphishing email usually tries to give a plausible reason why the file should be opened, and may explain how to bypass system protections in order to do so. The email may also contain instructions on how to decrypt an attachment, such as a zip file password, in order to evade email boundary defenses. Adversaries frequently manipulate file extensions and icons in order to make attached executables appear to be document files, or files exploiting one application appear to be a file for a different one. 

#### Properties

- id: T1566.001
- name: Spearphishing Attachment
- created: 2020-03-02 19:05:18.137000+00:00
- modified: 2025-10-24 17:48:35.522000+00:00
- type: attack-pattern
- x_mitre_version: 2.2
- x_mitre_domains: enterprise-attack

### T1566.002: Spearphishing Link
^t1566002-spearphishing-link

**Parent Technique**
- [[T1566-phishing|T1566: Phishing]]

**Tactic**
- [[initial_access|Initial Access]]

Adversaries may send spearphishing emails with a malicious link in an attempt to gain access to victim systems. Spearphishing with a link is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of links to download malware contained in email, instead of attaching malicious files to the email itself, to avoid defenses that may inspect email attachments. Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this case, the malicious emails contain links. Generally, the links will be accompanied by social engineering text and require the user to actively click or copy and paste a URL into a browser, leveraging [User Execution](https://attack.mitre.org/techniques/T1204). The visited website may compromise the web browser using an exploit, or the user will be prompted to download applications, documents, zip files, or even executables depending on the pretext for the email in the first place.

Adversaries may also include links that are intended to interact directly with an email reader, including embedded images intended to exploit the end system directly. Additionally, adversaries may use seemingly benign links that abuse special characters to mimic legitimate websites (known as an "IDN homograph attack").(Citation: CISA IDN ST05-016) URLs may also be obfuscated by taking advantage of quirks in the URL schema, such as the acceptance of integer- or hexadecimal-based hostname formats and the automatic discarding of text before an “@” symbol: for example, `hxxp://google.com@1157586937`.(Citation: Mandiant URL Obfuscation 2023)

Adversaries may also utilize links to perform consent phishing/spearphishing campaigns to [Steal Application Access Token](https://attack.mitre.org/techniques/T1528)s that grant immediate access to the victim environment. For example, a user may be lured into granting adversaries permissions/access via a malicious OAuth 2.0 request URL that when accepted by the user provide permissions/access for malicious applications.(Citation: Trend Micro Pawn Storm OAuth 2017)(Citation: Microsoft OAuth 2.0 Consent Phishing 2021) These stolen access tokens allow the adversary to perform various actions on behalf of the user via API calls.(Citation: Microsoft OAuth 2.0 Consent Phishing 2021)

Similarly, malicious links may also target device-based authorization, such as OAuth 2.0 device authorization grant flow which is typically used to authenticate devices without UIs/browsers. Known as “device code phishing,” an adversary may send a link that directs the victim to a malicious authorization page where the user is tricked into entering a code/credentials that produces a device token.(Citation: SecureWorks Device Code Phishing 2021)(Citation: Netskope Device Code Phishing 2021)(Citation: Optiv Device Code Phishing 2021)

#### Properties

- id: T1566.002
- name: Spearphishing Link
- created: 2020-03-02 19:15:44.182000+00:00
- modified: 2025-10-24 17:48:34.123000+00:00
- type: attack-pattern
- x_mitre_version: 2.8
- x_mitre_domains: enterprise-attack

### T1566.003: Spearphishing via Service
^t1566003-spearphishing-via-service

**Parent Technique**
- [[T1566-phishing|T1566: Phishing]]

**Tactic**
- [[initial_access|Initial Access]]

Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim systems. Spearphishing via service is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of third party services rather than directly via enterprise email channels. 

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries send messages through various social media services, personal webmail, and other non-enterprise controlled services.(Citation: Lookout Dark Caracal Jan 2018) These services are more likely to have a less-strict security policy than an enterprise. As with most kinds of spearphishing, the goal is to generate rapport with the target or get the target's interest in some way. Adversaries will create fake social media accounts and message employees for potential job opportunities. Doing so allows a plausible reason for asking about services, policies, and software that's running in an environment. The adversary can then send malicious links or attachments through these services.

A common example is to build rapport with a target via social media, then send content to a personal webmail service that the target uses on their work computer. This allows an adversary to bypass some email restrictions on the work account, and the target is more likely to open the file since it's something they were expecting. If the payload doesn't work as expected, the adversary can continue normal communications and troubleshoot with the target on how to get it working.

#### Properties

- id: T1566.003
- name: Spearphishing via Service
- created: 2020-03-02 19:24:00.951000+00:00
- modified: 2025-10-24 17:49:37.487000+00:00
- type: attack-pattern
- x_mitre_version: 2.0
- x_mitre_domains: enterprise-attack

### T1566.004: Spearphishing Voice
^t1566004-spearphishing-voice

**Parent Technique**
- [[T1566-phishing|T1566: Phishing]]

**Tactic**
- [[initial_access|Initial Access]]

Adversaries may use voice communications to ultimately gain access to victim systems. Spearphishing voice is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of manipulating a user into providing access to systems through a phone call or other forms of voice communications. Spearphishing frequently involves social engineering techniques, such as posing as a trusted source (ex: [Impersonation](https://attack.mitre.org/techniques/T1656)) and/or creating a sense of urgency or alarm for the recipient.

All forms of phishing are electronically delivered social engineering. In this scenario, adversaries are not directly sending malware to a victim vice relying on [User Execution](https://attack.mitre.org/techniques/T1204) for delivery and execution. For example, victims may receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,(Citation: sygnia Luna Month)(Citation: CISA Remote Monitoring and Management Software) or install adversary-accessible remote management tools ([Remote Access Tools](https://attack.mitre.org/techniques/T1219)) onto their computer.(Citation: Unit42 Luna Moth)

Adversaries may also combine voice phishing with [Multi-Factor Authentication Request Generation](https://attack.mitre.org/techniques/T1621) in order to trick users into divulging MFA credentials or accepting authentication prompts.(Citation: Proofpoint Vishing)

#### Properties

- id: T1566.004
- name: Spearphishing Voice
- created: 2023-09-07 21:50:08.827000+00:00
- modified: 2025-07-02 18:06:37.932000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1047-audit|M1047: Audit]]
- [[M1049-antivirus_antimalware|M1049: Antivirus/Antimalware]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows

## Tools


