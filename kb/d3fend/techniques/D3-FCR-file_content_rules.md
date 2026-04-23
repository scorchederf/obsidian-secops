---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FCR"
d3fend_name: "File Content Rules"
d3fend_ontology_id: "d3f:FileContentRules"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AFileContentRules/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-FCR: File Content Rules

Employing a pattern matching rule language to analyze the content of files.

## Parent Technique

- [[D3-FCOA-file_content_analysis|D3-FCOA: File Content Analysis]]

## Knowledge Base Article

## How it works
Rules, often called signatures, are used for both generic and targeted malware detection. The rules are usually expressed in a domain specific language (DSL), then deployed to software that scans files for matches. The rules are developed and broadly distributed by commercial vendors, or they are developed and deployed by enterprise security teams to address highly targeted or custom malware. Conceptually, there are public and private rule sets. Both leverage the same technology, but they are intended to detect different types of cyber adversaries.

## Considerations
* Patterns expressed in the DSLs range in their complexity. Some scanning engines support file parsing and normalization for high fidelity matching, others support only simple regular expression matching against raw file data. Engineers must make a trade-off in terms of:
     * The fidelity of the matching capabilities in order to balance high recall with avoiding false positives,
     * The computational load for scanning, and
     * The resilience of the engine to deal with adversarial content presented in different forms-- content which in some cases is designed to exploit or defeat the scanning engines.
 * Signature libraries can become large over time and impact scanning performance.
 * Some vendors who sell signatures have to delete old signatures over time.
 * Simple signatures against raw content cannot match against encoded, encrypted, or sufficiently obfuscated content.

## Implementations
 * YARA
 * ClamAV

## Ontology Relationships

- [[D3-FCOA-file_content_analysis|D3-FCOA: File Content Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-fcr-notes|Open workspace note]]

