---
id: T1021
name: Remote Services
created: 2017-05-31 21:30:29.858000+00:00
modified: 2025-10-24 17:48:48.472000+00:00
type: attack-pattern
x_mitre_version: 1.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[lateral_movement|Lateral Movement]]

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

In an enterprise environment, servers and workstations can be organized into domains. Domains provide centralized identity management, allowing users to login using one set of credentials across the entire network. If an adversary is able to obtain a set of valid domain credentials, they could login to many different machines using remote access protocols such as secure shell (SSH) or remote desktop protocol (RDP).(Citation: SSH Secure Shell)(Citation: TechNet Remote Desktop Services) They could also login to accessible SaaS or IaaS services, such as those that federate their identities to the domain, or management platforms for internal virtualization environments such as VMware vCenter. 

Legitimate applications (such as [Software Deployment Tools](https://attack.mitre.org/techniques/T1072) and other administrative programs) may utilize [Remote Services](https://attack.mitre.org/techniques/T1021) to access remote hosts. For example, Apple Remote Desktop (ARD) on macOS is native software used for remote management. ARD leverages a blend of protocols, including [VNC](https://attack.mitre.org/techniques/T1021/005) to send the screen and control buffers and [SSH](https://attack.mitre.org/techniques/T1021/004) for secure file transfer.(Citation: Remote Management MDM macOS)(Citation: Kickstart Apple Remote Desktop commands)(Citation: Apple Remote Desktop Admin Guide 3.3) Adversaries can abuse applications such as ARD to gain remote code execution and perform lateral movement. In versions of macOS prior to 10.14, an adversary can escalate an SSH session to an ARD session which enables an adversary to accept TCC (Transparency, Consent, and Control) prompts without user interaction and gain access to data.(Citation: FireEye 2019 Apple Remote Desktop)(Citation: Lockboxx ARD 2019)(Citation: Kickstart Apple Remote Desktop commands)

## Properties

- id: T1021
- name: Remote Services
- created: 2017-05-31 21:30:29.858000+00:00
- modified: 2025-10-24 17:48:48.472000+00:00
- type: attack-pattern
- x_mitre_version: 1.6
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1021.001: Remote Desktop Protocol

^t1021001-remote-desktop-protocol

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services) 

Adversaries may connect to a remote system over RDP/RDS to expand access if the service is enabled and allows access to accounts with known credentials. Adversaries will likely use Credential Access techniques to acquire credentials to use with RDP. Adversaries may also use RDP in conjunction with the [Accessibility Features](https://attack.mitre.org/techniques/T1546/008) or [Terminal Services DLL](https://attack.mitre.org/techniques/T1505/005) for Persistence.(Citation: Alperovitch Malware)

#### Properties

- id: T1021.001
- name: Remote Desktop Protocol
- created: 2020-02-11 18:23:26.059000+00:00
- modified: 2025-10-24 17:49:33.524000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

### T1021.002: SMB/Windows Admin Shares

^t1021002-smb-windows-admin-shares

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with a remote network share using Server Message Block (SMB). The adversary may then perform actions as the logged-on user.

SMB is a file, printer, and serial port sharing protocol for Windows machines on the same network or domain. Adversaries may use SMB to interact with file shares, allowing them to move laterally throughout a network. Linux and macOS implementations of SMB typically use Samba.

Windows systems have hidden network shares that are accessible only to administrators and provide the ability for remote file copy and other administrative functions. Example network shares include `C$`, `ADMIN$`, and `IPC$`. Adversaries may use this technique in conjunction with administrator-level [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely access a networked system over SMB,(Citation: Wikipedia Server Message Block) to interact with systems using remote procedure calls (RPCs),(Citation: TechNet RPC) transfer files, and run transferred binaries through remote Execution. Example execution techniques that rely on authenticated sessions over SMB/RPC are [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), [Service Execution](https://attack.mitre.org/techniques/T1569/002), and [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047). Adversaries can also use NTLM hashes to access administrator shares on systems with [Pass the Hash](https://attack.mitre.org/techniques/T1550/002) and certain configuration and patch levels.(Citation: Microsoft Admin Shares)

#### Properties

- id: T1021.002
- name: SMB/Windows Admin Shares
- created: 2020-02-11 18:25:28.212000+00:00
- modified: 2025-10-24 17:48:45.700000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1021.003: Distributed Component Object Model

^t1021003-distributed-component-object-model

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with remote machines by taking advantage of Distributed Component Object Model (DCOM). The adversary may then perform actions as the logged-on user.

The Windows Component Object Model (COM) is a component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces. Through COM, a client object can call methods of server objects, which are typically Dynamic Link Libraries (DLL) or executables (EXE). Distributed COM (DCOM) is transparent middleware that extends the functionality of COM beyond a local computer using remote procedure call (RPC) technology.(Citation: Fireeye Hunting COM June 2019)(Citation: Microsoft COM)

Permissions to interact with local and remote server COM objects are specified by access control lists (ACL) in the Registry.(Citation: Microsoft Process Wide Com Keys) By default, only Administrators may remotely activate and launch COM objects through DCOM.(Citation: Microsoft COM ACL)

Through DCOM, adversaries operating in the context of an appropriately privileged user can remotely obtain arbitrary and even direct shellcode execution through Office applications(Citation: Enigma Outlook DCOM Lateral Movement Nov 2017) as well as other Windows objects that contain insecure methods.(Citation: Enigma MMC20 COM Jan 2017)(Citation: Enigma DCOM Lateral Movement Jan 2017) DCOM can also execute macros in existing documents(Citation: Enigma Excel DCOM Sept 2017) and may also invoke [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002) (DDE) execution directly through a COM created instance of a Microsoft Office application(Citation: Cyberreason DCOM DDE Lateral Movement Nov 2017), bypassing the need for a malicious document. DCOM can be used as a method of remotely interacting with [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047). (Citation: MSDN WMI)

#### Properties

- id: T1021.003
- name: Distributed Component Object Model
- created: 2020-02-11 18:26:36.444000+00:00
- modified: 2025-10-24 17:48:53.724000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1021.004: SSH

^t1021004-ssh

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into remote machines using Secure Shell (SSH). The adversary may then perform actions as the logged-on user.

SSH is a protocol that allows authorized users to open remote shells on other computers. Many Linux and macOS versions come with SSH installed by default, although typically disabled until the user enables it. On ESXi, SSH can be enabled either directly on the host (e.g., via `vim-cmd hostsvc/enable_ssh`) or via vCenter.(Citation: Sygnia ESXi Ransomware 2025)(Citation: TrendMicro ESXI Ransomware)(Citation: Sygnia Abyss Locker 2025) The SSH server can be configured to use standard password authentication or public-private keypairs in lieu of or in addition to a password. In this authentication scenario, the user’s public key must be in a special file on the computer running the server that lists which keypairs are allowed to login as that user (i.e., [SSH Authorized Keys](https://attack.mitre.org/techniques/T1098/004)).

#### Properties

- id: T1021.004
- name: SSH
- created: 2020-02-11 18:27:15.774000+00:00
- modified: 2025-10-24 17:48:34.985000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1021.005: VNC

^t1021005-vnc

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely control machines using Virtual Network Computing (VNC).  VNC is a platform-independent desktop sharing system that uses the RFB (“remote framebuffer”) protocol to enable users to remotely control another computer’s display by relaying the screen, mouse, and keyboard inputs over the network.(Citation: The Remote Framebuffer Protocol)

VNC differs from [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) as VNC is screen-sharing software rather than resource-sharing software. By default, VNC uses the system's authentication, but it can be configured to use credentials specific to VNC.(Citation: MacOS VNC software for Remote Desktop)(Citation: VNC Authentication)

Adversaries may abuse VNC to perform malicious actions as the logged-on user such as opening documents, downloading files, and running arbitrary commands. An adversary could use VNC to remotely control and monitor a system to collect data and information to pivot to other systems within the network. Specific VNC libraries/implementations have also been susceptible to brute force attacks and memory usage exploitation.(Citation: Hijacking VNC)(Citation: macOS root VNC login without authentication)(Citation: VNC Vulnerabilities)(Citation: Offensive Security VNC Authentication Check)(Citation: Attacking VNC Servers PentestLab)(Citation: Havana authentication bug)

#### Properties

- id: T1021.005
- name: VNC
- created: 2020-02-11 18:28:44.950000+00:00
- modified: 2025-10-24 17:48:19.567000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1021.006: Windows Remote Management

^t1021006-windows-remote-management

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

WinRM is the name of both a Windows service and a protocol that allows a user to interact with a remote system (e.g., run an executable, modify the Registry, modify services).(Citation: Microsoft WinRM) It may be called with the `winrm` command or by any number of programs such as PowerShell.(Citation: Jacobsen 2014) WinRM  can be used as a method of remotely interacting with [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047).(Citation: MSDN WMI)

#### Properties

- id: T1021.006
- name: Windows Remote Management
- created: 2020-02-11 18:29:47.757000+00:00
- modified: 2025-10-24 17:48:51+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1021.007: Cloud Services

^t1021007-cloud-services

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may log into accessible cloud services within a compromised environment using [Valid Accounts](https://attack.mitre.org/techniques/T1078) that are synchronized with or federated to on-premises user identities. The adversary may then perform management actions or access cloud-hosted resources as the logged-on user. 

Many enterprises federate centrally managed user identities to cloud services, allowing users to login with their domain credentials in order to access the cloud control plane. Similarly, adversaries may connect to available cloud services through the web console or through the cloud command line interface (CLI) (e.g., [Cloud API](https://attack.mitre.org/techniques/T1059/009)), using commands such as <code>Connect-AZAccount</code> for Azure PowerShell, <code>Connect-MgGraph</code> for Microsoft Graph PowerShell, and <code>gcloud auth login</code> for the Google Cloud CLI.

In some cases, adversaries may be able to authenticate to these services via [Application Access Token](https://attack.mitre.org/techniques/T1550/001) instead of a username and password. 

#### Properties

- id: T1021.007
- name: Cloud Services
- created: 2023-02-21 19:38:13.371000+00:00
- modified: 2025-04-15 22:03:56.494000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1021.008: Direct Cloud VM Connections

^t1021008-direct-cloud-vm-connections

**Parent Technique**
- [[T1021-remote_services|T1021: Remote Services]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may leverage [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log directly into accessible cloud hosted compute infrastructure through cloud native methods. Many cloud providers offer interactive connections to virtual infrastructure that can be accessed through the [Cloud API](https://attack.mitre.org/techniques/T1059/009), such as Azure Serial Console(Citation: Azure Serial Console), AWS EC2 Instance Connect(Citation: EC2 Instance Connect)(Citation: lucr-3: Getting SaaS-y in the cloud), and AWS System Manager.(Citation: AWS System Manager).

Methods of authentication for these connections can include passwords, application access tokens, or SSH keys. These cloud native methods may, by default, allow for privileged access on the host with SYSTEM or root level access. 

Adversaries may utilize these cloud native methods to directly access virtual infrastructure and pivot through an environment.(Citation: SIM Swapping and Abuse of the Microsoft Azure Serial Console) These connections typically provide direct console access to the VM rather than the execution of scripts (i.e., [Cloud Administration Command](https://attack.mitre.org/techniques/T1651)).

#### Properties

- id: T1021.008
- name: Direct Cloud VM Connections
- created: 2023-06-02 15:27:55.412000+00:00
- modified: 2025-04-15 22:18:53.305000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Linux
- macOS
- Windows
- IaaS
- ESXi

## Tools

- [[S1063-brute_ratel_c4|S1063: Brute Ratel C4]]

