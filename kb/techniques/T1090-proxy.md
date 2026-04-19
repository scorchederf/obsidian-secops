---
id: T1090
name: Proxy
created: 2017-05-31 21:31:08.479000+00:00
modified: 2025-10-24 17:48:57.330000+00:00
type: attack-pattern
x_mitre_version: 3.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries may chain together multiple proxies to further disguise the source of malicious traffic.

Adversaries can also take advantage of routing schemes in Content Delivery Networks (CDNs) to proxy command and control traffic.

## Subtechniques

### T1090.001: Internal Proxy

^t1090001-internal-proxy

**Parent Technique**
- [[T1090-proxy|T1090: Proxy]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may use an internal proxy to direct command and control traffic between two or more systems in a compromised environment. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use internal proxies to manage command and control communications inside a compromised environment, to reduce the number of simultaneous outbound network connections, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between infected systems to avoid suspicion. Internal proxy connections may use common peer-to-peer (p2p) networking protocols, such as SMB, to better blend in with the environment.

By using a compromised internal system as a proxy, adversaries may conceal the true destination of C2 traffic while reducing the need for numerous connections to external systems.

### T1090.002: External Proxy

^t1090002-external-proxy

**Parent Technique**
- [[T1090-proxy|T1090: Proxy]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may use an external proxy to act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths to avoid suspicion.

External connection proxies are used to mask the destination of C2 traffic and are typically implemented with port redirectors. Compromised systems outside of the victim environment may be used for these purposes, as well as purchased infrastructure such as cloud-based resources or virtual private servers. Proxies may be chosen based on the low likelihood that a connection to them from a compromised system would be investigated. Victim systems would communicate directly with the external proxy on the Internet and then the proxy would forward communications to the C2 server.

### T1090.003: Multi-hop Proxy

^t1090003-multi-hop-proxy

**Parent Technique**
- [[T1090-proxy|T1090: Proxy]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may chain together multiple proxies to disguise the source of malicious traffic. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source.

For example, adversaries may construct or use onion routing networks – such as the publicly available [Tor](https://attack.mitre.org/software/S0183) network – to transport encrypted C2 traffic through a compromised population, allowing communication with any device within the network.(Citation: Onion Routing) Adversaries may also use operational relay box (ORB) networks composed of virtual private servers (VPS), Internet of Things (IoT) devices, smart devices, and end-of-life routers to obfuscate their operations.(Citation: ORB Mandiant) 

In the case of network infrastructure, it is possible for an adversary to leverage multiple compromised devices to create a multi-hop proxy chain (i.e., [Network Devices](https://attack.mitre.org/techniques/T1584/008)). By leveraging [Patch System Image](https://attack.mitre.org/techniques/T1601/001) on routers, adversaries can add custom code to the affected network devices that will implement onion routing between those nodes. This method is dependent upon the [Network Boundary Bridging](https://attack.mitre.org/techniques/T1599) method allowing the adversaries to cross the protected network boundary of the Internet perimeter and into the organization’s Wide-Area Network (WAN).  Protocols such as ICMP may be used as a transport.  

Similarly, adversaries may abuse peer-to-peer (P2P) and blockchain-oriented infrastructure to implement routing between a decentralized network of peers.(Citation: NGLite Trojan)

### T1090.004: Domain Fronting

^t1090004-domain-fronting

**Parent Technique**
- [[T1090-proxy|T1090: Proxy]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may take advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. (Citation: Fifield Blocking Resistent Communication through domain fronting 2015) Domain fronting involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. If both domains are served from the same CDN, then the CDN may route to the address specified in the HTTP header after unwrapping the TLS header. A variation of the the technique, "domainless" fronting, utilizes a SNI field that is left blank; this may allow the fronting to work even when the CDN attempts to validate that the SNI and HTTP Host fields match (if the blank SNI fields are ignored).

For example, if domain-x and domain-y are customers of the same CDN, it is possible to place domain-x in the TLS header and domain-y in the HTTP header. Traffic will appear to be going to domain-x, however the CDN may route it to domain-y.

## Mitigations

- [[M1020-ssl_tls_inspection|M1020: SSL/TLS Inspection]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

