---
mitre_id: "T1566"
mitre_name: "Phishing"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--a62a8db3-f23a-4d8f-afd6-9dbc77e7813b"
mitre_created: "2020-03-02T18:45:07.892Z"
mitre_modified: "2025-10-24T17:49:11.351Z"
mitre_version: "2.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1566/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Identity Provider"
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0001"
d3fend_ids:
  - "D3-APCA"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-CSPP"
  - "D3-DA"
  - "D3-DF"
  - "D3-DI"
  - "D3-EF"
  - "D3-EFA"
  - "D3-ER"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HD"
  - "D3-IAA"
  - "D3-ISVA"
  - "D3-ITF"
  - "D3-LFP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RE"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RTSD"
  - "D3-SMRA"
  - "D3-SRA"
  - "D3-UA"
  - "D3-UGLPA"
  - "D3-URA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns.

Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services, like social media platforms. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., [[T1564-hide_artifacts#^t1564008-email-hiding-rules|T1564.008: Email Hiding Rules]]).(Citation: Microsoft OAuth Spam 2022)(Citation: Palo Alto Unit 42 VBA Infostealer 2014) Another way to accomplish this is by [[T1672-email_spoofing|T1672: Email Spoofing]](Citation: Proofpoint-spoof) the identity of the sender, which can be used to fool both the human recipient as well as automated security tools,(Citation: cyberproof-double-bounce) or by including the intended target as a party to an existing email thread that includes malicious files or links (i.e., "thread hijacking").(Citation: phishing-krebs)

Victims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,(Citation: sygnia Luna Month)(Citation: CISA Remote Monitoring and Management Software) or install adversary-accessible remote management tools onto their computer (i.e., [[T1204-user_execution|T1204: User Execution]]).(Citation: Unit42 Luna Moth)

## Workspace

- [[workspaces/attack/techniques/T1566-phishing-note|Open workspace note]]

![[workspaces/attack/techniques/T1566-phishing-note]]

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-EF-email_filtering|D3-EF: Email Filtering]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-ER-email_removal|D3-ER: Email Removal]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HD-homoglyph_detection|D3-HD: Homoglyph Detection]]
- [[D3-IAA-identifier_activity_analysis|D3-IAA: Identifier Activity Analysis]]
- [[D3-ISVA-inbound_session_volume_analysis|D3-ISVA: Inbound Session Volume Analysis]]
- [[D3-ITF-inbound_traffic_filtering|D3-ITF: Inbound Traffic Filtering]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RE-restore_email|D3-RE: Restore Email]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-SMRA-sender_mta_reputation_analysis|D3-SMRA: Sender MTA Reputation Analysis]]
- [[D3-SRA-sender_reputation_analysis|D3-SRA: Sender Reputation Analysis]]
- [[D3-UA-url_analysis|D3-UA: URL Analysis]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]
- [[D3-URA-url_reputation_analysis|D3-URA: URL Reputation Analysis]]

## Subtechniques

### T1566.001: Spearphishing Attachment

^t1566001-spearphishing-attachment

Adversaries may send spearphishing emails with a malicious attachment in an attempt to gain access to victim systems. Spearphishing attachment is a specific variant of spearphishing. Spearphishing attachment is different from other forms of spearphishing in that it employs the use of malware attached to an email. All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon [[T1204-user_execution|T1204: User Execution]] to gain execution.(Citation: Unit 42 DarkHydrus July 2018) Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

There are many options for the attachment such as Microsoft Office documents, executables, PDFs, or archived files. Upon opening the attachment (and potentially clicking past protections), the adversary's payload exploits a vulnerability or directly executes on the user's system. The text of the spearphishing email usually tries to give a plausible reason why the file should be opened, and may explain how to bypass system protections in order to do so. The email may also contain instructions on how to decrypt an attachment, such as a zip file password, in order to evade email boundary defenses. Adversaries frequently manipulate file extensions and icons in order to make attached executables appear to be document files, or files exploiting one application appear to be a file for a different one. 

### T1566.002: Spearphishing Link

^t1566002-spearphishing-link

Adversaries may send spearphishing emails with a malicious link in an attempt to gain access to victim systems. Spearphishing with a link is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of links to download malware contained in email, instead of attaching malicious files to the email itself, to avoid defenses that may inspect email attachments. Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this case, the malicious emails contain links. Generally, the links will be accompanied by social engineering text and require the user to actively click or copy and paste a URL into a browser, leveraging [[T1204-user_execution|T1204: User Execution]]. The visited website may compromise the web browser using an exploit, or the user will be prompted to download applications, documents, zip files, or even executables depending on the pretext for the email in the first place.

Adversaries may also include links that are intended to interact directly with an email reader, including embedded images intended to exploit the end system directly. Additionally, adversaries may use seemingly benign links that abuse special characters to mimic legitimate websites (known as an "IDN homograph attack").(Citation: CISA IDN ST05-016) URLs may also be obfuscated by taking advantage of quirks in the URL schema, such as the acceptance of integer- or hexadecimal-based hostname formats and the automatic discarding of text before an “@” symbol: for example, `hxxp://google.com@1157586937`.(Citation: Mandiant URL Obfuscation 2023)

Adversaries may also utilize links to perform consent phishing/spearphishing campaigns to [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]s that grant immediate access to the victim environment. For example, a user may be lured into granting adversaries permissions/access via a malicious OAuth 2.0 request URL that when accepted by the user provide permissions/access for malicious applications.(Citation: Trend Micro Pawn Storm OAuth 2017)(Citation: Microsoft OAuth 2.0 Consent Phishing 2021) These stolen access tokens allow the adversary to perform various actions on behalf of the user via API calls.(Citation: Microsoft OAuth 2.0 Consent Phishing 2021)

Similarly, malicious links may also target device-based authorization, such as OAuth 2.0 device authorization grant flow which is typically used to authenticate devices without UIs/browsers. Known as “device code phishing,” an adversary may send a link that directs the victim to a malicious authorization page where the user is tricked into entering a code/credentials that produces a device token.(Citation: SecureWorks Device Code Phishing 2021)(Citation: Netskope Device Code Phishing 2021)(Citation: Optiv Device Code Phishing 2021)

### T1566.003: Spearphishing via Service

^t1566003-spearphishing-via-service

Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim systems. Spearphishing via service is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of third party services rather than directly via enterprise email channels. 

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries send messages through various social media services, personal webmail, and other non-enterprise controlled services.(Citation: Lookout Dark Caracal Jan 2018) These services are more likely to have a less-strict security policy than an enterprise. As with most kinds of spearphishing, the goal is to generate rapport with the target or get the target's interest in some way. Adversaries will create fake social media accounts and message employees for potential job opportunities. Doing so allows a plausible reason for asking about services, policies, and software that's running in an environment. The adversary can then send malicious links or attachments through these services.

A common example is to build rapport with a target via social media, then send content to a personal webmail service that the target uses on their work computer. This allows an adversary to bypass some email restrictions on the work account, and the target is more likely to open the file since it's something they were expecting. If the payload doesn't work as expected, the adversary can continue normal communications and troubleshoot with the target on how to get it working.

### T1566.004: Spearphishing Voice

^t1566004-spearphishing-voice

Adversaries may use voice communications to ultimately gain access to victim systems. Spearphishing voice is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of manipulating a user into providing access to systems through a phone call or other forms of voice communications. Spearphishing frequently involves social engineering techniques, such as posing as a trusted source (ex: [[T1656-impersonation|T1656: Impersonation]]) and/or creating a sense of urgency or alarm for the recipient.

All forms of phishing are electronically delivered social engineering. In this scenario, adversaries are not directly sending malware to a victim vice relying on [[T1204-user_execution|T1204: User Execution]] for delivery and execution. For example, victims may receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,(Citation: sygnia Luna Month)(Citation: CISA Remote Monitoring and Management Software) or install adversary-accessible remote management tools ([[T1219-remote_access_tools|T1219: Remote Access Tools]]) onto their computer.(Citation: Unit42 Luna Moth)

Adversaries may also combine voice phishing with [[T1621-multi-factor_authentication_request_generation|T1621: Multi-Factor Authentication Request Generation]] in order to trick users into divulging MFA credentials or accepting authentication prompts.(Citation: Proofpoint Vishing)

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

