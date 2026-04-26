---
mitre_id: "T1657"
mitre_name: "Financial Theft"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--851e071f-208d-4c79-adc6-5974c85c78f3"
mitre_created: "2023-08-18T20:50:04.222Z"
mitre_modified: "2025-04-15T22:36:03.465Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1657/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0040"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware,(Citation: FBI-ransomware) business email compromise (BEC) and fraud,(Citation: FBI-BEC) "pig butchering,"(Citation: wired-pig butchering) bank hacking,(Citation: DOJ-DPRK Heist) and exploiting cryptocurrency networks.(Citation: BBC-Ronin) 

Adversaries may [[T1586-compromise_accounts|T1586: Compromise Accounts]] to conduct unauthorized transfers of funds.(Citation: Internet crime report 2022) In the case of business email compromise or email fraud, an adversary may utilize [[T1656-impersonation|T1656: Impersonation]] of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary.(Citation: FBI-BEC) This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft.(Citation: VEC)

Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]] (Citation: NYT-Colonial) and [[TA0010-exfiltration|TA0010: Exfiltration]] of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary.(Citation: Mandiant-leaks) Adversaries may use dedicated leak sites to distribute victim data.(Citation: Crowdstrike-leaks)

Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as [[T1485-data_destruction|T1485: Data Destruction]] and business disruption.(Citation: AP-NotPetya)

## Workspace

- [[workspaces/attack/techniques/T1657-financial_theft-note|Open workspace note]]

![[workspaces/attack/techniques/T1657-financial_theft-note]]

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1018-user_account_management|M1018: User Account Management]]

## Platforms

- Linux
- macOS
- Office Suite
- SaaS
- Windows

