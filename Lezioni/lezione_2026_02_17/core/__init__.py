import pymysql

pymysql.version_info = (2, 2, 1, 'final', 0)
pymysql.install_as_MySQLdb()  # Fa sembrare a Django che PymySQL sia 'MySQLClient', un'altro driver per la connessione
# al DBMS SQL, che è scritto in C++
# Non usiamo mysqlclient perchè richiede una configurazione più estesa e complessa.

# SOLO PER CHI HA UNA VERSIONE VECCHIA DI MARIA DB
try:
    from django.db.backends.mysql.base import DatabaseWrapper
    DatabaseWrapper.check_database_version_supported = lambda self: None
except ImportError:
    pass