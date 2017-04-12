import configparser
import os
import sqlalchemy

def write_new_config():
    
    config = configparser.ConfigParser()

    config['DEFAULT'] = {'MySQLUser':'mysqluser',
            'MySQLPass':'mysqlpass',
            'MySQLHost':'mysqlhost',
            'mailserver':'server',
            'mailfromaddr':'fromaddr',
            'mailpass':'mailpass',
            'db':'translogrify',
            'table':'log'
            }

    with open(os.path.join(os.path.expanduser('~'),'.translogrify.conf'),'w') as configfile:
        config.write(configfile)

def read_config():

    config = configparser.ConfigParser()

    config.read(os.path.join(os.path.expanduser('~'),'.translogrify.conf'))

    return config['DEFAULT']

def create_db_and_table():

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.expanduser('~'),'.translogrify.conf'))

    conf = config['DEFAULT']
   
    conn_str = "mysql+pymysql://{S}:{P}@{H}".format(
            S=conf['mysqluser'],
            P=conf['mysqlpass'],
            H=conf['mysqlhost'])

    try:
        engine = sqlalchemy.create_engine(conn_str)
        con = engine.connect()
        cur = con.connection.cursor() 
        
        qry_str = """
            create database {D}
            """.format(D=conf['db'])

        cur.execute(qry_str)

        qry_str = """
            create table {D}.{T} (
                id MEDIUMINT NOT NULL AUTO_INCREMENT,
                level SMALLINT NOT NULL,
                message TEXT NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                recipient TEXT NOT NULL,

                PRIMARY KEY (id)
                );
                """.format(D=conf['db'],
                    T=conf['table'])

        cur.execute(qry_str)

    except Exception as e:
        print(e)
        print("table {D}.{T} not created!".format(D=conf['db'],
            T=conf['table']))
