from snowflake.snowpark.session import Session
from src.app import run


def test_app_dim(session: Session):
    expected = session.create_dataframe(
        [["Welcome to Snowflake!"], ["Learn more: https://www.snowflake.com/snowpark/"]],
        ["hello_world"])
    
    actual = run(session)

    assert expected.collect() == actual.collect()
