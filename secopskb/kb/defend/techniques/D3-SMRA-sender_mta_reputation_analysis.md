---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SMRA"
d3fend_name: "Sender MTA Reputation Analysis"
d3fend_ontology_id: "d3f:SenderMTAReputationAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASenderMTAReputationAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1114"
  - "T1114.001"
  - "T1534"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Characterizing the reputation of mail transfer agents (MTA) to determine the security risk in emails.

## Workspace

- [[workspaces/defend/techniques/D3-SMRA-sender_mta_reputation_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SMRA-sender_mta_reputation_analysis-note]]

## Parent Technique

- [[D3-MA-message_analysis|D3-MA: Message Analysis]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
- [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]

## Knowledge Base Article

## How it works
The sender message transfer agent (MTA) trust rating can be considered an indicator of the level of security risk and/or a trust level associated with sender MTAs in an email header.

The features considered in determining the trust rating may include:

* Length of time MTA has interacted with the enterprise
* Number of sender domains sending emails from the MTA
* Number of recipients in the enterprise the MTA sends emails to
* Number of emails received from this MTA
* Number of email replies received from this MTA

For example, higher values for the length of time an MTA has interacted with the enterprise, or number of emails received from an MTA can result in a higher trust rating. The trust rating categorizes the sender MTA as unrated, neutral, trusted, suspicious, or malicious.

## Considerations
Legitimate emails from a sender MTA may receive a lower trust rating over time if the sender's domain gets spoofed and is used to send unauthorized emails.

## Ontology Relationships

- [[D3-MA-message_analysis|D3-MA: Message Analysis]]

