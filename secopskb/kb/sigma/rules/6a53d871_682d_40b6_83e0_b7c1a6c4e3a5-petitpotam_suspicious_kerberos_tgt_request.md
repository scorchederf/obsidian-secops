---
sigma_id: "6a53d871-682d-40b6-83e0-b7c1a6c4e3a5"
title: "PetitPotam Suspicious Kerberos TGT Request"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_petitpotam_susp_tgt_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_petitpotam_susp_tgt_request.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "6a53d871-682d-40b6-83e0-b7c1a6c4e3a5"
  - "PetitPotam Suspicious Kerberos TGT Request"
attack_technique_ids:
  - "T1187"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PetitPotam Suspicious Kerberos TGT Request

Detect suspicious Kerberos TGT requests.
Once an attacer obtains a computer certificate by abusing Active Directory Certificate Services in combination with PetitPotam, the next step would be to leverage the certificate for malicious purposes.
One way of doing this is to request a Kerberos Ticket Granting Ticket using a tool like Rubeus.
This request will generate a 4768 event with some unusual fields depending on the environment.
This analytic will require tuning, we recommend filtering Account_Name to the Domain Controller computer accounts.

## Metadata

- Rule ID: 6a53d871-682d-40b6-83e0-b7c1a6c4e3a5
- Status: test
- Level: high
- Author: Mauricio Velazco, Michael Haag
- Date: 2021-09-02
- Modified: 2022-10-05
- Source Path: rules/windows/builtin/security/win_security_petitpotam_susp_tgt_request.yml

## Logsource

- definition: The advanced audit policy setting "Account Logon > Kerberos Authentication Service" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1187-forced_authentication|T1187]]

## Detection

```yaml
selection:
  EventID: 4768
  TargetUserName|endswith: $
  CertThumbprint|contains: '*'
filter_local:
  IpAddress: ::1
filter_thumbprint:
  CertThumbprint: ''
condition: selection and not 1 of filter_*
```

## False Positives

- False positives are possible if the environment is using certificates for authentication. We recommend filtering Account_Name to the Domain Controller computer accounts.

## References

- https://github.com/topotam/PetitPotam
- https://isc.sans.edu/forums/diary/Active+Directory+Certificate+Services+ADCS+PKI+domain+admin+vulnerability/27668/
- https://github.com/splunk/security_content/blob/88d689fe8a055d8284337b9fad5d9152b42043db/detections/endpoint/petitpotam_suspicious_kerberos_tgt_request.yml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_petitpotam_susp_tgt_request.yml)
