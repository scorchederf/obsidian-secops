---
mitre_id: "T1598"
mitre_name: "Phishing for Information"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--cca0ccb6-a068-4574-a722-b1556f86833a"
mitre_created: "2020-10-02T17:07:01.502Z"
mitre_modified: "2025-10-24T17:49:24.096Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1598/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0043"
tags:
  - "attack"
  - "technique"
  - "offense"
---

# T1598: Phishing for Information

Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Phishing for information is different from [[T1566-phishing|T1566: Phishing]] in that the objective is gathering data from the victim rather than executing malicious code.

All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass credential harvesting campaigns.

Adversaries may also try to obtain information directly through the exchange of emails, instant messages, or other electronic conversation means.(Citation: ThreatPost Social Media Phishing)(Citation: TrendMictro Phishing)(Citation: PCMag FakeLogin)(Citation: Sophos Attachment)(Citation: GitHub Phishery) Victims may also receive phishing messages that direct them to call a phone number where the adversary attempts to collect confidential information.(Citation: Avertium callback phishing)

Phishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]) and/or sending multiple, seemingly urgent messages. Another way to accomplish this is by [[T1672-email_spoofing|T1672: Email Spoofing]](Citation: Proofpoint-spoof) the identity of the sender, which can be used to fool both the human recipient as well as automated security tools.(Citation: cyberproof-double-bounce) 

Phishing for information may also involve evasive techniques, such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., [[T1564-hide_artifacts#^t1564008-email-hiding-rules|T1564.008: Email Hiding Rules]]).(Citation: Microsoft OAuth Spam 2022)(Citation: Palo Alto Unit 42 VBA Infostealer 2014)

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1598.001: Spearphishing Service

^t1598001-spearphishing-service

Adversaries may send spearphishing messages via third-party services to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries send messages through various social media services, personal webmail, and other non-enterprise controlled services.(Citation: ThreatPost Social Media Phishing) These services are more likely to have a less-strict security policy than an enterprise. As with most kinds of spearphishing, the goal is to generate rapport with the target or get the target's interest in some way. Adversaries may create fake social media accounts and message employees for potential job opportunities. Doing so allows a plausible reason for asking about services, policies, and information about their environment. Adversaries may also use information from previous reconnaissance efforts (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]) to craft persuasive and believable lures.

### T1598.002: Spearphishing Attachment

^t1598002-spearphishing-attachment

Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email. In some cases, they may rely upon the recipient populating information, then returning the file.(Citation: Sophos Attachment)(Citation: GitHub Phishery) The text of the spearphishing email usually tries to give a plausible reason why the file should be filled-in, such as a request for information from a business associate. In other cases, adversaries may leverage techniques such as [[T1027-obfuscated_files_or_information#^t1027006-html-smuggling|T1027.006: HTML Smuggling]] to harvest user credentials via fake login portals.(Citation: Huntress HTML Smuggling 2024)

Adversaries may also use information from previous reconnaissance efforts (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]) to craft persuasive and believable lures.

### T1598.003: Spearphishing Link

^t1598003-spearphishing-link

Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [[T1585-establish_accounts|T1585: Establish Accounts]] or [[T1586-compromise_accounts|T1586: Compromise Accounts]]) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, the malicious emails contain links generally accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser.(Citation: TrendMictro Phishing)(Citation: PCMag FakeLogin) The given website may be a clone of a legitimate site (such as an online or corporate login portal) or may closely resemble a legitimate site in appearance and have a URL containing elements from the real site. URLs may also be obfuscated by taking advantage of quirks in the URL schema, such as the acceptance of integer- or hexadecimal-based hostname formats and the automatic discarding of text before an “@” symbol: for example, `hxxp://google.com@1157586937`.(Citation: Mandiant URL Obfuscation 2023)

Adversaries may also embed “tracking pixels,” "web bugs," or "web beacons" within phishing messages to verify the receipt of an email, while also potentially profiling and tracking victim information such as IP address.(Citation: NIST Web Bug)(Citation: Ryte Wiki) These mechanisms often appear as small images (typically one pixel in size) or otherwise obfuscated objects and are typically delivered as HTML code containing a link to a remote server.(Citation: Ryte Wiki)(Citation: IAPP)

Adversaries may also be able to spoof a complete website using what is known as a "browser-in-the-browser" (BitB) attack. By generating a fake browser popup window with an HTML-based address bar that appears to contain a legitimate URL (such as an authentication portal), they may be able to prompt users to enter their credentials while bypassing typical URL verification methods.(Citation: ZScaler BitB 2020)(Citation: Mr. D0x BitB 2022)

Adversaries can use phishing kits such as `EvilProxy` and `Evilginx2` to perform adversary-in-the-middle phishing by proxying the connection between the victim and the legitimate website. On a successful login, the victim is redirected to the legitimate website, while the adversary captures their session cookie (i.e., [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]) in addition to their username and password. This may enable the adversary to then bypass MFA via [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]].(Citation: Proofpoint Human Factor)

Adversaries may also send a malicious link in the form of Quick Response (QR) Codes (also known as “quishing”). These links may direct a victim to a credential phishing page.(Citation: QR-campaign-energy-firm) By using a QR code, the URL may not be exposed in the email and may thus go undetected by most automated email security scans.(Citation: qr-phish-agriculture) These QR codes may be scanned by or delivered directly  to a user’s mobile device (i.e., [Phishing](https://attack.mitre.org/techniques/T1660)), which may be less secure in several relevant ways.(Citation: qr-phish-agriculture) For example, mobile users may not be able to notice minor differences between genuine and credential harvesting websites due to mobile’s smaller form factor.

From the fake website, information is gathered in web forms and sent to the adversary. Adversaries may also use information from previous reconnaissance efforts (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]) to craft persuasive and believable lures.

### T1598.004: Spearphishing Voice

^t1598004-spearphishing-voice

Adversaries may use voice communications to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [[T1656-impersonation|T1656: Impersonation]]) and/or creating a sense of urgency or alarm for the recipient.

All forms of phishing are electronically delivered social engineering. In this scenario, adversaries use phone calls to elicit sensitive information from victims. Known as voice phishing (or "vishing"), these communications can be manually executed by adversaries, hired call centers, or even automated via robocalls. Voice phishers may spoof their phone number while also posing as a trusted entity, such as a business partner or technical support staff.(Citation: BOA Telephone Scams)

Victims may also receive phishing messages that direct them to call a phone number ("callback phishing") where the adversary attempts to collect confidential information.(Citation: Avertium callback phishing)

Adversaries may also use information from previous reconnaissance efforts (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]) to tailor pretexts to be even more persuasive and believable for the victim.

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- PRE

## Workspace

- [[kb/notes/attack/techniques/t1598-notes|Open workspace note]]

