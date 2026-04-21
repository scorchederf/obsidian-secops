---
id: T1188
name: Multi-hop Proxy
created: 2018-01-16 16:13:52.465000+00:00
modified: 2025-10-24 17:49:00.838000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

To disguise the source of malicious traffic, adversaries may chain together multiple proxies. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source.

## Platforms

- Linux
- macOS
- Windows

