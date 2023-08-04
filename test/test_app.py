"""
Tests for the procedure module.
"""

from snowflake.snowpark.session import Session
from src.app import run
from src import functions

def test_app_dim(session: Session):
    session.add_import(functions.__file__, 'src.functions')
    expected = session.create_dataframe(
        [["Welcome to Snowflake!"], ["Learn more: https://www.snowflake.com/snowpark/"]],
        ["hello_world"])
    
    actual = run(session)

    assert expected.collect() == actual.collect()
