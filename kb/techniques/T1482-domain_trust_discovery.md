---
mitre_id: "T1482"
mitre_name: "Domain Trust Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--767dbf9e-df3f-45cb-8998-4903ab5f80c0"
mitre_created: "2019-02-14T16:15:05.974Z"
mitre_modified: "2025-10-24T17:48:58.061Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1482/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1482: Domain Trust Discovery

Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.(Citation: Microsoft Trusts) Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct [[T1134-access_token_manipulation#^t1134005-sid-history-injection|T1134.005: SID-History Injection]], [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]], and [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]].(Citation: AdSecurity Forging Trust Tickets)(Citation: Harmj0y Domain Trusts) Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP.(Citation: Harmj0y Domain Trusts) The Windows utility [[nltest|Nltest]] is known to be used by adversaries to enumerate domain trusts.(Citation: Microsoft Operation Wilysupply)

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[dsquery|dsquery]]
- [[powersploit|PowerSploit]]
- [[nltest|Nltest]]
- [[empire|Empire]]
- [[poshc2|PoshC2]]
- [[bloodhound|BloodHound]]
- [[adfind|AdFind]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[rubeus|Rubeus]]

## Platforms

- Windows

