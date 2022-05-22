import getpass
import cx_Oracle

__connection = None

def login(dsn):
    global __connection
    
    username = input('DB username? ')
    password = getpass.getpass('DB Password? ')
    
    try:
        __connection = cx_Oracle.connect(username, password, dsn)
    except:
        return False
    else:
        return True
    
def logout():
    global __connection
    
    if __connection:
        print('Logging out from the DB...')
        __connection.close()
        print('Logout complete')
        
def query(qry):
    global __connection
    tuples = []
    
    if __connection:
        cur = __connection.cursor()
        results = cur.execute(qry)
        for result in results:
            tuples += [result]
        cur.close()
        
        return tuples
    else:
        raise RuntimeError('Error: establish a connection first!')
    
def query_with_params(qry, params):
    global __connection
    tuples = []
    
    if __connection:
        cur = __connection.cursor()
        results = cur.execute(qry, params)
        
        if results is not None:
            for result in results:
                tuples += [result]
        cur.close()
        
        return tuples
    else:
        raise RuntimeError('Error: establish a connection first!')
    
def insert_product(supplier_name, prod_name, quantity, unit_price):
    global __connection
    
    supp_query = 'SELECT ID FROM SUPPLIERS WHERE NAME = :name'
    supplier_id = query_with_params(supp_query, [supplier_name])
    supplier_id = int(supplier_id[0][0])
    
    insert_data = [supplier_id, prod_name, quantity, unit_price]
    insert_query = 'INSERT INTO PRODUCTS VALUES (NULL, :supp, :pname, :qty, :uprice)'
    _ = query_with_params(insert_query, insert_data)
    
    __connection.commit()