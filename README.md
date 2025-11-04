# 🗂️ Python Backup Script

A simple Python script to back up files and folders automatically with logs and timestamps.

---

## ⚙️ Features
- Backup files from a source to destination folder  
- Auto-create timestamped backup folders  
- Log each backup run in a text file  
- Configurable paths via `config.json`

---

## 🧩 How to Use
1. Update paths in `config.json`:
   ```json
   {
       "source_folder": "D:/MYPROJECTS/source_files",
       "backup_folder": "D:/MYPROJECTS/backups"
   }
2. Run the script:
    python backup.py


3. Check logs in logs/backup_log.txt

📁 Project Structure -->

backup_script/
├── backup.py
├── config.json
└── logs/

🧠 Tools Used

Python3

Modules: os, shutil, datetime, json

Author: Farhan Mumtaz Ali
📧 farhan_mk4@hotmail.com