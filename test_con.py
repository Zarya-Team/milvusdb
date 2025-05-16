from loguru import logger

import milvusdb
from test import sql_list

if __name__ == '__main__':
    conn = milvusdb.connect(
        host='https://localhost',
        token='',
        user="",
        password="!",
    )
    cur = conn.cursor()
    for sql in sql_list:
        cur.execute(sql)
        logger.info(cur.fetchall())  # [('result1',), ('result2',)]
    cur.close()
    conn.close()


