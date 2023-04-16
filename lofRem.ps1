
#change line 75 to change how offen the script checks the disk usage, note that it is in seconds and it is a day by default. 
#it also works as a delay so if you put in one second it will check every second and if you put in 60 it will check every minute.
#you get the point :)


#here you can change the path to the log files, the drive witch is checked.
$folder = "C:\ANC2010\Data\LoggingManager\*.*"
$Drive = "C:"

Write-Host @"
To be able to run this application you need to accept the licence agreement.
"@


#asks the user if they want to accept the license agreement, if not it will exit the application


$termsAwnser = Read-Host "Do you accept the licence agreement(there is none, it is just for fun :) ) (y/n)"
if ($termsAwnser -eq "n") {
    exit
}
elseif ($termsAwnser -eq "y") {
   


   





    #sets the path to the loggfiles, spesefies the drive and runs the enitial disk usage prosentage
  
    $DriveSize = (Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='$Drive'").Size
    $DriveFree = (Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='$Drive'").FreeSpace
    $DriveUsed = $DriveSize - $DriveFree
    $DriveUsedProsent = [math]::Round(($DriveUsed / $DriveSize) * 100, 0)
    #writes initial disk usage prosentage
    write-host $DriveUsedProsent




    # A while loop that checks if the license is expired and if the disk is full.

    while (1 -lt 2 ) {
        $DriveSize = (Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='$Drive'").Size
        $DriveFree = (Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='$Drive'").FreeSpace
        $DriveUsed = $DriveSize - $DriveFree
        $DriveUsedProsent = [math]::Round(($DriveUsed / $DriveSize) * 100, 0)
        
        
            
    
        # Checking if the disk is full and if it is it will prompt the user if they want to delete the log
        # files.
    
   
        if ($DriveUsedProsent -gt 80) {
            Write-Host "Warning! $Drive is almost full. $DriveUsedProsent% used" -ForegroundColor Red
            $answer = Read-Host "Do you want to delete the log files in $folder? (y/n)"
            if ($answer -eq "y") {


            
                Remove-Item -Path $folder -Recurse -Force
                Write-Host "Log files deleted" -ForegroundColor Green
            }
            else {
                Write-Host "Log files not deleted" -ForegroundColor Red
            }
        }
        
    
        Start-Sleep -Seconds 86400
            
    }

}
else {
    Write-Host "You did not enter a valid answer, please try again" -ForegroundColor Red
    exit
}

