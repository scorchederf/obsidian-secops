---
id: T1195
name: Supply Chain Compromise
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-10-24 17:48:41.675000+00:00
type: attack-pattern
x_mitre_version: 1.7
x_mitre_domains: enterprise-attack
---

## Tactic

- [[initial_access|Initial Access]]

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

## Subtechniques

### T1195.001: Compromise Software Dependencies and Development Tools
^t1195001-compromise-software-dependencies-and-development-tools

**Parent Technique**
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]

**Tactic**
- [[initial_access|Initial Access]]

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications, such as pip and NPM packages, may be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)(Citation: Bitdefender NPM Repositories Compromised 2021)(Citation: MANDVI Malicious npm and PyPI Packages Disguised) This may also include abandoned packages, which in some cases could be re-registered by threat actors after being removed by adversaries.(Citation: The Hacker News PyPi Revival Hijack 2024) Adversaries may also employ "typosquatting" or name-confusion by choosing names similar to existing popular libraries or packages in order to deceive a user.(Citation: Ahmed Backdoors in Python and NPM Packages)(Citation: Meyer PyPI Supply Chain Attack Uncovered)(Citation: Checkmarx-oss-seo)

Additionally, CI/CD pipeline components, such as GitHub Actions, may be targeted in order to gain access to the building, testing, and deployment cycles of an application.(Citation: Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025) By adding malicious code into a GitHub action, a threat actor may be able to collect runtime credentials (e.g., via [Proc Filesystem](https://attack.mitre.org/techniques/T1003/007)) or insert further malicious components into the build pipelines for a second-order supply chain compromise.(Citation: OWASP CICD-SEC-4) As GitHub Actions are often dependent on other GitHub Actions, threat actors may be able to infect a large number of repositories via the compromise of a single Action.(Citation: Palo Alto Networks GitHub Actions Worm 2023)

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims. 

#### Properties

- id: T1195.001
- name: Compromise Software Dependencies and Development Tools
- created: 2020-03-11 14:13:42.916000+00:00
- modified: 2025-10-24 17:48:27.436000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1195.002: Compromise Software Supply Chain
^t1195002-compromise-software-supply-chain

**Parent Technique**
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]

**Tactic**
- [[initial_access|Initial Access]]

Adversaries may manipulate application software prior to receipt by a final consumer for the purpose of data or system compromise. Supply chain compromise of software can take place in a number of ways, including manipulation of the application source code, manipulation of the update/distribution mechanism for that software, or replacing compiled releases with a modified version.

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.(Citation: Avast CCleaner3 2018)(Citation: Command Five SK 2011)  

#### Properties

- id: T1195.002
- name: Compromise Software Supply Chain
- created: 2020-03-11 14:17:21.153000+00:00
- modified: 2025-10-24 17:49:18.341000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1195.003: Compromise Hardware Supply Chain
^t1195003-compromise-hardware-supply-chain

**Parent Technique**
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]

**Tactic**
- [[initial_access|Initial Access]]

Adversaries may manipulate hardware components in products prior to receipt by a final consumer for the purpose of data or system compromise. By modifying hardware or firmware in the supply chain, adversaries can insert a backdoor into consumer networks that may be difficult to detect and give the adversary a high degree of control over the system. Hardware backdoors may be inserted into various devices, such as servers, workstations, network infrastructure, or peripherals.

#### Properties

- id: T1195.003
- name: Compromise Hardware Supply Chain
- created: 2020-03-11 14:28:40.064000+00:00
- modified: 2025-10-24 17:48:39.693000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

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

## Tools


