---
id: T1118
name: InstallUtil
created: 2017-05-31 21:31:27.510000+00:00
modified: 2025-10-24 17:49:37.916000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

InstallUtil is a command-line utility that allows for installation and uninstallation of resources by executing specific installer components specified in .NET binaries. (Citation: MSDN InstallUtil) InstallUtil is located in the .NET directories on a Windows system: <code>C:\Windows\Microsoft.NET\Framework\v<version>\InstallUtil.exe</code> and <code>C:\Windows\Microsoft.NET\Framework64\v<version>\InstallUtil.exe</code>. InstallUtil.exe is digitally signed by Microsoft.

Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil may also be used to bypass process whitelisting through use of attributes within the binary that execute the class decorated with the attribute <code>[System.ComponentModel.RunInstaller(true)]</code>. (Citation: LOLBAS Installutil)

## Platforms

- Windows

