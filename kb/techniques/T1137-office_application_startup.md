---
id: T1137
name: Office Application Startup
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:34.614000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page.(Citation: SensePost Ruler GitHub) These persistence mechanisms can work within Outlook or be used through Office 365.(Citation: TechNet O365 Outlook Rules)

## Subtechniques

### T1137.001: Office Template Macros
^t1137001-office-template-macros

**Parent Technique**
- [[T1137-office_application_startup|T1137: Office Application Startup]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse Microsoft Office templates to obtain persistence on a compromised system. Microsoft Office contains templates that are part of common Office applications and are used to customize styles. The base templates within the application are used each time an application starts. (Citation: Microsoft Change Normal Template)

Office Visual Basic for Applications (VBA) macros (Citation: MSDN VBA in Office) can be inserted into the base template and used to execute code when the respective Office application starts in order to obtain persistence. Examples for both Word and Excel have been discovered and published. By default, Word has a Normal.dotm template created that can be modified to include a malicious macro. Excel does not have a template file created by default, but one can be added that will automatically be loaded.(Citation: enigma0x3 normal.dotm)(Citation: Hexacorn Office Template Macros) Shared templates may also be stored and pulled from remote locations.(Citation: GlobalDotName Jun 2019) 

Word Normal.dotm location:<br>
<code>C:\Users\&lt;username&gt;\AppData\Roaming\Microsoft\Templates\Normal.dotm</code>

Excel Personal.xlsb location:<br>
<code>C:\Users\&lt;username&gt;\AppData\Roaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB</code>

Adversaries may also change the location of the base template to point to their own by hijacking the application's search order, e.g. Word 2016 will first look for Normal.dotm under <code>C:\Program Files (x86)\Microsoft Office\root\Office16\</code>, or by modifying the GlobalDotName registry key. By modifying the GlobalDotName registry key an adversary can specify an arbitrary location, file name, and file extension to use for the template that will be loaded on application startup. To abuse GlobalDotName, adversaries may first need to register the template as a trusted document or place it in a trusted location.(Citation: GlobalDotName Jun 2019) 

An adversary may need to enable macros to execute unrestricted depending on the system or enterprise security policy on use of macros.

#### Properties

- id: T1137.001
- name: Office Template Macros
- created: 2019-11-07 20:29:17.788000+00:00
- modified: 2025-10-24 17:48:59.432000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1137.002: Office Test
^t1137002-office-test

**Parent Technique**
- [[T1137-office_application_startup|T1137: Office Application Startup]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system. An Office Test Registry location exists that allows a user to specify an arbitrary DLL that will be executed every time an Office application is started. This Registry key is thought to be used by Microsoft to load DLLs for testing and debugging purposes while developing Office applications. This Registry key is not created by default during an Office installation.(Citation: Hexacorn Office Test)(Citation: Palo Alto Office Test Sofacy)

There exist user and global Registry keys for the Office Test feature, such as:

* <code>HKEY_CURRENT_USER\Software\Microsoft\Office test\Special\Perf</code>
* <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Office test\Special\Perf</code>

Adversaries may add this Registry key and specify a malicious DLL that will be executed whenever an Office application, such as Word or Excel, is started.

#### Properties

- id: T1137.002
- name: Office Test
- created: 2019-11-07 19:44:04.475000+00:00
- modified: 2025-10-24 17:49:34.588000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1137.003: Outlook Forms
^t1137003-outlook-forms

**Parent Technique**
- [[T1137-office_application_startup|T1137: Office Application Startup]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system. Outlook forms are used as templates for presentation and functionality in Outlook messages. Custom Outlook forms can be created that will execute code when a specifically crafted email is sent by an adversary utilizing the same custom Outlook form.(Citation: SensePost Outlook Forms)

Once malicious forms have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious forms will execute when an adversary sends a specifically crafted email to the user.(Citation: SensePost Outlook Forms)

#### Properties

- id: T1137.003
- name: Outlook Forms
- created: 2019-11-07 20:06:02.624000+00:00
- modified: 2025-10-24 17:49:12.562000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1137.004: Outlook Home Page
^t1137004-outlook-home-page

**Parent Technique**
- [[T1137-office_application_startup|T1137: Office Application Startup]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse Microsoft Outlook's Home Page feature to obtain persistence on a compromised system. Outlook Home Page is a legacy feature used to customize the presentation of Outlook folders. This feature allows for an internal or external URL to be loaded and presented whenever a folder is opened. A malicious HTML page can be crafted that will execute code when loaded by Outlook Home Page.(Citation: SensePost Outlook Home Page)

Once malicious home pages have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious Home Pages will execute when the right Outlook folder is loaded/reloaded.(Citation: SensePost Outlook Home Page)


#### Properties

- id: T1137.004
- name: Outlook Home Page
- created: 2019-11-07 20:09:56.536000+00:00
- modified: 2025-10-24 17:49:18.872000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1137.005: Outlook Rules
^t1137005-outlook-rules

**Parent Technique**
- [[T1137-office_application_startup|T1137: Office Application Startup]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse Microsoft Outlook rules to obtain persistence on a compromised system. Outlook rules allow a user to define automated behavior to manage email messages. A benign rule might, for example, automatically move an email to a particular folder in Outlook if it contains specific words from a specific sender. Malicious Outlook rules can be created that can trigger code execution when an adversary sends a specifically crafted email to that user.(Citation: SilentBreak Outlook Rules)

Once malicious rules have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious rules will execute when an adversary sends a specifically crafted email to the user.(Citation: SilentBreak Outlook Rules)

#### Properties

- id: T1137.005
- name: Outlook Rules
- created: 2019-11-07 20:00:25.560000+00:00
- modified: 2025-10-24 17:48:41.026000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1137.006: Add-ins
^t1137006-add-ins

**Parent Technique**
- [[T1137-office_application_startup|T1137: Office Application Startup]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system. Office add-ins can be used to add functionality to Office programs. (Citation: Microsoft Office Add-ins) There are different types of add-ins that can be used by the various Office products; including Word/Excel add-in Libraries (WLL/XLL), VBA add-ins, Office Component Object Model (COM) add-ins, automation add-ins, VBA Editor (VBE), Visual Studio Tools for Office (VSTO) add-ins, and Outlook add-ins. (Citation: MRWLabs Office Persistence Add-ins)(Citation: FireEye Mail CDS 2018)

Add-ins can be used to obtain persistence because they can be set to execute code when an Office application starts. 

#### Properties

- id: T1137.006
- name: Add-ins
- created: 2019-11-07 19:52:52.801000+00:00
- modified: 2025-10-24 17:48:37.911000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1051-update_software|M1051: Update Software]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Windows
- Office Suite

