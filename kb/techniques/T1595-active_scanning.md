---
id: T1595
name: Active Scanning
created: 2020-10-02 16:53:16.526000+00:00
modified: 2025-10-24 17:48:53.018000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[reconnaissance|Reconnaissance]]

Adversaries may execute active reconnaissance scans to gather information that can be used during targeting. Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of reconnaissance that do not involve direct interaction.

Adversaries may perform different forms of active scanning depending on what information they seek to gather. These scans can also be performed in various ways, including using native features of network protocols such as ICMP.(Citation: Botnet Scan)(Citation: OWASP Fingerprinting) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190)).

## Subtechniques

### T1595.001: Scanning IP Blocks
^t1595001-scanning-ip-blocks

**Parent Technique**
- [[T1595-active_scanning|T1595: Active Scanning]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may scan victim IP blocks to gather information that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses.

Adversaries may scan IP blocks in order to [Gather Victim Network Information](https://attack.mitre.org/techniques/T1590), such as which IP addresses are actively in use as well as more detailed information about hosts assigned these addresses. Scans may range from simple pings (ICMP requests and responses) to more nuanced scans that may reveal host software/versions via server banners or other network artifacts.(Citation: Botnet Scan) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

#### Properties

- id: T1595.001
- name: Scanning IP Blocks
- created: 2020-10-02 16:54:23.193000+00:00
- modified: 2025-10-24 17:49:28.603000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1595.002: Vulnerability Scanning
^t1595002-vulnerability-scanning

**Parent Technique**
- [[T1595-active_scanning|T1595: Active Scanning]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may scan victims for vulnerabilities that can be used during targeting. Vulnerability scans typically check if the configuration of a target host/application (ex: software and version) potentially aligns with the target of a specific exploit the adversary may seek to use.

These scans may also include more broad attempts to [Gather Victim Host Information](https://attack.mitre.org/techniques/T1592) that can be used to identify more commonly known, exploitable vulnerabilities. Vulnerability scans typically harvest running software and version numbers via server banners, listening ports, or other network artifacts.(Citation: OWASP Vuln Scanning) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190)).

#### Properties

- id: T1595.002
- name: Vulnerability Scanning
- created: 2020-10-02 16:55:16.047000+00:00
- modified: 2025-10-24 17:48:48.647000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1595.003: Wordlist Scanning
^t1595003-wordlist-scanning

**Parent Technique**
- [[T1595-active_scanning|T1595: Active Scanning]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may iteratively probe infrastructure using brute-forcing and crawling techniques. While this technique employs similar methods to [Brute Force](https://attack.mitre.org/techniques/T1110), its goal is the identification of content and infrastructure rather than the discovery of valid credentials. Wordlists used in these scans may contain generic, commonly used names and file extensions or terms specific to a particular software. Adversaries may also create custom, target-specific wordlists using data gathered from other Reconnaissance techniques (ex: [Gather Victim Org Information](https://attack.mitre.org/techniques/T1591), or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).

For example, adversaries may use web content discovery tools such as Dirb, DirBuster, and GoBuster and generic or custom wordlists to enumerate a website’s pages and directories.(Citation: ClearSky Lebanese Cedar Jan 2021) This can help them to discover old, vulnerable pages or hidden administrative portals that could become the target of further operations (ex: [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190) or [Brute Force](https://attack.mitre.org/techniques/T1110)).  

As cloud storage solutions typically use globally unique names, adversaries may also use target-specific wordlists and tools such as s3recon and GCPBucketBrute to enumerate public and private buckets on cloud infrastructure.(Citation: S3Recon GitHub)(Citation: GCPBucketBrute) Once storage objects are discovered, adversaries may leverage [Data from Cloud Storage](https://attack.mitre.org/techniques/T1530) to access valuable information that can be exfiltrated or used to escalate privileges and move laterally. 

#### Properties

- id: T1595.003
- name: Wordlist Scanning
- created: 2022-03-04 18:56:38.844000+00:00
- modified: 2025-10-24 17:49:18.777000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

