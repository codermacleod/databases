# EXAMPLE USER STORY:
# (analyse only the relevant part - here the final line).

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.


Nouns:
coach
student
list
name
cohort

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Table name: Students

| Record                | Properties          |
| --------------------- | ------------------  |
| students              | cohort,name

Name of the table (always plural): `students` 

Column names: `cohort`

# EXAMPLE:

id: SERIAL
cohort: text
name: text


## 4. Write the SQL.

```sql
-- EXAMPLE
-- file: students_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort text
);