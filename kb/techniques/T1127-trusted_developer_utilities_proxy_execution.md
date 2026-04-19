---
id: T1127
name: Trusted Developer Utilities Proxy Execution
created: 2017-05-31 21:31:39.262000+00:00
modified: 2025-10-24 17:49:40.055000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering.(Citation: engima0x3 DNX Bypass)(Citation: engima0x3 RCSI Bypass)(Citation: Exploit Monday WinDbg)(Citation: LOLBAS Tracker) These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application control solutions.

Smart App Control is a feature of Windows that blocks applications it considers potentially malicious from running by verifying unsigned applications against a known safe list from a Microsoft cloud service before executing them.(Citation: Microsoft Smart App Control) However, adversaries may leverage "reputation hijacking" to abuse an operating system’s trust of safe, signed applications that support the execution of arbitrary code. By leveraging [Trusted Developer Utilities Proxy Execution](https://attack.mitre.org/techniques/T1127) to run their malicious code, adversaries may bypass Smart App Control protections.(Citation: Elastic Security Labs)

## Subtechniques

### T1127.001: MSBuild

^t1127001-msbuild

**Parent Technique**
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use MSBuild to proxy execution of code through a trusted Windows utility. MSBuild.exe (Microsoft Build Engine) is a software build platform used by Visual Studio. It handles XML formatted project files that define requirements for loading and building various platforms and configurations.(Citation: MSDN MSBuild)

Adversaries can abuse MSBuild to proxy execution of malicious code. The inline task capability of MSBuild that was introduced in .NET version 4 allows for C# or Visual Basic code to be inserted into an XML project file.(Citation: MSDN MSBuild)(Citation: Microsoft MSBuild Inline Tasks 2017) MSBuild will compile and execute the inline task. MSBuild.exe is a signed Microsoft binary, so when it is used this way it can execute arbitrary code and bypass application control defenses that are configured to allow MSBuild.exe execution.(Citation: LOLBAS Msbuild)

### T1127.002: ClickOnce

^t1127002-clickonce

**Parent Technique**
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code through a trusted Windows utility.(Citation: Burke/CISA ClickOnce BlackHat) ClickOnce is a deployment that enables a user to create self-updating Windows-based .NET applications (i.e, .XBAP, .EXE, or .DLL) that install and run from a file share or web page with minimal user interaction. The application launches as a child process of DFSVC.EXE, which is responsible for installing, launching, and updating the application.(Citation: SpectorOps Medium ClickOnce)

Because ClickOnce applications receive only limited permissions, they do not require administrative permissions to install.(Citation: Microsoft Learn ClickOnce) As such, adversaries may abuse ClickOnce to proxy execution of malicious code without needing to escalate privileges.

ClickOnce may be abused in a number of ways. For example, an adversary may rely on [User Execution](https://attack.mitre.org/techniques/T1204). When a user visits a malicious website, the .NET malware is disguised as legitimate software and a ClickOnce popup is displayed for installation.(Citation: NetSPI ClickOnce)

Adversaries may also abuse ClickOnce to execute malware via a [Rundll32](https://attack.mitre.org/techniques/T1218/011) script using the command `rundll32.exe dfshim.dll,ShOpenVerbApplication1`.(Citation: LOLBAS /Dfsvc.exe)

Additionally, an adversary can move the ClickOnce application file to a remote user’s startup folder for continued malicious code deployment (i.e., [Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001)).(Citation: Burke/CISA ClickOnce BlackHat)(Citation: Burke/CISA ClickOnce Paper)

### T1127.003: JamPlus

^t1127003-jamplus

**Parent Technique**
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use `JamPlus` to proxy the execution of a malicious script. `JamPlus` is a build utility tool for code and data build systems. It works with several popular compilers and can be used for generating workspaces in code editors such as Visual Studio.(Citation: JamPlus manual)

Adversaries may abuse the `JamPlus` build utility to execute malicious scripts via a `.jam` file, which describes the build process and required dependencies. Because the malicious script is executed from a reputable developer tool, it may subvert application control security systems such as Smart App Control.(Citation: Cyble)(Citation: Elastic Security Labs)

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Windows

