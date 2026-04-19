---
id: S0183
name: Tor
created: 2018-01-16 16:13:52.465000+00:00
modified: 2025-09-29 20:22:30.453000+00:00
type: tool
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

# Tor

[Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router)

## Properties

- id: S0183
- name: Tor
- created: 2018-01-16 16:13:52.465000+00:00
- modified: 2025-09-29 20:22:30.453000+00:00
- type: tool
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1090-proxy|T1090: Proxy]]
    - [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

