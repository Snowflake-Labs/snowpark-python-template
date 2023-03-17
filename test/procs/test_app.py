import os
import pytest
from snowflake.snowpark.session import Session
from snowflake.snowpark.types import StringType
from src.util.local import get_env_var_config
from src.procs.app import run


@pytest.fixture(autouse=True)
def set_working_directory():
    # Sets the working directory to sources root so relative imports resolve properly
    os.chdir("src")


@pytest.fixture
def local_session():
    return Session.builder.configs(get_env_var_config()).create()


@pytest.mark.snowflake_vcr
def test_app_dim(local_session):
    expected_n_rows = 2
    actual_n_rows = run(local_session)
    assert expected_n_rows == actual_n_rows
