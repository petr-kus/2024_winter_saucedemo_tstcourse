# 2024_winter_saucedemo_tstcourse
Repository fortesting course winter 2024. 

## Related Documentation links
Documentation for Selenium 
https://selenium-python.readthedocs.io/getting-started.html
https://www.selenium.dev/documentation/

Documentation Locators in selenium 
https://selenium-python.readthedocs.io/locating-elements.html

Packages page:
https://pypi.org/

Documentation around virtual enviroments
https://docs.python.org/3/library/venv.html

Documentation Set-Execution policy 
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4

## How to prepare virtual enviroment 
Start Powershell command line as Administrator and use command 
```bash
Set-ExecutionPolicy –ExecutionPolicy RemoteSigned –Scope CurrentUser
```

Start visual studio code (VS Code), open folder with your project and start from the terminal:
```bash
.\install_dependencies.ps1
```

Save installed packages:
```bash
pip freeze > requirements.txt 
```

## How to run test from terminal in VS Code
```bash
python .\tests.py 
```