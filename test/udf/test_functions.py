
import pytest
from snowflake.snowpark.session import Session
from src.util.local import get_env_var_config

@pytest.fixture
def session():
    return Session.builder.configs(get_env_var_config()).create()

def test_combine(session):
    from src.udf.functions import combine
    expected = "hello world"
    actual = combine("hello ", "world")
    import pdb; pdb.set_trace()
    assert expected == actual
