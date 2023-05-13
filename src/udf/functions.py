"""
This module contains the UDFs for the project.
"""

from snowflake.snowpark.functions import udf

@udf(is_permanent=False)
def combine(string_a: str, string_b: str) -> str:
    """
    A sample UDF implementation
    """
    return string_a + string_b
