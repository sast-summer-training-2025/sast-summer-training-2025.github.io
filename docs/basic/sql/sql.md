# 数据库 & SQL

## 课程概述

### 数据库

为什么需要数据库？在日常生活中，我们经常会遇到各种需要存储和处理数据的场景。一所大学需要维护自己学校各个院系、人员和课程的各项信息；一个实验项目可能会面临存储时间、温度、转化率等各项实验过程指标和数据的需求；一个大模型的训练，也需要用到海量的训练数据。

不同的数据类型和应用场景，导向了不同的数据存储方式。小到一个文本文件、表格文件，大到一个专门存储数据的服务器，在开发和生产环境中，我们有很多类似的工具来帮助我们方便高效地存储、读取和处理数据，数据库就是其中的一种解决方案。

数据库相比于普通的文件或表格工具，具备以下优势：

- **高效的数据检索和查询**：数据库支持复杂的查询语句，可以快速从大量数据中筛选出需要的信息，而不是像文本文件那样只能逐行查找。
- **数据一致性和完整性保障**：通过主键、外键、约束等机制，数据库可以保证数据的准确性和一致性，避免重复或错误的数据。
- **并发访问和权限控制**：数据库允许多个用户同时访问和操作数据，并能通过权限管理控制不同用户的访问范围，保证数据安全。
- **事务支持**：数据库支持事务操作，能够保证一组操作要么全部成功、要么全部失败，防止数据出现中间状态。
- **可扩展性和备份恢复**：数据库可以方便地扩展存储容量，并支持数据的备份与恢复，降低数据丢失风险。

因此，数据库不仅能高效地存储和管理大量结构化数据，还能提供数据安全、完整性和高并发等特性，对于处理工程级别、企业规模的数据具有极好的优势，已经是现代信息系统不可或缺的基础组件。

### 关系型数据库

所谓“数据库”是以一定方式储存在一起、能予多个用户共享、具有尽可能小的冗余度、与应用程序彼此独立的数据集合。应用程序只需调用数据库软件提供的 API 接口便可以实现数据的读写，而无需在意数据在文件中如何存储以及如何索引。同学们可在“数据库系统概论”课程深入学习数据的存储方式与检索方式。

根据数据模型进行分类，可以将数据库分为：

- **关系型数据库**，包括 [MySQL](https://www.mysql.com/)、[PostgreSQL](https://www.postgresql.org)、[SQLite](https://www.sqlite.org/)、[Oracle](https://www.oracle.com/database/) 等；
- **非关系型数据库（NoSQL）**，包括 [MongoDB](https://www.mongodb.com/)、[Redis](https://redis.io/)、[Apache Cassandra](https://cassandra.apache.org/) 等。

什么是关系型数据库？我们可以类比 Excel 表格：Excel 表格使用列表示属性、行表示不同的实例，而关系型数据库与之很相似，关系型数据库使用表（Table）来存储数据，其中：

- 每一行代表一条**记录（Record）**，也就是一条完整的数据；
- 每一列代表一个**字段（Field）**，代表一条记录的某个属性。

与 Excel 不同的是，关系型数据库通过关系（Relations）将不同表中的数据连接起来，使得用户可以更方便地进行数据查询和操作。

!!! note

    #### 理解关系型数据库的“关系”

    关系型数据库中的“关系”是指表与表之间的连接或关联。这种关系通过特定的键（Key）来实现，主要包括以下几种类型：

    - **一对一关系（One-to-One Relationship）**：学生表与学号表的关系。

    - **一对多关系（One-to-Many Relationship）**：学生表与院系表的关系。

    - **多对多关系（Many-to-Many Relationship）**：学生表和课程表的关系。
  

    在多对多关系中，一个学生可以选修多门课程，一门课程也可以有多名学生选修。多对多关系通常通过一个中间表（关联表）来实现。

    多对多关系也很好体现了关系型数据库存储的一些优势，考虑这样一种情形：每位同学拥有 `[sid, name, major]` 三个属性，每个课程拥有 `[cid, title, credit, time]` 四个属性，对于每个同学都有 `grade` 属性。
    
    如果用一张 Excel 表格来存储有 10 个学生、每个学生均选择了 10 门相同的课程的情况，那么 Excel 表格的数据存储量约为
    $$
    (3 + 5) \times 10 \times 10 = 800
    $$

    而如果用数据库存储，我们只需要建立 `Students`, 'Courses', 'Association' 三张表。这里的  `Association` 就是中间表，用于存储同学与课程的选课关系，此时数据存储量约为 
    $$
    4 \times 10 + 5 \times 10 + 4 \times 10 \times 10 = 490
    $$
    相比使用 Excel 减少了很多。


### 非关系型数据库（NoSQL）

与关系型数据库不同，**非关系型数据库（NoSQL）** 并不采用表格结构来存储数据，而是根据不同的应用场景，采用了多种灵活的数据模型。常见的 NoSQL 数据库类型包括：

- **文档型数据库**：如 [MongoDB](https://www.mongodb.com/)，以类似 JSON 的文档格式存储数据，适合存储结构灵活、层次丰富的数据。
- **键值型数据库**：如 [Redis](https://redis.io/)，以键值对的形式存储数据，读写速度极快，常用于缓存和会话管理。
- **列式数据库**：如 [Apache Cassandra](https://cassandra.apache.org/)，以列为单位存储数据，适合大规模分布式场景和分析型应用。
- **图数据库**：如 [Neo4j](https://neo4j.com/)，以节点和边的形式存储数据，适合处理复杂的关系网络，如社交网络、推荐系统等。

#### 关系型数据库与非关系型数据库的主要区别

| 特性           | 关系型数据库（SQL）         | 非关系型数据库（NoSQL）         |
| -------------- | -------------------------- | ------------------------------- |
| 数据结构       | 表格（行和列）              | 文档、键值、列、图等多种结构    |
| 规范性         | 严格的模式（Schema）        | 灵活或无模式                    |
| 事务支持       | 完整的 ACID 支持            | 部分支持，强调高可用和扩展性    |
| 扩展方式       | 垂直扩展为主                | 水平扩展为主                    |
| 查询语言       | SQL                        | 各自特定的 API 或查询语言       |
| 适用场景       | 结构化数据、强一致性需求    | 海量数据、高并发、灵活结构      |

**示例：**

- 关系型数据库：适合银行、订单管理等对数据一致性要求高的场景。
- 非关系型数据库：适合社交网络、日志分析、物联网等对扩展性和灵活性要求高的场景。

通过结合使用关系型和非关系型数据库，可以根据实际需求选择最合适的数据存储方案。


## SQL 入门

本次 **数据库与 SQL** 教程相比较于去年和前年的课程做了些许改变，不再使用 MySQL 作为示例工具进行展示和教学，而是使用了兼容更标准、功能更强大的 [PostgreSQL](https://www.postgresql.org/) 作为主要的数据库示例。

PostgreSQL 以其高度的标准兼容性、丰富的特性和良好的扩展性，广泛应用于学术和工业界，同样是学习和实践 SQL 的优秀选择。

> 有关 PostgreSQL 的安装，大家可以参考 https://www.postgresql.org/download/ 自行进行安装。

（讲师授课和演示基于 macOS，部分指令还会给出 Ubuntu 版本，使用 Windows 的同学可以自行依照官方文档尝试或查询）

PostgreSQL 官网提供了非常全面的[技术文档](https://www.postgresql.org/docs/)，同学们可以前往下载阅读或查询。

同时，PostgreSQL 官方还提供了一套面向 SQL 初学者的[入门练习](https://pgexercises.com)，练习中设计了一个真实情境下的场馆管理系统，通过类似实际案例查询的形式，帮助初学者熟悉从简单到复杂的一系列 SQL 基本写法。

考虑到官方文档庞大的体量和阅读难度，本讲将会结合[该入门练习](https://pgexercises.com)的部分例子，对照着文档循序渐进地进行部分 SQL 指令的讲解，**在运用中学习是一个很好的学习方式**。

- 提供给大家练习用的 sql 脚本：

    - [一个学生、课程关系的数据库](/basic/sql/Practice/summer.sql)
    - [来自于 PostgreSQL Exercises 上的会员、设施、预订关系的数据库](/basic/sql/Practice/clubdata.sql)

### 基本概念

回到正题，所以什么是 SQL ？

**SQL（Structured Query Language，结构化查询语言）** 是一种专门用来与关系型数据库进行交互的标准化语言。它可以用来**创建、查询、更新和删除**数据库中的数据和结构，是数据库操作的核心工具。

SQL 主要包括以下几类指令：

- **数据查询语言（DQL）**：如 `SELECT`，用于从数据库中检索数据。
- **数据定义语言（DDL）**：如 `CREATE`、`ALTER`、`DROP`，用于定义和修改数据库结构（如表、视图等）。
- **数据操作语言（DML）**：如 `INSERT`、`UPDATE`、`DELETE`，用于对表中的数据进行增、删、改操作。
- **数据控制语言（DCL）**：如 `GRANT`、`REVOKE`，用于控制对数据库的访问权限。

SQL 语句通常具有高度的可读性和结构化特点。例如，下面是一条简单的 SQL 查询语句：

```sql
SELECT name, age FROM students WHERE age > 18;
```

这条语句的含义是：从 `students` 表中查询所有 `age` 大于 18 的学生的 `name` 和 `age` 字段。

SQL 是一种声明式语言，用户只需描述“想要什么”，而不需要关心“如何实现”。数据库系统会自动优化和执行这些操作。

同时，SQL 也具有如下语言特性：

- 脚本语言（类似 Python）：可以交互执行也可以事先写好后一次性执行；
- 强类型（区别于 MySQL 的弱类型）

<p align="center">
    <img src="/basic/sql/Practice/MySQL.jpg" alt="MySQL" width="45%"/>
    <img src="/basic/sql/Practice/PostgreSQL.png" alt="PostgreSQL" width="60%"/>
</p>

在 PostgreSQL 中，有关大小写的区分：

- SQL 关键字：不区分大小写（如 SELECT, FROM, WHERE）。
- 标识符（表名、列名等）：
	- 如果你不加双引号，PostgreSQL 会自动将其转为小写；
	- 如果你加双引号，则会严格区分大小写。

> 在 PostgreSQL 中，`'` 标识的部分表示**字符串常量**，`"` 标识的部分表示**精确标识符（区分大小写）**。

### 数据类型

PostgreSQL 支持丰富且灵活的数据类型，主要分为数值、字符、日期/时间、布尔、枚举、数组等类型。常用类型如下：

- **整数类型**
    - `INTEGER`（或 `INT`）：4 字节，范围 $[-2^{31}, 2^{31}-1]$
    - `BIGINT`：8 字节，范围 $[-2^{63}, 2^{63}-1]$
    - `SMALLINT`：2 字节，范围 $[-2^{15}, 2^{15}-1]$
    - PostgreSQL 不支持 `UNSIGNED` 关键字，所有整数类型均为有符号类型。

- **浮点类型**
    - `REAL`：4 字节，单精度浮点数
    - `DOUBLE PRECISION`：8 字节，双精度浮点数
    - `NUMERIC(p, s)` / `DECIMAL(p, s)`：可变精度定点数，适合高精度计算（如财务数据）

- **字符类型**
    - `CHAR(n)`：定长字符串，长度为 n，空白自动填充
    - `VARCHAR(n)`：变长字符串，最大长度 n
    - `TEXT`：变长字符串，无长度限制，适合存储大文本

- **日期/时间类型**
    - `DATE`：仅日期，格式 `YYYY-MM-DD`
    - `TIME`：仅时间，格式 `hh:mm:ss`
    - `TIMESTAMP`：日期和时间，格式 `YYYY-MM-DD hh:mm:ss[.fraction]`
    - `TIMESTAMPTZ`：带时区的时间戳

- **布尔类型**
    - `BOOLEAN`：取值为 `TRUE`、`FALSE`

- **其他常用类型**
    - `SERIAL` / `BIGSERIAL`：自增整数，常用于主键（本质上是整数+序列）
    - `UUID`：通用唯一标识符
    - `ARRAY`：数组类型，如 `INTEGER[]`
    - `JSON` / `JSONB`：存储 JSON 格式数据，`JSONB` 支持高效索引和查询

- 特别的，`NULL` 表示空值（与 `0` 和 `''` 作区分）。在没有被分配值且没有默认值得字段在插入时会被分配 NULL 这个空值来表示记录中的某个字段没有数据。

**示例：**

```sql
CREATE TABLE example (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INTEGER,
        balance NUMERIC(10, 2),
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        is_active BOOLEAN DEFAULT TRUE,
        tags TEXT[],
        profile JSONB
);
```

**特别说明：**
- PostgreSQL 推荐尽量避免允许字段为 `NULL`，以简化查询和提升性能。
- 与 MySQL 不同，PostgreSQL 没有 `UNSIGNED` 类型，若需存储非负数请自行约束。
- `TEXT` 类型在 PostgreSQL 中没有长度限制，适合大文本存储。
- `TIMESTAMPTZ` 推荐用于需要时区信息的时间存储。

更多详细数据类型可参考官方文档：[PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html)


### 主键、外键和索引

#### 主键（Primary Key）

主键用于唯一标识表中的每一行，要求**唯一且非空**。在 PostgreSQL 中，常用 `SERIAL` 或 `BIGSERIAL` 类型配合 `PRIMARY KEY` 自动生成自增主键。例如：

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

也可以使用多个字段作为**联合主键**：

```sql
CREATE TABLE association (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id)
);
```

#### 外键（Foreign Key）

外键用于建立表与表之间的关联，保证引用的数据存在，维护数据一致性。例如：

```sql
CREATE TABLE association (
    student_id INT REFERENCES students(id),
    course_id INT REFERENCES courses(id)
);
```

可以通过 `ON DELETE CASCADE` 等选项设置级联操作：

```sql
CREATE TABLE association (
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(id)
);
```

!!! note

    **级联操作**是指在数据库中，当对某个表（如父表）执行删除或更新操作时，相关联的另一个表（如子表）会自动进行相应的操作。例如，使用 ON DELETE CASCADE 时，如果删除了父表中的一条记录，所有引用该记录的子表数据也会被自动删除。这有助于保持数据的一致性，避免出现“孤儿”数据。

    常见的级联操作有：

    - `ON DELETE CASCADE`：删除父表记录时，自动删除所有相关的子表记录。
    - `ON UPDATE CASCADE`：更新父表主键时，自动更新所有相关的子表外键。
    - `ON DELETE SET NULL`：删除父表记录时，将子表中相关外键字段设置为 NULL。
    - `ON DELETE RESTRICT`：如果子表中存在相关记录，则不允许删除父表记录。
  
    这样可以简化数据维护，减少手动同步数据的工作量。

#### 索引（Index）

索引用于加速查询，主键和唯一约束会自动创建索引。对于经常查询的字段，可以手动添加索引：

```sql
CREATE INDEX idx_name ON students(name);
```

索引提升查询效率，但会略微影响插入和更新性能。

更多约束如 `UNIQUE`、`NOT NULL`、`CHECK`、`DEFAULT` 也可用于保证数据完整性，具体语法与 MySQL 类似。

### 数据库和数据表操作

#### 前期准备

**1. 启动 PostgreSQL 服务**

- **macOS**：
    ```bash
    brew services start postgresql@xx
    ```
- **Ubuntu**：
    ```bash
    sudo systemctl start postgresql
    ```

**2. 登录 PostgreSQL 服务**

- **选择数据库进行连接**：
    - **macOS**：
    ```bash
    psql -U <用户名> -f <sql脚本文件> -d <数据库名>
    ```
    > 没有指定 `-U` 参数时，会以默认 `whoami` 的用户进行登录。

    默认情况下，PostgreSQL 安装完后会自带一个 postgres 数据库，用于帮助用户进入命令行工具。

    ```bash
    psql postgres
    ```

    - **Ubuntu**：
    在 Ubuntu 等 Linux 系统中，需要先切换到 postgres 用户，随后再进入 PostgreSQL 服务：
    ```bash
    sudo -i -u postgres
    psql
    ```


#### 数据库相关

**1. 创建数据库（CREATE）**

  ```bash
  createdb -U <用户名> <数据库名>
  ```

  你也可以进入 PostgreSQL，然后执行：
  ```sql
  CREATE DATABASE mydb;
  ```

**2. 切换数据库**

在 `psql` 命令行下，使用如下命令切换数据库：

```sql
\c summer25
```

- `\c` 是 `connect` 的含义。

**3. 查看数据库列表**

列出所有数据库：
  ```sql
  \l
  ```

- `\l` 是 `list` 的含义。

**4. 删除数据库（DROP）**

  ```sql
  DROP DATABASE summer25;
  ```

**5. 重命名数据库（ALTER）**

只能在数据库未被连接时操作（不能重命名当前连接的数据库），例如：

  ```sql
  ALTER DATABASE oldname RENAME TO newname;
  ```

#### 表相关

**1.创建数据表（CREATE）**

```sql
CREATE TABLE Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sid CHAR(10) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    major VARCHAR(255) NOT NULL,
);

CREATE TABLE Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cid VARCHAR(8) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    credit INT NOT NULL,
    time VARCHAR(255)
);

CREATE TABLE Association (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade CHAR(2),
    CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES Students(id),
    CONSTRAINT fk_course_id FOREIGN KEY (course_id) REFERENCES Courses(id)
);
```

**2.查看数据表**

- **列出当前数据库的所有表**：
    ```sql
    \dt
    ```

    - `\dt` 是 `describe tables` 或 `display tables`

- **查看表结构**：

    ```sql
    \d association
    ```

    - `\d` 是 `describe` 的含义

**3.修改表结构（ALTER）**

- **添加字段**：
    ```sql
    ALTER TABLE students ADD gender VARCHAR(10);
    ```
- **删除字段**：
    ```sql
    ALTER TABLE students DROP COLUMN gender;
    ```
- **修改字段类型**：
    ```sql
    ALTER TABLE students ALTER COLUMN sid TYPE CHAR(20);
    ```
- **添加索引**：
    ```sql
    CREATE INDEX idx_sid ON students(sid);
    ```
- **删除外键**（需先查外键名）：
    ```sql
    ALTER TABLE association DROP CONSTRAINT association_student_id_fkey;
    ```

**4.重命名表和字段**

- **重命名表**：
    ```sql
    ALTER TABLE students RENAME TO learners;
    ```
- **重命名字段**：
    ```sql
    ALTER TABLE learners RENAME COLUMN name TO full_name;
    ```

**5.删除表（DROP）**

- **删除表**：
    ```sql
    DROP TABLE learners;
    ```

> **更多 `psql` 命令可通过 `\h`（查看 SQL 语法帮助）和 `\?`（查看 psql 命令帮助）获取。**

### CRUD

> In computer programming, **create, read, update, and delete** (**CRUD**) are the four basic operations of [persistent storage](https://en.wikipedia.org/wiki/Persistent_storage).

每个字母代表一个操作：

|  CRUD  |  SQL   |
| :----: | :----: |
| Create | INSERT |
|  Read  | SELECT |
| Update | UPDATE |
| Delete | DELETE |

本部分讲义基于 [PostgreSQL Exercises](https://pgexercises.com) 上的练习题目展开，读者可以自行前往 https://pgexercises.com/gettingstarted.html 下载该部分练习使用的**数据库文件**和**查询对应的表结构**。


<p align="center">
    <img src="/basic/sql/Practice/schema-horizontal.svg" alt="schema" width="800"/>
</p>


#### INSERT

Modifying Data 相关的操作都比较简单。读者可参考 https://pgexercises.com/questions/updates/ 自行学习。此处仅给出代码示例。

- 插入单条记录：
    ```sql
    insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    values (9, 'Spa', 20, 30, 100000, 800);  
    ```

    如果按照一开始定义表时的字段顺序，下述插入指令也是可以的：

    ```sql
    insert into cd.facilities values (9, 'Spa', 20, 30, 100000, 800);
    ```

- 插入多条记录：
  ```sql
  insert into cd.facilities
      (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
      values
          (9, 'Spa', 20, 30, 100000, 800),
          (10, 'Squash Court 2', 3.5, 17.5, 5000, 80);  
  ```
    
    另一种写法：

    ```sql
    insert into cd.facilities
        (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
        SELECT 9, 'Spa', 20, 30, 100000, 800
        UNION ALL
            SELECT 10, 'Squash Court 2', 3.5, 17.5, 5000, 80;
    ```

- 带有计算的插入记录：
    ```sql
    insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    select (select max(facid) from cd.facilities)+1, 'Spa', 20, 30, 100000, 800;   
    ```

#### UPDATE

- 更新单个字段：
    ```sql
    update cd.facilities
    set initialoutlay = 10000
    where facid = 1;          
    ```

    不通过 `where` 指定的话，会更新所有记录。

- 更新多个字段：
  ```sql
  update cd.facilities
    set
        membercost = 6,
        guestcost = 30
    where facid in (0,1);   
  ```

- 依据记录更新字段：
  ```sql
  update cd.facilities facs
      set
          membercost = (select membercost * 1.1 from cd.facilities where facid = 0),
          guestcost = (select guestcost * 1.1 from cd.facilities where facid = 0)
      where facs.facid = 1;  
  ```

    Postgres 提供了一个名为 UPDATE...FROM SQL 的非标准扩展，它允许您提供一个 FROM 子句来生成用于子 SET 句的值。
    ```sql
    update cd.facilities facs
    set
        membercost = facs2.membercost * 1.1,
        guestcost = facs2.guestcost * 1.1
    from (select * from cd.facilities where facid = 0) facs2
    where facs.facid = 1;
    ```

#### DELETE

- 删除表中所有字段：
  ```sql
  delete from cd.bookings;    
  ```

    你还可以使用 `TRUNCATE`，这个指令更快更底层。
    ```sql
    truncate cd.bookings;
    ```

- 删除表中指定记录：
  ```sql
  delete from cd.members where memid = 37;   
  ```

- 运用子查询：
  ```sql
  delete from cd.members where memid not in (select memid from cd.bookings);    
  ```

#### SELECT

`SELECT` 是获取数据最基本的操作。

##### BASIC

- 获取 **所有** 字段（[Basic.Q1](https://pgexercises.com/questions/basic/selectall.html)）：
    ```sql
    select * from cd.facilities;
    ```

- 获取 **部分** 字段（[Basic.Q2](https://pgexercises.com/questions/basic/selectspecific.html)）：
    ```sql
    select name, membercost from cd.facilities;
    ```

##### WHERE

- 获取 **条件筛选** 后的字段（[Basic.Q3](https://pgexercises.com/questions/basic/where.html), [Basic.Q4](https://pgexercises.com/questions/basic/where2.html)）：
    
    在 SQL 中，使用 `WHERE` 配合 `SELECT`，可以实现基于条件表达式的筛选：

    ```sql
    select * from cd.facilities where membercost > 0;

    select facid, name, membercost, monthlymaintenance from cd.facilities where monthlymaintenance = 3000;
    ```

    > SQL 中的“不等于”可以使用 `<>` 或 `!=`，等于只需要使用 `=` 。

##### AND, OR, NOT

  除此之外，SQL 还支持多个条件表达式的逻辑组合。

  - 基本的逻辑关系符有 `AND`, `OR`, `NOT`。
      ```sql
      select memid, firstname, surname from cd.members 
          where memid != 0 
          and firstname is not null
          and not surname is null;
      ```

##### NULL

  上述例子也展现了一个特殊的类型: `NULL` 类型。

  如前所述，没有被分配值且没有默认值得字段在插入时会被分配 `NULL` 这个空值来表示记录中的某个字段没有数据。
  
  在 PostgreSQL 中，不能直接通过 `firstname = NULL` 这样的语句来判断一个值是不是 `NULL`，而需要通过 `is null` 和 `is not null` 表达式。

##### IN

- 基于 **指定范围** 的条件筛选（[Basic.Q6](https://pgexercises.com/questions/basic/where4.html)）：
    ```sql
    select *
    	from cd.facilities 
    	where 
    		facid in (1,5);

    select * 
    	from cd.facilities
    	where
    		facid in (
    			select facid from cd.facilities
    			);
    ```

##### LIKE

- 基于 **匹配** 的条件筛选（[Basic.Q5](https://pgexercises.com/questions/basic/where3.html), [String.Q4](https://pgexercises.com/questions/string/reg.html)）：
    ```sql
    select *
    	from cd.facilities 
    	where 
    		name like '%Tennis%'; 
    ```

    > SQL's `LIKE` operator provides simple pattern matching on strings. It's pretty much universally implemented, and is nice and simple to use - it just takes a string with the % character matching any string, and _ matching any single character. 

    顺带一提，也可以使用 `~` 来匹配**正则表达式**，不过使用 `LIKE` 处理简单匹配会更加的便携一些。

##### CASE

- 依据条件 **分类** 进行筛选（[Basic.Q7](https://pgexercises.com/questions/basic/classify.html)）：
    ```sql
    select name, 
    	case when (monthlymaintenance > 100) then
    		'expensive'
    	else
    		'cheap'
    	end as cost
    	from cd.facilities;          
    ```

    `CASE` 语句实际上支持多个 `WHEN`，且并不一定需要 `ELSE` 来（也就是并不需要覆盖所有情况），对于未覆盖到的情况，则会返回 `NULL` 。

##### OPERATION ON DATE

在 SQL 中，日期具有固定的类型和格式，比如对于 `timestamp` 时间戳，固定为 `YYYY-MM-DD HH:MM:SS.nnnnnn` 格式。

- 对于时间戳，用户像比较 unix 时间戳一样比较它们（[Basic.Q8](https://pgexercises.com/questions/basic/date.html)）：

    ```sql
    select memid, surname, firstname, joindate 
  	from cd.members
  	where joindate >= '2012-09-01';  
    ```

- 也可以通过将时间戳 **相减**，得到 **时间间隔** （[Date.Q2](https://pgexercises.com/questions/date/interval.html)）。

    ```sql
    select timestamp '2012-08-31 01:00:00' - timestamp '2012-07-30 01:00:00' as interval;
    ```

更多有关 `Date` 相应类型的操作和用法，读者可以继续阅读和尝试如下[Date 练习](https://pgexercises.com/questions/date/)。配合 `extract`, `date_trunc` 等函数使用，可以实现更多效果。

##### DISTINCT

- **去重**（[Basic.Q9](https://pgexercises.com/questions/basic/unique.html)）：

    ```sql
    select distinct surname from cd.members;
    ```

##### ORDER BY & Limit

- **排序和限制输出个数**（[Basic.Q9](https://pgexercises.com/questions/basic/unique.html)）：

    ```sql
    select distinct surname 
    	from cd.members
    order by surname
    limit 10;   
    ```

    运用 `LIMIT` 和 `ORDER BY`，实际上可以起到了筛选最大值/最小值的效果（[Basic.Q12](https://pgexercises.com/questions/basic/agg2.html)）：

    ```sql
    select firstname, surname, joindate
    	from cd.members
    order by joindate desc
    limit 1;
    ```

##### UNION
- **链接** 不同表的查询结果（[Basic.Q10](https://pgexercises.com/questions/basic/union.html)）
    
    通过 `UNION` 可以将多个表的查询结果，合并在一张表中（记录层面上的链接，而非字段）
    ```sql
    select surname from cd.members union select name from cd.facilities;
    ```

#### Joins and Subqueries

<p align="center">
    <img src="/basic/sql/Practice/join.png" alt="Join" width="600"/>
</p>

很多时候出于设计的规范性与便携性，我们会在各个对象（会员、设施等）各自表中维护具体的字段（名称、费用等），而在 `Association` 表（比如这里等 `cd.bookings` 表）中，仅维护其他对象表的 `id` 和必要的信息。比如在这里的预定表中，我们通过维护 `memid` 和 `facid` 两个外键，来关联到会员表和设施表。

但是仅仅通过 `id`，并不能让我们在查询预订表中获得更多的信息，查询起来也显得不够便捷。比如我希望查询名为 David Farrell 的用户的所有预订，我就需要经历

  1. 通过 `cd.members` 表查询用户 `memid`
  2. 利用 `memid` 在 `cd.bookings` 中查询对应预订信息

当关联的表格增多，关系变复杂时，这种操作是不太能容忍的。有没有什么方式，可以更加便捷地进行查询呢？

观察我们在查询步骤中的核心思想，其实是需要找出两张表中有关联的字段，然后像原先我们存储在 Excel 中那样，扩展成一张大的表，随后再进行查询时，就能获得足够多我们想要的信息了。

PostgreSQL 为我们提供了 `JOIN` 这样的工具，来帮助我们完成这一操作。

`JOIN` 的**基本思想**是，将两张表的记录逐一取出，依据 `ON` 提供的条件式进行比对，当满足条件时，放入一张新的表。**也就是说，`JOIN` 的结果是一张新的表。**

你可以使用 `AS` 给表起别名，或者直接将别名跟在表后。

**实际上，一次 `SELECT`，就是一次生成表的过程。**在 `Subqueries` 中我们将看到，我们可以通过 `()` 的形式，来捕获一次表生成的结果，用来给另一条语句使用，也就构成了多重查询。

有关 `JOIN` 和 `Subqueries` 的使用方式和原理，在 [Joins and Subqueries](https://pgexercises.com/questions/joins/) 中有极好的体现，推荐读者自行前往尝试下链接中的几个习题。此处摘出其中的两道作为样例与对比：

- [Produce a list of costly bookings](https://pgexercises.com/questions/joins/threejoin2.html)

  ```sql
  select mems.firstname || ' ' || mems.surname as member, 
  	facs.name as facility, 
  	case 
  		when mems.memid = 0 then
  			bks.slots*facs.guestcost
  		else
  			bks.slots*facs.membercost
  	end as cost
          from
                  cd.members mems                
                  inner join cd.bookings bks
                          on mems.memid = bks.memid
                  inner join cd.facilities facs
                          on bks.facid = facs.facid
          where
  		bks.starttime >= '2012-09-14' and 
  		bks.starttime < '2012-09-15' and (
  			(mems.memid = 0 and bks.slots*facs.guestcost > 30) or
  			(mems.memid != 0 and bks.slots*facs.membercost > 30)
  		)
  order by cost desc;   
  ```

- [Produce a list of costly bookings, using a subquery](https://pgexercises.com/questions/joins/tjsub.html)

  ```sql
  select member, facility, cost from (
  	select 
  		mems.firstname || ' ' || mems.surname as member,
  		facs.name as facility,
  		case
  			when mems.memid = 0 then
  				bks.slots*facs.guestcost
  			else
  				bks.slots*facs.membercost
  		end as cost
  		from
  			cd.members mems
  			inner join cd.bookings bks
  				on mems.memid = bks.memid
  			inner join cd.facilities facs
  				on bks.facid = facs.facid
  		where
  			bks.starttime >= '2012-09-14' and
  			bks.starttime < '2012-09-15'
  	) as bookings
  	where cost > 30
  order by cost desc;          
  ```

- [Produce a list of all members, along with their recommender](https://pgexercises.com/questions/joins/self2.html)

  ```sql
  select mems.firstname as memfname, mems.surname as memsname, recs.firstname as recfname, recs.surname as recsname
  	from 
  		cd.members mems
  		left outer join cd.members recs
  			on recs.memid = mems.recommendedby
  order by memsname, memfname; 
  ```

- [Produce a list of all members, along with their recommender, using no joins.](https://pgexercises.com/questions/joins/sub.html)

  ```sql
  select distinct mems.firstname || ' ' ||  mems.surname as member,
  	(select recs.firstname || ' ' || recs.surname as recommender 
  		from cd.members recs 
  		where recs.memid = mems.recommendedby
  	)
  	from 
  		cd.members mems
  order by member;          
  ```

另外一个子查询极好的例子，我们将在 **Aggregates** 部分结束后看到。

- 顺带一提，上述例子展现了 **字符串拼接** 的基本方式。

#### Aggregates

##### BASIC

- **聚合** 函数（[Basic.Q11](https://pgexercises.com/questions/basic/agg.html), [Basic.Q12](https://pgexercises.com/questions/basic/agg2.html)）

    SQL 提供了**聚合**函数这一强大的工具，用于将表中某一字段所有记录的数据通过某种特定的计算得到一个新的值。

    - 例如在（[Aggregates.Q1](https://pgexercises.com/questions/aggregates/count.html)） 中，我们通过 `COUNT` 计算表中所有条目的个数：

    ```sql
    select count(*) from cd.facilities;
    ```

    - `COUNT` 等函数也可以配合 `WHERE` 使用（[Aggregates.Q2](https://pgexercises.com/questions/aggregates/count2.html)）：
    
    ```sql
    select count(*) from cd.facilities where guestcost >= 10;
    ```

    - 在（[Basic.Q11](https://pgexercises.com/questions/basic/agg.html), [Basic.Q12](https://pgexercises.com/questions/basic/agg2.html)）中，我们通过 `MAX` 来得到表中的最大值。
  
    ```sql
    select firstname, surname, joindate
	from cd.members
	where joindate = 
		(select max(joindate) 
			from cd.members);          
    ```

    !!! note

        你可能会在（[Basic.Q12](https://pgexercises.com/questions/basic/agg2.html)）中尝试如下代码：

        ```sql
        select firstname, surname, max(joindate)
        from cd.members;
        ```

        这是一个很自然的想法，但是不幸的是，这在 SQL 中并行不通，这是因为 `MAX` 并不是像 `WHERE` 那样限制选出的行，而是仅接受一大堆值，然后返回一个最大的值。上述代码会导致 PostgreSQL 不知道怎么将返回了一堆行的firstname, surname 的列表和只返回一行的 `MAX` 匹配连接起来。所以从语义上，你必须说“为我找到入会日期与最大入会日期相同的行”，也就是 **两步** 操作。

        当然，你也可以通过排序然后取顶部行解决这个问题，二者是等价的。

    最常用的聚合函数，有 `COUNT`, `MAX`, `MIN`, `AVG`, `SUM`。

    更多 PostgreSQL 提供的聚合函数，可以去如下网址查找 https://www.postgresql.org/docs/current/functions-aggregate.html。

##### GROUP BY

我们在上一节中提到，如果你使用如下代码，PostgreSQL 会因为不知如何连接多值和单值而报错：

  ```sql
  select firstname, surname, max(joindate)
          from cd.members;
  ```

但是不是意味着 `select firstname, surname, max(joindate)` 这样子的语句就不能存在了呢？实际上并不是，我们其实经常会遇到如下需要将表计算值和行记录连接在一起的情形：

- **分组统计**（[Aggregates.Q4](https://pgexercises.com/questions/aggregates/fachours.html)）：

  我有一张设施使用记录的表，现在我想统计每个设施的总使用时长:

  ```sql
  select facid, sum(slots) as "Total Slots"
  	from cd.bookings
  	group by facid
  order by facid;          
  ```

  `GROUP BY` 会将数据批处理成组，并为每个组单独运行聚合函数。指定 GROUP BY 时，数据库会为提供的列中的每个不同值生成聚合值。这样子，就能实现我们分组统计的目的。

  **需要注意的是**，在 PostgreSQL 中使用 `GROUP BY` 时，出现在 `SELECT` 中的非 `Aggregates` 的字段，都需要放入 `GROUP BY` 中，尽管有时候看上去对一些唯一的字段（如 id）做分组并没有意义。（MySQL 中似乎可以选择是否开启这个检查）

##### HAVING

考虑上面那道题的进阶版，我希望列出设施使用总 slots 超过 1000 的设施（[Aggregates.Q8](https://pgexercises.com/questions/aggregates/fachours1a.html)）：

对于分组统计的情形，你有时可能希望运行如下命令：

```sql
select facid, sum(slots) as "Total Slots"
        from cd.bookings
		where sum(slots) > 1000
        group by facid
        order by facid;
```

通过运行上述指令，你会发现 PostgreSQL 提供了如下报错：

```sql
ERROR: aggregate functions are not allowed in WHERE
  Position: 76

 Query was: select facid, sum(slots) as "Total Slots"
        from cd.bookings
		where sum(slots) > 1000
        group by facid
        order by facid;
```

这是因为 PostgreSQL 不允许在 `WHERE` 中运行 `Aggregates` 相关的函数。取而代之的，你可以通过 `HAVING` 达成相似的目的：

```sql
select facid, sum(slots) as "Total Slots"
        from cd.bookings
        group by facid
        having sum(slots) > 1000
        order by facid;
```

> The behaviour of HAVING is easily confused with that of WHERE. The best way to think about it is that in the context of a query with an aggregate function, WHERE is used to filter what data gets input into the aggregate function, while HAVING is used to filter the data once it is output from the function. Try experimenting to explore this difference!

> HAVING 的行为很容易与 WHERE 的行为混淆。最好的思考方式是，在具有聚合函数的查询上下文中， WHERE 用于过滤输入到聚合函数中的数据，而 HAVING 用于过滤从函数输出的数据。尝试尝试探索这种差异！

#### CTEs

这里我们看这个一个例子（[Aggregates.Q11](https://pgexercises.com/questions/aggregates/fachours2.html)）:

- Output the facility id that has the highest number of slots booked. (输出预订 slots 数最多的设施)

在已经有 `GROUP` 的情况下，使用 `LIMIT` 和 `ORDER` 固然可以很轻松地实现，但让我们来看看不用 `LIMIT` 的版本：

```sql
select facid, sum(slots) as totalslots
	from cd.bookings
	group by facid
	having sum(slots) = (select max(sum2.totalslots) from
		(select sum(slots) as totalslots
		from cd.bookings
		group by facid
		) as sum2);
```

这是有关子查询（Subqueries）的一个极好的例子，同时也很好体现了 `GROUP` 如何结合 `HAVING`，又如何造成了查询上的不便局面。

值得一提的是，PostgreSQL 还提供了 [Common Table Expressions](https://www.postgresql.org/docs/current/static/queries-with.html)(CTEs) 的概念，CTEs 可以被理解成 PostgreSQL 允许您在查询中内联定义数据库视图，然后像使用宏一样去使用它。

CTE 以 的形式 WITH CTEName as (SQL-Expression) 声明。您可以在下面看到我们的查询重新定义以使用 CTE：

```sql
with sum as (select facid, sum(slots) as totalslots
	from cd.bookings
	group by facid
)
select facid, totalslots 
	from sum
	where totalslots = (select max(totalslots) from sum);
```

这既美化了代码风格，又提高了可读性。

#### More About

这里最后讲一个 PostgreSQL 提供的神奇特性：`Window Function`。

在 PostgreSQL 中，`Aggregates` 函数默认会导致聚合的结果，也就是一大堆输入的数据最后塌缩为一个数据。反过来，当我们不希望折叠数据时，我们可以在 `Aggregates` 函数后加上 `over`，并用 `partition` 指定分组依据（类似 `group`）。比如下面这个例子：

- [Produce a list of member names, with each row containing the total member count](https://pgexercises.com/questions/aggregates/countmembers.html)

但是产生一堆一样的值其实没有太大的用处，`Window Function` 更大的用处在于不分组的情况下产生与分组有关的信息，以及对 `rank()` 的支持：

- 输出会员名单与该会员在其加入当月的位次。
  ```sql
  select count(*) over(partition by date_trunc('month',joindate) order by joindate),
  	firstname, surname
  	from cd.members
  order by joindate;
  ```

- 按四舍五入后的时间对成员排序。
  ```sql
  select firstname, surname,
  	((sum(bks.slots)+10)/20)*10 as hours,
  	rank() over (order by ((sum(bks.slots)+10)/20)*10 desc) as rank

  	from cd.bookings bks
  	inner join cd.members mems
  		on bks.memid = mems.memid
  	group by mems.memid
  order by rank, surname, firstname;  
  ```

更多有趣的机制，比如 `Recursive Queries`，大家可以自行去 [PostgreSQL Exercises](https://pgexercises.com/questions/recursive/) 学习与练习。


### EXPLAIN

你可能关心查询是如何被数据库执行的，这是可以使用 `EXPLAIN ANALYZE`，让 MySQL 打印执行计划，例如：

```mysql
EXPLAIN ANALYZE
  select count(*) over(partition by date_trunc('month',joindate) order by joindate),
  	firstname, surname
  	from cd.members
  order by joindate;
```

### ORM

在我们实际开发中，通常会直接使用成熟的后端框架来操作数据库，例如 Django 等，在这些框架中，你无需手写 SQL 语句，而可以直接使用它的 ORM 框架（或者其他框架）。

ORM 全称为 Objected Relational Mapping，其构造了数据库对象与 Python 对象中的如下映射：

```
TABLE -> Class
Record -> Instance（实例）
Column -> Attribute（属性）
```
实际上，ORM 在执行操作时依然会将对应的操作转换成数据库原生语句，但是其拥有如下优点：

- **提高开发效率**：开发者可以直接操作对象，无需编写繁琐的 SQL 语句，代码更简洁易读。
- **跨数据库兼容性**：ORM 屏蔽了底层数据库的差异，切换数据库时通常只需修改配置，无需重写大量代码。
- **类型安全与自动校验**：ORM 能根据模型定义自动校验数据类型和约束，减少运行时错误。
- **防止 SQL 注入**：ORM 默认采用参数化查询，能有效防止 SQL 注入等安全问题。
- **便于维护和重构**：数据表结构变更时，只需修改模型类，维护成本低，易于重构。
- **支持复杂查询和关联**：ORM 支持对象之间的关联关系（如一对多、多对多），并能方便地进行复杂查询和数据操作。

除了 Django 提供的 ORM 框架外，不同编程语言也有其他的 ORM 框架：

- Python：[SQLAlchemy](https://www.sqlalchemy.org/)
- Rust：[Diesel](https://diesel.rs/)、[SeaORM](https://www.sea-ql.org/SeaORM/)
- Node.js：[Sequelize](https://sequelize.org/)、[TypeORM](https://typeorm.io/)；
- Java：[Hibernate](https://hibernate.org/)；
- Go：[GORM](https://gorm.io/)。
  

#### 常见 ORM 使用示例

**1. Django ORM 示例（使用 SQLite）**

```python
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

# 创建数据
student = Student.objects.create(name="Alice", age=20)

# 查询数据
students = Student.objects.filter(age__gte=18)

# 更新数据
student.age = 21
student.save()

# 删除数据
student.delete()
```

**2. Node.js 使用 Mongoose 操作 MongoDB**

```js
// models/student.js
const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema({
  name: String,
  age: Number
});

const Student = mongoose.model('Student', studentSchema);

// 创建数据
const student = new Student({ name: 'Bob', age: 22 });
await student.save();

// 查询数据
const students = await Student.find({ age: { $gte: 18 } });

// 更新数据
student.age = 23;
await student.save();

// 删除数据
await Student.deleteOne({ name: 'Bob' });
```

**3. Rust 使用 Diesel 操作 PostgreSQL**

```rust
// models.rs
use diesel::prelude::*;
use diesel::pg::PgConnection;

#[derive(Queryable, Insertable)]
#[table_name = "students"]
struct Student {
    id: i32,
    name: String,
    age: i32,
}

// 插入数据
let new_student = Student { id: 1, name: "Carol".to_string(), age: 19 };
diesel::insert_into(students::table)
    .values(&new_student)
    .execute(&conn)?;

// 查询数据
let results = students::table
    .filter(students::age.ge(18))
    .load::<Student>(&conn)?;

// 更新数据
diesel::update(students::table.find(1))
    .set(students::age.eq(20))
    .execute(&conn)?;

// 删除数据
diesel::delete(students::table.find(1)).execute(&conn)?;
```

**4. 使用 ORM 连接服务器类型数据库的示例（以 Python SQLAlchemy 连接 PostgreSQL 为例）**

ORM 框架不仅支持本地文件型数据库（如 SQLite），也能方便地连接远程服务器类型数据库（如 PostgreSQL、MySQL）。只需更换数据库连接字符串即可。例如，使用 SQLAlchemy 连接远程 PostgreSQL：

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 连接远程 PostgreSQL 数据库
engine = create_engine("postgresql://username:password@host:5432/dbname")
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 创建数据
student = Student(name="David", age=24)
session.add(student)
session.commit()

# 查询数据
students = session.query(Student).filter(Student.age >= 18).all()
```

这种方式可以轻松切换本地与远程数据库，适用于生产环境下多用户并发访问和大规模数据存储的需求。


### SQL 注入

SQL 注入攻击（SQL Injection）是一种网络攻击手段，攻击者通过在输入字段中插入恶意的 SQL 代码来操纵数据库，从而访问、修改或删除数据。攻击的目标通常是那些没有对用户输入进行适当验证和过滤的 Web 应用程序。

#### 基本原理

SQL 注入的发生本质上来源于程序设计中对 SQL 语言使用时的设计缺陷。考虑如下情形，假设有一个登录功能，其 SQL 查询如下：

```sql
SELECT * FROM users WHERE username = 'user' AND password = 'pass';
```

如果用户输入的 `username` 为 `' OR '1'='1`，则生成的SQL查询变为：

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = 'pass';
```

由于 `'1'='1'` 总是为真，这个查询将绕过验证，导致攻击者可以登录系统。

#### 预防措施

- 对数据进行转义，永远不要信任用户的输入，要对用户的输入进行校验，可以通过正则表达式，或限制长度，对单引号和双”-“进行转换等；
- 永远不要使用动态拼装 SQL，可以使用参数化的 SQL 或者直接使用存储过程进行数据查询存取；
- 不要把机密信息明文存放，请加密或者 hash 掉密码和敏感的信息；
- 使用 ORM（对象关系映射）。

## 参考资料

- PostgreSQL 官方文档: https://www.postgresql.org/docs/
- PostgreSQL Exercises: https://pgexercises.com
- 酒井科协 & 算协联合暑培 2024【数据库 & SQL】课程讲义 by Andonade: https://summer24.net9.org/basic/sql/handout/
- 酒井科协暑培 2023 数据库 & SQL by 刘铠铭 @kaiming: https://summer23.net9.org/basic/sql/#523-count-max-min-sum-avg