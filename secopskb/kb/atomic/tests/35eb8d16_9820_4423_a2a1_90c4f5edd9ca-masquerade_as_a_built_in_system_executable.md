---
atomic_guid: "35eb8d16-9820-4423-a2a1-90c4f5edd9ca"
title: "Masquerade as a built-in system executable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.005"
attack_technique_name: "Masquerading: Match Legitimate Name or Location"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.005/T1036.005.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "35eb8d16-9820-4423-a2a1-90c4f5edd9ca"
  - "Masquerade as a built-in system executable"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Launch an executable that attempts to masquerade as a legitimate executable.

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]

## Input Arguments

### executable_filepath

- description: File path where the generated executable will be dropped and executed from. The filename should be the name of a built-in system utility.
- type: string
- default: $Env:windir\Temp\svchost.exe

## Executor

- name: powershell

### Command

```powershell
Add-Type -TypeDefinition @'
public class Test {
    public static void Main(string[] args) {
        System.Console.WriteLine("tweet, tweet");
    }
}
'@ -OutputAssembly "#{executable_filepath}"

Start-Process -FilePath "#{executable_filepath}"
```

### Cleanup

```powershell
Remove-Item -Path "#{executable_filepath}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.005/T1036.005.yaml)
