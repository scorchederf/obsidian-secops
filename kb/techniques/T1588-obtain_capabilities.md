---
id: T1588
name: Obtain Capabilities
created: 2020-10-01 01:56:24.776000+00:00
modified: 2025-10-24 17:49:24.545000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[resource_development|Resource Development]]

Adversaries may buy and/or steal capabilities that can be used during targeting. Rather than developing their own capabilities in-house, adversaries may purchase, freely download, or steal them. Activities may include the acquisition of malware, software (including licenses), exploits, certificates, and information relating to vulnerabilities. Adversaries may obtain capabilities to support their operations throughout numerous phases of the adversary lifecycle.

In addition to downloading free malware, software, and exploits from the internet, adversaries may purchase these capabilities from third-party entities. Third-party entities can include technology companies that specialize in malware and exploits, criminal marketplaces, or from individuals.(Citation: NationsBuying)(Citation: PegasusCitizenLab)

In addition to purchasing capabilities, adversaries may steal capabilities from third-party entities (including other adversaries). This can include stealing software licenses, malware, SSL/TLS and code-signing certificates, or raiding closed databases of vulnerabilities or exploits.(Citation: DiginotarCompromise)

## Subtechniques

### T1588.001: Malware
^t1588001-malware

**Parent Technique**
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may buy, steal, or download malware that can be used during targeting. Malicious software can include payloads, droppers, post-compromise tools, backdoors, packers, and C2 protocols. Adversaries may acquire malware to support their operations, obtaining a means for maintaining control of remote machines, evading defenses, and executing post-compromise behaviors.

In addition to downloading free malware from the internet, adversaries may purchase these capabilities from third-party entities. Third-party entities can include technology companies that specialize in malware development, criminal marketplaces (including Malware-as-a-Service, or MaaS), or from individuals. In addition to purchasing malware, adversaries may steal and repurpose malware from third-party entities (including other adversaries).

#### Properties

- id: T1588.001
- name: Malware
- created: 2020-10-01 02:06:11.499000+00:00
- modified: 2025-10-24 17:48:58.766000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1588.002: Tool
^t1588002-tool

**Parent Technique**
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://attack.mitre.org/software/S0029)). 

Adversaries may obtain tools to support their operations, including to support execution of post-compromise behaviors. Tools may also be leveraged for testing – for example, evaluating malware against commercial antivirus or endpoint detection and response (EDR) applications.(Citation: Forescout Conti Leaks 2022)(Citation: Sentinel Labs Top Tier Target 2025)

Tool acquisition may involve the procurement of commercial software licenses, including for red teaming tools such as Cobalt Strike. In addition to freely downloading or purchasing software, adversaries may steal software and/or software licenses from third-party entities (including other adversaries). Threat actors may also crack trial versions of software.(Citation: Recorded Future Beacon 2019)

#### Properties

- id: T1588.002
- name: Tool
- created: 2020-10-01 02:08:33.977000+00:00
- modified: 2025-10-24 17:49:10.900000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1588.003: Code Signing Certificates
^t1588003-code-signing-certificates

**Parent Technique**
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may buy and/or steal code signing certificates that can be used during targeting. Code signing is the process of digitally signing executables and scripts to confirm the software author and guarantee that the code has not been altered or corrupted. Code signing provides a level of authenticity for a program from the developer and a guarantee that the program has not been tampered with.(Citation: Wikipedia Code Signing) Users and/or security tools may trust a signed piece of code more than an unsigned piece of code even if they don't know who issued the certificate or who the author is.

Prior to [Code Signing](https://attack.mitre.org/techniques/T1553/002), adversaries may purchase or steal code signing certificates for use in operations. The purchase of code signing certificates may be done using a front organization or using information stolen from a previously compromised entity that allows the adversary to validate to a certificate provider as that entity. Adversaries may also steal code signing materials directly from a compromised third-party.

#### Properties

- id: T1588.003
- name: Code Signing Certificates
- created: 2020-10-01 02:11:47.237000+00:00
- modified: 2025-10-24 17:49:32.891000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1588.004: Digital Certificates
^t1588004-digital-certificates

**Parent Technique**
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may buy and/or steal SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner.

Adversaries may purchase or steal SSL/TLS certificates to further their operations, such as encrypting C2 traffic (ex: [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002) with [Web Protocols](https://attack.mitre.org/techniques/T1071/001)) or even enabling [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) if the certificate is trusted or otherwise added to the root of trust (i.e. [Install Root Certificate](https://attack.mitre.org/techniques/T1553/004)). The purchase of digital certificates may be done using a front organization or using information stolen from a previously compromised entity that allows the adversary to validate to a certificate provider as that entity. Adversaries may also steal certificate materials directly from a compromised third-party, including from certificate authorities.(Citation: DiginotarCompromise) Adversaries may register or hijack domains that they will later purchase an SSL/TLS certificate for.

Certificate authorities exist that allow adversaries to acquire SSL/TLS certificates, such as domain validation certificates, for free.(Citation: Let's Encrypt FAQ)

After obtaining a digital certificate, an adversary may then install that certificate (see [Install Digital Certificate](https://attack.mitre.org/techniques/T1608/003)) on infrastructure under their control.

#### Properties

- id: T1588.004
- name: Digital Certificates
- created: 2020-10-01 02:14:18.044000+00:00
- modified: 2025-10-24 17:48:27.525000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1588.005: Exploits
^t1588005-exploits

**Parent Technique**
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may buy, steal, or download exploits that can be used during targeting. An exploit takes advantage of a bug or vulnerability in order to cause unintended or unanticipated behavior to occur on computer hardware or software. Rather than developing their own exploits, an adversary may find/modify exploits from online or purchase them from exploit vendors.(Citation: Exploit Database)(Citation: TempertonDarkHotel)(Citation: NationsBuying)

In addition to downloading free exploits from the internet, adversaries may purchase exploits from third-party entities. Third-party entities can include technology companies that specialize in exploit development, criminal marketplaces (including exploit kits), or from individuals.(Citation: PegasusCitizenLab)(Citation: Wired SandCat Oct 2019) In addition to purchasing exploits, adversaries may steal and repurpose exploits from third-party entities (including other adversaries).(Citation: TempertonDarkHotel)

An adversary may monitor exploit provider forums to understand the state of existing, as well as newly discovered, exploits. There is usually a delay between when an exploit is discovered and when it is made public. An adversary may target the systems of those known to conduct exploit research and development in order to gain that knowledge for use during a subsequent operation.

Adversaries may use exploits during various phases of the adversary lifecycle (i.e. [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190), [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203), [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068), [Exploitation for Defense Evasion](https://attack.mitre.org/techniques/T1211), [Exploitation for Credential Access](https://attack.mitre.org/techniques/T1212), [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210), and [Application or System Exploitation](https://attack.mitre.org/techniques/T1499/004)).

#### Properties

- id: T1588.005
- name: Exploits
- created: 2020-10-01 02:17:46.086000+00:00
- modified: 2025-10-24 17:49:36.851000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1588.006: Vulnerabilities
^t1588006-vulnerabilities

**Parent Technique**
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may acquire information about vulnerabilities that can be used during targeting. A vulnerability is a weakness in computer hardware or software that can, potentially, be exploited by an adversary to cause unintended or unanticipated behavior to occur. Adversaries may find vulnerability information by searching open databases or gaining access to closed vulnerability databases.(Citation: National Vulnerability Database)

An adversary may monitor vulnerability disclosures/databases to understand the state of existing, as well as newly discovered, vulnerabilities. There is usually a delay between when a vulnerability is discovered and when it is made public. An adversary may target the systems of those known to conduct vulnerability research (including commercial vendors). Knowledge of a vulnerability may cause an adversary to search for an existing exploit (i.e. [Exploits](https://attack.mitre.org/techniques/T1588/005)) or to attempt to develop one themselves (i.e. [Exploits](https://attack.mitre.org/techniques/T1587/004)).

#### Properties

- id: T1588.006
- name: Vulnerabilities
- created: 2020-10-15 02:59:38.628000+00:00
- modified: 2025-10-24 17:48:34.033000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1588.007: Artificial Intelligence
^t1588007-artificial-intelligence

**Parent Technique**
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may obtain access to generative artificial intelligence tools, such as large language models (LLMs), to aid various techniques during targeting. These tools may be used to inform, bolster, and enable a variety of malicious tasks, including conducting [Reconnaissance](https://attack.mitre.org/tactics/TA0043), creating basic scripts, assisting social engineering, and even developing payloads.(Citation: MSFT-AI) 

For example, by utilizing a publicly available LLM an adversary is essentially outsourcing or automating certain tasks to the tool. Using AI, the adversary may draft and generate content in a variety of written languages to be used in [Phishing](https://attack.mitre.org/techniques/T1566)/[Phishing for Information](https://attack.mitre.org/techniques/T1598) campaigns. The same publicly available tool may further enable vulnerability or other offensive research supporting [Develop Capabilities](https://attack.mitre.org/techniques/T1587). AI tools may also automate technical tasks by generating, refining, or otherwise enhancing (e.g., [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027)) malicious scripts and payloads.(Citation: OpenAI-CTI) Finally, AI-generated text, images, audio, and video may be used for fraud, [Impersonation](https://attack.mitre.org/techniques/T1656), and other malicious activities.(Citation: Google-Vishing24)(Citation: IC3-AI24)(Citation: WSJ-Vishing-AI24)


#### Properties

- id: T1588.007
- name: Artificial Intelligence
- created: 2024-03-11 13:37:31.836000+00:00
- modified: 2025-10-24 17:48:23.190000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

