---
mitre_id: "T1650"
mitre_name: "Acquire Access"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d21bb61f-08ad-4dc1-b001-81ca6cb79954"
mitre_created: "2023-03-10T15:37:21.782Z"
mitre_modified: "2025-10-24T17:49:25.997Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1650/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0042"
---

# T1650: Acquire Access

Adversaries may purchase or otherwise acquire an existing access to a target system or network. A variety of online services and initial access broker networks are available to sell access to previously compromised systems.(Citation: Microsoft Ransomware as a Service)(Citation: CrowdStrike Access Brokers)(Citation: Krebs Access Brokers Fortune 500) In some cases, adversary groups may form partnerships to share compromised systems with each other.(Citation: CISA Karakurt 2022)

Footholds to compromised systems may take a variety of forms, such as access to planted backdoors (e.g., [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]) or established access via [[T1133-external_remote_services|T1133: External Remote Services]]. In some cases, access brokers will implant compromised systems with a “load” that can be used to install additional malware for paying customers.(Citation: Microsoft Ransomware as a Service)

By leveraging existing access broker networks rather than developing or obtaining their own initial access capabilities, an adversary can potentially reduce the resources required to gain a foothold on a target network and focus their efforts on later stages of compromise. Adversaries may prioritize acquiring access to systems that have been determined to lack security monitoring or that have high privileges, or systems that belong to organizations in a particular sector.(Citation: Microsoft Ransomware as a Service)(Citation: CrowdStrike Access Brokers)

In some cases, purchasing access to an organization in sectors such as IT contracting, software development, or telecommunications may allow an adversary to compromise additional victims via a [[T1199-trusted_relationship|T1199: Trusted Relationship]], [[T1111-multi-factor_authentication_interception|T1111: Multi-Factor Authentication Interception]], or even [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]].

**Note:** while this technique is distinct from other behaviors such as [[T1597-search_closed_sources#^t1597002-purchase-technical-data|T1597.002: Purchase Technical Data]] and [[T1589-gather_victim_identity_information#^t1589001-credentials|T1589.001: Credentials]], they may often be used in conjunction (especially where the acquired foothold requires [[T1078-valid_accounts|T1078: Valid Accounts]]).

## Tactics

- [[TA0042-resource_development|TA0042: Resource Development]]

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

