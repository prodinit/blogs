# Database Optimisation: Indexing vs Sharding with Postgres and Django ORM examples

Hello everyone, let me assume the reason you are here.

* Learning about Indexing, OR
* Learning about sharding, OR
* Stealing database related content, OR
* Getting to know about prodinit, OR
* Learning how to built efficient data systems, OR
* Actually strugging with poor database performance, slow queries and what not.

Anyways, now that you are here, I'll try to make sure you learn something new or revise the concepts you already know.

Directly coming to the problem statement I had a few months back, to optimise the database performance. A came up with a few theories on to why our database should be performing the way it is performing. Though the solution I implemented for that particular use case was to increase the size of our database instance, BUT, I learned few database optimisation techniques during that phase.

There are a number of different techniques that can be used to optimize a database, and the two we are discussing today are indexing and sharding.

### Indexing

An index is a data structure that organizes the data in a database table in a specific way to make it easier and faster to search for specific data values. Indexes can be created on any column in a table, but they are most commonly created on columns that are frequently used in queries.

For example, if you have a table of customer data, you might create an index on the customer\_name column to make it easier to search for customers by name. When you create an index on a column, the database engine creates a sorted copy of the data in that column. This sorted copy of the data is then used by the database engine to speed up queries that involve searching for specific values in that column.

#### When to Use Indexing:

* **Frequent Search Queries**: If your application relies heavily on search operations.
* **Small to Medium-sized Datasets**: Ideal for databases with relatively modest data sizes.
* **Complex Joins**: When your queries involve multiple tables and joins.

#### Benefits:

* **Faster Query Performance**: Speeds up data retrieval, especially for SELECT queries.
* **Improved Efficiency**: Reduces the load on servers, leading to more efficient use of resources.

### Sharding

Sharding is the process of dividing a large database into multiple smaller databases. This is done to improve the performance and scalability of the database system.

When you shard a database, you typically divide the data into different shards based on a specific key, such as the customer ID or the date of the transaction. Each shard is then stored on a separate database server.

When a query is executed, the database engine determines which shard contains the data that is needed to answer the query. The database engine then sends the query to the appropriate shard server for execution.

#### When to Use Sharding:

* **Enormous Datasets**: Ideal for applications dealing with massive volumes of data.
* **High Throughput Applications**: When your application experiences a high volume of transactions.
* **Scalability Concerns**: For businesses expecting rapid growth and increased data demands.

#### Benefits:

* **Infinite Scalability**: Allows your application to grow limitlessly without compromising performance.
* **Enhanced Fault Tolerance**: Reduces the risk of a complete system failure since data is distributed.

## ENOUGH THEORY 😤

### PostgreSQL

#### Index

PostgreSQL supports both indexing and sharding. To create an index on a column in PostgreSQL, you use the `CREATE INDEX` statement.

Let's see how we can create an index on the `customer_name` column in the `customers` table.

```
CREATE INDEX idx_customers_customer_name ON customers (customer_name);
```

#### Shard

To shard a database in PostgreSQL, you use the `CREATE TABLE` statement with the `PARTITION BY` clause.

Let's see how we can create a partitioned table to shard the `customers` table by the `customer_id` column

```
CREATE TABLE customers_sharded (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(255),
  timestamp TIMESTAMP NOT NULL
) PARTITION BY RANGE (timestamp)
```

### Django ORM

Django ORM supports indexing and sharding through the `Model.Meta.indexes` attribute and `django-partitions` library.

#### Index

To create an index on a column in Django ORM, you add an Index() object to the Model.Meta.indexes attribute.

Let's see how we can create an index on the `customer_name` column in the `Customer` model.

```
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)

    class Meta:
        indexes = [
            Index(fields=['customer_name']),
        ]
```

#### Shard

To shard a database in Django ORM, we can use the django-partitions library, which provides a convenient way to partition a database table.

Let's see how we can shard the `Customer` model by the `customer_id` column class

```
from django_partitions.models import PartitionedModel

Customer(PartitionedModel):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)

    class Meta:
        partitioning = {
            'partition_type': 'range',
            'partition_subtype': 'integer',
            'partition_column': 'customer_id',
            'partition_range': [(0, 100), (101, 200), (201, 300)],
        }
```

### What is the best way to approach database optimisation?

* **Evaluate the need for indexing/sharding**: Consider your application’s workload and growth projections to determine whether indexing/sharding is necessary.
* **Choose a strategy**: Consider factors such as data distribution, query patterns, and hardware requirements
* **Plan for data migration**: Consider using tools such as pg\_dump and pg\_restore to simplify the migration process.
* **Backup and recovery strategies**
* **Monitor and optimize performance**

If you’re interested in implementing PostgreSQL sharding or are looking for a more complete database optimsation solution, Prodinit can help.

**Written by -** [**Dishant Sethi**](https://linkedin.com/in/dishantsethi)

**Tags**

![Databases](https://img.shields.io/badge/Databases-8A2BE2) ![Backend Engineering](https://img.shields.io/badge/Backend\_Engineering-8A2BE2)

#### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.
