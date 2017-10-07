from configparser import ConfigParser
import os
import sqlalchemy

def write_new_config():
    
    config = ConfigParser()

    config.set('DEFAULT','mysqluser','mysqluser')
    config.set('DEFAULT','mysqlpass','mysqlpass')
    config.set('DEFAULT','mysqlhost','mysqlhost')
    config.set('DEFAULT','mailserver','mailserver')
    config.set('DEFAULT','mailfromaddr','fromaddr')
    config.set('DEFAULT','mailpass','mailpass')
    config.set('DEFAULT','db','translogrify')
    config.set('DEFAULT','table','log')
    config.set('DEFAULT','port','587')
    config.set('DEFAULT','email_requires_login','True')

    with open(os.path.join(os.path.expanduser('~'),'.translogrify.conf'),'w') as configfile:
        config.write(configfile)

def read_config():

    config = ConfigParser()

    config.read(os.path.join(os.path.expanduser('~'),'.translogrify.conf'))

    cfg = {}

    cfg['mysqluser']            = config.get('DEFAULT','mysqluser')
    cfg['mysqlpass']            = config.get('DEFAULT','mysqlpass')
    cfg['mysqlhost']            = config.get('DEFAULT','mysqlhost')
    cfg['mailserver']           = config.get('DEFAULT','mailserver')
    cfg['mailfromaddr']         = config.get('DEFAULT','mailfromaddr')
    cfg['mailpass']             = config.get('DEFAULT','mailpass')
    cfg['db']                   = config.get('DEFAULT','db')
    cfg['table']                = config.get('DEFAULT','table')
    cfg['port']                 = int(config.get('DEFAULT','port'))
    cfg['email_requires_login'] = config.get('DEFAULT','email_requires_login')

    return cfg


def create_db_and_table():

    config = ConfigParser()
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
