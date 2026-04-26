---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DNSTA"
d3fend_name: "DNS Traffic Analysis"
d3fend_ontology_id: "d3f:DNSTrafficAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADNSTrafficAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1040"
  - "T1071"
  - "T1071.004"
  - "T1568"
  - "T1568.001"
  - "T1568.002"
  - "T1568.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Analysis of domain name metadata, including name and DNS records, to determine whether the domain is likely to resolve to an undesirable host.

## Workspace

- [[workspaces/defend/techniques/D3-DNSTA-dns_traffic_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DNSTA-dns_traffic_analysis-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Related ATT&CK Techniques

- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution#^t1568001-fast-flux-dns|T1568.001: Fast Flux DNS]]
- [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1568-dynamic_resolution#^t1568003-dns-calculation|T1568.003: DNS Calculation]]

## Knowledge Base Article

## How it works
This technique can be accomplished in a number of ways.

* One example analytic determines whether or not a domain name was generated with an algorithm. Domain generation algorithms (DGAs) are sometimes used to create a domain name automatically  that will resolve to C2 infrastructure, without directly coding the domains in question into the malicious code.
* Another method analyzes information about domains that have been visited, including whether a domain name is longer than a common length,  if a dynamic DNS domain was visited, if a fast-flux domain was visited, and if a recently created domain was visited. These factors are used to develop a score and if that score is over a certain threshold, an alert is generated.
* Collected malware samples can be executed in a virtual environment to identify network domains that are connected to during execution. The network domains are then generated into signatures to identity bad domains for other hosts.

This technique does not check for content hosted at the domain.

## Considerations

* DNS produces a large amount of traffic which can be resource-intensive to analyze in real time.
* If a server is compromised, for example, as part of a watering hole attack, but the DNS information pointing to that server is not altered, this technique would not catch such an incident.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

