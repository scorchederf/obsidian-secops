---
mitre_id: "T1600"
mitre_name: "Weaken Encryption"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1f9012ef-1e10-4e48-915e-e03563435fe8"
mitre_created: "2020-10-19T18:47:08.759Z"
mitre_modified: "2025-10-24T17:48:30.124Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1600/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Network Devices"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would otherwise protect data communications. (Citation: Cisco Synful Knock Evolution)

Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer keys increase the cost of cryptanalysis, or decryption without the key.

Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors such as [[T1601-modify_system_image|T1601: Modify System Image]], [[T1600-weaken_encryption#^t1600001-reduce-key-space|T1600.001: Reduce Key Space]], and [[T1600-weaken_encryption#^t1600002-disable-crypto-hardware|T1600.002: Disable Crypto Hardware]], an adversary can negatively effect and/or eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and may help facilitate data manipulation, Credential Access, or Collection efforts. (Citation: Cisco Blog Legacy Device Attacks)

## Workspace

- [[workspaces/attack/techniques/T1600-weaken_encryption-note|Open workspace note]]

![[workspaces/attack/techniques/T1600-weaken_encryption-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Subtechniques

### T1600.001: Reduce Key Space

^t1600001-reduce-key-space

Adversaries may reduce the level of effort required to decrypt data transmitted over the network by reducing the cipher strength of encrypted communications.(Citation: Cisco Synful Knock Evolution)

Adversaries can weaken the encryption software on a compromised network device by reducing the key size used by the software to convert plaintext to ciphertext (e.g., from hundreds or thousands of bytes to just a couple of bytes). As a result, adversaries dramatically reduce the amount of effort needed to decrypt the protected information without the key.

Adversaries may modify the key size used and other encryption parameters using specialized commands in a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] introduced to the system through [[T1601-modify_system_image|T1601: Modify System Image]] to change the configuration of the device. (Citation: Cisco Blog Legacy Device Attacks)

### T1600.002: Disable Crypto Hardware

^t1600002-disable-crypto-hardware

Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weaknesses in software encryption in order to reduce the effort involved in collecting, manipulating, and exfiltrating transmitted data.

Many network devices such as routers, switches, and firewalls, perform encryption on network traffic to secure transmission across networks. Often, these devices are equipped with special, dedicated encryption hardware to greatly increase the speed of the encryption process as well as to prevent malicious tampering. When an adversary takes control of such a device, they may disable the dedicated hardware, for example, through use of [[T1601-modify_system_image|T1601: Modify System Image]], forcing the use of software to perform encryption on general processors. This is typically used in conjunction with attacks to weaken the strength of the cipher in software (e.g., [[T1600-weaken_encryption#^t1600001-reduce-key-space|T1600.001: Reduce Key Space]]). (Citation: Cisco Blog Legacy Device Attacks)

## Platforms

- Network Devices

