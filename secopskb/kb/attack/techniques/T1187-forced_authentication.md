---
mitre_id: "T1187"
mitre_name: "Forced Authentication"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b77cf5f3-6060-475d-bd60-40ccbf28fdc2"
mitre_created: "2018-01-16T16:13:52.465Z"
mitre_modified: "2025-10-24T17:49:16.134Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1187/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-AEM"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-OPM"
  - "D3-RF"
  - "D3-RFAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may gather credential material by invoking or forcing a user to automatically provide authentication information through a mechanism in which they can intercept.

The Server Message Block (SMB) protocol is commonly used in Windows networks for authentication and communication between systems for access to resources and file sharing. When a Windows system attempts to connect to an SMB resource it will automatically attempt to authenticate and send credential information for the current user to the remote system.(Citation: Wikipedia Server Message Block) This behavior is typical in enterprise environments so that users do not need to enter credentials to access network resources.

Web Distributed Authoring and Versioning (WebDAV) is also typically used by Windows systems as a backup protocol when SMB is blocked or fails. WebDAV is an extension of HTTP and will typically operate over TCP ports 80 and 443.(Citation: Didier Stevens WebDAV Traffic)(Citation: Microsoft Managing WebDAV Security)

Adversaries may take advantage of this behavior to gain access to user account hashes through forced SMB/WebDAV authentication. An adversary can send an attachment to a user through spearphishing that contains a resource link to an external server controlled by the adversary  (i.e. [[T1221-template_injection|T1221: Template Injection]]), or place a specially crafted file on navigation path for privileged accounts (e.g. .SCF file placed on desktop) or on a publicly accessible share to be accessed by victim(s). When the user's system accesses the untrusted resource, it will attempt authentication and send information, including the user's hashed credentials, over SMB to the adversary-controlled server.(Citation: GitHub Hashjacking) With access to the credential hash, an adversary can perform off-line [[T1110-brute_force|T1110: Brute Force]] cracking to gain access to plaintext credentials.(Citation: Cylance Redirect to SMB)

There are several different ways this can occur.(Citation: Osanda Stealing NetNTLM Hashes) Some specifics from in-the-wild use include:

* A spearphishing attachment containing a document with a resource that is automatically loaded when the document is opened (i.e. [[T1221-template_injection|T1221: Template Injection]]). The document can include, for example, a request similar to `file[:]//[remote address]/Normal.dotm` to trigger the SMB request.(Citation: US-CERT APT Energy Oct 2017)
* A modified .LNK or .SCF file with the icon filename pointing to an external reference such as `\\[remote address]\pic.png` that will force the system to load the resource when the icon is rendered to repeatedly gather credentials.(Citation: US-CERT APT Energy Oct 2017)

Alternatively, by leveraging the `EfsRpcOpenFileRaw` function, an adversary can send SMB requests to a remote system's MS-EFSRPC interface and force the victim computer to initiate an authentication procedure and share its authentication details. The Encrypting File System Remote Protocol (EFSRPC) is a protocol used in Windows networks for maintenance and management operations on encrypted data that is stored remotely to be accessed over a network. Utilization of `EfsRpcOpenFileRaw` function in EFSRPC is used to open an encrypted object on the server for backup or restore. Adversaries can collect this data and abuse it as part of a NTLM relay attack to gain access to remote systems on the same internal network.(Citation: Rapid7)(Citation: GitHub)



## Workspace

- [[workspaces/attack/techniques/T1187-forced_authentication-note|Open workspace note]]

![[workspaces/attack/techniques/T1187-forced_authentication-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-09-003-smb_session_setups|CAR-2013-09-003: SMB Session Setups]]

### Sigma Rules

- [[kb/sigma/rules/0ed99dda_6a35_11ef_8c99_0242ac120002-attempts_of_kerberos_coercion_via_dns_spn_spoofing|Attempts of Kerberos Coercion Via DNS SPN Spoofing (high; windows / process_creation)]]
- [[kb/sigma/rules/1ce8c8a3_2723_48ed_8246_906ac91061a6-possible_petitpotam_coerce_authentication_attempt|Possible PetitPotam Coerce Authentication Attempt (high; windows / security)]]
- [[kb/sigma/rules/5588576c_5898_4fac_bcdd_7475a60e8f43-suspicious_dns_query_indicating_kerberos_coercion_via_dns_object_spn_spoofing_network|Suspicious DNS Query Indicating Kerberos Coercion via DNS Object SPN Spoofing - Network (high; zeek / dns)]]
- [[kb/sigma/rules/6a53d871_682d_40b6_83e0_b7c1a6c4e3a5-petitpotam_suspicious_kerberos_tgt_request|PetitPotam Suspicious Kerberos TGT Request (high; windows / security)]]
- [[kb/sigma/rules/e7a21b5f_d8c4_4ae5_b8d9_93c5d3f28e1c-suspicious_dns_query_indicating_kerberos_coercion_via_dns_object_spn_spoofing|Suspicious DNS Query Indicating Kerberos Coercion via DNS Object SPN Spoofing (high; windows / dns_query)]]

### Atomic Tests

- [[kb/atomic/tests/485ce873_2e65_4706_9c7e_ae3ab9e14213-petitpotam|PetitPotam (powershell; windows)]]
- [[kb/atomic/tests/7f06b25c_799e_40f1_89db_999c9cc84317-winpwn_powersharppack_retrieving_ntlm_hashes_without_touching_lsass|WinPwn - PowerSharpPack - Retrieving NTLM Hashes without Touching LSASS (powershell; windows)]]
- [[kb/atomic/tests/81cfdd7f_1f41_4cc5_9845_bb5149438e37-trigger_an_authenticated_rpc_call_to_a_target_server_with_no_sign_flag_set|Trigger an authenticated RPC call to a target server with no Sign flag set (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-AEM-application_exception_monitoring|D3-AEM: Application Exception Monitoring]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-OPM-operational_process_monitoring|D3-OPM: Operational Process Monitoring]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]

## Mitigations

- [[M1027-password_policies|M1027: Password Policies]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Platforms

- Windows

