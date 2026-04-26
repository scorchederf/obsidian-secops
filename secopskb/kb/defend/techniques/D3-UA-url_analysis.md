---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-UA"
d3fend_name: "URL Analysis"
d3fend_ontology_id: "d3f:URLAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AURLAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1189"
  - "T1204"
  - "T1204.001"
  - "T1566"
  - "T1566.002"
  - "T1566.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Determining if a URL is benign or malicious by analyzing the URL or its components.

## Workspace

- [[workspaces/defend/techniques/D3-UA-url_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-UA-url_analysis-note]]

## Parent Technique

- [[D3-ID-identifier_analysis|D3-ID: Identifier Analysis]]

## Related ATT&CK Techniques

- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
- [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]

## Knowledge Base Article

## How it works

URLs may contain components, for example:

 * scheme
 * userinfo
 * host name
 * port
 * path
 * query
 * fragment

These components are used as features in analysis algorithms.

Contextual information about a URL such as where it is embedded (ex. emails, files, network protocols), header, path, location, and origin information, as well as information about the content returned from the URL request, may be incorporated into an analytic for URL analysis. For example, if a URL indicates a .pdf file but an executable is actually returned, the combination of these two pieces of information indicates suspicious activity.

Additional techniques include:

* Extracting features of a URL such as domain name length, ratio of consecutive consonants, percentage of digits in a domain, and number of vowels. Values for each feature are combined to develop a score for the URL.
* Determining the probability of a character occurring in the URL given the preceding two characters. For example, for google.com, the probability of a 'g' occurring at the beginning of a word, the probability of an 'o' occurring after a "g, the probability of an o" occurring after a 'g' and "o, and so forth. A dictionary or a list of known good domains is used to determine probability. Probabilities are multiplied to develop a score for the URL.

URL analysis may trigger follow-on analytics such as **File Analysis**

## Considerations

* Volume of URLs being analyzed, combined with the speed at which they are analyzed
* Fidelity of analysis technique at detecting brand new URLs versus analyzing URLs of established domains

## Ontology Relationships

- [[D3-ID-identifier_analysis|D3-ID: Identifier Analysis]]

