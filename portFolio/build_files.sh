python3.9 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip3 install --upgrade pip
pip3 install psycopg2
pip3 install psycopg2-binary
pip3 install -r requirements.txt 
python3.9 manage.py makemigrations  
python3.9 manage.py migrate 
python3.9 manage.py collectstatic