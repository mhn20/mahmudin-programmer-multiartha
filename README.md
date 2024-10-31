## Setup
### Windows
```bash
python -m venv venv
```
```bash
venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```
### Linux
```bash
python3 -m venv venv
```
```bash
venv/bin/activate
```
```bash
pip3 install -r requirements.txt
```
# Tugas
### Tugas 1
```
# Open File tugas1.py
$ input your_username
$ input your_password
```
### Tugas 2
```
# Open File tugas2.py
$ sisipkan api_key
# open postman 
$ url : http://127.0.0.1:5000/ask
$ method : POST
$ headers : Accept application/json
$ body : raw json {"question" : "Apa itu facebook ?" }
```
### Tugas 3 & 4
```bash
cd tugas3_tugas4
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
```bash
http://localhost:8000/admin-dashboard/users/
```


