---
mitre_id: "T1137"
mitre_name: "Office Application Startup"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--2c4d4e92-0ccf-4a97-b54c-86d662988a53"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2025-10-24T17:48:34.614Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1137/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0003"
d3fend_ids:
  - "D3-AVE"
  - "D3-CF"
  - "D3-CI"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-DI"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RC"
  - "D3-RD"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RS"
  - "D3-SCP"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page.(Citation: SensePost Ruler GitHub) These persistence mechanisms can work within Outlook or be used through Office 365.(Citation: TechNet O365 Outlook Rules)

## Workspace

- [[workspaces/attack/techniques/T1137-office_application_startup-note|Open workspace note]]

![[workspaces/attack/techniques/T1137-office_application_startup-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/0e20c89d_2264_44ae_8238_aeeaba609ece-potential_persistence_via_microsoft_office_startup_folder|Potential Persistence Via Microsoft Office Startup Folder (high; windows / file_event)]]
- [[kb/sigma/rules/117d3d3a_755c_4a61_b23e_9171146d094c-suspicious_outlook_macro_created|Suspicious Outlook Macro Created (high; windows / file_event)]]
- [[kb/sigma/rules/36fbec91_fa1b_4d5d_8df1_8d8edcb632ad-code_executed_via_office_add_in_xll_file|Code Executed Via Office Add-in XLL File (high; windows / ps_script)]]
- [[kb/sigma/rules/396ae3eb_4174_4b9b_880e_dc0364d78a19-potential_persistence_via_outlook_loadmacroprovideronboot_setting|Potential Persistence Via Outlook LoadMacroProviderOnBoot Setting (high; windows / registry_set)]]
- [[kb/sigma/rules/69483748_1525_4a6c_95ca_90dc8d431b68-suspicious_microsoft_office_child_process_macos|Suspicious Microsoft Office Child Process - MacOS (high; macos / process_creation)]]
- [[kb/sigma/rules/8e1cb247_6cf6_42fa_b440_3f27d57e9936-potential_persistence_via_microsoft_office_add_in|Potential Persistence Via Microsoft Office Add-In (high; windows / file_event)]]
- [[kb/sigma/rules/961e33d1_4f86_4fcf_80ab_930a708b2f82-potential_persistence_via_excel_add_in_registry|Potential Persistence Via Excel Add-in - Registry (high; windows / registry_set)]]
- [[kb/sigma/rules/c3edc6a5_d9d4_48d8_930e_aab518390917-potential_persistence_via_outlook_form|Potential Persistence Via Outlook Form (high; windows / file_event)]]
- [[kb/sigma/rules/e3b50fa5_3c3f_444e_937b_0a99d33731cd-outlook_macro_execution_without_warning_setting_enabled|Outlook Macro Execution Without Warning Setting Enabled (high; windows / registry_set)]]

### Atomic Tests

- [[kb/atomic/tests/082141ed_b048_4c86_99c7_2b8da5b5bf48-persistent_code_execution_via_excel_vba_add_in_file_xlam|Persistent Code Execution Via Excel VBA Add-in File (XLAM) (powershell; windows)]]
- [[kb/atomic/tests/441b1a0f_a771_428a_8af0_e99e4698cda3-code_executed_via_excel_add_in_file_xll|Code Executed Via Excel Add-in File (XLL) (powershell; windows)]]
- [[kb/atomic/tests/5ff5249a_5807_480e_ab52_c430497a8a25-outlook_rules_enumerate_existing_rules_via_powershell_com_object|Outlook Rules - Enumerate Existing Rules via PowerShell COM Object (powershell; windows)]]
- [[kb/atomic/tests/7a91ad51_e6d2_4d43_9471_f26362f5738e-install_outlook_home_page_persistence|Install Outlook Home Page Persistence (command_prompt; windows)]]
- [[kb/atomic/tests/940db09e_80b6_4dd0_8d4d_7764f89b47a8-injecting_a_macro_into_the_word_normal_dotm_template_for_persistence_via_powershell|Injecting a Macro into the Word Normal.dotm Template for Persistence via PowerShell (powershell; windows)]]
- [[kb/atomic/tests/95408a99_4fa7_4cd6_a7ef_cb65f86351cf-persistent_code_execution_via_word_add_in_file_wll|Persistent Code Execution Via Word Add-in File (WLL) (powershell; windows)]]
- [[kb/atomic/tests/9c307886_9fef_41d5_b344_073a0f5b2f5f-persistent_code_execution_via_excel_add_in_file_xll|Persistent Code Execution Via Excel Add-in File (XLL) (powershell; windows)]]
- [[kb/atomic/tests/b0bd3d76_a57c_4699_83f4_8cd798dd09bd-outlook_rule_auto_forward_emails_to_external_address_via_com_object|Outlook Rule - Auto-Forward Emails to External Address via COM Object (powershell; windows)]]
- [[kb/atomic/tests/bddfd8d4_7687_4971_b611_50a537ab3ab4-outlook_rule_sender_address_trigger_with_deletepermanently_action_via_com_object|Outlook Rule - Sender Address Trigger with DeletePermanently Action via COM Object (powershell; windows)]]
- [[kb/atomic/tests/bfe6ac15_c50b_4c4f_a186_0fc6b8ba936c-office_application_startup_outlook_as_a_c2|Office Application Startup - Outlook as a C2 (command_prompt; windows)]]
- 4 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SCP-system_configuration_permissions|D3-SCP: System Configuration Permissions]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Subtechniques

### T1137.001: Office Template Macros

^t1137001-office-template-macros

Adversaries may abuse Microsoft Office templates to obtain persistence on a compromised system. Microsoft Office contains templates that are part of common Office applications and are used to customize styles. The base templates within the application are used each time an application starts. (Citation: Microsoft Change Normal Template)

Office Visual Basic for Applications (VBA) macros (Citation: MSDN VBA in Office) can be inserted into the base template and used to execute code when the respective Office application starts in order to obtain persistence. Examples for both Word and Excel have been discovered and published. By default, Word has a Normal.dotm template created that can be modified to include a malicious macro. Excel does not have a template file created by default, but one can be added that will automatically be loaded.(Citation: enigma0x3 normal.dotm)(Citation: Hexacorn Office Template Macros) Shared templates may also be stored and pulled from remote locations.(Citation: GlobalDotName Jun 2019) 

Word Normal.dotm location:<br>
`C:\Users\&lt;username&gt;\AppData\Roaming\Microsoft\Templates\Normal.dotm`

Excel Personal.xlsb location:<br>
`C:\Users\&lt;username&gt;\AppData\Roaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB`

Adversaries may also change the location of the base template to point to their own by hijacking the application's search order, e.g. Word 2016 will first look for Normal.dotm under `C:\Program Files (x86)\Microsoft Office\root\Office16\`, or by modifying the GlobalDotName registry key. By modifying the GlobalDotName registry key an adversary can specify an arbitrary location, file name, and file extension to use for the template that will be loaded on application startup. To abuse GlobalDotName, adversaries may first need to register the template as a trusted document or place it in a trusted location.(Citation: GlobalDotName Jun 2019) 

An adversary may need to enable macros to execute unrestricted depending on the system or enterprise security policy on use of macros.

### T1137.002: Office Test

^t1137002-office-test

Adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system. An Office Test Registry location exists that allows a user to specify an arbitrary DLL that will be executed every time an Office application is started. This Registry key is thought to be used by Microsoft to load DLLs for testing and debugging purposes while developing Office applications. This Registry key is not created by default during an Office installation.(Citation: Hexacorn Office Test)(Citation: Palo Alto Office Test Sofacy)

There exist user and global Registry keys for the Office Test feature, such as:

* `HKEY_CURRENT_USER\Software\Microsoft\Office test\Special\Perf`
* `HKEY_LOCAL_MACHINE\Software\Microsoft\Office test\Special\Perf`

Adversaries may add this Registry key and specify a malicious DLL that will be executed whenever an Office application, such as Word or Excel, is started.

### T1137.003: Outlook Forms

^t1137003-outlook-forms

Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system. Outlook forms are used as templates for presentation and functionality in Outlook messages. Custom Outlook forms can be created that will execute code when a specifically crafted email is sent by an adversary utilizing the same custom Outlook form.(Citation: SensePost Outlook Forms)

Once malicious forms have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious forms will execute when an adversary sends a specifically crafted email to the user.(Citation: SensePost Outlook Forms)

### T1137.004: Outlook Home Page

^t1137004-outlook-home-page

Adversaries may abuse Microsoft Outlook's Home Page feature to obtain persistence on a compromised system. Outlook Home Page is a legacy feature used to customize the presentation of Outlook folders. This feature allows for an internal or external URL to be loaded and presented whenever a folder is opened. A malicious HTML page can be crafted that will execute code when loaded by Outlook Home Page.(Citation: SensePost Outlook Home Page)

Once malicious home pages have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious Home Pages will execute when the right Outlook folder is loaded/reloaded.(Citation: SensePost Outlook Home Page)


### T1137.005: Outlook Rules

^t1137005-outlook-rules

Adversaries may abuse Microsoft Outlook rules to obtain persistence on a compromised system. Outlook rules allow a user to define automated behavior to manage email messages. A benign rule might, for example, automatically move an email to a particular folder in Outlook if it contains specific words from a specific sender. Malicious Outlook rules can be created that can trigger code execution when an adversary sends a specifically crafted email to that user.(Citation: SilentBreak Outlook Rules)

Once malicious rules have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious rules will execute when an adversary sends a specifically crafted email to the user.(Citation: SilentBreak Outlook Rules)

### T1137.006: Add-ins

^t1137006-add-ins

Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system. Office add-ins can be used to add functionality to Office programs. (Citation: Microsoft Office Add-ins) There are different types of add-ins that can be used by the various Office products; including Word/Excel add-in Libraries (WLL/XLL), VBA add-ins, Office Component Object Model (COM) add-ins, automation add-ins, VBA Editor (VBE), Visual Studio Tools for Office (VSTO) add-ins, and Outlook add-ins. (Citation: MRWLabs Office Persistence Add-ins)(Citation: FireEye Mail CDS 2018)

Add-ins can be used to obtain persistence because they can be set to execute code when an Office application starts. 

## Mitigations

- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1051-update_software|M1051: Update Software]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Windows
- Office Suite

