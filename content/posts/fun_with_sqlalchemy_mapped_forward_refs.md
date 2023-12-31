---
title: "Fun with SQLAlchemy Mapped forward refs"
date: 2023-12-30
draft: false
---
[SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/internals.html#sqlalchemy.orm.Mapped) has nifty declarative mapping type support with the `Mapped` typing descriptor. 
If you are in the habit of typing your Python, this is a welcome tool that reduces boilerplate while still feeling quite natural: 
```
class Banana(SqlalchemyBase):
	is_squishy:Mapped[Optional[bool]] = mapped_column(server_default=text("TRUE"))
	picked_date:Mapped[datetime]
	belongs_to: Mapped["User"] = relationship("User", lazy="selectin", back_references="bananas")
```
But interestingly, `Mapped` does not support forward refs outside the ORM. so 
`picked_date:Mapped["datetime"]` will error with an _ArgumentError_ if `datetime` was not otherwise imported in the module. However, our 
forward ref to `"User"` will be fine as long as you've imported `User` via `TYPE_CHECKING`.  

So in conclusion, this works: 
```
...
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from . import User # avoids circular refs

class Banana(SqlalchemyBase):
	is_squishy:Mapped[Optional[bool]] = mapped_column(server_default=text("TRUE"))
	picked_date:Mapped[datetime]
	belongs_to: Mapped["User"] = relationship("User", lazy="selectin", back_references="bananas")
```
but if you try to forward ref anything _not_ inheriting from `SqlalchemyBase`, :scream_cat:!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMzNDI3ODk1MV19
-->