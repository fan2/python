
[Python中枚举的使用](https://blog.csdn.net/m0_38061927/article/details/76058133)

```
from enum import Enum

class Color (Enum):
      red=1
      orange=2
      yellow=3
      green=4
      blue=5
      indigo=6
      purple=7
```

如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器 `@unique`:

```
from enum import Enum, unique

@unique
class Color(Enum):

```

## access

通过成员的名称来获取成员：

```
>>> Color['red']
<Color.red: 1>
```

通过成员的值来获取成员：

```
>>> Color(1)
<Color.red: 1>
```

通过成员，来获取它的名称和值：

```
>>> Color.red
<Color.red: 1>

>>> Color.red.name
'red'
>>> Color.red.value
1
```