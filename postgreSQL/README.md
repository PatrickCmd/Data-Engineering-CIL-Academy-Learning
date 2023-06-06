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


## Simple EXPLAIN and EXPLAIN ANALYZE

### EXPLAIN command

PostgreSQL can calculate results for a given query in a number of ways. For a WHERE clause, it could go through every row on a table, or use an index (if available) for required fields. When calculating joins, PostgreSQL can use indexes on one or both tables, or build hash tables or other data structures to help calculate results faster.

PostgreSQL considers information such as number of rows on a table, size of each row, and number of distinct values for an attribute. This helps estimate the cost of each calculation method to find and apply the most economical one.

Using the EXPLAIN command, you can see how PostgreSQL calculates both results and cost estimates as it determines how to proceed. Keep in mind that the EXPLAIN command covered here is specific to PostgreSQL, although other database engines provide similar facilities.

### Simple EXPLAIN

To run the EXPLAIN command, type EXPLAIN, and then the query you want to evaluate. End the query with a semicolon, similar to all SQL commands in psql.

```sql
EXPLAIN SELECT * FROM CUSTOMER;
```

Example output of the `EXPLAIN SELECT * FROM CUSTOMER;` command:

```
EXPLAIN
  ->  Seq Scan on customer  (cost=0.00..20.40 rows=1040 width=76)
```

**Explanation of the output**:

The `EXPLAIN` command provides information about how the database query planner intends to execute a given SQL statement. It helps in understanding the query execution plan, which includes details about the steps taken by the database engine to retrieve and process the requested data.

In the example output, we see a line starting with `->` representing the execution step. 

The first step mentioned is `Seq Scan`, which stands for `sequential scan`. It indicates that the database will perform a sequential scan on the `customer` table. This means that it will read each row of the table in the order they are physically stored on disk, without using any specific index or optimization technique.

The cost information is displayed in the format `cost=0.00..20.40`. The cost represents an estimated measure of how much work the database has to perform to execute the query. In this case, the cost ranges from 0.00 to 20.40 units. Lower costs generally indicate more efficient execution plans.

The next part, `rows=1040`, indicates that the query planner estimates that there are 1040 rows in the `customer` table that match the query.

The final part, `width=76`, specifies the estimated average width of each row in bytes.

Overall, this `EXPLAIN` output suggests that the database engine will perform a sequential scan on the `customer` table, reading all the rows and returning all columns (`*`). The cost and row estimates may vary depending on the size and complexity of the table, as well as the available indexes and other factors considered by the query planner.

### EXPLAIN ANALYZE

A variation of the EXPLAIN command, called `EXPLAIN ANALYZE`, will execute the query. This command displays both estimated and actual costs.

```sql
EXPLAIN ANALYZE SELECT * FROM CUSTOMER;
```

Example output of the `EXPLAIN ANALYZE SELECT * FROM CUSTOMER;` command:

```
QUERY PLAN
  ->  Seq Scan on customer  (cost=0.00..20.40 rows=1040 width=76) (actual time=0.052..0.057 rows=1000 loops=1)
```

**Explanation of the output**:

The `EXPLAIN ANALYZE` command provides a detailed execution plan along with actual runtime performance statistics of the query. It not only explains how the database intends to execute the query but also provides information on the actual time taken and the number of rows processed during the query execution.

In the example output, we see a line starting with `->` representing the execution step.

Similar to the previous example, the first step mentioned is `Seq Scan`, indicating a sequential scan on the `customer` table.

The cost information is displayed in the format `cost=0.00..20.40`, representing the estimated cost range for executing the query.

The `rows=1040` indicates the estimated number of rows in the `customer` table that match the query.

The `width=76` specifies the estimated average width of each row in bytes.

In addition to the execution plan details, this output includes actual runtime performance statistics within parentheses. For example, `(actual time=0.052..0.057 rows=1000 loops=1)` provides the following information:

- `actual time=0.052..0.057` indicates the actual execution time taken to perform the query. In this case, it took between 0.052 and 0.057 units of time.
- `rows=1000` represents the actual number of rows returned by the query.
- `loops=1` specifies the number of repetitions or iterations performed during the execution. In this case, it executed the query once (`loops=1`).

Overall, this `EXPLAIN ANALYZE` output not only provides the execution plan and cost estimates but also gives valuable insights into the actual runtime performance of the query, including execution time and the number of rows processed. These actual statistics can be helpful in evaluating and optimizing the query's performance.


## Multi-Level EXPLAIN

### Multi-level EXPLAIN output

When queries are more complicated, PostgreSQL may perform several operations. The input of one feeds into another in a tree-like formation. In this case, the output of EXPLAIN will reflect this tree, with indentation signaling nesting. When reviewing this output, start from the deeper levels of nesting.

#### Two-level example

The following example shows an EXPLAIN output with two levels. First PostgreSQL reads all rows from the table, and then it sorts them.

```sql
EXPLAIN SELECT * FROM customer ORDER BY city;
```

Example output of the `EXPLAIN SELECT * FROM customer ORDER BY city;` command:

```
EXPLAIN
  ->  Sort  (cost=20.80..21.32 rows=208 width=76)
        Sort Key: city
        ->  Seq Scan on customer  (cost=0.00..13.60 rows=208 width=76)
```

**Explanation of the output**:

The `EXPLAIN` command provides information about the query execution plan, including how the database intends to execute the query and any optimizations it may apply. In this case, the query is retrieving all columns (`*`) from the `customer` table and ordering the results by the `city` column.

In the example output, we see multiple lines representing the execution steps, with indentation indicating the hierarchy of the steps.

The first step mentioned is the `Sort` operation. It indicates that the database will perform a sorting operation on the results. The `Sort Key: city` line specifies that the sorting will be done based on the `city` column.

The cost information for the `Sort` step is displayed as `cost=20.80..21.32`. The cost represents the estimated amount of work required to perform the sorting operation. In this case, the estimated cost ranges from 20.80 to 21.32 units.

Inside the `Sort` step, we have another step mentioned, which is the `Seq Scan` operation. It stands for sequential scan, indicating that the database will perform a sequential scan on the `customer` table to retrieve the data. This means it will read each row of the table in the order they are physically stored on disk.

The cost information for the `Seq Scan` step is displayed as `cost=0.00..13.60`. The estimated cost ranges from 0.00 to 13.60 units. It represents the estimated amount of work required to perform the sequential scan.

The `rows=208` indicates the estimated number of rows in the `customer` table that match the query. This estimate is used by the query planner to determine the execution plan.

The `width=76` specifies the estimated average width of each row in bytes.

Overall, this `EXPLAIN` output suggests that the database engine will perform a sequential scan on the `customer` table and then apply a sorting operation on the results based on the `city` column. The cost estimates can vary depending on the size and complexity of the table, as well as the available indexes and other factors considered by the query planner.

#### More than two levels

More complicated queries can exceed two levels of nesting, which makes deciphering output harder. If you read from the inside out, you can usually better understand how PostgreSQL will proceed.

```sql
EXPLAIN ANALYZE SELECT * FROM customer JOIN contact USING (last_name);
```

Example output of the `EXPLAIN ANALYZE SELECT * FROM customer JOIN contact USING (last_name);` command:

```
QUERY PLAN
  ->  Hash Join  (cost=30.40..45.50 rows=1000 width=154) (actual time=0.173..0.230 rows=100 loops=1)
        Hash Cond: (customer.last_name = contact.last_name)
        ->  Seq Scan on customer  (cost=0.00..13.60 rows=1000 width=114) (actual time=0.037..0.076 rows=100 loops=1)
        ->  Hash  (cost=20.00..20.00 rows=1000 width=40) (actual time=0.120..0.120 rows=100 loops=1)
              Buckets: 1024  Batches: 1  Memory Usage: 18kB
              ->  Seq Scan on contact  (cost=0.00..20.00 rows=1000 width=40) (actual time=0.020..0.074 rows=100 loops=1)
Planning Time: 0.139 ms
Execution Time: 0.275 ms
```

**Explanation of the output:**

The `EXPLAIN ANALYZE` command provides a detailed execution plan along with actual runtime performance statistics of the query. It explains how the database intends to execute the query and provides information on the actual time taken, the number of rows processed, and other relevant details.

In the example output, we see multiple lines representing the execution steps, with indentation indicating the hierarchy of the steps.

The first step mentioned is the `Hash Join` operation. It indicates that the database will perform a hash-based join operation to combine the rows from the `customer` and `contact` tables based on the `last_name` column.

The cost information for the `Hash Join` step is displayed as `cost=30.40..45.50`. The cost represents the estimated amount of work required to perform the join operation. In this case, the estimated cost ranges from 30.40 to 45.50 units.

The `Hash Cond: (customer.last_name = contact.last_name)` line specifies the join condition used for the hash join. It indicates that the join is performed by matching the `last_name` column between the `customer` and `contact` tables.

Inside the `Hash Join` step, we have two sub-steps. The first sub-step is a `Seq Scan` operation on the `customer` table, and the second sub-step is a `Hash` operation on the `contact` table.

The `Seq Scan` step on the `customer` table performs a sequential scan to retrieve the data. The cost information for this step is displayed as `cost=0.00..13.60`, and the actual runtime performance statistics show that it took between 0.037 and 0.076 units of time to scan and retrieve 100 rows.

The `Hash` step on the `contact` table builds a hash table for efficient join matching. The cost information for this step is displayed as `cost=0.00..20.00`, and the actual runtime performance statistics show that it took between 0.020 and 0.074 units of time to process and build the hash table with 100 rows.

The `Planning Time` represents the time taken by the query planner to generate the execution plan, and `Execution Time` represents the actual time taken to execute the query.

Overall, this `EXPLAIN ANALYZE` output provides a detailed view of the query execution plan, including the join operation, scan operations, costs, and actual runtime performance statistics. It helps in understanding how


## Diagnosing Performance Issues

The EXPLAIN command is your first tool for performance diagnosis, although its output can be hard to interpret with a complicated query plan. EXPLAIN can also uncover complicated views.

In the example below, selecting from pg_indexes results in a complicated view. However, without looking at output from EXPLAIN, you might expect it to be a simple table.

Even when EXPLAIN provides insight into slower operations, you might be unable to speed up your query. In the example, the first hash join runs longest, but little can be done to change the database structure and query time.

```sql
EXPLAIN ANALYZE SELECT * FROM pg_indexes WHERE tablename='pg constraint';
```


Example output of the `EXPLAIN ANALYZE SELECT * FROM pg_indexes WHERE tablename='pg_constraint';` command:

```
QUERY PLAN
  ->  Seq Scan on pg_indexes  (cost=0.00..20.84 rows=21 width=244) (actual time=0.016..0.097 rows=4 loops=1)
        Filter: (tablename = 'pg_constraint'::name)
        Rows Removed by Filter: 3
Planning Time: 0.157 ms
Execution Time: 0.126 ms
```

**Explanation of the output:**

The `EXPLAIN ANALYZE` command provides a detailed execution plan along with actual runtime performance statistics of the query. It explains how the database intends to execute the query and provides information on the actual time taken, the number of rows processed, and other relevant details.

In the example output, we see multiple lines representing the execution steps, with indentation indicating the hierarchy of the steps.

The first step mentioned is the `Seq Scan` operation. It indicates that the database will perform a sequential scan on the `pg_indexes` table to retrieve the data.

The cost information for the `Seq Scan` step is displayed as `cost=0.00..20.84`. The cost represents the estimated amount of work required to perform the scan operation. In this case, the estimated cost ranges from 0.00 to 20.84 units.

The `width=244` specifies the estimated average width of each row in bytes.

The actual runtime performance statistics show that the scan operation took between 0.016 and 0.097 units of time. It retrieved 4 rows from the `pg_indexes` table.

The `Filter: (tablename = 'pg_constraint'::name)` line represents the filter condition applied during the scan operation. It indicates that only rows where the `tablename` column matches the value `'pg_constraint'` are selected.

The `Rows Removed by Filter: 3` indicates that the filter condition removed 3 rows during the scan operation that did not match the filter criteria.

The `Planning Time` represents the time taken by the query planner to generate the execution plan, and `Execution Time` represents the actual time taken to execute the query.

Overall, this `EXPLAIN ANALYZE` output provides a detailed view of the query execution plan, including the scan operation, cost estimates, actual runtime performance statistics, and the filter condition applied. It helps in understanding how the database executes the query and provides insights into the performance of the query.

### EXPLAIN options

The `EXPLAIN` command in PostgreSQL supports several options to modify output. You can specify whether to include cost estimates, actual timings, or buffers. You can also indicate if you prefer text output or XML, JSON, or YAML output to use with other tools.

To specify these options, place them in parentheses after the EXPLAIN keyword. Include more than one option by separating with commas.

- **COSTS [ Boolean ]**
    - Determines whether to show costs of each node.
- **BUFFERS [ Boolean ]**
    - Determines whether to show buffer usage.
- **TIMING [ Boolean ]**
    - Determines whether to show actual timings.
    - Requires `ANALYZE` option.
- **FORMAT { TEXT | XML | JSON | YAML }**
    - Determines output format.
    - Defaults to text.

```sql
EXPLAIN (ANALZE, BUFFERS true, FORMAT json)
    SELECT bid, sum(abalance) FROM pbbench_accounts
        GROUP BY 1 ORDER BY 1;
```

Example output of the command:

```json
[
  {
    "Plan": {
      "Node Type": "Sort",
      "Parallel Aware": false,
      "Relation Name": "pgbench_accounts",
      "Alias": "pgbench_accounts",
      "Startup Cost": 231520.00,
      "Total Cost": 232070.96,
      "Plan Rows": 1000000,
      "Plan Width": 12,
      "Actual Startup Time": 59.128,
      "Actual Total Time": 87.785,
      "Actual Rows": 1000000,
      "Actual Loops": 1,
      "Sort Key": ["bid"],
      "Sort Method": "quicksort",
      "Sort Space Used": 110672,
      "Sort Space Type": "Memory",
      "Sort Space Used Condition": "<",
      "Shared Hit Blocks": 11887,
      "Shared Read Blocks": 10292,
      "Shared Dirtied Blocks": 0,
      "Shared Written Blocks": 0,
      "Local Hit Blocks": 0,
      "Local Read Blocks": 0,
      "Local Dirtied Blocks": 0,
      "Local Written Blocks": 0,
      "Temp Read Blocks": 0,
      "Temp Written Blocks": 0,
      "Plans": [
        {
          "Node Type": "Seq Scan",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Relation Name": "pgbench_accounts",
          "Alias": "pgbench_accounts",
          "Startup Cost": 0.00,
          "Total Cost": 32920.00,
          "Plan Rows": 1000000,
          "Plan Width": 12,
          "Actual Startup Time": 0.019,
          "Actual Total Time": 12.490,
          "Actual Rows": 1000000,
          "Actual Loops": 1,
          "Shared Hit Blocks": 11887,
          "Shared Read Blocks": 10292,
          "Shared Dirtied Blocks": 0,
          "Shared Written Blocks": 0,
          "Local Hit Blocks": 0,
          "Local Read Blocks": 0,
          "Local Dirtied Blocks": 0,
          "Local Written Blocks": 0,
          "Temp Read Blocks": 0,
          "Temp Written Blocks": 0
        }
      ]
    },
    "Planning Time": 0.090,
    "Triggers": [],
    "Execution Time": 88.279
  }
]
```

**Explanation of the output:**

The output is in `JSON` format and provides a detailed execution plan and runtime statistics for the given query. It includes information about the various steps performed, such as sorting and sequential scanning, as well as details about buffers, timings, and I/O operations.

In this example output, we can see that the query involves a `Sort` operation and a nested `Seq Scan` operation.

The `Sort` operation indicates that the database will sort the results based on the `bid` column. It uses the quicksort method and a memory space of 110672. The estimated startup cost is 231520.00 units, and the total cost is 232070.96 units. The `Plan Rows` represents the estimated number of rows in the plan, and the `Plan Width` represents the average width of each row in bytes.

The nested `Seq Scan` operation scans the `pgbench_accounts` table sequentially. The estimated startup cost is 0.00 units, and the total cost is 32920.00 units. The `Plan Rows` indicates the estimated number of rows in the plan, and the `Plan

