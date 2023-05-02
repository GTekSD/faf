:: This is a Windows batch script that creates directories based on a list of names in a text file called "list.txt".

@echo off
for /f "tokens=*" %%a in (list.txt) do (
    mkdir "%%a"
)
