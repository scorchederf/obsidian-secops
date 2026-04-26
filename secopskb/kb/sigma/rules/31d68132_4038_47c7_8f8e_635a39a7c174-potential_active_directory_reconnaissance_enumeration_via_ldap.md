---
sigma_id: "31d68132-4038-47c7-8f8e-635a39a7c174"
title: "Potential Active Directory Reconnaissance/Enumeration Via LDAP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/ldap/win_ldap_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ldap/win_ldap_recon.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / ldap"
aliases:
  - "31d68132-4038-47c7-8f8e-635a39a7c174"
  - "Potential Active Directory Reconnaissance/Enumeration Via LDAP"
attack_technique_ids:
  - "T1069.002"
  - "T1087.002"
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Active Directory Reconnaissance/Enumeration Via LDAP

Detects potential Active Directory enumeration via LDAP

## Metadata

- Rule ID: 31d68132-4038-47c7-8f8e-635a39a7c174
- Status: test
- Level: medium
- Author: Adeem Mawani
- Date: 2021-06-22
- Modified: 2025-07-04
- Source Path: rules/windows/builtin/ldap/win_ldap_recon.yml

## Logsource

- definition: Requirements: Microsoft-Windows-LDAP-Client/Debug ETW logging
- product: windows
- service: ldap

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
generic_search:
  EventID: 30
  SearchFilter|contains:
  - (groupType:1.2.840.113556.1.4.803:=2147483648)
  - (groupType:1.2.840.113556.1.4.803:=2147483656)
  - (groupType:1.2.840.113556.1.4.803:=2147483652)
  - (groupType:1.2.840.113556.1.4.803:=2147483650)
  - (sAMAccountType=805306369)
  - (sAMAccountType=805306368)
  - (sAMAccountType=536870913)
  - (sAMAccountType=536870912)
  - (sAMAccountType=268435457)
  - (sAMAccountType=268435456)
  - (objectCategory=groupPolicyContainer)
  - (objectCategory=organizationalUnit)
  - (objectCategory=nTDSDSA)
  - (objectCategory=server)
  - (objectCategory=domain)
  - (objectCategory=person)
  - (objectCategory=group)
  - (objectCategory=user)
  - (objectClass=trustedDomain)
  - (objectClass=computer)
  - (objectClass=server)
  - (objectClass=group)
  - (objectClass=user)
  - (primaryGroupID=521)
  - (primaryGroupID=516)
  - (primaryGroupID=515)
  - (primaryGroupID=512)
  - Domain Admins
  - objectGUID=\*
  - (schemaIDGUID=\*)
  - admincount=1
distinguished_name_enumeration:
  EventID: 30
  SearchFilter: (objectclass=\*)
  DistinguishedName|contains:
  - CN=Domain Admins
  - CN=Enterprise Admins
  - CN=Group Policy Creator Owners
suspicious_flag:
  EventID: 30
  SearchFilter|contains:
  - (userAccountControl:1.2.840.113556.1.4.803:=4194304)
  - (userAccountControl:1.2.840.113556.1.4.803:=2097152)
  - '!(userAccountControl:1.2.840.113556.1.4.803:=1048574)'
  - (userAccountControl:1.2.840.113556.1.4.803:=524288)
  - (userAccountControl:1.2.840.113556.1.4.803:=65536)
  - (userAccountControl:1.2.840.113556.1.4.803:=8192)
  - (userAccountControl:1.2.840.113556.1.4.803:=544)
  - '!(UserAccountControl:1.2.840.113556.1.4.803:=2)'
  - msDS-AllowedToActOnBehalfOfOtherIdentity
  - msDS-AllowedToDelegateTo
  - msDS-GroupManagedServiceAccount
  - (accountExpires=9223372036854775807)
  - (accountExpires=0)
  - (adminCount=1)
  - ms-MCS-AdmPwd
narrow_down_filter:
  EventID: 30
  SearchFilter|contains:
  - (domainSid=*)
  - (objectSid=*)
condition: (generic_search and not narrow_down_filter) or suspicious_flag or distinguished_name_enumeration
```

## References

- https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/hunting-for-reconnaissance-activities-using-ldap-search-filters/ba-p/824726
- https://github.com/PowerShellMafia/PowerSploit/blob/d943001a7defb5e0d1657085a77a0e78609be58f/Recon/PowerView.ps1
- https://github.com/BloodHoundAD/SharpHound3/blob/7d96b991b1887ff50349ce59c80980bc0d95c86a/SharpHound3/LdapBuilder.cs
- https://medium.com/falconforce/falconfriday-detecting-active-directory-data-collection-0xff21-c22d1a57494c
- https://github.com/fox-it/BloodHound.py/blob/d65eb614831cd30f26028ccb072f5e77ca287e0b/bloodhound/ad/domain.py#L427
- https://ipurple.team/2024/07/15/sharphound-detection/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ldap/win_ldap_recon.yml)
