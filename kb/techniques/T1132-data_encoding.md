---
id: T1132
name: Data Encoding
created: 2017-05-31 21:31:43.540000+00:00
modified: 2025-10-24 17:49:23.915000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) Some data encoding systems may also result in data compression, such as gzip.

## Subtechniques

### T1132.001: Standard Encoding

^t1132001-standard-encoding

**Parent Technique**
- [[T1132-data_encoding|T1132: Data Encoding]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may encode data with a standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system that adheres to existing protocol specifications. Common data encoding schemes include ASCII, Unicode, hexadecimal, Base64, and MIME.(Citation: Wikipedia Binary-to-text Encoding)(Citation: Wikipedia Character Encoding) Some data encoding systems may also result in data compression, such as gzip.

### T1132.002: Non-Standard Encoding

^t1132002-non-standard-encoding

**Parent Technique**
- [[T1132-data_encoding|T1132: Data Encoding]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may encode data with a non-standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a non-standard data encoding system that diverges from existing protocol specifications. Non-standard data encoding schemes may be based on or related to standard data encoding schemes, such as a modified Base64 encoding for the message body of an HTTP request.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) 

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- Linux
- macOS
- Windows
- ESXi

