mysql -u root -p$MYSQL_ROOT_PASSWORD --execute \
"CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE;"
echo "Finished creating databases"