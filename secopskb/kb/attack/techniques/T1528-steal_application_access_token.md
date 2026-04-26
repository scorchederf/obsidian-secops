---
mitre_id: "T1528"
mitre_name: "Steal Application Access Token"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--890c9858-598c-401d-a4d5-c67ebcdd703a"
mitre_created: "2019-09-04T15:54:25.684Z"
mitre_modified: "2025-10-24T17:49:04.660Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1528/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "SaaS"
  - "Containers"
  - "IaaS"
  - "Office Suite"
  - "Identity Provider"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-ANCI"
  - "D3-CCSA"
  - "D3-CH"
  - "D3-CR"
  - "D3-CRO"
  - "D3-CTS"
  - "D3-DUC"
  - "D3-MFA"
  - "D3-RIC"
  - "D3-TB"
  - "D3-TBA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries can steal application access tokens as a means of acquiring credentials to access remote systems and resources.

Application access tokens are used to make authorized API requests on behalf of a user or service and are commonly used as a way to access resources in cloud and container-based applications and software-as-a-service (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019)  Adversaries who steal account API tokens in cloud and containerized environments may be able to access data and perform actions with the permissions of these accounts, which can lead to privilege escalation and further compromise of the environment.

For example, in Kubernetes environments, processes running inside a container may communicate with the Kubernetes API server using service account tokens. If a container is compromised, an adversary may be able to steal the container’s token and thereby gain access to Kubernetes API commands.(Citation: Kubernetes Service Accounts)  

Similarly, instances within continuous-development / continuous-integration (CI/CD) pipelines will often use API tokens to authenticate to other services for testing and deployment.(Citation: Cider Security Top 10 CICD Security Risks) If these pipelines are compromised, adversaries may be able to steal these tokens and leverage their privileges. 

In Azure, an adversary who compromises a resource with an attached Managed Identity, such as an Azure VM, can request short-lived tokens through the Azure Instance Metadata Service (IMDS). These tokens can then facilitate unauthorized actions or further access to other Azure services, bypassing typical credential-based authentication.(Citation: Entra Managed Identities 2025)(Citation: SpecterOps Managed Identity 2022)

Token theft can also occur through social engineering, in which case user action may be required to grant access. OAuth is one commonly implemented framework that issues tokens to users for access to systems. An application desiring access to cloud-based services or protected APIs can gain entry using OAuth 2.0 through a variety of authorization protocols. An example commonly-used sequence is Microsoft's Authorization Code Grant flow.(Citation: Microsoft Identity Platform Protocols May 2019)(Citation: Microsoft - OAuth Code Authorization flow - June 2019) An OAuth access token enables a third-party application to interact with resources containing user data in the ways requested by the application without obtaining user credentials. 
 
Adversaries can leverage OAuth authorization by constructing a malicious application designed to be granted access to resources with the target user's OAuth token.(Citation: Amnesty OAuth Phishing Attacks, August 2019)(Citation: Trend Micro Pawn Storm OAuth 2017) The adversary will need to complete registration of their application with the authorization server, for example Microsoft Identity Platform using Azure Portal, the Visual Studio IDE, the command-line interface, PowerShell, or REST API calls.(Citation: Microsoft - Azure AD App Registration - May 2019) Then, they can send a [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]] to the target user to entice them to grant access to the application. Once the OAuth access token is granted, the application can gain potentially long-term access to features of the user account through [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]].(Citation: Microsoft - Azure AD Identity Tokens - Aug 2019)

Application access tokens may function within a limited lifetime, limiting how long an adversary can utilize the stolen token. However, in some cases, adversaries can also steal application refresh tokens(Citation: Auth0 Understanding Refresh Tokens), allowing them to obtain new access tokens without prompting the user.  

## Workspace

- [[workspaces/attack/techniques/T1528-steal_application_access_token-note|Open workspace note]]

![[workspaces/attack/techniques/T1528-steal_application_access_token-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/0055ad1f_be85_4798_83cf_a6da17c993b3-application_uri_configuration_changes|Application URI Configuration Changes (high; azure / auditlogs)]]
- [[kb/sigma/rules/0adc67e0_a68f_4ffd_9c43_28905aad5d6a-hacktool_koh_default_named_pipe|HackTool - Koh Default Named Pipe (critical; windows / pipe_created)]]
- [[kb/sigma/rules/25cde13e_8e20_4c29_b949_4e795b76f16f-suspicious_teams_application_related_objectacess_event|Suspicious Teams Application Related ObjectAcess Event (high; windows / security)]]
- [[kb/sigma/rules/53acd925_2003_440d_a1f3_71a5253fe237-anonymous_ip_address|Anonymous IP Address (high; azure / riskdetection)]]
- [[kb/sigma/rules/6555754e_5e7f_4a67_ad1c_4041c413a007-anomalous_token|Anomalous Token (high; azure / riskdetection)]]
- [[kb/sigma/rules/8a4519e8_e64a_40b6_ae85_ba8ad2177559-renamed_browsercore_exe_execution|Renamed BrowserCore.EXE Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/a6355fbe_f36f_45d8_8efc_ab42465cbc52-delegated_permissions_granted_for_all_users|Delegated Permissions Granted For All Users (high; azure / auditlogs)]]
- [[kb/sigma/rules/a84fc3b1_c9ce_4125_8e74_bdcdb24021f1-primary_refresh_token_access_attempt|Primary Refresh Token Access Attempt (high; azure / riskdetection)]]
- [[kb/sigma/rules/c1d147ae_a951_48e5_8b41_dcd0170c7213-app_granted_microsoft_permissions|App Granted Microsoft Permissions (high; azure / auditlogs)]]

### Atomic Tests

- [[kb/atomic/tests/67aaf4cb_54ce_42e2_ab56_e0a9bcc089b1-azure_functions_code_upload_functions_code_injection_via_file_share_modification_to_retrieve_the_functions_identity_access_token|Azure - Functions code upload - Functions code injection via File Share modification to retrieve the Functions identity access token (powershell; iaas:azure)]]
- [[kb/atomic/tests/9a5352e4_56e5_45c2_9b3f_41a46d3b3a43-azure_functions_code_upload_functions_code_injection_via_blob_upload|Azure - Functions code upload - Functions code injection via Blob upload (powershell; iaas:azure)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-ANCI-authentication_cache_invalidation|D3-ANCI: Authentication Cache Invalidation]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]
- [[D3-CR-credential_revocation|D3-CR: Credential Revocation]]
- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]
- [[D3-CTS-credential_transmission_scoping|D3-CTS: Credential Transmission Scoping]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]
- [[D3-MFA-multi-factor_authentication|D3-MFA: Multi-factor Authentication]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]
- [[D3-TB-token_binding|D3-TB: Token Binding]]
- [[D3-TBA-token-based_authentication|D3-TBA: Token-based Authentication]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[aadinternals|AADInternals (S0677)]]
- [[peirates|Peirates (S0683)]]

## Platforms

- SaaS
- Containers
- IaaS
- Office Suite
- Identity Provider

