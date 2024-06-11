python3.9 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip3 install --upgrade pip

pip3 install -r requirements.txt 
python3.9 manage.py collectstatic