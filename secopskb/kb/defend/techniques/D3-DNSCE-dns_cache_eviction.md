---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DNSCE"
d3fend_name: "DNS Cache Eviction"
d3fend_ontology_id: "d3f:DNSCacheEviction"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADNSCacheEviction/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Flushing DNS to clear any IP addresses or other DNS records from the cache.

## Workspace

- [[notes/defend/techniques/D3-DNSCE-dns_cache_eviction-note|Open workspace note]]

![[notes/defend/techniques/D3-DNSCE-dns_cache_eviction-note]]

## Parent Technique

- [[D3-OE-object_eviction|D3-OE: Object Eviction]]

## Knowledge Base Article

# How it works

Flushing the DNS Cache will clear the IP addresses of websites you have visited recently. This can help remediate DNS Cache Poisoning attacks, which is a type of cyber attack where corrupted DNS data is inserted into the cache, causing redirects to malicious websites.

On windows, the DNS cache can be wiped by issuing the command `ipconfig /flushdns`.

## Ontology Relationships

- [[D3-OE-object_eviction|D3-OE: Object Eviction]]

