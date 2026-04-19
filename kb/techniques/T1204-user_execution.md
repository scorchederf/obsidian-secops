---
id: T1204
name: User Execution
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-10-24 17:49:04.940000+00:00
type: attack-pattern
x_mitre_version: 1.8
x_mitre_domains: enterprise-attack
---

## Tactic

- [[execution|Execution]]

An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of [Phishing](https://attack.mitre.org/techniques/T1566).

While [User Execution](https://attack.mitre.org/techniques/T1204) frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534).

Adversaries may also deceive users into performing actions such as:

* Enabling [Remote Access Tools](https://attack.mitre.org/techniques/T1219), allowing direct control of the system to the adversary
* Running malicious JavaScript in their browser, allowing adversaries to [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539)s(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)
* Downloading and executing malware for [User Execution](https://attack.mitre.org/techniques/T1204)
* Coerceing users to copy, paste, and execute malicious code manually(Citation: Reliaquest-execution)(Citation: proofpoint-selfpwn)

For example, tech support scams can be facilitated through [Phishing](https://attack.mitre.org/techniques/T1566), vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or [Remote Access Tools](https://attack.mitre.org/techniques/T1219).(Citation: Telephone Attack Delivery)

## Subtechniques

### T1204.001: Malicious Link
^t1204001-malicious-link

**Parent Technique**
- [[T1204-user_execution|T1204: User Execution]]

**Tactic**
- [[execution|Execution]]

An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002). Clicking on a link may also lead to other execution techniques such as exploitation of a browser or application vulnerability via [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203). Links may also lead users to download files that require execution via [Malicious File](https://attack.mitre.org/techniques/T1204/002).

#### Properties

- id: T1204.001
- name: Malicious Link
- created: 2020-03-11 14:43:31.706000+00:00
- modified: 2025-10-24 17:49:35.144000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1204.002: Malicious File
^t1204002-malicious-file

**Parent Technique**
- [[T1204-user_execution|T1204: User Execution]]

**Tactic**
- [[execution|Execution]]

An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected to social engineering to get them to open a file that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001). Adversaries may use several types of files that require a user to execute them, including .doc, .pdf, .xls, .rtf, .scr, .exe, .lnk, .pif, .cpl, .reg, and .iso.(Citation: Mandiant Trojanized Windows 10)

Adversaries may employ various forms of [Masquerading](https://attack.mitre.org/techniques/T1036) and [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027) to increase the likelihood that a user will open and successfully execute a malicious file. These methods may include using a familiar naming convention and/or password protecting the file and supplying instructions to a user on how to open it.(Citation: Password Protected Word Docs) 

While [Malicious File](https://attack.mitre.org/techniques/T1204/002) frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534).

#### Properties

- id: T1204.002
- name: Malicious File
- created: 2020-03-11 14:49:36.954000+00:00
- modified: 2025-10-24 17:48:31.674000+00:00
- type: attack-pattern
- x_mitre_version: 1.6
- x_mitre_domains: enterprise-attack

### T1204.003: Malicious Image
^t1204003-malicious-image

**Parent Technique**
- [[T1204-user_execution|T1204: User Execution]]

**Tactic**
- [[execution|Execution]]

Adversaries may rely on a user running a malicious image to facilitate execution. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be backdoored. Backdoored images may be uploaded to a public repository via [Upload Malware](https://attack.mitre.org/techniques/T1608/001), and users may then download and deploy an instance or container from the image without realizing the image is malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that executes cryptocurrency mining, in the instance or container.(Citation: Summit Route Malicious AMIs)

Adversaries may also name images a certain way to increase the chance of users mistakenly deploying an instance or container from the image (ex: [Match Legitimate Resource Name or Location](https://attack.mitre.org/techniques/T1036/005)).(Citation: Aqua Security Cloud Native Threat Report June 2021)

#### Properties

- id: T1204.003
- name: Malicious Image
- created: 2021-03-30 17:20:05.789000+00:00
- modified: 2025-10-24 17:49:13.999000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1204.004: Malicious Copy and Paste
^t1204004-malicious-copy-and-paste

**Parent Technique**
- [[T1204-user_execution|T1204: User Execution]]

**Tactic**
- [[execution|Execution]]

An adversary may rely upon a user copying and pasting code in order to gain execution. Users may be subjected to social engineering to get them to copy and paste code directly into a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059). One such strategy is "ClickFix," in which adversaries present users with seemingly helpful solutions—such as prompts to fix errors or complete CAPTCHAs—that instead instruct the user to copy and paste malicious code.

Malicious websites, such as those used in [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), may present fake error messages or CAPTCHA prompts that instruct users to open a terminal or the Windows Run Dialog box and execute an arbitrary command. These commands may be obfuscated using encoding or other techniques to conceal malicious intent. Once executed, the adversary will typically be able to establish a foothold on the victim's machine.(Citation: CloudSEK Lumma Stealer 2024)(Citation: Sekoia ClickFake 2025)(Citation: Reliaquest CAPTCHA 2024)(Citation: AhnLab LummaC2 2025)

Adversaries may also leverage phishing emails for this purpose. When a user attempts to open an attachment, they may be presented with a fake error and offered a malicious command to paste as a solution, consistent with the "ClickFix" strategy.(Citation: Proofpoint ClickFix 2024)(Citation: AhnLab Malicioys Copy Paste 2024)

Tricking a user into executing a command themselves may help to bypass email filtering, browser sandboxing, or other mitigations designed to protect users against malicious downloaded files. 

#### Properties

- id: T1204.004
- name: Malicious Copy and Paste
- created: 2025-03-18 12:57:50.188000+00:00
- modified: 2025-10-05 17:30:01.834000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1204.005: Malicious Library
^t1204005-malicious-library

**Parent Technique**
- [[T1204-user_execution|T1204: User Execution]]

**Tactic**
- [[execution|Execution]]

Adversaries may rely on a user installing a malicious library to facilitate execution. Threat actors may [Upload Malware](https://attack.mitre.org/techniques/T1608/001) to package managers such as NPM and PyPi, as well as to public code repositories such as GitHub. User may install libraries without realizing they are malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that establishes persistence, steals data, or mines cryptocurrency.(Citation: Datadog Security Labs Malicious PyPi Packages 2024)(Citation: Fortinet Malicious NPM Packages 2023)

In some cases, threat actors may compromise and backdoor existing popular libraries (i.e., [Compromise Software Dependencies and Development Tools](https://attack.mitre.org/techniques/T1195/001)). Alternatively, they may create entirely new packages and leverage behaviors such as typosquatting to encourage users to install them.

#### Properties

- id: T1204.005
- name: Malicious Library
- created: 2025-05-22 19:50:18.472000+00:00
- modified: 2025-05-22 21:22:40.822000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

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

## Tools


