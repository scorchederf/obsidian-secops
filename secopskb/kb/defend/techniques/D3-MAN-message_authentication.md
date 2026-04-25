---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-MAN"
d3fend_name: "Message Authentication"
d3fend_ontology_id: "d3f:MessageAuthentication"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AMessageAuthentication/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Authenticating the sender of a message and ensuring message integrity.

## Workspace

- [[notes/defend/techniques/D3-MAN-message_authentication-note|Open workspace note]]

![[notes/defend/techniques/D3-MAN-message_authentication-note]]

## Parent Technique

- [[D3-MH-message_hardening|D3-MH: Message Hardening]]

## Child Techniques

- [[D3-BMA-bus_message_authentication|D3-BMA: Bus Message Authentication]]

## Knowledge Base Article

## How it works

### Digital Signature
Digital signatures are used to verifying a message is from the expected sender. In email, Secure/Multipurpose Internet Mail Extensions (S/MIME) protocol is typically used to digitally sign messages. A hash value of the sender's message is created and encrypted with the sender's private key to create a digital signature. The message and the digital signature are sent to the recipient where the sender's public key is used to decrypt the digital signature and compute the hash of the message. The computed hash is compared with the hash from the received message, and any difference in the hash values signify the message did not originate from the sender and has been alerted in transit.

### Message Authentication Code (MAC)
MAC is a fixed size string that is appended to a message to provide message authentication and integrity. The sender MAC signing algorithm takes as input a secret symmetric key shared between sender and recipient and the message to calculate a short tag that is appended to the message. The recipient receives the message with the appended tag, and a MAC verification algorithm is run using the symmetric key to verify the message came from the stated sender and ensure the message has not been tampered with.

## Considerations
- Public keys associated with digital signatures should be verified by a Certification Authority (CA) to prevent impersonation. The CA verifies the owner of a public key and puts the sender's identity and public key into a certificate that is signed by the CA.
- Digital signatures provide non-repudiation where a third party can verify the authenticity of the message using the sender's digital certificate signed by the CA.
- Symmetric keys must be exchanged securely via a private channel and management of new symmetric keys are needed for each pair of participants wishing to exchange messages.

## Ontology Relationships

- [[D3-MH-message_hardening|D3-MH: Message Hardening]]

