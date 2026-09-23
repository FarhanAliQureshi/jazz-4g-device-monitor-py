# Jazz 4G WiFi Device Monitor
Jazz 4G WiFi Device Monitoring Desktop App written using Python.

## Setup
### Clone This Repository
```bash
git clone https://github.com/FarhanAliQureshi/jazz-4g-device-monitor-py.git
cd jazz-4g-device-monitor-py
```
> [!NOTE]
> I used Python 3.14.7 while I was writing this program.

### Python Virtual Environment
#### For Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
#### For Windows:
```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run
#### For Linux:
```bash
cd jazz-4g-device-monitor-py
source .venv/bin/activate
python3 main.py
```
#### For Windows:
```cmd
cd jazz-4g-device-monitor-py
.venv\Scripts\activate
python main.py
```

## Tests
Run unit tests as following:
#### For Linux:
```bash
cd jazz-4g-device-monitor-py
source .venv/bin/activate
python3 -m unittest discover -s tests
```
#### For Windows:
```cmd
cd jazz-4g-device-monitor-py
.venv\Scripts\activate
python -m unittest discover -s tests
```

# License
Copyright © Farhan Ali Qureshi. All rights reserved. Read the [GPLv3 LICENSE](LICENSE) file for details.
