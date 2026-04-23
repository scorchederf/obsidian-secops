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
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
  - "TA0004"
---

# T1134: Access Token Manipulation

Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.

An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]) or used to spawn a new process (i.e. [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system.(Citation: Pentestlab Token Manipulation)

Any standard user can use the `runas` command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

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

- [[powersploit|PowerSploit]]
- [[empire|Empire]]
- [[poshc2|PoshC2]]
- [[sliver|Sliver]]

## Platforms

- Windows

