"""
Tests for the procedure module.
"""

from snowflake.snowpark.session import Session
import functions
from app import run

def test_app_dim(session: Session):
    session.add_import(functions.__file__, 'functions')
    expected = session.create_dataframe(
        [["Welcome to Snowflake!"], ["Learn more: https://www.snowflake.com/snowpark/"]],
        ["hello_world"])
    
    actual = run(session)

    assert expected.collect() == actual.collect()
