---
id: T1001
name: Data Obfuscation
created: 2017-05-31 21:30:18.931000+00:00
modified: 2025-10-24 17:49:13.380000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may obfuscate command and control traffic to make it more difficult to detect.(Citation: Bitdefender FunnyDream Campaign November 2020) Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, or impersonating legitimate protocols. 

## Properties

- id: T1001
- name: Data Obfuscation
- created: 2017-05-31 21:30:18.931000+00:00
- modified: 2025-10-24 17:49:13.380000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1001.001: Junk Data

^t1001001-junk-data

**Parent Technique**
- [[T1001-data_obfuscation|T1001: Data Obfuscation]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may add junk data to protocols used for command and control to make detection more difficult.(Citation: FireEye SUNBURST Backdoor December 2020) By adding random or meaningless data to the protocols used for command and control, adversaries can prevent trivial methods for decoding, deciphering, or otherwise analyzing the traffic. Examples may include appending/prepending data with junk characters or writing junk characters between significant characters. 

#### Properties

- id: T1001.001
- name: Junk Data
- created: 2020-03-15 00:30:25.444000+00:00
- modified: 2025-10-24 17:49:38.011000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1001.002: Steganography

^t1001002-steganography

**Parent Technique**
- [[T1001-data_obfuscation|T1001: Data Obfuscation]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may use steganographic techniques to hide command and control traffic to make detection efforts more difficult. Steganographic techniques can be used to hide data in digital messages that are transferred between systems. This hidden information can be used for command and control of compromised systems. In some cases, the passing of files embedded using steganography, such as image or document files, can be used for command and control. 

#### Properties

- id: T1001.002
- name: Steganography
- created: 2020-03-15 00:37:58.963000+00:00
- modified: 2025-10-24 17:49:35.060000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1001.003: Protocol or Service Impersonation

^t1001003-protocol-or-service-impersonation

**Parent Technique**
- [[T1001-data_obfuscation|T1001: Data Obfuscation]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activity and thwart analysis efforts. By impersonating legitimate protocols or web services, adversaries can make their command and control traffic blend in with legitimate network traffic.  

Adversaries may impersonate a fake SSL/TLS handshake to make it look like subsequent traffic is SSL/TLS encrypted, potentially interfering with some security tooling, or to make the traffic look like it is related with a trusted entity. 

Adversaries may also leverage legitimate protocols to impersonate expected web traffic or trusted services. For example, adversaries may manipulate HTTP headers, URI endpoints, SSL certificates, and transmitted data to disguise C2 communications or mimic legitimate services such as Gmail, Google Drive, and Yahoo Messenger.(Citation: ESET Okrum July 2019)(Citation: Malleable-C2-U42)

#### Properties

- id: T1001.003
- name: Protocol or Service Impersonation
- created: 2020-03-15 00:40:27.503000+00:00
- modified: 2025-10-24 17:49:20.574000+00:00
- type: attack-pattern
- x_mitre_version: 2.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

## Tools


