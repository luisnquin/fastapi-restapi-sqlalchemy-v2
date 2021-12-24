echo "You will need to have Python(with pip) and PostgreSQl installed"
echo ""
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

pip install -r requirements.txt

echo "Windows[1], Ubuntu[2]: "
read option

if [[ "$option" == "1" ]]
then
    export dbname
    export dbuser
    export dbpassword
    export dbhost
    export dbport
    py src/db/migrations.py
    echo "Visit: http://127.0.0.1:8000/docs"
    uvicorn src.main:app --reload --port=8000
elif [[ "$option" == "2" ]]
then
    export dbname
    export dbuser
    export dbpassword
    export dbhost
    export dbport
    python3 src/db/migrations.py
    echo "Visit: http://127.0.0.1:8000/docs or reload the page"
    xdg-open http://127.0.0.1:8000/docs
    uvicorn src.main:app --reload --port=8000
else
    echo "Bad option"
fi
