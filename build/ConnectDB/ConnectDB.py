# Press the green button in the gutter to run the script.

import psycopg2
import pandas as pd

if __name__ == '__main__':
    print("Hello World")
    conn = psycopg2.connect(database="EVOFINDER_DB",
                        host="192.168.10.141",
                        user="EVOFINDERAdmin",
                        password="Thailand-2023",
                        port="5432")
    cursor = conn.cursor()

    cmd_ex = "Select * from \"View_jpgBullet\""
    print(cmd_ex)
    cursor.execute(cmd_ex)

    df = pd.DataFrame(cursor.fetchall())

    r,c = df.shape
    print("row = ", r ," column = " ,c)

    print(df)
    #print(df[0][0], df[1][0])



