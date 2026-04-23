---
mitre_id: "T1021"
mitre_name: "Remote Services"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--54a649ff-439a-41a4-9856-8d144a2551ba"
mitre_created: "2017-05-31T21:30:29.858Z"
mitre_modified: "2025-10-24T17:48:48.472Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1021/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "IaaS"
  - "ESXi"
mitre_tactic_ids:
  - "TA0008"
---

# T1021: Remote Services

Adversaries may use [[T1078-valid_accounts|T1078: Valid Accounts]] to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

In an enterprise environment, servers and workstations can be organized into domains. Domains provide centralized identity management, allowing users to login using one set of credentials across the entire network. If an adversary is able to obtain a set of valid domain credentials, they could login to many different machines using remote access protocols such as secure shell (SSH) or remote desktop protocol (RDP).(Citation: SSH Secure Shell)(Citation: TechNet Remote Desktop Services) They could also login to accessible SaaS or IaaS services, such as those that federate their identities to the domain, or management platforms for internal virtualization environments such as VMware vCenter. 

Legitimate applications (such as [[T1072-software_deployment_tools|T1072: Software Deployment Tools]] and other administrative programs) may utilize [[T1021-remote_services|T1021: Remote Services]] to access remote hosts. For example, Apple Remote Desktop (ARD) on macOS is native software used for remote management. ARD leverages a blend of protocols, including [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]] to send the screen and control buffers and [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]] for secure file transfer.(Citation: Remote Management MDM macOS)(Citation: Kickstart Apple Remote Desktop commands)(Citation: Apple Remote Desktop Admin Guide 3.3) Adversaries can abuse applications such as ARD to gain remote code execution and perform lateral movement. In versions of macOS prior to 10.14, an adversary can escalate an SSH session to an ARD session which enables an adversary to accept TCC (Transparency, Consent, and Control) prompts without user interaction and gain access to data.(Citation: FireEye 2019 Apple Remote Desktop)(Citation: Lockboxx ARD 2019)(Citation: Kickstart Apple Remote Desktop commands)

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

## Subtechniques

### T1021.001: Remote Desktop Protocol

^t1021001-remote-desktop-protocol

Adversaries may use [[T1078-valid_accounts|T1078: Valid Accounts]] to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services) 

Adversaries may connect to a remote system over RDP/RDS to expand access if the service is enabled and allows access to accounts with known credentials. Adversaries will likely use Credential Access techniques to acquire credentials to use with RDP. Adversaries may also use RDP in conjunction with the [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]] or [[T1505-server_software_component#^t1505005-terminal-services-dll|T1505.005: Terminal Services DLL]] for Persistence.(Citation: Alperovitch Malware)

### T1021.002: SMB/Windows Admin Shares

^t1021002-smb-windows-admin-shares

Adversaries may use [[T1078-valid_accounts|T1078: Valid Accounts]] to interact with a remote network share using Server Message Block (SMB). The adversary may then perform actions as the logged-on user.

SMB is a file, printer, and serial port sharing protocol for Windows machines on the same network or domain. Adversaries may use SMB to interact with file shares, allowing them to move laterally throughout a network. Linux and macOS implementations of SMB typically use Samba.

Windows systems have hidden network shares that are accessible only to administrators and provide the ability for remote file copy and other administrative functions. Example network shares include `C$`, `ADMIN$`, and `IPC$`. Adversaries may use this technique in conjunction with administrator-level [[T1078-valid_accounts|T1078: Valid Accounts]] to remotely access a networked system over SMB,(Citation: Wikipedia Server Message Block) to interact with systems using remote procedure calls (RPCs),(Citation: TechNet RPC) transfer files, and run transferred binaries through remote Execution. Example execution techniques that rely on authenticated sessions over SMB/RPC are [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]], [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]], and [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]. Adversaries can also use NTLM hashes to access administrator shares on systems with [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]] and certain configuration and patch levels.(Citation: Microsoft Admin Shares)

### T1021.003: Distributed Component Object Model

^t1021003-distributed-component-object-model

Adversaries may use [[T1078-valid_accounts|T1078: Valid Accounts]] to interact with remote machines by taking advantage of Distributed Component Object Model (DCOM). The adversary may then perform actions as the logged-on user.

The Windows Component Object Model (COM) is a component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces. Through COM, a client object can call methods of server objects, which are typically Dynamic Link Libraries (DLL) or executables (EXE). Distributed COM (DCOM) is transparent middleware that extends the functionality of COM beyond a local computer using remote procedure call (RPC) technology.(Citation: Fireeye Hunting COM June 2019)(Citation: Microsoft COM)

Permissions to interact with local and remote server COM objects are specified by access control lists (ACL) in the Registry.(Citation: Microsoft Process Wide Com Keys) By default, only Administrators may remotely activate and launch COM objects through DCOM.(Citation: Microsoft COM ACL)

Through DCOM, adversaries operating in the context of an appropriately privileged user can remotely obtain arbitrary and even direct shellcode execution through Office applications(Citation: Enigma Outlook DCOM Lateral Movement Nov 2017) as well as other Windows objects that contain insecure methods.(Citation: Enigma MMC20 COM Jan 2017)(Citation: Enigma DCOM Lateral Movement Jan 2017) DCOM can also execute macros in existing documents(Citation: Enigma Excel DCOM Sept 2017) and may also invoke [[T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]] (DDE) execution directly through a COM created instance of a Microsoft Office application(Citation: Cyberreason DCOM DDE Lateral Movement Nov 2017), bypassing the need for a malicious document. DCOM can be used as a method of remotely interacting with [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]. (Citation: MSDN WMI)

### T1021.004: SSH

^t1021004-ssh

Adversaries may use [[T1078-valid_accounts|T1078: Valid Accounts]] to log into remote machines using Secure Shell (SSH). The adversary may then perform actions as the logged-on user.

SSH is a protocol that allows authorized users to open remote shells on other computers. Many Linux and macOS versions come with SSH installed by default, although typically disabled until the user enables it. On ESXi, SSH can be enabled either directly on the host (e.g., via `vim-cmd hostsvc/enable_ssh`) or via vCenter.(Citation: Sygnia ESXi Ransomware 2025)(Citation: TrendMicro ESXI Ransomware)(Citation: Sygnia Abyss Locker 2025) The SSH server can be configured to use standard password authentication or public-private keypairs in lieu of or in addition to a password. In this authentication scenario, the user’s public key must be in a special file on the computer running the server that lists which keypairs are allowed to login as that user (i.e., [[T1098-account_manipulation#^t1098004-ssh-authorized-keys|T1098.004: SSH Authorized Keys]]).

### T1021.005: VNC

^t1021005-vnc

Adversaries may use [[T1078-valid_accounts|T1078: Valid Accounts]] to remotely control machines using Virtual Network Computing (VNC).  VNC is a platform-independent desktop sharing system that uses the RFB (“remote framebuffer”) protocol to enable users to remotely control another computer’s display by relaying the screen, mouse, and keyboard inputs over the network.(Citation: The Remote Framebuffer Protocol)

VNC differs from [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]] as VNC is screen-sharing software rather than resource-sharing software. By default, VNC uses the system's authentication, but it can be configured to use credentials specific to VNC.(Citation: MacOS VNC software for Remote Desktop)(Citation: VNC Authentication)

Adversaries may abuse VNC to perform malicious actions as the logged-on user such as opening documents, downloading files, and running arbitrary commands. An adversary could use VNC to remotely control and monitor a system to collect data and information to pivot to other systems within the network. Specific VNC libraries/implementations have also been susceptible to brute force attacks and memory usage exploitation.(Citation: Hijacking VNC)(Citation: macOS root VNC login without authentication)(Citation: VNC Vulnerabilities)(Citation: Offensive Security VNC Authentication Check)(Citation: Attacking VNC Servers PentestLab)(Citation: Havana authentication bug)

### T1021.006: Windows Remote Management

^t1021006-windows-remote-management

Adversaries may use [[T1078-valid_accounts|T1078: Valid Accounts]] to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

WinRM is the name of both a Windows service and a protocol that allows a user to interact with a remote system (e.g., run an executable, modify the Registry, modify services).(Citation: Microsoft WinRM) It may be called with the `winrm` command or by any number of programs such as PowerShell.(Citation: Jacobsen 2014) WinRM  can be used as a method of remotely interacting with [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]].(Citation: MSDN WMI)

### T1021.007: Cloud Services

^t1021007-cloud-services

Adversaries may log into accessible cloud services within a compromised environment using [[T1078-valid_accounts|T1078: Valid Accounts]] that are synchronized with or federated to on-premises user identities. The adversary may then perform management actions or access cloud-hosted resources as the logged-on user. 

Many enterprises federate centrally managed user identities to cloud services, allowing users to login with their domain credentials in order to access the cloud control plane. Similarly, adversaries may connect to available cloud services through the web console or through the cloud command line interface (CLI) (e.g., [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]]), using commands such as `Connect-AZAccount` for Azure PowerShell, `Connect-MgGraph` for Microsoft Graph PowerShell, and `gcloud auth login` for the Google Cloud CLI.

In some cases, adversaries may be able to authenticate to these services via [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]] instead of a username and password. 

### T1021.008: Direct Cloud VM Connections

^t1021008-direct-cloud-vm-connections

Adversaries may leverage [[T1078-valid_accounts|T1078: Valid Accounts]] to log directly into accessible cloud hosted compute infrastructure through cloud native methods. Many cloud providers offer interactive connections to virtual infrastructure that can be accessed through the [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]], such as Azure Serial Console(Citation: Azure Serial Console), AWS EC2 Instance Connect(Citation: EC2 Instance Connect)(Citation: lucr-3: Getting SaaS-y in the cloud), and AWS System Manager.(Citation: AWS System Manager).

Methods of authentication for these connections can include passwords, application access tokens, or SSH keys. These cloud native methods may, by default, allow for privileged access on the host with SYSTEM or root level access. 

Adversaries may utilize these cloud native methods to directly access virtual infrastructure and pivot through an environment.(Citation: SIM Swapping and Abuse of the Microsoft Azure Serial Console) These connections typically provide direct console access to the VM rather than the execution of scripts (i.e., [[T1651-cloud_administration_command|T1651: Cloud Administration Command]]).

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[brute_ratel_c4|Brute Ratel C4]]

## Platforms

- Linux
- macOS
- Windows
- IaaS
- ESXi

