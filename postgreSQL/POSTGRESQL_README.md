# POSTGRESQL SQL COMMANDS

### Log to postgres database

```
psql --username=name dbname=database_name
```

### List databases

```
\l
```

### Connect to database
```
\c database_name
```

### View tables in database
```
\d
```

### View table details
```
\d table_name
```

### Create Database

```sql
CREATA DATABASE databasename;
```

### Create table in database without columns

```sql
CREATE TABLE table_name();
```

### Add columns to table

```sql
ALTER TABLE table_name ADD COLUMN column_name DATATYPE;
```

```sql
ALTER TABLE table_name ADD COLUMN id SERIAL PRIMARY KEY;
```

```sql
ALTER TABLE table_name ADD COLUMN age INT NOT NULL;
```

```sql
ALTER TABLE table_name ADD COLUMN name VARCHAR(30);
```

### Create table with columns

```sql
CREATE TABLE table_name(column_name DATATYPE CONSTRAINTS);
```

### Change column name

```sql
ALTER TABLE table_name RENAME COLUMN column_name1 TO column_name2;
```

### Drop column from table

```sql
ALTER TABLE table_name DROP COLUMN column_name;
```

### Delete/drop table

```sql
DROP TABLE table_name;
```

### Rename database

```
ALTER DATABASE databasename RENAME TO new_databasename;
```

### Add primary key constraint to column

```sql
ALTER TABLE table_name ADD PRIMARY KEY(columnname);
```

### Add composite primary key to table

```sql
ALTER TABLE table_name ADD PRIMARY KEY(column1, column2);
```

### Remove primary key constraint

```sql
ALTER TABLE table_name DROP CONSTRAINT constraint_name;
```

```sql
ALTER TABLE table_name DROP CONSTRAINT table_name_pkey;
```

### Insert row records in table

```sql
INSERT INTO table_name(col1, col2, col3) VALUES(v1, v2, v3);
```

### Add ForeignKey constraint on adding column

```sql
ALTER TABLE table_name ADD COLUMN column_name DATATYPE REFERENCES referenced_table_name(referenced_column_name);
```

### Add One-to-Many ForeignKey COnstraint on adding column

```sql
ALTER TABLE table_name ADD COLUMN column_name DATATYPE CONSTRAINT REFERENCES referenced_table_name(referenced_column_name);
```

```sql
ALTER TABLE sounds ADD COLUMN character_id INT NOT NULL REFERENCES characters(character_id);
```

### Add Foreign Key constraint

```sql
ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES referenced_table(referenced_column);
```

### Add Unique Constraint

```sql
ALTER TABLE table_name ADD UNIQUE(column_name);
```

### Add NOT NULL constraint

```sql
ALTER TABLE table_name ALTER COLUMN column_name SET NOT NULL;
```

