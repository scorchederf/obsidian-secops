---
id: T1145
name: Private Keys
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:49.203000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[credential_access|Credential Access]]

Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures. (Citation: Wikipedia Public Key Crypto)

Adversaries may gather private keys from compromised systems for use in authenticating to [Remote Services](https://attack.mitre.org/techniques/T1021) like SSH or for use in decrypting other collected files such as email. Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. Adversaries may also look in common key directories, such as <code>~/.ssh</code> for SSH keys on * nix-based systems or <code>C:\Users\(username)\.ssh\</code> on Windows.

Private keys should require a password or passphrase for operation, so an adversary may also use [Input Capture](https://attack.mitre.org/techniques/T1056) for keylogging or attempt to [Brute Force](https://attack.mitre.org/techniques/T1110) the passphrase off-line.

Adversary tools have been discovered that search compromised systems for file extensions relating to cryptographic keys and certificates. (Citation: Kaspersky Careto) (Citation: Palo Alto Prince of Persia)

## Platforms

- Linux
- macOS
- Windows

