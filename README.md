📝 AWS Cloud Notes
A sleek, full-stack deployment project: Note-taking app on RHEL 10 with a secure EBS backup strategy.

🚀 Technology Stack

Provider: AWS (EC2 & EBS) 

Platform: Red Hat Enterprise Linux 10 

Language: Python (Flask Framework) 

Database: MariaDB (Persistent Storage) 

✨ Core Features

Simple Web Interface: For effortless note creation and submission.

Live Feed: Displays submitted notes with real-time timestamps.

Data Reliability: All notes are securely stored in a MariaDB database.

🛡️ Storage & Backup

EBS Volume: A dedicated 1GB volume for data safety.

Mount Point: Integrated directly into the system at /backup.

Backup Method: Regular database snapshots saved as .sql files.
