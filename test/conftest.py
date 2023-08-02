import pytest
from snowflake.snowpark.session import Session
from src.util.local import get_env_var_config

@pytest.fixture
def session(scope='module'):
    return Session.builder.configs(get_env_var_config()).create()
