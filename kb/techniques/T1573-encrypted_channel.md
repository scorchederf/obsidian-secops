---
id: T1573
name: Encrypted Channel
created: 2020-03-16 15:33:01.739000+00:00
modified: 2025-10-24 17:49:17.042000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

## Subtechniques

### T1573.001: Symmetric Cryptography

^t1573001-symmetric-cryptography

Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key for plaintext encryption and ciphertext decryption. Common symmetric encryption algorithms include AES, DES, 3DES, Blowfish, and RC4.

### T1573.002: Asymmetric Cryptography

^t1573002-asymmetric-cryptography

Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Asymmetric cryptography, also known as public key cryptography, uses a keypair per party: one public that can be freely distributed, and one private. Due to how the keys are generated, the sender encrypts data with the receiver’s public key and the receiver decrypts the data with their private key. This ensures that only the intended recipient can read the encrypted data. Common public key encryption algorithms include RSA and ElGamal.

For efficiency, many protocols (including SSL/TLS) use symmetric cryptography once a connection is established, but use asymmetric cryptography to establish or transmit a key. As such, these protocols are classified as [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002).

## Mitigations

- [[M1020-ssl_tls_inspection|M1020: SSL/TLS Inspection]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

