---
id: S0357
name: Impacket
created: 2019-01-31 01:39:56.283000+00:00
modified: 2025-04-04 17:16:12.597000+00:00
type: tool
x_mitre_version: 1.8
x_mitre_domains: enterprise-attack
---

# Impacket

[Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools)

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
    - [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
    - [[T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558005-ccache-files|T1558.005: Ccache Files]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

