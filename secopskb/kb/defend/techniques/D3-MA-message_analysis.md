---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-MA"
d3fend_name: "Message Analysis"
d3fend_ontology_id: "d3f:MessageAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AMessageAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Analyzing email or instant message content to detect unauthorized activity.

## Workspace

- [[workspaces/defend/techniques/D3-MA-message_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-MA-message_analysis-note]]

## Child Techniques

- [[D3-SMRA-sender_mta_reputation_analysis|D3-SMRA: Sender MTA Reputation Analysis]]
- [[D3-SRA-sender_reputation_analysis|D3-SRA: Sender Reputation Analysis]]

## Knowledge Base Article

## Technique Overview

Email and messaging are frequently used to deliver malicious content to targets. These enterprise capabilities are used to deliver software exploits or social engineering tricks. If the recipient of a message trusts the sender, attackers can avoid escalating suspicion.

Emails and messages are also complex data structures. They contain files and links, and complex data encodings which vary region to region. Thus the defensive techniques used to analyze emails and messages are highly varied ranging from deep content analysis and execution to social network graph-style analytics to analyze trust or risk.

