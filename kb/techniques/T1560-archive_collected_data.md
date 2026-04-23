---
mitre_id: "T1560"
mitre_name: "Archive Collected Data"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--53ac20cd-aca3-406e-9aa0-9fc7fdc60a5a"
mitre_created: "2020-02-20T20:53:45.725Z"
mitre_modified: "2025-10-24T17:48:48.023Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1560/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0009"
---

# T1560: Archive Collected Data

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Subtechniques

### T1560.001: Archive via Utility

^t1560001-archive-via-utility

Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport.

Adversaries may abuse various utilities to compress or encrypt data before exfiltration. Some third party utilities may be preinstalled, such as `tar` on Linux and macOS or `zip` on Windows systems. 

On Windows, `diantz` or `makecab` may be used to package collected files into a cabinet (.cab) file. `diantz` may also be used to download and compress files from remote locations (i.e. [[T1074-data_staged#^t1074002-remote-data-staging|T1074.002: Remote Data Staging]]).(Citation: diantz.exe_lolbas) `xcopy` on Windows can copy files and directories with a variety of options. Additionally, adversaries may use [[certutil|certutil]] to Base64 encode collected data before exfiltration. 

Adversaries may use also third party utilities, such as 7-Zip, WinRAR, and WinZip, to perform similar activities.(Citation: 7zip Homepage)(Citation: WinRAR Homepage)(Citation: WinZip Homepage)

### T1560.002: Archive via Library

^t1560002-archive-via-library

An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party libraries. Many libraries exist that can archive data, including [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]] rarfile (Citation: PyPI RAR), libzip (Citation: libzip), and zlib (Citation: Zlib Github). Most libraries include functionality to encrypt and/or compress data.

Some archival libraries are preinstalled on systems, such as bzip2 on macOS and Linux, and zip on Windows. Note that the libraries are different from the utilities. The libraries can be linked against when compiling, while the utilities require spawning a subshell, or a similar execution mechanism.

### T1560.003: Archive via Custom Method

^t1560003-archive-via-custom-method

An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method. Adversaries may choose to use custom archival methods, such as encryption with XOR or stream ciphers implemented with no external library or utility references. Custom implementations of well-known compression algorithms have also been used.(Citation: ESET Sednit Part 2)

## Mitigations

- [[M1047-audit|M1047: Audit]]

## Tools

- [[empire|Empire]]
- [[shimratreporter|ShimRatReporter]]
- [[bloodhound|BloodHound]]

## Platforms

- Linux
- macOS
- Windows

