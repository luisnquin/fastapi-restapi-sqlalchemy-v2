echo "First, create a database, enter the dbname once time are ready: "
read dbname
echo "Second, your username: "
read dbuser
echo "Password: "
read dbpassword
echo "Host: "
read dbhost
echo "Port: "
read dbport

export dbname
export dbuser
export dbpassword
export dbhost
export dbport

echo "Visit: http://127.0.0.1:8000/docs"
pip install -r requirements.txt

echo "Linux[1] or Windows[2]: "
read option

python3 src/db/migrations.py


xdg-open http://127.0.0.1:8000/docs
uvicorn src.main:app --reload --port=8000