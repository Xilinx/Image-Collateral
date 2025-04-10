@echo off
echo Generating file list, please wait...
for /r %%f in (*) do @echo %%f >> file_list.txt
echo File list has been generated successfully as "file_list.txt" in the current directory.