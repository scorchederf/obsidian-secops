---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FRDDL"
d3fend_name: "Forward Resolution Domain Denylisting"
d3fend_ontology_id: "d3f:ForwardResolutionDomainDenylisting"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AForwardResolutionDomainDenylisting/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Blocking a lookup based on the query's domain name value.

## Workspace

- [[workspaces/defend/techniques/D3-FRDDL-forward_resolution_domain_denylisting-note|Open workspace note]]

![[workspaces/defend/techniques/D3-FRDDL-forward_resolution_domain_denylisting-note]]

## Parent Technique

- [[D3-DNSDL-dns_denylisting|D3-DNSDL: DNS Denylisting]]

## Child Techniques

- [[D3-HDDL-hierarchical_domain_denylisting|D3-HDDL: Hierarchical Domain Denylisting]]
- [[D3-HDL-homoglyph_denylisting|D3-HDL: Homoglyph Denylisting]]

## Related ATT&CK Techniques

- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution#^t1568001-fast-flux-dns|T1568.001: Fast Flux DNS]]
- [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1568-dynamic_resolution#^t1568003-dns-calculation|T1568.003: DNS Calculation]]

## Knowledge Base Article

## How it works

Policies are created that filter DNS queries using fully qualified domain name (FQDN) of record in the query. A DNS policy can be created for blocking DNS queries from FQDNs that have been identified as unauthorized.

## Considerations

Continuous maintenance of unauthorized domain lists is needed to keep up to date as updates occur.

## Ontology Relationships

- [[D3-DNSDL-dns_denylisting|D3-DNSDL: DNS Denylisting]]

