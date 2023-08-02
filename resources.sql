
!variables;

CREATE STAGE IF NOT EXISTS artifacts;

PUT file://&artifact_name @artifacts AUTO_COMPRESS=FALSE OVERWRITE=TRUE;

CREATE OR REPLACE PROCEDURE HELLO_WORLD_PROC()
    RETURNS TABLE(hello_world string)
    LANGUAGE PYTHON
    RUNTIME_VERSION = 3.8
    IMPORTS = ('@artifacts/&artifact_name')
    HANDLER = 'src.app.run'
    PACKAGES = ('pytest','snowflake-snowpark-python','tomli','toml');

CREATE OR REPLACE FUNCTION COMBINE(a String, b String)
    RETURNS String
    LANGUAGE PYTHON
    RUNTIME_VERSION = 3.8
    IMPORTS = ('@artifacts/&artifact_name')
    HANDLER = 'src.functions.combine'
    PACKAGES = ('pytest','snowflake-snowpark-python','tomli','toml');
