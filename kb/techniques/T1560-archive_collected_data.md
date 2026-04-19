---
id: T1560
name: Archive Collected Data
created: 2020-02-20 20:53:45.725000+00:00
modified: 2025-10-24 17:48:48.023000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Properties

- id: T1560
- name: Archive Collected Data
- created: 2020-02-20 20:53:45.725000+00:00
- modified: 2025-10-24 17:48:48.023000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1560.001: Archive via Utility

^t1560001-archive-via-utility

**Parent Technique**
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]

**Tactic**
- [[collection|Collection]]

Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport.

Adversaries may abuse various utilities to compress or encrypt data before exfiltration. Some third party utilities may be preinstalled, such as <code>tar</code> on Linux and macOS or <code>zip</code> on Windows systems. 

On Windows, <code>diantz</code> or <code> makecab</code> may be used to package collected files into a cabinet (.cab) file. <code>diantz</code> may also be used to download and compress files from remote locations (i.e. [Remote Data Staging](https://attack.mitre.org/techniques/T1074/002)).(Citation: diantz.exe_lolbas) <code>xcopy</code> on Windows can copy files and directories with a variety of options. Additionally, adversaries may use [certutil](https://attack.mitre.org/software/S0160) to Base64 encode collected data before exfiltration. 

Adversaries may use also third party utilities, such as 7-Zip, WinRAR, and WinZip, to perform similar activities.(Citation: 7zip Homepage)(Citation: WinRAR Homepage)(Citation: WinZip Homepage)

#### Properties

- id: T1560.001
- name: Archive via Utility
- created: 2020-02-20 21:01:25.428000+00:00
- modified: 2025-10-24 17:48:19.477000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1560.002: Archive via Library

^t1560002-archive-via-library

**Parent Technique**
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]

**Tactic**
- [[collection|Collection]]

An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party libraries. Many libraries exist that can archive data, including [Python](https://attack.mitre.org/techniques/T1059/006) rarfile (Citation: PyPI RAR), libzip (Citation: libzip), and zlib (Citation: Zlib Github). Most libraries include functionality to encrypt and/or compress data.

Some archival libraries are preinstalled on systems, such as bzip2 on macOS and Linux, and zip on Windows. Note that the libraries are different from the utilities. The libraries can be linked against when compiling, while the utilities require spawning a subshell, or a similar execution mechanism.

#### Properties

- id: T1560.002
- name: Archive via Library
- created: 2020-02-20 21:08:52.529000+00:00
- modified: 2025-10-24 17:48:42.345000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1560.003: Archive via Custom Method

^t1560003-archive-via-custom-method

**Parent Technique**
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]

**Tactic**
- [[collection|Collection]]

An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method. Adversaries may choose to use custom archival methods, such as encryption with XOR or stream ciphers implemented with no external library or utility references. Custom implementations of well-known compression algorithms have also been used.(Citation: ESET Sednit Part 2)

#### Properties

- id: T1560.003
- name: Archive via Custom Method
- created: 2020-02-20 21:09:55.995000+00:00
- modified: 2025-10-24 17:48:26.190000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1047-audit|M1047: Audit]]

## Platforms

- Linux
- macOS
- Windows

## Tools

- [[S0363-empire|S0363: Empire]]
- [[S0445-shimratreporter|S0445: ShimRatReporter]]
- [[S0521-bloodhound|S0521: BloodHound]]

