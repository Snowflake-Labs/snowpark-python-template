
import pytest
from snowflake.snowpark.session import Session
from src.util.local import get_env_var_config
from src.procs.app import run


@pytest.fixture
def session():
    return Session.builder.configs(get_env_var_config()).create()



def test_app_dim(session: Session):
    expected = session.create_dataframe(
        [["Welcome to Snowflake!"], ["Learn more: https://www.snowflake.com/snowpark/"]],
        ["hello_world"])
    actual = run(session)
    assert expected.collect() == actual.collect()

    # Alertnate impl:
    # expected = [Row("Welcome to Snowflake!"), Row("Learn more: https://www.snowflake.com/snowpark/")]
    # actual = run(session)
    # assert expected.select("hello_world").collect() == actual