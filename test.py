from loguru import logger

from milvusdb.converter.transform import MilvusTransform

sql_text1 = """
CREATE TABLE car_vectors (
    id INT64 PRIMARY KEY,
    brand VARCHAR(50),
    mileage INT32,
    vector FLOAT_VECTOR[128]
);
"""

sql_text2 = """
INSERT INTO car_vectors (id, brand, mileage, vector)
VALUES (1, 'Toyota', 30000, [0.1, 0.2, 0.2]),
(2, 'Prius', 30000, [0.3, 0.3, 0.3]);
"""

sql_text3 = """
INSERT INTO car_vectors (id, mileage, brand, vector)
VALUES (1, 30000, 'Toyota', [0.1, 0.2, 0.2]);
"""

sql_text4 = """
CREATE INDEX idx_vector
ON car_vectors (HNSW(vector))
"""

sql_text5 = """
SELECT id, brand
FROM car_vectors
WHERE mileage < 50000
  AND brand = 'Honda'
  AND vector SIMILAR TO [0.1, 0.2]
USING L2
LIMIT 10;
"""

sql_text6 = """
SELECT id, brand
FROM car_vectors
WHERE id IN (1, 2, 3);
"""

sql_text7 = """
DELETE FROM car_vectors
WHERE id = 1;
"""

sql_text8 = """
DROP TABLE car_vectors;
"""

sql_list = [
    sql_text1,
    sql_text2,
    sql_text3,
    sql_text4,
    # sql_text5,
    sql_text6,
    sql_text7,
    sql_text8
]

if __name__ == "__main__":
    for j, i in enumerate(sql_list):
        logger.info(f"{j}: {i}")
        logger.info(MilvusTransform().parameter_request(i))
