"""
An example stored procedure. __main__ provides an entrypoint for local development
and testing.
"""

from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import col, DataFrame
from snowflake.snowpark.types import StringType


def run(snowpark_session: Session) -> DataFrame:
    """
    A sample stored procedure which creates a small DataFrame, prints it to the
    console, and returns the number of rows in the table.
    """

    # Register UDF
    from src.udf.functions import combine

    schema = ["col_1", "col_2"]

    data = [
        ("Welcome to ", "Snowflake!"),
        ("Learn more: ", "https://www.snowflake.com/snowpark/"),
    ]

    df = snowpark_session.create_dataframe(data, schema)

    df2 = df.select(combine(col("col_1"), col("col_2")).as_("hello_world")).sort(
        "hello_world", ascending=False
    )

    return df2


if __name__ == "__main__":
    # This entrypoint is used for local development.

    from src.util.local import get_env_var_config

    print("Creating session...")
    session = Session.builder.configs(get_env_var_config()).create()

    print("Running stored procedure...")
    result = run(session)

    print("Stored procedure complete:")
    result.show()
