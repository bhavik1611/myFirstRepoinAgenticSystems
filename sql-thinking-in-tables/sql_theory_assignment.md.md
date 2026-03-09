# SQL THOERY ASSIGNMENT

## 1. **Importance of Databases in Real-World AI Systems**

- Databases are essential in real-world AI systems because they provide a reliable and efficient way to store, organize, and retrieve large amounts of structured or unstructured data.
- AI systems typically require access to various kinds of data, such as user profiles, historical transactions, sensor logs, or training datasets.
  - For example, an AI-powered recommender system might need to access user information, product details, and purchase history, all of which are best stored in a structured database.
- Structured storage ensures that data is consistent, easily searchable, and maintains its integrity, which is especially important when supporting automated decision-making and maintaining data quality at scale.

## 2. **The Relational Database Mental Model**

- A relational database organizes data into tables that mimic the structure of a spreadsheet. Each table represents a single type of entity such as "Customers" or "Products".
- Within a table:
  - **Rows** correspond to individual records (e.g., one row per customer).
  - **Columns** define the attributes of each entity (e.g., name, email, address).
- Each table should focus on just one entity to avoid redundant or inconsistent data. For example:

  | CustomerID | Name   | Email             |
  |------------|--------|-------------------|
  | 1          | Alice  | <alice@email.com> |
  | 2          | Bob    | <bob@email.com>   |

  - Here, the "Customers" table represents only customers; their orders would be stored in a separate "Orders" table.

## 3. **The Concept of a Primary Key**

- A primary key is a special column (or combination of columns) in a table that uniquely identifies each record.
- Primary keys must always have unique, non-null values to ensure that every row can be individually referenced.
- They help prevent duplicate records and make it possible to retrieve or update specific entries efficiently.
- Example: In the "Customers" table above, `CustomerID` is the primary key because each customer has a unique ID.

## 4. **Understanding Database Schemas**

- A database schema defines the structure of the database:
  - the tables it contains
  - the columns in each table (including their data types)
  - constraints (like uniqueness or required fields)
  - and how tables are related.
- Schemas are crucial as they provide a blueprint that ensures data is organized consistently, prevents errors, and makes collaboration possible.
- For example, a schema might specify that the "Orders" table has an integer `OrderID` (primary key), a date, and a `CustomerID` (which relates to the Customers table).

## 5. **Relationships and Foreign Keys in Relational Databases**

- Relationships between tables allow you to connect related data.
- This is done using foreign keys (columns in one table that reference the primary key of another table).
- For example, to track which customer placed which order, the "Orders" table might look like:

  | OrderID | CustomerID | Date       |
  |---------|------------|------------|
  | 101     | 1          | 2024-06-10 |
  | 102     | 2          | 2024-06-11 |

  - Here, `CustomerID` in "Orders" is a foreign key referring back to the primary key in "Customers". This connection allows you to join tables and answer questions like "Which orders did Alice place?"
