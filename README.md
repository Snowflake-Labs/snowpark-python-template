# Python Project Template for Snowpark

Use this template to start writing data applications on Snowflake using Scala.

## Setup

Set the following environment variables with your Snowflake account information:

```bash
# Linux/MacOS
set SNOWSQL_ACCOUNT=<replace with your account identifer>
set SNOWSQL_USER=<replace with your username>
set SNOWSQL_PWD=<replace with your password>
set SNOWSQL_DATABASE=<replace with your database>
set SNOWSQL_SCHEMA=<replace with your schema>
set SNOWSQL_WAREHOUSE=<replace with your warehouse>
```

```powershell
# Windows/PowerShell
$env:SNOWSQL_ACCOUNT = "<replace with your account identifer>"
$env:SNOWSQL_USER = "<replace with your username>"
$env:SNOWSQL_PWD = "<replace with your password>"
$env:SNOWSQL_DATABASE = "<replace with your database>"
$env:SNOWSQL_SCHEMA = "<replace with your schema>"
$env:SNOWSQL_WAREHOUSE = "<replace with your warehouse>"
```

Optional: You can set this env var permanently by editing your bash profile (on Linux/MacOS) or 
using the System Properties menu (on Windows).

### Install dependencies

Set up a virtual environment using [Anaconda](), [Miniconda](), or [virtualenv](). For example, the following command will create and activate a virtual environment named `venv`:

```bash
python3 -m venv venv
source venv/bin/activate
```

Next, import the packages in [requirements.txt](requirements.txt):

```bash
pip install -r requirements.txt
```


## Prereqs

To develop your applications locally, you will need

- A Snowflake account
- Python 3.8
- An IDE or code editor (VS Code, PyCharm, etc.)

## Usage

Once you've set your credentials and installed the packages, you can test your connection to Snowflake by executing the stored procedure in [`app.py`](src/procs/app.py):

```
cd src
python procs/app.py
```

You should see the following output:

```
------------------------------------------------------
|Hello world                                         |
------------------------------------------------------
|Welcome to Snowflake!                               |
|Learn more: https://www.snowflake.com/snowpark/     |
------------------------------------------------------
```

### Run tests

You can run the test suite locally from the project root:

```
python -m pytest
```

### Deploy to Snowflake

The GitHub Actions [workflow file](.github/workflows/build-and-deploy.yml) allows you to continously deploy your objects to Snowflake. When you're ready,
create secrets in your GitHub repository with the same name and values as the environment variables you created earler (`SNOWSQL_PWD`, `SNOWSQL_ACCOUNT`, etc.). The workflow will create a stage, upload the Python source code, and create the stored procedure object. For more information, see [`resources.sql`](resources.sql).

## Project Structure

- [procs/](src/procs/): Directory for stored procedures
- [udf/](src/udf/): Directory for your user-defined functions
- [util/](src/util/): Directory for methods/classes shared between UDFs and procedures

## Docs

- [Snowpark Developer Guide for Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)
- [Creating Stored Procedures](https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-sprocs)
- [Snowpark API Reference](https://docs.snowflake.com/developer-guide/snowpark/reference/python/index.html)


## Contributing

Have a question or ran into a bug? Please [file an issue](https://github.com/Snowflake-Labs/snowpark-scala-template/issues/new) and let us know.

Have an idea for an improvement? Fork this repository and open a PR with your idea!
