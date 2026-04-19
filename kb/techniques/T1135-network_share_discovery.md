---
id: T1135
name: Network Share Discovery
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:37.475000+00:00
type: attack-pattern
x_mitre_version: 3.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation: TechNet Shared Folder) [Net](https://attack.mitre.org/software/S0039) can be used to query a remote system for available shared drives using the <code>net view \\\\remotesystem</code> command. It can also be used to query shared drives on the local system using <code>net share</code>. For macOS, the <code>sharing -l</code> command lists all shared points used for smb services.

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]

## Platforms

- Linux
- macOS
- Windows

## Tools

- [[crackmapexec|CrackMapExec]]
- [[empire|Empire]]
- [[koadic|Koadic]]
- [[net|Net]]
- [[pupy|Pupy]]
- [[silenttrinity|SILENTTRINITY]]

