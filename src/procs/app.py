"""
An example stored procedure. __main__ provides an entrypoint for local development
and testing.
"""

from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import col, DataFrame
from snowflake.snowpark.types import StringType


def run(snowpark_session: Session) -> str:
    """
    A sample stored procedure which creates a small DataFrame, prints it to the
    console, and returns the number of rows in the table.
    """

    # Register UDF
    from src.udf.functions import combine

    snowpark_session.add_import(
        path="../src/udf/functions.py", import_path="src.udf.functions"
    )
    combine = snowpark_session.udf.register(
        combine, StringType(), input_types=[StringType(), StringType()]
    )

    schema = ["col_1", "col_2"]

    data = [
        ("Welcome to ", "Snowflake!"),
        ("Learn more: ", "https://www.snowflake.com/snowpark/"),
    ]

    df: DataFrame = snowpark_session.create_dataframe(data, schema)

    df2 = df.select(combine(col("col_1"), col("col_2")).as_("Hello world")).sort(
        "Hello world", ascending=False
    )

    df2.show()
    return df2.count()


if __name__ == "__main__":
    # This entrypoint is used for local development.

    import sys

    sys.path.insert(0, "..")  # Necessary to import from udf and util directories

    from src.util.local import get_env_var_config

    print("Creating session...")
    session = Session.builder.configs(get_env_var_config()).create()

    print("Running stored proc...")
    run(session)

    
