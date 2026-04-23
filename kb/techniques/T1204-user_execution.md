---
mitre_id: "T1204"
mitre_name: "User Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--8c32eb4d-805f-4fc5-bf60-c4d476c131b5"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:04.940Z"
mitre_version: "1.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1204/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
  - "IaaS"
  - "Containers"
mitre_tactic_ids:
  - "TA0002"
---

# T1204: User Execution

An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of [[T1566-phishing|T1566: Phishing]].

While [[T1204-user_execution|T1204: User Execution]] frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [[T1534-internal_spearphishing|T1534: Internal Spearphishing]].

Adversaries may also deceive users into performing actions such as:

* Enabling [[T1219-remote_access_tools|T1219: Remote Access Tools]], allowing direct control of the system to the adversary
* Running malicious JavaScript in their browser, allowing adversaries to [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]s(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)
* Downloading and executing malware for [[T1204-user_execution|T1204: User Execution]]
* Coerceing users to copy, paste, and execute malicious code manually(Citation: Reliaquest-execution)(Citation: proofpoint-selfpwn)

For example, tech support scams can be facilitated through [[T1566-phishing|T1566: Phishing]], vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or [[T1219-remote_access_tools|T1219: Remote Access Tools]].(Citation: Telephone Attack Delivery)

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Subtechniques

### T1204.001: Malicious Link

^t1204001-malicious-link

An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]. Clicking on a link may also lead to other execution techniques such as exploitation of a browser or application vulnerability via [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]. Links may also lead users to download files that require execution via [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]].

### T1204.002: Malicious File

^t1204002-malicious-file

An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected to social engineering to get them to open a file that will lead to code execution. This user action will typically be observed as follow-on behavior from [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]. Adversaries may use several types of files that require a user to execute them, including .doc, .pdf, .xls, .rtf, .scr, .exe, .lnk, .pif, .cpl, .reg, and .iso.(Citation: Mandiant Trojanized Windows 10)

Adversaries may employ various forms of [[T1036-masquerading|T1036: Masquerading]] and [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]] to increase the likelihood that a user will open and successfully execute a malicious file. These methods may include using a familiar naming convention and/or password protecting the file and supplying instructions to a user on how to open it.(Citation: Password Protected Word Docs) 

While [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]] frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [[T1534-internal_spearphishing|T1534: Internal Spearphishing]].

### T1204.003: Malicious Image

^t1204003-malicious-image

Adversaries may rely on a user running a malicious image to facilitate execution. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be backdoored. Backdoored images may be uploaded to a public repository via [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]], and users may then download and deploy an instance or container from the image without realizing the image is malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that executes cryptocurrency mining, in the instance or container.(Citation: Summit Route Malicious AMIs)

Adversaries may also name images a certain way to increase the chance of users mistakenly deploying an instance or container from the image (ex: [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]).(Citation: Aqua Security Cloud Native Threat Report June 2021)

### T1204.004: Malicious Copy and Paste

^t1204004-malicious-copy-and-paste

An adversary may rely upon a user copying and pasting code in order to gain execution. Users may be subjected to social engineering to get them to copy and paste code directly into a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]. One such strategy is "ClickFix," in which adversaries present users with seemingly helpful solutions—such as prompts to fix errors or complete CAPTCHAs—that instead instruct the user to copy and paste malicious code.

Malicious websites, such as those used in [[T1189-drive-by_compromise|T1189: Drive-by Compromise]], may present fake error messages or CAPTCHA prompts that instruct users to open a terminal or the Windows Run Dialog box and execute an arbitrary command. These commands may be obfuscated using encoding or other techniques to conceal malicious intent. Once executed, the adversary will typically be able to establish a foothold on the victim's machine.(Citation: CloudSEK Lumma Stealer 2024)(Citation: Sekoia ClickFake 2025)(Citation: Reliaquest CAPTCHA 2024)(Citation: AhnLab LummaC2 2025)

Adversaries may also leverage phishing emails for this purpose. When a user attempts to open an attachment, they may be presented with a fake error and offered a malicious command to paste as a solution, consistent with the "ClickFix" strategy.(Citation: Proofpoint ClickFix 2024)(Citation: AhnLab Malicioys Copy Paste 2024)

Tricking a user into executing a command themselves may help to bypass email filtering, browser sandboxing, or other mitigations designed to protect users against malicious downloaded files. 

### T1204.005: Malicious Library

^t1204005-malicious-library

Adversaries may rely on a user installing a malicious library to facilitate execution. Threat actors may [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]] to package managers such as NPM and PyPi, as well as to public code repositories such as GitHub. User may install libraries without realizing they are malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that establishes persistence, steals data, or mines cryptocurrency.(Citation: Datadog Security Labs Malicious PyPi Packages 2024)(Citation: Fortinet Malicious NPM Packages 2023)

In some cases, threat actors may compromise and backdoor existing popular libraries (i.e., [[T1195-supply_chain_compromise#^t1195001-compromise-software-dependencies-and-development-tools|T1195.001: Compromise Software Dependencies and Development Tools]]). Alternatively, they may create entirely new packages and leverage behaviors such as typosquatting to encourage users to install them.

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1033-limit_software_installation|M1033: Limit Software Installation]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Platforms

- Linux
- Windows
- macOS
- IaaS
- Containers

