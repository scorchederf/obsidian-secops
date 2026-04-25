---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SRA"
d3fend_name: "Sender Reputation Analysis"
d3fend_ontology_id: "d3f:SenderReputationAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASenderReputationAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1114"
  - "T1114.001"
  - "T1534"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Ascertaining sender reputation based on information associated with a message (e.g. email/instant messaging).

## Workspace

- [[notes/defend/techniques/D3-SRA-sender_reputation_analysis-note|Open workspace note]]

![[notes/defend/techniques/D3-SRA-sender_reputation_analysis-note]]

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

Sender trust rating can be considered an indicator of the level of security risk and/or a trust level associated with a sender. The features considered in determining the trust rating include:

* Length of time sender has sent emails to the enterprise
* Number of recipients in the enterprise the sender interacts with
* Sender vs. enterprise originated message ratio
* Sender messages opened vs. not-opened ratio
* Number of emails received from this sender
* Number of emails replied to this sender
* Number of emails from this sender not opened
* Number of emails from this sender not opened that contain an attachment
* Number of emails from this sender not opened that contain a URL
* Number of emails sent to this sender
* Number of email replies received from this sender.

Higher values for the number of recipients the sender has interacted with or the number of emails received from the sender, for example, results in a higher trust rating. The trust rating can categorize the sender as unrated, neutral, trusted, suspicious, or malicious.

## Considerations
Legitimate emails from a sender may receive a lower trust rating over time if the sender's domain gets spoofed and is used to send unauthorized emails.

## Ontology Relationships

- [[D3-MA-message_analysis|D3-MA: Message Analysis]]

