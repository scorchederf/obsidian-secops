---
atomic_guid: "30558d53-9d76-41c4-9267-a7bd5184bed3"
title: "Replace Desktop Wallpaper"
framework: "atomic"
generated: "true"
attack_technique_id: "T1491.001"
attack_technique_name: "Defacement: Internal Defacement"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "30558d53-9d76-41c4-9267-a7bd5184bed3"
  - "Replace Desktop Wallpaper"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Downloads an image from a URL and sets it as the desktop wallpaper.

## ATT&CK Mapping

- [[kb/attack/techniques/T1491-defacement#^t1491001-internal-defacement|T1491.001: Internal Defacement]]

## Input Arguments

### pointer_to_orginal_wallpaper

- description: Full path to where a file containing the original wallpaper location will be saved
- type: string
- default: $env:TEMP\T1491.001-OrginalWallpaperLocation

### url_of_wallpaper

- description: URL pointing to the image file you wish to set as wallpaper
- type: url
- default: https://redcanary.com/wp-content/uploads/Atomic-Red-Team-Logo.png

### wallpaper_location

- description: Full path to where the downloaded wallpaper image will be saved
- type: string
- default: $env:TEMP\T1491.001-newWallpaper.png

## Executor

- name: powershell

### Command

```powershell
$url = "#{url_of_wallpaper}"
$imgLocation = "#{wallpaper_location}"
$orgWallpaper = (Get-ItemProperty -Path Registry::'HKEY_CURRENT_USER\Control Panel\Desktop\' -Name WallPaper).WallPaper
$orgWallpaper | Out-File -FilePath "#{pointer_to_orginal_wallpaper}"
$updateWallpapercode = @' 
using System.Runtime.InteropServices; 
namespace Win32{

    public class Wallpaper{ 
        [DllImport("user32.dll", CharSet=CharSet.Auto)] 
         static extern int SystemParametersInfo (int uAction , int uParam , string lpvParam , int fuWinIni) ; 
         
         public static void SetWallpaper(string thePath){ 
            SystemParametersInfo(20,0,thePath,3); 
        }
    }
} 
'@
$wc = New-Object System.Net.WebClient  
try{  
    $wc.DownloadFile($url, $imgLocation)
    add-type $updateWallpapercode 
    [Win32.Wallpaper]::SetWallpaper($imgLocation)
} 
catch [System.Net.WebException]{  
    Write-Host("Cannot download $url") 
    add-type $updateWallpapercode 
    [Win32.Wallpaper]::SetWallpaper($imgLocation)
} 
finally{    
    $wc.Dispose()  
}
```

### Cleanup

```powershell
$updateWallpapercode = @' 
using System.Runtime.InteropServices; 
namespace Win32{

    public class Wallpaper{ 
        [DllImport("user32.dll", CharSet=CharSet.Auto)] 
         static extern int SystemParametersInfo (int uAction , int uParam , string lpvParam , int fuWinIni) ; 
         
         public static void SetWallpaper(string thePath){ 
            SystemParametersInfo(20,0,thePath,3); 
        }
    }
} 
'@
if (Test-Path -Path #{pointer_to_orginal_wallpaper} -PathType Leaf) {
     $orgImg = Get-Content -Path "#{pointer_to_orginal_wallpaper}"
     add-type $updateWallpapercode 
     [Win32.Wallpaper]::SetWallpaper($orgImg)
}
Remove-Item "#{pointer_to_orginal_wallpaper}" -ErrorAction Ignore
Remove-Item "#{wallpaper_location}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml)
