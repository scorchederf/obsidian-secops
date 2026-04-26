---
mitre_id: "T1195"
mitre_name: "Supply Chain Compromise"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3f18edba-28f4-4bb9-82c3-8aa60dcac5f7"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:48:41.675Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1195/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
  - "SaaS"
mitre_tactic_ids:
  - "TA0001"
d3fend_ids:
  - "D3-AVE"
  - "D3-HCI"
  - "D3-RH"
  - "D3-RS"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise.

Supply chain compromise can take place at any stage of the supply chain including:

* Manipulation of development tools
* Manipulation of a development environment
* Manipulation of source code repositories (public or private)
* Manipulation of source code in open-source dependencies
* Manipulation of software update/distribution mechanisms
* Compromised/infected system images (removable media infected at the factory)(Citation: IBM Storwize)(Citation: Schneider Electric USB Malware) 
* Replacement of legitimate software with modified versions
* Sales of modified/counterfeit products to legitimate distributors
* Shipment interdiction

While supply chain compromise can impact any component of hardware or software, adversaries looking to gain execution have often focused on malicious additions to legitimate software in software distribution or update channels.(Citation: Avast CCleaner3 2018)(Citation: Microsoft Dofoil 2018)(Citation: Command Five SK 2011) Adversaries may limit targeting to a desired victim set or distribute malicious software to a broad set of consumers but only follow up with specific victims.(Citation: Symantec Elderwood Sept 2012)(Citation: Avast CCleaner3 2018)(Citation: Command Five SK 2011) Popular open-source projects that are used as dependencies in many applications may also be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)

In some cases, adversaries may conduct “second-order” supply chain compromises by leveraging the access gained from an initial supply chain compromise to further compromise a software component.(Citation: Krebs 3cx overview 2023) This may allow the threat actor to spread to even more victims.  

## Workspace

- [[workspaces/attack/techniques/T1195-supply_chain_compromise-note|Open workspace note]]

![[workspaces/attack/techniques/T1195-supply_chain_compromise-note]]

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Subtechniques

### T1195.001: Compromise Software Dependencies and Development Tools

^t1195001-compromise-software-dependencies-and-development-tools

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications, such as pip and NPM packages, may be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)(Citation: Bitdefender NPM Repositories Compromised 2021)(Citation: MANDVI Malicious npm and PyPI Packages Disguised) This may also include abandoned packages, which in some cases could be re-registered by threat actors after being removed by adversaries.(Citation: The Hacker News PyPi Revival Hijack 2024) Adversaries may also employ "typosquatting" or name-confusion by choosing names similar to existing popular libraries or packages in order to deceive a user.(Citation: Ahmed Backdoors in Python and NPM Packages)(Citation: Meyer PyPI Supply Chain Attack Uncovered)(Citation: Checkmarx-oss-seo)

Additionally, CI/CD pipeline components, such as GitHub Actions, may be targeted in order to gain access to the building, testing, and deployment cycles of an application.(Citation: Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025) By adding malicious code into a GitHub action, a threat actor may be able to collect runtime credentials (e.g., via [[T1003-os_credential_dumping#^t1003007-proc-filesystem|T1003.007: Proc Filesystem]]) or insert further malicious components into the build pipelines for a second-order supply chain compromise.(Citation: OWASP CICD-SEC-4) As GitHub Actions are often dependent on other GitHub Actions, threat actors may be able to infect a large number of repositories via the compromise of a single Action.(Citation: Palo Alto Networks GitHub Actions Worm 2023)

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims. 

### T1195.002: Compromise Software Supply Chain

^t1195002-compromise-software-supply-chain

Adversaries may manipulate application software prior to receipt by a final consumer for the purpose of data or system compromise. Supply chain compromise of software can take place in a number of ways, including manipulation of the application source code, manipulation of the update/distribution mechanism for that software, or replacing compiled releases with a modified version.

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.(Citation: Avast CCleaner3 2018)(Citation: Command Five SK 2011)  

### T1195.003: Compromise Hardware Supply Chain

^t1195003-compromise-hardware-supply-chain

Adversaries may manipulate hardware components in products prior to receipt by a final consumer for the purpose of data or system compromise. By modifying hardware or firmware in the supply chain, adversaries can insert a backdoor into consumer networks that may be difficult to detect and give the adversary a high degree of control over the system. Hardware backdoors may be inserted into various devices, such as servers, workstations, network infrastructure, or peripherals.

## Mitigations

- [[M1013-application_developer_guidance|M1013: Application Developer Guidance]]
- [[M1016-vulnerability_scanning|M1016: Vulnerability Scanning]]
- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1033-limit_software_installation|M1033: Limit Software Installation]]
- [[M1046-boot_integrity|M1046: Boot Integrity]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- Linux
- Windows
- macOS
- SaaS

