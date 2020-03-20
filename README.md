## Prerequisites

* Download this repository on the target machine
* Visual Studio Code

## Setup

* Open powershell as administrator
* `Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
* `choco install python3 --version 3.7.3 -y`
* `choco install gauge --version 1.0.4 -y`
* `choco install nodejs.install -y`
* `choco install googlechrome -y`
* `choco install chromedriver -y`
* `choco install psexec -y`
* `choco install handle -y`
* Close powershell
* Open powershell as admin and navigate to the downloaded git repository folder
* `pip install -r requirements.txt`
* To verify if everything run as expected `gauge validate specs`

## Executing specs

* gauge run specs