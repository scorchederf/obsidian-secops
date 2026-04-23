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
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-HDDL: Hierarchical Domain Denylisting

Blocking the resolution of any subdomain of a specified domain name.

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

## Workspace

- [[kb/notes/d3fend/techniques/d3-hddl-notes|Open workspace note]]

