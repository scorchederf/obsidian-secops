---
id: T1600
name: Weaken Encryption
created: 2020-10-19 18:47:08.759000+00:00
modified: 2025-10-24 17:48:30.124000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would otherwise protect data communications. (Citation: Cisco Synful Knock Evolution)

Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer keys increase the cost of cryptanalysis, or decryption without the key.

Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors such as [Modify System Image](https://attack.mitre.org/techniques/T1601), [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001), and [Disable Crypto Hardware](https://attack.mitre.org/techniques/T1600/002), an adversary can negatively effect and/or eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and may help facilitate data manipulation, Credential Access, or Collection efforts. (Citation: Cisco Blog Legacy Device Attacks)

## Properties

- id: T1600
- name: Weaken Encryption
- created: 2020-10-19 18:47:08.759000+00:00
- modified: 2025-10-24 17:48:30.124000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1600.001: Reduce Key Space

^t1600001-reduce-key-space

**Parent Technique**
- [[T1600-weaken_encryption|T1600: Weaken Encryption]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may reduce the level of effort required to decrypt data transmitted over the network by reducing the cipher strength of encrypted communications.(Citation: Cisco Synful Knock Evolution)

Adversaries can weaken the encryption software on a compromised network device by reducing the key size used by the software to convert plaintext to ciphertext (e.g., from hundreds or thousands of bytes to just a couple of bytes). As a result, adversaries dramatically reduce the amount of effort needed to decrypt the protected information without the key.

Adversaries may modify the key size used and other encryption parameters using specialized commands in a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) introduced to the system through [Modify System Image](https://attack.mitre.org/techniques/T1601) to change the configuration of the device. (Citation: Cisco Blog Legacy Device Attacks)

#### Properties

- id: T1600.001
- name: Reduce Key Space
- created: 2020-10-19 19:03:48.310000+00:00
- modified: 2025-10-24 17:48:40.223000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1600.002: Disable Crypto Hardware

^t1600002-disable-crypto-hardware

**Parent Technique**
- [[T1600-weaken_encryption|T1600: Weaken Encryption]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weaknesses in software encryption in order to reduce the effort involved in collecting, manipulating, and exfiltrating transmitted data.

Many network devices such as routers, switches, and firewalls, perform encryption on network traffic to secure transmission across networks. Often, these devices are equipped with special, dedicated encryption hardware to greatly increase the speed of the encryption process as well as to prevent malicious tampering. When an adversary takes control of such a device, they may disable the dedicated hardware, for example, through use of [Modify System Image](https://attack.mitre.org/techniques/T1601), forcing the use of software to perform encryption on general processors. This is typically used in conjunction with attacks to weaken the strength of the cipher in software (e.g., [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001)). (Citation: Cisco Blog Legacy Device Attacks)

#### Properties

- id: T1600.002
- name: Disable Crypto Hardware
- created: 2020-10-19 19:11:18.757000+00:00
- modified: 2025-10-24 17:49:01.374000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- Network Devices

