import psycopg2

def load_to_redshift(data, table_name):
    conn = psycopg2.connect(
        dbname='your_dbname',
        user='your_username',
        password='your_password',
        host='your_redshift_cluster_endpoint',
        port='5439'
    )
    cur = conn.cursor()
    
    for record in data:
        cur.execute(f"INSERT INTO {table_name} VALUES ({', '.join(record)})")
    
    conn.commit()
    cur.close()
    conn.close()
    print(f"Data loaded into Redshift table {table_name}")

if __name__ == "__main__":
    data = [('value1', 'value2'), ('value3', 'value4')]  # Replace with your actual data
    table_name = 'your_table_name'
    
    load_to_redshift(data, table_name)

