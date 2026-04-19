---
id: T1176
name: Software Extensions
created: 2018-01-16 16:13:52.465000+00:00
modified: 2025-10-24 17:48:39.525000+00:00
type: attack-pattern
x_mitre_version: 2.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Adversaries may abuse software extensions to establish persistent access to victim systems. Software extensions are modular components that enhance or customize the functionality of software applications, including web browsers, Integrated Development Environments (IDEs), and other platforms.(Citation: Chrome Extension C2 Malware)(Citation: Abramovsky VSCode Security) Extensions are typically installed via official marketplaces, app stores, or manually loaded by users, and they often inherit the permissions and access levels of the host application. 

  
Malicious extensions can be introduced through various methods, including social engineering, compromised marketplaces, or direct installation by users or by adversaries who have already gained access to a system. Malicious extensions can be named similarly or identically to benign extensions in marketplaces. Security mechanisms in extension marketplaces may be insufficient to detect malicious components, allowing adversaries to bypass automated scanners or exploit trust established during the installation process. Adversaries may also abuse benign extensions to achieve their objectives, such as using legitimate functionality to tunnel data or bypass security controls. 

The modular nature of extensions and their integration with host applications make them an attractive target for adversaries seeking to exploit trusted software ecosystems. Detection can be challenging due to the inherent trust placed in extensions during installation and their ability to blend into normal application workflows. 

## Subtechniques

### T1176.001: Browser Extensions

^t1176001-browser-extensions

**Parent Technique**
- [[T1176-software_extensions|T1176: Software Extensions]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse internet browser extensions to establish persistent access to victim systems. Browser extensions or plugins are small programs that can add functionality to and customize aspects of internet browsers. They can be installed directly via a local file or custom URL or through a browser's app store - an official online platform where users can browse, install, and manage extensions for a specific web browser. Extensions generally inherit the web browser's permissions previously granted.(Citation: Wikipedia Browser Extension)(Citation: Chrome Extensions Definition) 
 
Malicious extensions can be installed into a browser through malicious app store downloads masquerading as legitimate extensions, through social engineering, or by an adversary that has already compromised a system. Security can be limited on browser app stores, so it may not be difficult for malicious extensions to defeat automated scanners.(Citation: Malicious Chrome Extension Numbers) Depending on the browser, adversaries may also manipulate an extension's update url to install updates from an adversary-controlled server or manipulate the mobile configuration file to silently install additional extensions. 

Adversaries may abuse how chromium-based browsers load extensions by modifying or replacing the Preferences and/or Secure Preferences files to silently install malicious extensions. When the browser is not running, adversaries can alter these files, ensuring the extension is loaded, granted desired permissions, and will persist in browser sessions. This method does not require user consent and extensions are silently loaded in the background from disk or from the browser's trusted store.(Citation: Pulsedive)
  
Previous to macOS 11, adversaries could silently install browser extensions via the command line using the <code>profiles</code> tool to install malicious <code>.mobileconfig</code> files. In macOS 11+, the use of the <code>profiles</code> tool can no longer install configuration profiles; however, <code>.mobileconfig</code> files can be planted and installed with user interaction.(Citation: xorrior chrome extensions macOS) 
 
Once the extension is installed, it can browse to websites in the background, steal all information that a user enters into a browser (including credentials), and be used as an installer for a RAT for persistence.(Citation: Chrome Extension Crypto Miner)(Citation: ICEBRG Chrome Extensions)(Citation: Banker Google Chrome Extension Steals Creds)(Citation: Catch All Chrome Extension) 

There have also been instances of botnets using a persistent backdoor through malicious Chrome extensions for [Command and Control](https://attack.mitre.org/tactics/TA0011).(Citation: Stantinko Botnet)(Citation: Chrome Extension C2 Malware) Adversaries may also use browser extensions to modify browser permissions and components, privacy settings, and other security controls for [Defense Evasion](https://attack.mitre.org/tactics/TA0005).(Citation: Browers FriarFox)(Citation: Browser Adrozek) 

### T1176.002: IDE Extensions

^t1176002-ide-extensions

**Parent Technique**
- [[T1176-software_extensions|T1176: Software Extensions]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may abuse an integrated development environment (IDE) extension to establish persistent access to victim systems.(Citation: Mnemonic misuse visual studio) IDEs such as Visual Studio Code, IntelliJ IDEA, and Eclipse support extensions - software components that add features like code linting, auto-completion, task automation, or integration with tools like Git and Docker. A malicious extension can be installed through an extension marketplace (i.e., [Compromise Software Dependencies and Development Tools](https://attack.mitre.org/techniques/T1195/001)) or side-loaded directly into the IDE.(Citation: Abramovsky VSCode Security)(Citation: Lakshmanan Visual Studio Marketplace)   

In addition to installing malicious extensions, adversaries may also leverage benign ones. For example, adversaries may establish persistent SSH tunnels via the use of the VSCode Remote SSH extension (i.e., [IDE Tunneling](https://attack.mitre.org/techniques/T1219/001)).  

Trust is typically established through the installation process; once installed, the malicious extension is run every time that the IDE is launched. The extension can then be used to execute arbitrary code, establish a backdoor, mine cryptocurrency, or exfiltrate data.(Citation: ExtensionTotal VSCode Extensions  2025)

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1033-limit_software_installation|M1033: Limit Software Installation]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1047-audit|M1047: Audit]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- Linux
- macOS
- Windows

