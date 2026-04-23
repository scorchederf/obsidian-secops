---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-MENCR"
d3fend_name: "Message Encryption"
d3fend_ontology_id: "d3f:MessageEncryption"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AMessageEncryption/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-MENCR: Message Encryption

Encrypting a message body using a cryptographic key.

## Parent Technique

- [[D3-MH-message_hardening|D3-MH: Message Hardening]]

## Knowledge Base Article

## How it works

### Asymmetric Cryptography
Asymmetric encryption is typically accomplished using public and private key certificates based on the X.509 standard. The sender encrypts messages using the recipient's public key and the receipt decrypts the message using their private key. Standards that can be used to implement user message encryption include S/MIME (Secure/Multipurpose Internet Mail Extensions) and PGP.

### Symmetric Cryptography
Symmetric encryption uses the same cryptographic key by both the sender and receiver to encrypt and decrypt a message. Asymmetric key exchange protocols such as Diffie-Hellman can be used to share the cryptographic key with the recipient. For synchronous or low-latency environments (like a message bus), a pre-shared or dynamically derived symmetric key is typically used to minimize computational overhead.

## Considerations
- Separate configuration settings to enable message encryption are often needed for each messenger client (e.g. webmail, desktop client, mobile).
- Continuous monitoring to ensure private keys are not compromised and the certificate authority (CA) is trusted.
- Secure transfer of private keys between multiple devices.
- Encryption adds latency and increases CPU utilization; while negligible for user-to-user messages, it can be a critical factor for real-time bus systems.

## Ontology Relationships

- [[D3-MH-message_hardening|D3-MH: Message Hardening]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-mencr-notes|Open workspace note]]

