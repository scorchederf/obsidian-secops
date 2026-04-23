---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-HDL"
d3fend_name: "Homoglyph Denylisting"
d3fend_ontology_id: "d3f:HomoglyphDenylisting"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AHomoglyphDenylisting/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-HDL: Homoglyph Denylisting

Blocking DNS queries that are deceptively similar to legitimate domain names.

## Parent Technique

- [[D3-FRDDL-forward_resolution_domain_denylisting|D3-FRDDL: Forward Resolution Domain Denylisting]]

## Knowledge Base Article

## How it works

Homoglyph domain blacklisting considers the domain and subdomain structure of a lookup and compares the named components to blacklisted named components. The blacklisted named components are typically crafted modifications of known good domains, e.g., gooogle.com versus google.com. The blacklisted domains typically resemble trusted domains, but have been altered slightly to deceive users.

The blacklisted named components also include consideration for fonts or Unicode characters that can make certain characters appear very similar (zero vs capital O and the letter l vs the number one). The blacklisted domains under certain fonts will appear to be a trusted domain.

## Considerations
* Maintaining the currency of the list can be a challenge especially with newly registered domain entries.
* Blacklists should have identified maintenance cycles to ensure lists are not stale.

## Ontology Relationships

- [[D3-FRDDL-forward_resolution_domain_denylisting|D3-FRDDL: Forward Resolution Domain Denylisting]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-hdl-notes|Open workspace note]]

