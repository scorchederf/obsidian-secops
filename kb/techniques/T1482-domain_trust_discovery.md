---
id: T1482
name: Domain Trust Discovery
created: 2019-02-14 16:15:05.974000+00:00
modified: 2025-10-24 17:48:58.061000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.(Citation: Microsoft Trusts) Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct [SID-History Injection](https://attack.mitre.org/techniques/T1134/005), [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003), and [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).(Citation: AdSecurity Forging Trust Tickets)(Citation: Harmj0y Domain Trusts) Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP.(Citation: Harmj0y Domain Trusts) The Windows utility [Nltest](https://attack.mitre.org/software/S0359) is known to be used by adversaries to enumerate domain trusts.(Citation: Microsoft Operation Wilysupply)

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Windows

## Tools

- [[adfind|AdFind]]
- [[bloodhound|BloodHound]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[dsquery|dsquery]]
- [[empire|Empire]]
- [[nltest|Nltest]]
- [[poshc2|PoshC2]]
- [[powersploit|PowerSploit]]
- [[rubeus|Rubeus]]

