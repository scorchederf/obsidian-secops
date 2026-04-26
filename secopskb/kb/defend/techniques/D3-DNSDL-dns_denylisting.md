---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DNSDL"
d3fend_name: "DNS Denylisting"
d3fend_ontology_id: "d3f:DNSDenylisting"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADNSDenylisting/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1071"
  - "T1071.004"
  - "T1568"
  - "T1568.001"
  - "T1568.002"
  - "T1568.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Blocking DNS Network Traffic based on criteria such as IP address, domain name, or DNS query type.

## Workspace

- [[workspaces/defend/techniques/D3-DNSDL-dns_denylisting-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DNSDL-dns_denylisting-note]]

## Parent Technique

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

## Child Techniques

- [[D3-FRDDL-forward_resolution_domain_denylisting|D3-FRDDL: Forward Resolution Domain Denylisting]]
- [[D3-FRIDL-forward_resolution_ip_denylisting|D3-FRIDL: Forward Resolution IP Denylisting]]
- [[D3-RRID-reverse_resolution_ip_denylisting|D3-RRID: Reverse Resolution IP Denylisting]]

## Related ATT&CK Techniques

- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution#^t1568001-fast-flux-dns|T1568.001: Fast Flux DNS]]
- [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1568-dynamic_resolution#^t1568003-dns-calculation|T1568.003: DNS Calculation]]

## Knowledge Base Article

## How it works
Rules are implemented that filter DNS queries using criteria such as:
- Client subnet
- Type of network protocol used in query
- Fully qualified domain name (FQDN) of record in the query
- DNS Server IP address that received the DNS request
- Type of DNS record being queried
- Time of day the query is received
- Size of the response

For example, a DNS policy can be created for blocking DNS queries for FQDNs that have been identified as unauthorized.

## Considerations
- Implementation considerations for DNS filtering policies to avoid over-blocking or under-blocking domains.
- Continuous maintenance of unauthorized domain lists is needed to keep up to date with possible site content changes.
- File sharing or content delivery networks may require other filtering techniques that are more fine-grained (URL blocking).
- Access to malicious websites or other network resources directly by IP instead of by DNS record, or after alteration of local DNS hosts file, may not result in DNS network traffic.

## Ontology Relationships

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

