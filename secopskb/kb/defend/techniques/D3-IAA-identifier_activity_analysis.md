---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-IAA"
d3fend_name: "Identifier Activity Analysis"
d3fend_ontology_id: "d3f:IdentifierActivityAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AIdentifierActivityAnalysis/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Taking known malicious identifiers and determining if they are present in a system.

## Workspace

- [[workspaces/defend/techniques/D3-IAA-identifier_activity_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-IAA-identifier_activity_analysis-note]]

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

Identifier activity analysis is the process of taking identifiers--typically known malicious identifiers--and determining the artifacts that have interacted with those identifiers.

There are many open and closed source repositories of identifiers that represent indicators of compromise. For example, VirusTotal contains hash signatures of malware and IP Addresses used by threat actors. Defenders can search for these indicators of compromise their own systems to gain context on activity around an identifier.

## Considerations

Indicator activity analysis is a good way to gain high precision analysis, but adversaries can modify their own signatures such as hashes quickly to evade detection. This is related to David Bianco’s Pyramid of Pain - Indicators on the lower level (hash values, IP addresses domain names) are easy for adversaries to change.

Identifier activity data of interest for analysis with the identifier might include, but is not limited to:

* network traffic activity where the identifier was used to identify communicating entities or referred to in the communication
* process activity referencing the identifier, especially for resource access
* file activity referencing the identifier
* registry settings referencing the identifier

## Ontology Relationships

- [[D3-ID-identifier_analysis|D3-ID: Identifier Analysis]]

