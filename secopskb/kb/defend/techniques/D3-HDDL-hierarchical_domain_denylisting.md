---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-HDDL"
d3fend_name: "Hierarchical Domain Denylisting"
d3fend_ontology_id: "d3f:HierarchicalDomainDenylisting"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AHierarchicalDomainDenylisting/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Blocking the resolution of any subdomain of a specified domain name.

## Workspace

- [[workspaces/defend/techniques/D3-HDDL-hierarchical_domain_denylisting-note|Open workspace note]]

![[workspaces/defend/techniques/D3-HDDL-hierarchical_domain_denylisting-note]]

## Parent Technique

- [[D3-FRDDL-forward_resolution_domain_denylisting|D3-FRDDL: Forward Resolution Domain Denylisting]]

## Knowledge Base Article

## How it works
This technique is used to block DNS queries from related domains and subdomains that are unauthorized.

Hierarchical domain blacklisting considers the blacklisting of second level domains and additional sub-domains and specific hosts for a given query value. A denylist is maintained that contains DNS names and corresponding subdomains, including wildcards, that should be blocked for a given lookup.

## Considerations
* The denylist of domain names will have to be maintained and will need to be kept up to date
* Other domains that resolve to the domain of interest for blocking (CNAME, etc).
* Denylists should have identified maintenance cycles to ensure lists are not stale.

## Ontology Relationships

- [[D3-FRDDL-forward_resolution_domain_denylisting|D3-FRDDL: Forward Resolution Domain Denylisting]]

