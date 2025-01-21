import dict_to_db as d_t_db
import pandas as pd

def cdv_to_dict():
    df = pd.read_csv("Clientes.csv")
    d = df.to_dict(orient='llist')
    return d
data = csv_to_dict()

for i in range(30):
    d_t_db.send_data_todb(i, data)