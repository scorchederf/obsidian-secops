---
mitre_id: "T1134"
mitre_name: "Access Token Manipulation"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--dcaa092b-7de9-4a21-977f-7fcb77e89c48"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2025-10-24T17:49:29.051Z"
mitre_version: "2.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1134/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
  - "TA0004"
d3fend_ids:
  - "D3-AEM"
  - "D3-AM"
  - "D3-ANCI"
  - "D3-CCSA"
  - "D3-CH"
  - "D3-CI"
  - "D3-CR"
  - "D3-CRO"
  - "D3-CTS"
  - "D3-DUC"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-HBPI"
  - "D3-MFA"
  - "D3-NTPM"
  - "D3-OPM"
  - "D3-PSA"
  - "D3-RC"
  - "D3-RIC"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-ST"
  - "D3-TB"
  - "D3-TBA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.

An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]) or used to spawn a new process (i.e. [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system.(Citation: Pentestlab Token Manipulation)

Any standard user can use the `runas` command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.

## Workspace

- [[workspaces/attack/techniques/T1134-access_token_manipulation-note|Open workspace note]]

![[workspaces/attack/techniques/T1134-access_token_manipulation-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/0adc67e0_a68f_4ffd_9c43_28905aad5d6a-hacktool_koh_default_named_pipe|HackTool - Koh Default Named Pipe (critical; windows / pipe_created)]]
- [[kb/sigma/rules/15619216_e993_4721_b590_4c520615a67d-potential_meterpreter_cobaltstrike_activity|Potential Meterpreter/CobaltStrike Activity (high; windows / process_creation)]]
- [[kb/sigma/rules/2617e7ed_adb7_40ba_b0f3_8f9945fe6c09-suspicious_system_user_process_creation|Suspicious SYSTEM User Process Creation (high; windows / process_creation)]]
- [[kb/sigma/rules/52ff7941_8211_46f9_84f8_9903efb7077d-hacktool_ppid_spoofing_selectmyparent_tool_execution|HackTool - PPID Spoofing SelectMyParent Tool Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/590a5f4c_6c8c_4f10_8307_89afe9453a9d-suspicious_child_process_created_as_system|Suspicious Child Process Created as System (high; windows / process_creation)]]
- [[kb/sigma/rules/7b14c76a_c602_4ae6_9717_eff868153fc0-hacktool_nofilter_execution|HackTool - NoFilter Execution (high; windows / security)]]
- [[kb/sigma/rules/843544a7_56e0_4dcc_a44f_5cc266dd97d6-meterpreter_or_cobalt_strike_getsystem_service_installation_system|Meterpreter or Cobalt Strike Getsystem Service Installation - System (high; windows / system)]]
- [[kb/sigma/rules/c7d33b50_f690_4b51_8cfb_0fb912a31e57-hacktool_sharpdpapi_execution|HackTool - SharpDPAPI Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/ecbc5e16_58e0_4521_9c60_eb9a7ea4ad34-meterpreter_or_cobalt_strike_getsystem_service_installation_security|Meterpreter or Cobalt Strike Getsystem Service Installation - Security (high; windows / security)]]
- [[kb/sigma/rules/f89b08d0_77ad_4728_817b_9b16c5a69c7a-hacktool_sharpimpersonation_execution|HackTool - SharpImpersonation Execution (high; windows / process_creation)]]
- 1 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/069258f4_2162_46e9_9a25_c9c6c56150d2-parent_pid_spoofing_using_powershell|Parent PID Spoofing using PowerShell (powershell; windows)]]
- [[kb/atomic/tests/14920ebd_1d61_491a_85e0_fe98efe37f25-parent_pid_spoofing_spawn_from_current_process|Parent PID Spoofing - Spawn from Current Process (powershell; windows)]]
- [[kb/atomic/tests/2988133e_561c_4e42_a15f_6281e6a9b2db-parent_pid_spoofing_spawn_from_new_process|Parent PID Spoofing - Spawn from New Process (powershell; windows)]]
- [[kb/atomic/tests/34f0a430_9d04_4d98_bcb5_1989f14719f0-sedebugprivilege_token_duplication|`SeDebugPrivilege` token duplication (powershell; windows)]]
- [[kb/atomic/tests/6bef32e5_9456_4072_8f14_35566fb85401-injection_sid_history_with_mimikatz|Injection SID-History with mimikatz (command_prompt; windows)]]
- [[kb/atomic/tests/7be1bc0f_d8e5_4345_9333_f5f67d742cb9-launch_nsudo_executable|Launch NSudo Executable (powershell; windows)]]
- [[kb/atomic/tests/90db9e27_8e7c_4c04_b602_a45927884966-named_pipe_client_impersonation|Named pipe client impersonation (powershell; windows)]]
- [[kb/atomic/tests/9c6d799b_c111_4749_a42f_ec2f8cb51448-bad_potato|Bad Potato (powershell; windows)]]
- [[kb/atomic/tests/cbbff285_9051_444a_9d17_c07cd2d230eb-parent_pid_spoofing_spawn_from_specified_process|Parent PID Spoofing - Spawn from Specified Process (powershell; windows)]]
- [[kb/atomic/tests/ccf4ac39_ec93_42be_9035_90e2f26bcd92-winpwn_get_system_shell_pop_system_shell_using_token_manipulation_technique|WinPwn - Get SYSTEM shell - Pop System Shell using Token Manipulation technique (powershell; windows)]]
- 3 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

## D3FEND

- [[D3-AEM-application_exception_monitoring|D3-AEM: Application Exception Monitoring]]
- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
- [[D3-ANCI-authentication_cache_invalidation|D3-ANCI: Authentication Cache Invalidation]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-CR-credential_revocation|D3-CR: Credential Revocation]]
- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]
- [[D3-CTS-credential_transmission_scoping|D3-CTS: Credential Transmission Scoping]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-MFA-multi-factor_authentication|D3-MFA: Multi-factor Authentication]]
- [[D3-NTPM-network_traffic_policy_mapping|D3-NTPM: Network Traffic Policy Mapping]]
- [[D3-OPM-operational_process_monitoring|D3-OPM: Operational Process Monitoring]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-ST-session_termination|D3-ST: Session Termination]]
- [[D3-TB-token_binding|D3-TB: Token Binding]]
- [[D3-TBA-token-based_authentication|D3-TBA: Token-based Authentication]]

## Subtechniques

### T1134.001: Token Impersonation/Theft

^t1134001-token-impersonation-theft

Adversaries may duplicate then impersonate another user's existing token to escalate privileges and bypass access controls. For example, an adversary can duplicate an existing token using `DuplicateToken` or `DuplicateTokenEx`.(Citation: DuplicateToken function) The token can then be used with `ImpersonateLoggedOnUser` to allow the calling thread to impersonate a logged on user's security context, or with `SetThreadToken` to assign the impersonated token to a thread.

An adversary may perform [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]] when they have a specific, existing process they want to assign the duplicated token to. For example, this may be useful for when the target user has a non-network logon session on the system.

When an adversary would instead use a duplicated token to create a new process rather than attaching to an existing process, they can additionally [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]] using `CreateProcessWithTokenW` or `CreateProcessAsUserW`. [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]] is also distinct from [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]] in that it refers to duplicating an existing token, rather than creating a new one.

### T1134.002: Create Process with Token

^t1134002-create-process-with-token

Adversaries may create a new process with an existing token to escalate privileges and bypass access controls. Processes can be created with the token and resulting security context of another user using features such as `CreateProcessWithTokenW` and `runas`.(Citation: Microsoft RunAs)

Creating processes with a token not associated with the current user may require the credentials of the target user, specific privileges to impersonate that user, or access to the token to be used. For example, the token could be duplicated via [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]] or created via [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]] before being used to create a process.

While this technique is distinct from [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]], the techniques can be used in conjunction where a token is duplicated and then used to create a new process.

### T1134.003: Make and Impersonate Token

^t1134003-make-and-impersonate-token

Adversaries may make new tokens and impersonate users to escalate privileges and bypass access controls. For example, if an adversary has a username and password but the user is not logged onto the system the adversary can then create a logon session for the user using the `LogonUser` function.(Citation: LogonUserW function) The function will return a copy of the new session's access token and the adversary can use `SetThreadToken` to assign the token to a thread.

This behavior is distinct from [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]] in that this refers to creating a new user token instead of stealing or duplicating an existing one.

### T1134.004: Parent PID Spoofing

^t1134004-parent-pid-spoofing

Adversaries may spoof the parent process identifier (PPID) of a new process to evade process-monitoring defenses or to elevate privileges. New processes are typically spawned directly from their parent, or calling, process unless explicitly specified. One way of explicitly assigning the PPID of a new process is via the `CreateProcess` API call, which supports a parameter that defines the PPID to use.(Citation: DidierStevens SelectMyParent Nov 2009) This functionality is used by Windows features such as User Account Control (UAC) to correctly set the PPID after a requested elevated process is spawned by SYSTEM (typically via `svchost.exe` or `consent.exe`) rather than the current user context.(Citation: Microsoft UAC Nov 2018)

Adversaries may abuse these mechanisms to evade defenses, such as those blocking processes spawning directly from Office documents, and analysis targeting unusual/potentially malicious parent-child process relationships, such as spoofing the PPID of [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]/[[T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]] to be `explorer.exe` rather than an Office document delivered as part of [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]].(Citation: CounterCept PPID Spoofing Dec 2018) This spoofing could be executed via [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]] within a malicious Office document or any code that can perform [[T1106-native_api|T1106: Native API]].(Citation: CTD PPID Spoofing Macro Mar 2019)(Citation: CounterCept PPID Spoofing Dec 2018)

Explicitly assigning the PPID may also enable elevated privileges given appropriate access rights to the parent process. For example, an adversary in a privileged user context (i.e. administrator) may spawn a new process and assign the parent as a process running as SYSTEM (such as `lsass.exe`), causing the new process to be elevated via the inherited access token.(Citation: XPNSec PPID Nov 2017)

### T1134.005: SID-History Injection

^t1134005-sid-history-injection

Adversaries may use SID-History Injection to escalate privileges and bypass access controls. The Windows security identifier (SID) is a unique value that identifies a user or group account. SIDs are used by Windows security in both security descriptors and access tokens. (Citation: Microsoft SID) An account can hold additional SIDs in the SID-History Active Directory attribute (Citation: Microsoft SID-History Attribute), allowing inter-operable account migration between domains (e.g., all values in SID-History are included in access tokens).

With Domain Administrator (or equivalent) rights, harvested or well-known SID values (Citation: Microsoft Well Known SIDs Jun 2017) may be inserted into SID-History to enable impersonation of arbitrary users/groups such as Enterprise Administrators. This manipulation may result in elevated access to local resources and/or access to otherwise inaccessible domains via lateral movement techniques such as [[T1021-remote_services|T1021: Remote Services]], [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]], or [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]].

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]

## Tools
- [[empire|Empire (S0363)]]
- [[poshc2|PoshC2 (S0378)]]
- [[powersploit|PowerSploit (S0194)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- Windows

