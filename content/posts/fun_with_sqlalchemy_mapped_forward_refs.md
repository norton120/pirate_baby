---
title: "Fun with SQLAlchemy `Mapped` forward refs"
date: 2023-12-30
draft: false
---
[SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/internals.html#sqlalchemy.orm.Mapped) has nifty declarative mapping type support with the `Mapped` typing descriptor. 
If you are in the habit of typing your Python, this is a welcome tool both reduces boilerplate while feeling quite natural: 
```
class Banana(SqlalchemyBase):
	is_squishy:Mapped[Optional[bool]] = mapped_column(server_default=text(
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk2NTY3Mzg1NF19
-->