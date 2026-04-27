---
atomic_guid: "68190529-069b-4ffc-a942-919704158065"
title: "Domain Password Policy Check: No Number in Password"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "68190529-069b-4ffc-a942-919704158065"
  - "Domain Password Policy Check: No Number in Password"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attempt to change the password of the current domain user in order to check password policy. Ideally, you would only run this atomic test to verify that your password policy is blocking the use of the new password.
If the password is succesfully changed to the new password, the credential file will be updated to reflect the new password. You can then run the atomic manually and specify a new password of your choosing, however the
password policy will likely prevent you from setting the password back to what it was.

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098: Account Manipulation]]

## Input Arguments

### cred_file

- description: A file containing the password of the current user
- type: path
- default: $env:LOCALAPPDATA\AtomicRedTeam\$env:USERNAME.txt

### new_password

- description: The password to set for the current domain user (default is long and has upper and lower case and special character but no number)
- type: string
- default: UpperLowerLong-special

## Dependencies

Password for current user must be stored in a credential file

### Prerequisite Check

```untitled
if (Test-Path #{cred_file}) {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory (split-path "#{cred_file}") -ErrorAction Ignore | Out-Null
$cred = Get-Credential -UserName  $env:USERNAME -message "Enter password for $env:USERNAME to use during password change attempt"
$cred.Password | ConvertFrom-SecureString | Out-File "#{cred_file}"
```

## Executor

- name: powershell

### Command

```powershell
$credFile = "#{cred_file}"
if (Test-Path $credFile) {
    $cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $env:USERNAME, (Get-Content $credFile | ConvertTo-SecureString)
    if($cred.GetNetworkCredential().Password -eq "#{new_password}"){
      Write-Host -ForegroundColor Yellow "The new password is the same as the password stored in the credential file. Please specify a different new password."; exit -1
    }
    try {
        $newPassword = ConvertTo-SecureString #{new_password} -AsPlainText -Force
        Set-ADAccountPassword -Identity $env:USERNAME -OldPassword $cred.password -NewPassword $newPassword
    }
    catch { 
        $_.Exception
        $errCode = $_.Exception.ErrorCode
        Write-Host "Error code: $errCode"
        if ($errCode -eq 86) {
            Write-Host -ForegroundColor Yellow "The stored password for the current user is incorrect. Please run the prereq commands to set the correct credentials"
            Remove-Item $credFile
        }
        exit $errCode
    }
    Write-Host -ForegroundColor Cyan "Successfully changed the password to #{new_password}"
    $newCred = New-Object System.Management.Automation.PSCredential ($env:USERNAME, $(ConvertTo-SecureString "#{new_password}" -AsPlainText -Force))
    $newCred.Password | ConvertFrom-SecureString | Out-File $credFile
}
else {
    Write-Host -ForegroundColor Yellow "You must store the password of the current user by running the prerequisite commands first"
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
