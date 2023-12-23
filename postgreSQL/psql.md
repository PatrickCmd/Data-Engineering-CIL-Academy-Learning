## Logging in
|Option	|Description |
|:------|:-----------|
|-h	|Database server host (Amazon RDS endpoint name)|
|-p	|Database server port (default 5432)|
|-U |User name |

## psql client options
### Some frequently used options for psql
**-f**: Run a file against a database

**-c**: Run the command specified

**--help**: Shows the help screen

### Powerful help options

**\?**: provides help with psql-specific options

### \h to provide context-specific help with SQL commands

Help is also available on **PostgreSQL.org**

![psql help](images/psql-help.jpeg)

## psql client

### Meta commands

Meta commands are a feature of psql that help you perform powerful operations without querying a database. There are many meta commands.

![Meta commands](images/meta-commands.png)

> Each command supports adding + at the end for expanded information. These commands are useful for those who are unfamiliar with using catalog system tables or information schema tables to query. For more information on psql commands, see the [**PostgreSQL Client Applications documentation**](https://www.postgresql.org/docs/13/app-psql.html).

### Interact with the OS
psql can also be used to interact with the OS.

#### Use \! to query the local client OS.
Use `\! pwd `to query the OS for the current working directory.

```sh
postgres=# \! pwd
```

#### Change the working directory
Use the `\cd` command to change your working directory

```sh
postgres=# \cd <directory>
```

#### Run a file.
Run a local file with `psql` using `\i` followed by the path to the file. Functions and permissions vary according to client OS.

(**Note**: You can also run a file without being logged in by using `psql -h hostname -p port -d dbanme -U username -f script.sql`.)

```sh
postgres=# \i /path/to/file.sql
```

#### Exit from OS shell.
Exit to return to the psql client from the OS shell. 

![Exit OS shell](images/exit-os-shell.png)

### Connect Using psql Client

#### Check for network connection to the RDS instance
```sh
nc -zv RDS_ENDPOINT RDS_PORT
```

```sh
nc -zv rds-postgresql-sample.cyhiiz99ooer.us-east-1.rds.amazonaws.com 5432
```

#### Connecting to psql

This is a simple example of a connection into a psql client using a nontraditional port of `7777`.

The code snippet here lists the user name (-U) and database (-d) as postgres

![psql connect](images/psql-connect.png)

```sh
psql -h rds-postgresql-sample.cyhiiz99ooer.us-east-1.rds.amazonaws.com -p 5432 -d myDatabase -U PrimaryUsername
```

**Using a connection string***
```sh
psql "postgresql://myusername:mypassword@myrdsinstance.cdefghijklmn.us-west-2.rds.amazonaws.com:5432/mydatabase"
```

```sh
export RDS_USERNAME=PrimaryUsername
export RDS_PASSWORD=dbpassword
export RDS_ENDPOINT=rds-postgresql-sample.cyhiiz99ooer.us-east-1.rds.amazonaws.com
export CONNECTION_URL="postgresql://${RDS_USERNAME}:${RDS_PASSWORD}@${RDS_ENDPOINT}:5432/myDatabase"
echo $CONNECTION_URL
psql $CONNECTION_URL
```

#### Connecting to PostgreSQL over SSL
```sh
export RDS_USERNAME=PrimaryUsername
export RDS_ENDPOINT=rds-postgresql-sample.cyhiiz99ooer.us-east-1.rds.amazonaws.com
psql -h $RDS_ENDPOINT -p 5432 \
  "dbname=myDatabase user=${RDS_USERNAME} sslrootcert=postgreSQL/us-east-1-bundle.pem sslmode=verify-full"
```

#### psql client additional information

Here are some more key points about psql client:
- It natively supports history searches using the up and down arrow keys.
- There are a number of backslash commands available for controlling input, output, and other behavior.

### Create a Test Table
First, use the CREATE TABLE command. In this snippet example, the table is named people.

```sql
CREATE TABLE people (id int, fname text, lname text);
```

### Add data

Now, add data to the table using the `INSERT INTO people VALUES` statement. Add rows of data in the format `(id, 'first name', 'last name')`, separating rows with a comma, and terminating the final data row with a semicolon (;). In this example, six people are added as values.

```sql
INSERT INTO people VALUES(1, 'John', 'Doe'),
                   (2, 'Mary', 'Major'),
                   (3, 'Jane', 'Doe'),
                   (4, 'Richard', 'Roe'),
                   (5, 'Nikki', 'Wolf'),
                   (6, 'Jane', 'Roe');
```

### List tables

To list the tables in the current database, you can run the `\dt` command in psql. This displays each table in the database as a row, as shown in the previous graphic.
When the people table was created, it was assigned the default public schema type.

The snippet here shows the people table example with `\dt+.` The plus sign adds the Size and Description columns to the output.

![List tables](images/list-tables.jpeg)

### Describe table

To describe a table, use the `\d+` command. The snippet here shows the people table example.

```
myDatabase=> \d+ people
                                          Table "public.people"
 Column |  Type   | Collation | Nullable | Default | Storage  | Compression | Stats target | Description 
--------+---------+-----------+----------+---------+----------+-------------+--------------+-------------
 id     | integer |           |          |         | plain    |             |              | 
 fname  | text    |           |          |         | extended |             |              | 
 lname  | text    |           |          |         | extended |             |              | 
Access method: heap

myDatabase=> 
```

#### All Together

```
export RDS_USERNAME=PrimaryUsername
export RDS_PASSWORD=dbpassword
export RDS_ENDPOINT=rds-postgresql-sample.cyhiiz99ooer.us-east-1.rds.amazonaws.com
export CONNECTION_URL="postgresql://${RDS_USERNAME}:${RDS_PASSWORD}@${RDS_ENDPOINT}:5432/myDatabase"
echo $CONNECTION_URL
psql $CONNECTION_URL
psql (15.5 (Ubuntu 15.5-1.pgdg22.04+1), server 15.4)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, compression: off)
Type "help" for help.

myDatabase=> \dt
Did not find any relations.
myDatabase=> CREATE TABLE people (id int, fname text, lname text);
CREATE TABLE
myDatabase=> \dt+
                                         List of relations
 Schema |  Name  | Type  |      Owner      | Persistence | Access method |    Size    | Description 
--------+--------+-------+-----------------+-------------+---------------+------------+-------------
 public | people | table | PrimaryUsername | permanent   | heap          | 8192 bytes | 
(1 row)

myDatabase=> INSERT INTO people VALUES(1, 'John', 'Doe'),
                   (2, 'Mary', 'Major'),
                   (3, 'Jane', 'Doe'),
                   (4, 'Richard', 'Roe'),
                   (5, 'Nikki', 'Wolf'),
                   (6, 'Jane', 'Roe');
INSERT 0 6
myDatabase=> \d people 
               Table "public.people"
 Column |  Type   | Collation | Nullable | Default 
--------+---------+-----------+----------+---------
 id     | integer |           |          | 
 fname  | text    |           |          | 
 lname  | text    |           |          | 

myDatabase=> SELECT * FROM people;
 id |  fname  | lname 
----+---------+-------
  1 | John    | Doe
  2 | Mary    | Major
  3 | Jane    | Doe
  4 | Richard | Roe
  5 | Nikki   | Wolf
  6 | Jane    | Roe
(6 rows)

myDatabase=> \d+ people
                                          Table "public.people"
 Column |  Type   | Collation | Nullable | Default | Storage  | Compression | Stats target | Description 
--------+---------+-----------+----------+---------+----------+-------------+--------------+-------------
 id     | integer |           |          |         | plain    |             |              | 
 fname  | text    |           |          |         | extended |             |              | 
 lname  | text    |           |          |         | extended |             |              | 
Access method: heap

myDatabase=> 
```

## Export results to a file

You can use the psql client to export data to a file by using the `\copy` command or by using the output control flags. Either method will export and create a comma-separated values (CSV) file. A standard query returns aligned output.

### Change output format 

If needed, you can change the output format.

#### Disabling aligned output mode
Use `\a` to toggle table alignment to aligned or unaligned.

#### Setting the field separator to ","
Use the `\f  ,` command to change the field separator to a comma as in a CSV file.

#### Displaying the unalignrd data
Use `SELECT * FROM people` to display the data. The data displayed includes the table header (id, fname, lname), followed by the rows of data output, ending with a total of output (six rows).

![Unaligned data](images/unaligned-data.png)

### Output format options

Review the following table for output format options.

![Output formats](images/output-formats.png)

### Change other parameters

Users can also change output parameters related to timing, send a query to a specific file, or write a string to the query output stream.

- **\timing**

Toggle concise timings when running a query.

- **\o [FILE]**

Send all query output results to a specified file.

- **\f [STRING]**

Specify the name of the input file.

### Expanded output mode

When there is a lot of data to deal with, the expanded output mode wraps the page and provides a clear view of the data. The command `\x` toggles the expanded output mode on or off.

#### Expanded output mode disabled

The snippet example here shows a table with expanded output mode disabled. The larger data in the columns is not clearly organized.

![Expanded output mode disabled](images/expanded-output-disabled.png)

#### Expanded output mode enabled

The example snippet here shows the same table with expanded output mode enabled. The table columns are wrapped on the page.

![Expanded output mode enabled](images/expanded-output-enabled.jpeg)

## SET parameters

SET parameters are parameters you can set to control the exchange of data between a server and the client. They can be preconfigured in the `.psqlrc` file.

For example, you can configure `AUTOCOMMIT` to implicitly wrap a `BEGIN` transaction, run the `INSERT`, and `COMMIT` the transaction with an `INSERT` statement.

- `\SET [parameter] {value}`
- `[parameter] {value} in ~/.psqlrc file`

### .psqlrc file

**psqlrc** is the configuration file read by the client. This file needs to be created. For Linux users, the file must be placed in the user's home directory. Users can set common parameters in the `.psqlrc` file.

![set psqlrc](images/set-psqlrc.png)

### Prompts

Prompt characters can be used to return various types of information in psql. Review the following table to see some of the more common ones.

![Prompts](images/prompts.png)

## Watch queries

There will be times when a user needs to view all of the currently running queries. This can be done by setting up a `\watch` command. The query and timing can be set to the user's preferences.

**Run a query**

You can also watch queries. Run the query in this example.

```sql
SELECT count(*) FROM pg_stat_activity;
```

**Add \watch 2 to replay**

Next, use `\watch 2` to replay the query every 2 seconds.

### Use scripts

Scripts are a series of commands that can typically be run on the command line. A Bash script is a plain text file that contains a series of commands. These commands are a mixture of commands we would normally type ourselves on the command line and commands we could type but generally wouldn't.

The following sample Bash script uses psql commands to accomplish tasks within the script.

![use scripts](images/use-scripts.jpeg)

## Install PostgreSQL Ubuntu
```sh
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | sudo tee  /etc/apt/sources.list.d/pgdg.list
sudo apt update
sudo apt install -y postgresql-client-15 libpq-dev
```
