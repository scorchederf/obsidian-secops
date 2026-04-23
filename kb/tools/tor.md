---
mitre_id: "S0183"
mitre_name: "Tor"
mitre_type: "tool"
mitre_stix_id: "tool--ed7d0cb1-87a6-43b4-9f46-ef1bc56d6c68"
mitre_created: "2018-01-16T16:13:52.465Z"
mitre_modified: "2025-09-29T20:22:30.453Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0183/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_aliases:
  - "Tor"
---

# Tor

[Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router)

## Uses Techniques

- [[T1090-proxy|T1090: Proxy]]
- [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
- [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

