---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RRID"
d3fend_name: "Reverse Resolution IP Denylisting"
d3fend_ontology_id: "d3f:ReverseResolutionIPDenylisting"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AReverseResolutionIPDenylisting/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1071"
  - "T1071.004"
  - "T1568"
  - "T1568.001"
  - "T1568.002"
  - "T1568.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Blocking a reverse lookup based on the query's IP address value.

## Workspace

- [[notes/defend/techniques/D3-RRID-reverse_resolution_ip_denylisting-note|Open workspace note]]

![[notes/defend/techniques/D3-RRID-reverse_resolution_ip_denylisting-note]]

## Parent Technique

- [[D3-DNSDL-dns_denylisting|D3-DNSDL: DNS Denylisting]]

## Related ATT&CK Techniques

- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution#^t1568001-fast-flux-dns|T1568.001: Fast Flux DNS]]
- [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1568-dynamic_resolution#^t1568003-dns-calculation|T1568.003: DNS Calculation]]

## Knowledge Base Article

## How it works
This technique prevents a client from learning domains deemed to be potentially malicious, which would have been delivered via reverse resolution responses over the DNS protocol.

Queries for reverse resolution requests (that is, requests where IP(s) are sent and a domain is returned) are collected, and the IP address(es) included in the query are examined. If the IP address(es) are in a range included in the blacklist, then the query is dropped.

## Considerations
- The blacklist will have to be maintained and will need to be kept up to date with identified maintenance cycles to ensure lists are not stale.
- DNS query traffic can be transmitted over many different protocols, which presents a challenge to implementing methods to extract all DNS query IP address value(s).
  - DNS has historically used UDP port 53, with TCP port 53 instead used for responses over 512 bytes or after a lack of response over UDP.
  - Usage of new protocols to provide confidentiality for DNS traffic, such as DoH (DNS over HTTPS) and DoT (DNS over TLS), complicates collection of the IP address(es) in DNS queries. These protocols have often been enabled in browser settings transparently after a browser update, with DNS queries proxied over one of these cryptographic protocols through a specified host.

## Ontology Relationships

- [[D3-DNSDL-dns_denylisting|D3-DNSDL: DNS Denylisting]]

