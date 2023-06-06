# PostgreSQL Fundamentals
- PostgreSQL is an enterprise class, open source relational database management system.

- PostgreSQL has a rich history and was created at UC Berkeley. PostgreSQL is flexible, and can scale into the future.

- The PostgreSQL engine adds new features and functionality to appeal to new use cases.

## Documentation, Release notes, and community
- https://www.postgresql.org/

### ACID compliance

**Atomicity**: Store data in an all-or-nothing approach.
**Consistency**: Give me a consistent picture of the data.
**Isolation**: Prevent concurrent data updates from incorrect reads/writes.
**Durability**: When I say `COMMIT`; the data, make sure it is safe until I explicitly destroy it.

### Database transactions
- A transaction is a unit of work.
- A transaction is all or nothing:
    - Beginning (BEGIN;)
    - Work (INSERT/UPDATE/DELETE/SELECT)
    - Ending (END;) results in one of  the following:
        - COMMIT; (save everything)
        - ROLLBACK; (undo all changes, and save nothing)
- Once the transaction ends, it either makes ALL of the changes between BEGIN; and COMMIT; or NONE of them (if there is an error, for example).

### PostgreSQL features
- ACID compliant
- Transactional (uses WAL/REDO)
- Partitioning
- Multiversion concurrency control (readers don’t block writers)
- Online maintenance operations
- Hot/warm Standby
- Full-text search
- Rich geospatial (PostGIS)
- Procedural languages

### Database limitations

#### General database limitations

![Limitations](images/postgres_limit.jpg)

### PostgreSQL terminology
PostgreSQL was designed in academia:
- Objects defined in academic terms
- Terminology based on relational calculus/algebra

#### Common database object names

![Terminology](images/postgres_teminology.jpg)


## SQL Command Line

### Introduction to psql

**psql**

psql is the default command-line program that communicates with PostgreSQL. There is widespread GUI and database client program support for PostgreSQL, but it's still a good idea to be familiar with psql in order to understand documentation and code samples.

**Four main parameters (Connection parameters)**
- **-h**    Hostname
- **-p**    Port, defaults to 5342
- **-U**    Username (notice uppercase "U")
- **-d**    Database name

**SQL commands**

- Type commands in several lines.
- End SQL commands in ";" to be executed.

**Exit**

- **\q** or **Ctrl+D**    Exit

**Executing**

- **-f**    Execute file and exit.
- **-c**    Execute one command and exit.

#### Help

**Outside psql**

- **psql**  --help

**Inside psql**

- **\h**   Help on SQL commands
- **\?**   Help on psql commands

#### Other Commands

**Describing**

- `\d`    Describes things, + for extra info.
- `\d followed by a name`    Describes that specific object.
- `\d followed by certain letters`    Lists kinds of objects, such as:
- `\dt`    Lists tables.
- `\dv`    Lists views.

**Miscellaneous**

- `\timing`    Toggles reporting time spent on each query executed.
- `\a`    Toggles aligned output.
- `\x`    Toggles expanded output.
- `\o`    Saves query output to external file, instead of showing on screen.
- `\i`    Executes one file.
- `\!`    Executes a shell command.


### Resources
- [Official psql documentation](https://www.postgresql.org/docs/11/app-psql.html)
- [Transition from Legacy Databases to a Modern Data Architecture](https://www.devprojournal.com/technology-trends/open-source/transition-from-legacy-databases-to-a-modern-data-architecture/)
