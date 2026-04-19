---
id: T1048
name: Exfiltration Over Alternative Protocol
created: 2017-05-31 21:30:44.720000+00:00
modified: 2025-10-24 17:49:10.460000+00:00
type: attack-pattern
x_mitre_version: 1.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[exfiltration|Exfiltration]]

Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.  

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. 

[Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048) can be done using various common operating system utilities such as [Net](https://attack.mitre.org/software/S0039)/SMB or FTP.(Citation: Palo Alto OilRig Oct 2016) On macOS and Linux <code>curl</code> may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system.(Citation: 20 macOS Common Tools and Techniques)

Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or [Cloud API](https://attack.mitre.org/techniques/T1059/009).

## Properties

- id: T1048
- name: Exfiltration Over Alternative Protocol
- created: 2017-05-31 21:30:44.720000+00:00
- modified: 2025-10-24 17:49:10.460000+00:00
- type: attack-pattern
- x_mitre_version: 1.6
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol

^t1048001-exfiltration-over-symmetric-encrypted-non-c2-protocol

**Parent Technique**
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Symmetric encryption algorithms are those that use shared or the same keys/secrets on each end of the channel. This requires an exchange or pre-arranged agreement/possession of the value used to encrypt and decrypt data. 

Network protocols that use asymmetric encryption often utilize symmetric encryption once keys are exchanged, but adversaries may opt to manually share keys and implement symmetric cryptographic algorithms (ex: RC4, AES) vice using mechanisms that are baked into a protocol. This may result in multiple layers of encryption (in protocols that are natively encrypted such as HTTPS) or encryption in protocols that not typically encrypted (such as HTTP or FTP). 

#### Properties

- id: T1048.001
- name: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
- created: 2020-03-15 15:30:42.378000+00:00
- modified: 2025-10-24 17:48:59.332000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol

^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol

**Parent Technique**
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may steal data by exfiltrating it over an asymmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Asymmetric encryption algorithms are those that use different keys on each end of the channel. Also known as public-key cryptography, this requires pairs of cryptographic keys that can encrypt/decrypt data from the corresponding key. Each end of the communication channels requires a private key (only in the procession of that entity) and the public key of the other entity. The public keys of each entity are exchanged before encrypted communications begin. 

Network protocols that use asymmetric encryption (such as HTTPS/TLS/SSL) often utilize symmetric encryption once keys are exchanged. Adversaries may opt to use these encrypted mechanisms that are baked into a protocol. 

#### Properties

- id: T1048.002
- name: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- created: 2020-03-15 15:34:30.767000+00:00
- modified: 2025-10-24 17:49:05.552000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol

^t1048003-exfiltration-over-unencrypted-non-c2-protocol

**Parent Technique**
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.(Citation: copy_cmd_cisco)

Adversaries may opt to obfuscate this data, without the use of encryption, within network protocols that are natively unencrypted (such as HTTP, FTP, or DNS). This may include custom or publicly available encoding/compression algorithms (such as base64) as well as embedding data within protocol headers and fields. 

#### Properties

- id: T1048.003
- name: Exfiltration Over Unencrypted Non-C2 Protocol
- created: 2020-03-15 15:37:47.583000+00:00
- modified: 2025-10-24 17:49:39.079000+00:00
- type: attack-pattern
- x_mitre_version: 2.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Office Suite
- SaaS
- Windows

## Tools

- [[S0677-aadinternals|S0677: AADInternals]]

