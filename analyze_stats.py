from pprint import pprint
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from IPython.display import display
import matplotlib.pyplot as plt

if __name__ == '__main__':
    interview = '5fb165fd4c76f4f7756359a7'
    querry = f"SELECT OutboundVideo_bytesSent_in_bitsS, dateTimeStamp  FROM test2 WHERE interview='{interview}' and OutboundVideo_bytesSent_in_bitsS is not null"
    db_connection_str = 'mysql+pymysql://admin:admin@10.1.10.106/webrtcStatsTest'
    db_connection = create_engine(db_connection_str)
    df = pd.read_sql(querry, con=db_connection)
    display(df)
    avrg = df['OutboundVideo_bytesSent_in_bitsS'].mean()
    avrg_formatted = round(avrg/1024)
    print(f"Average outbound speed is {avrg_formatted} kbit/sec")
    df.plot(kind='line', x='dateTimeStamp', y='OutboundVideo_bytesSent_in_bitsS')
    plt.show()

