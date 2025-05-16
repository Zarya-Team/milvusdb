from milvusdb.converter.transform import MilvusTransform


def test_milvus_transform():
    sql_text1 = """
    CREATE TABLE car_vectors (
        id INT64 PRIMARY KEY,
        brand VARCHAR(50),
        mileage INT32,
        vector FLOAT_VECTOR[128]
    );
    """
    milvus_transform = MilvusTransform().parameter_request(sql_text1)
    assert milvus_transform is not None
