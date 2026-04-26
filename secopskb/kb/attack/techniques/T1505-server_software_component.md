---
mitre_id: "T1505"
mitre_name: "Server Software Component"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d456de47-a16f-4e46-8980-e67478a12dcb"
mitre_created: "2019-06-28T17:52:07.296Z"
mitre_modified: "2025-10-24T17:49:27.065Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1505/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "ESXi"
mitre_tactic_ids:
  - "TA0003"
d3fend_ids:
  - "D3-ABPI"
  - "D3-AVE"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-CS"
  - "D3-DA"
  - "D3-DF"
  - "D3-DLV"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-EHB"
  - "D3-ER"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-HR"
  - "D3-HS"
  - "D3-KBPI"
  - "D3-LFP"
  - "D3-LLM"
  - "D3-NNI"
  - "D3-PLA"
  - "D3-PLM"
  - "D3-PS"
  - "D3-PSA"
  - "D3-PSMD"
  - "D3-PT"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RNA"
  - "D3-RS"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-SU"
  - "D3-SWI"
  - "D3-TL"
  - "D3-VI"
  - "D3-WSAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may abuse legitimate extensible development features of servers to establish persistent access to systems. Enterprise server applications may include features that allow developers to write and install software or scripts to extend the functionality of the main application. Adversaries may install malicious components to extend and abuse server applications.(Citation: volexity_0day_sophos_FW)

## Workspace

- [[workspaces/attack/techniques/T1505-server_software_component-note|Open workspace note]]

![[workspaces/attack/techniques/T1505-server_software_component-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-ABPI-application-based_process_isolation|D3-ABPI: Application-based Process Isolation]]
- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-CS-credential_scrubbing|D3-CS: Credential Scrubbing]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DLV-domain_logic_validation|D3-DLV: Domain Logic Validation]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-EHB-endpoint_health_beacon|D3-EHB: Endpoint Health Beacon]]
- [[D3-ER-email_removal|D3-ER: Email Removal]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-HR-host_reboot|D3-HR: Host Reboot]]
- [[D3-HS-host_shutdown|D3-HS: Host Shutdown]]
- [[D3-KBPI-kernel-based_process_isolation|D3-KBPI: Kernel-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-LLM-logical_link_mapping|D3-LLM: Logical Link Mapping]]
- [[D3-NNI-network_node_inventory|D3-NNI: Network Node Inventory]]
- [[D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]
- [[D3-PLM-physical_link_mapping|D3-PLM: Physical Link Mapping]]
- [[D3-PS-process_suspension|D3-PS: Process Suspension]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-PSMD-process_self-modification_detection|D3-PSMD: Process Self-Modification Detection]]
- [[D3-PT-process_termination|D3-PT: Process Termination]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RNA-restore_network_access|D3-RNA: Restore Network Access]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]
- [[D3-TL-trusted_library|D3-TL: Trusted Library]]
- [[D3-VI-variable_initialization|D3-VI: Variable Initialization]]
- [[D3-WSAM-web_session_access_mediation|D3-WSAM: Web Session Access Mediation]]

## Subtechniques

### T1505.001: SQL Stored Procedures

^t1505001-sql-stored-procedures

Adversaries may abuse SQL stored procedures to establish persistent access to systems. SQL Stored Procedures are code that can be saved and reused so that database users do not waste time rewriting frequently used SQL queries. Stored procedures can be invoked via SQL statements to the database using the procedure name or via defined events (e.g. when a SQL server application is started/restarted).

Adversaries may craft malicious stored procedures that can provide a persistence mechanism in SQL database servers.(Citation: NetSPI Startup Stored Procedures)(Citation: Kaspersky MSSQL Aug 2019) To execute operating system commands through SQL syntax the adversary may have to enable additional functionality, such as xp_cmdshell for MSSQL Server.(Citation: NetSPI Startup Stored Procedures)(Citation: Kaspersky MSSQL Aug 2019)(Citation: Microsoft xp_cmdshell 2017) 

Microsoft SQL Server can enable common language runtime (CLR) integration. With CLR integration enabled, application developers can write stored procedures using any .NET framework language (e.g. VB .NET, C#, etc.).(Citation: Microsoft CLR Integration 2017) Adversaries may craft or modify CLR assemblies that are linked to stored procedures since these CLR assemblies can be made to execute arbitrary commands.(Citation: NetSPI SQL Server CLR) 

### T1505.002: Transport Agent

^t1505002-transport-agent

Adversaries may abuse Microsoft transport agents to establish persistent access to systems. Microsoft Exchange transport agents can operate on email messages passing through the transport pipeline to perform various tasks such as filtering spam, filtering malicious attachments, journaling, or adding a corporate signature to the end of all outgoing emails.(Citation: Microsoft TransportAgent Jun 2016)(Citation: ESET LightNeuron May 2019) Transport agents can be written by application developers and then compiled to .NET assemblies that are subsequently registered with the Exchange server. Transport agents will be invoked during a specified stage of email processing and carry out developer defined tasks. 

Adversaries may register a malicious transport agent to provide a persistence mechanism in Exchange Server that can be triggered by adversary-specified email events.(Citation: ESET LightNeuron May 2019) Though a malicious transport agent may be invoked for all emails passing through the Exchange transport pipeline, the agent can be configured to only carry out specific tasks in response to adversary defined criteria. For example, the transport agent may only carry out an action like copying in-transit attachments and saving them for later exfiltration if the recipient email address matches an entry on a list provided by the adversary. 

### T1505.003: Web Shell

^t1505003-web-shell

Adversaries may backdoor web servers with web shells to establish persistent access to systems. A Web shell is a Web script that is placed on an openly accessible Web server to allow an adversary to access the Web server as a gateway into a network. A Web shell may provide a set of functions to execute or a command-line interface on the system that hosts the Web server.(Citation: volexity_0day_sophos_FW)

In addition to a server-side script, a Web shell may have a client interface program that is used to talk to the Web server (e.g. [China Chopper](https://attack.mitre.org/software/S0020) Web shell client).(Citation: Lee 2013)

### T1505.004: IIS Components

^t1505004-iis-components

Adversaries may install malicious components that run on Internet Information Services (IIS) web servers to establish persistence. IIS provides several mechanisms to extend the functionality of the web servers. For example, Internet Server Application Programming Interface (ISAPI) extensions and filters can be installed to examine and/or modify incoming and outgoing IIS web requests. Extensions and filters are deployed as DLL files that export three functions: `Get{Extension/Filter}Version`, `Http{Extension/Filter}Proc`, and (optionally) `Terminate{Extension/Filter}`. IIS modules may also be installed to extend IIS web servers.(Citation: Microsoft ISAPI Extension Overview 2017)(Citation: Microsoft ISAPI Filter Overview 2017)(Citation: IIS Backdoor 2011)(Citation: Trustwave IIS Module 2013)

Adversaries may install malicious ISAPI extensions and filters to observe and/or modify traffic, execute commands on compromised machines, or proxy command and control traffic. ISAPI extensions and filters may have access to all IIS web requests and responses. For example, an adversary may abuse these mechanisms to modify HTTP responses in order to distribute malicious commands/content to previously comprised hosts.(Citation: Microsoft ISAPI Filter Overview 2017)(Citation: Microsoft ISAPI Extension Overview 2017)(Citation: Microsoft ISAPI Extension All Incoming 2017)(Citation: Dell TG-3390)(Citation: Trustwave IIS Module 2013)(Citation: MMPC ISAPI Filter 2012)

Adversaries may also install malicious IIS modules to observe and/or modify traffic. IIS 7.0 introduced modules that provide the same unrestricted access to HTTP requests and responses as ISAPI extensions and filters. IIS modules can be written as a DLL that exports `RegisterModule`, or as a .NET application that interfaces with ASP.NET APIs to access IIS HTTP requests.(Citation: Microsoft IIS Modules Overview 2007)(Citation: Trustwave IIS Module 2013)(Citation: ESET IIS Malware 2021)

### T1505.005: Terminal Services DLL

^t1505005-terminal-services-dll

Adversaries may abuse components of Terminal Services to enable persistent access to systems. Microsoft Terminal Services, renamed to Remote Desktop Services in some Windows Server OSs as of 2022, enable remote terminal connections to hosts. Terminal Services allows servers to transmit a full, interactive, graphical user interface to clients via RDP.(Citation: Microsoft Remote Desktop Services)

[[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]s that are run as a "generic" process (ex: `svchost.exe`) load the service's DLL file, the location of which is stored in a Registry entry named `ServiceDll`.(Citation: Microsoft System Services Fundamentals) The `termsrv.dll` file, typically stored in `%SystemRoot%\System32\`, is the default `ServiceDll` value for Terminal Services in `HKLM\System\CurrentControlSet\services\TermService\Parameters\`.

Adversaries may modify and/or replace the Terminal Services DLL to enable persistent access to victimized hosts.(Citation: James TermServ DLL) Modifications to this DLL could be done to execute arbitrary payloads (while also potentially preserving normal `termsrv.dll` functionality) as well as to simply enable abusable features of Terminal Services. For example, an adversary may enable features such as concurrent [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]] sessions by either patching the `termsrv.dll` file or modifying the `ServiceDll` value to point to a DLL that provides increased RDP functionality.(Citation: Windows OS Hub RDP)(Citation: RDPWrap Github) On a non-server Windows OS this increased functionality may also enable an adversary to avoid Terminal Services prompts that warn/log out users of a system when a new RDP session is created.

### T1505.006: vSphere Installation Bundles

^t1505006-vsphere-installation-bundles

Adversaries may abuse vSphere Installation Bundles (VIBs) to establish persistent access to ESXi hypervisors. VIBs are collections of files used for software distribution and virtual system management in VMware environments. Since ESXi uses an in-memory filesystem where changes made to most files are stored in RAM rather than in persistent storage, these modifications are lost after a reboot. However, VIBs can be used to create startup tasks, apply custom firewall rules, or deploy binaries that persist across reboots. Typically, administrators use VIBs for updates and system maintenance.

VIBs can be broken down into three components:(Citation: VMware VIBs)

* VIB payload: a `.vgz` archive containing the directories and files to be created and executed on boot when the VIBs are loaded.  
* Signature file: verifies the host acceptance level of a VIB, indicating what testing and validation has been done by VMware or its partners before publication of a VIB. By default, ESXi hosts require a minimum acceptance level of PartnerSupported for VIB installation, meaning the VIB is published by a trusted VMware partner. However, privileged users can change the default acceptance level using the `esxcli` command line interface. Additionally, VIBs are able to be installed regardless of acceptance level by using the `esxcli software vib install --force` command. 
* XML descriptor file: a configuration file containing associated VIB metadata, such as the name of the VIB and its dependencies.  

Adversaries may leverage malicious VIB packages to maintain persistent access to ESXi hypervisors, allowing system changes to be executed upon each bootup of ESXi – such as using  `esxcli` to enable firewall rules for backdoor traffic, creating listeners on hard coded ports, and executing backdoors.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) Adversaries may also masquerade their malicious VIB files as PartnerSupported by modifying the XML descriptor file.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1024-restrict_registry_permissions|M1024: Restrict Registry Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1045-code_signing|M1045: Code Signing]]
- [[M1046-boot_integrity|M1046: Boot Integrity]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Windows
- Linux
- macOS
- Network Devices
- ESXi

