
## 传递任意数量的实参

《Python编程从入门到实践》中的 第8章 函数 - 8.5 传递任意数量的实参。

下面的函数只有一个形参 `*toppings`，但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中：

```python
def make_pizza(*toppings):
    """打印顾客点的所有配料""" 
    print(toppings)
```

形参名 `*toppings` 中的星号让 Python 创建一个名为 toppings 的空元组，并将收到的所有值都封装到这个元组中。

```shell
>>> def make_pizza(*toppings):
...     """打印顾客点的所有配料""" 
...     print(toppings)
... 
>>> make_pizza('pepperoni')
('pepperoni',)
>>> make_pizza('mushrooms', 'green peppers', 'extra cheese')
('mushrooms', 'green peppers', 'extra cheese')
```

### 使用任意数量的关键字实参

有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种 情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。

```shell
>>> def build_profile(first, last, **user_info):
...     """创建一个字典，其中包含我们知道的有关用户的一切"""
...     profile = {}
...     profile['first_name'] = first
...     profile['last_name'] = last
...     for key, value in user_info.items():
...         profile[key] = value
...     return profile
... 
>>> user_profile = build_profile('albert',
...                              'einstein',
...                              location='princeton',
...                              field='physics')
>>> print(user_profile)
{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
>>> 
```

函数 build_profile()的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称值对。
形参 `**user_info` 中的两个星号让 Python 创建一个名为 user_info 的空字典，并将收到的所 有 名称—值 对都封装到这个字典中。
在这个函数中，可以像访问其他字典那样访问 user_info 中的 名称—值 对。
