---
mitre_id: "T1587"
mitre_name: "Develop Capabilities"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--edadea33-549c-4ed1-9783-8f5a5853cbdf"
mitre_created: "2020-10-01T01:30:00.877Z"
mitre_modified: "2025-10-24T17:49:34.675Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1587/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may build capabilities that can be used during targeting. Rather than purchasing, freely downloading, or stealing capabilities, adversaries may develop their own capabilities in-house. This is the process of identifying development requirements and building solutions such as malware, exploits, and self-signed certificates. Adversaries may develop capabilities to support their operations throughout numerous phases of the adversary lifecycle.(Citation: Mandiant APT1)(Citation: Kaspersky Sofacy)(Citation: Bitdefender StrongPity June 2020)(Citation: Talos Promethium June 2020)

As with legitimate development efforts, different skill sets may be required for developing capabilities. The skills needed may be located in-house, or may need to be contracted out. Use of a contractor may be considered an extension of that adversary's development capabilities, provided the adversary plays a role in shaping requirements and maintains a degree of exclusivity to the capability.

## Workspace

- [[workspaces/attack/techniques/T1587-develop_capabilities-note|Open workspace note]]

![[workspaces/attack/techniques/T1587-develop_capabilities-note]]

## Tactics

- [[TA0042-resource_development|TA0042: Resource Development]]

## Subtechniques

### T1587.001: Malware

^t1587001-malware

Adversaries may develop malware and malware components that can be used during targeting. Building malicious software can include the development of payloads, droppers, post-compromise tools, backdoors (including backdoored images), packers, C2 protocols, and the creation of infected removable media. Adversaries may develop malware to support their operations, creating a means for maintaining control of remote machines, evading defenses, and executing post-compromise behaviors.(Citation: Mandiant APT1)(Citation: Kaspersky Sofacy)(Citation: ActiveMalwareEnergy)(Citation: FBI Flash FIN7 USB)

During malware development, adversaries may intentionally include indicators aligned with other known actors in order to mislead attribution by defenders.(Citation: Olympic Destroyer)(Citation: Risky Bulletin Threat actor impersonates FSB APT)(Citation: GamaCopy organization)

As with legitimate development efforts, different skill sets may be required for developing malware. The skills needed may be located in-house, or may need to be contracted out. Use of a contractor may be considered an extension of that adversary's malware development capabilities, provided the adversary plays a role in shaping requirements and maintains a degree of exclusivity to the malware.

Some aspects of malware development, such as C2 protocol development, may require adversaries to obtain additional infrastructure. For example, malware developed that will communicate with Twitter for C2, may require use of [[T1583-acquire_infrastructure#^t1583006-web-services|T1583.006: Web Services]].(Citation: FireEye APT29)

### T1587.002: Code Signing Certificates

^t1587002-code-signing-certificates

Adversaries may create self-signed code signing certificates that can be used during targeting. Code signing is the process of digitally signing executables and scripts to confirm the software author and guarantee that the code has not been altered or corrupted. Code signing provides a level of authenticity for a program from the developer and a guarantee that the program has not been tampered with.(Citation: Wikipedia Code Signing) Users and/or security tools may trust a signed piece of code more than an unsigned piece of code even if they don't know who issued the certificate or who the author is.

Prior to [[T1553-subvert_trust_controls#^t1553002-code-signing|T1553.002: Code Signing]], adversaries may develop self-signed code signing certificates for use in operations.

### T1587.003: Digital Certificates

^t1587003-digital-certificates

Adversaries may create self-signed SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner. In the case of self-signing, digital certificates will lack the element of trust associated with the signature of a third-party certificate authority (CA).

Adversaries may create self-signed SSL/TLS certificates that can be used to further their operations, such as encrypting C2 traffic (ex: [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]] with [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]) or even enabling [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]] if added to the root of trust (i.e. [[T1553-subvert_trust_controls#^t1553004-install-root-certificate|T1553.004: Install Root Certificate]]).

After creating a digital certificate, an adversary may then install that certificate (see [[T1608-stage_capabilities#^t1608003-install-digital-certificate|T1608.003: Install Digital Certificate]]) on infrastructure under their control.

### T1587.004: Exploits

^t1587004-exploits

Adversaries may develop exploits that can be used during targeting. An exploit takes advantage of a bug or vulnerability in order to cause unintended or unanticipated behavior to occur on computer hardware or software. Rather than finding/modifying exploits from online or purchasing them from exploit vendors, an adversary may develop their own exploits.(Citation: NYTStuxnet) Adversaries may use information acquired via [[T1588-obtain_capabilities#^t1588006-vulnerabilities|T1588.006: Vulnerabilities]] to focus exploit development efforts. As part of the exploit development process, adversaries may uncover exploitable vulnerabilities through methods such as fuzzing and patch analysis.(Citation: Irongeek Sims BSides 2017)

As with legitimate development efforts, different skill sets may be required for developing exploits. The skills needed may be located in-house, or may need to be contracted out. Use of a contractor may be considered an extension of that adversary's exploit development capabilities, provided the adversary plays a role in shaping requirements and maintains an initial degree of exclusivity to the exploit.

Adversaries may use exploits during various phases of the adversary lifecycle (i.e. [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]], [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]], [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]], [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]], [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]], [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]], and [[T1499-endpoint_denial_of_service#^t1499004-application-or-system-exploitation|T1499.004: Application or System Exploitation]]).

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

