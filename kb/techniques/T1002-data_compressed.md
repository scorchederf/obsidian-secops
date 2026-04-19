---
id: T1002
name: Data Compressed
created: 2017-05-31 21:30:19.338000+00:00
modified: 2025-10-24 17:49:17.460000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[exfiltration|Exfiltration]]

An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration in order to make it portable and minimize the amount of data sent over the network. The compression is done separately from the exfiltration channel and is performed using a custom program or algorithm, or a more common compression library or utility such as 7zip, RAR, ZIP, or zlib.

## Platforms

- Linux
- Windows
- macOS

