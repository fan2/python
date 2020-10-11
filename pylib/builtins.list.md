# [list](https://docs.python.org/3/library/stdtypes.html#list)（有序列表）

```shell
>>> type(sys.argv)
<class 'list'>
```

```shell
# 判断模块名称中是否包含 '__doc__' 和 '__file__'
>>> import builtins
>>> '__doc__' in dir(builtins)
True
>>> '__file__' in dir(builtins)
False

>>> import os
>>> '__doc__' in dir(os)
True
>>> '__file__' in dir(os)
True
```

## why not [array](https://docs.python.org/3/library/array.html) ?

`array` — Efficient arrays of numeric values

This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers.  Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is **constrained**.  
The type is specified at object creation time by using a *type code*, which is a single character.  

```
a=array.array('i', [1, 2, 3, 4, 5])
```

当我们要存储操作大规模的标量数值类型时，数组（array）的效率要比列表（list）要高得多。
因为数组在背后存的并不是对象，而是数字的机器翻译，也就是字节表述。

> [python之数组模块array](https://www.cnblogs.com/jlf0103/p/9168093.html)  
> [python3之数组(array)](https://blog.csdn.net/xc_zhou/article/details/88538793)  

array 相比 list 的局限在于：list 可以混合存储任意类型，而 array 在构造时必须指定确定的数值类型。
一般 list 用的场合比较多。

## empty list

1. `l=list()`: 构造一个空列表对象。  
2. `l=[]`：中括号定义空列表。  

多个元素之间以逗号分隔，例如 `l1=[1,2,3,4]`。  

列表支持基于脚标索引访问元素（access through subscripted index）。

## expressions

- `len(l)`: Return the number of elements in list l.  
- `e in l`: Test e for membership in l.  
- `e not in l`: Test e for non-membership in l.  
- `for e in l`: enumerate elements in l.  

## api

在 python shell 中，构造一个空列表 l，然后输入 `l.` 再输入 tab 键自动提示可用的成员函数：

```
>>> l=list()
>>> l.
l.append(   l.copy(     l.extend(   l.insert(   l.remove(   l.sort(
l.clear(    l.count(    l.index(    l.pop(      l.reverse(
```

## add

向列表中添加元素，有两种方式：

1. 调用 `l.append(e)`，将新元素 e 添加到列表 l 的末尾；  
2. 调用 `l.insert(i, e)`，将新元素 e 插入到列表 l 原来索引为 i 的元素之前：

    > 原来索引 i 及其后的元素顺势后移一位，新元素 e 占据索引 i 的位置。

- 头插法：`l.insert(0,e)`;  
- 尾追法：`l.append(e)`;  

### extend

`append` 一般是将单个元素追加到列表末尾，如何在已有列表后面追加（衔接）另外一个列表呢？

这涉及到 extend 接口：`extend` list by appending elements from the iterable.

我们创建列表 l1 及其副本 l2，接下来看看它们分别通过 append 和 extend 追加的效果。

```
>>> l1=list(range(1,5))
>>> l1
[1, 2, 3, 4]
>>> l2 = l1.copy()
>>> l2
[1, 2, 3, 4]
>>> l3=list(range(5,9))
>>> l3
[5, 6, 7, 8]
```

`l1.append(l3)` 将 l3 追加到 l1，是将列表 l3 作为一个元素追加到 l1：

```
>>> l1.append(l3)
>>> l1
[1, 2, 3, 4, [5, 6, 7, 8]]
>>> len(l1)
5
>>> l1[4]
[5, 6, 7, 8]
>>> type(l1[4])
<class 'list'>
```

`l2.extend(l3)` 则将 l3 中的列表元素逐个 append 追加到 l2 后面，实现了预期的列表衔接。

```
>>> l2.extend(l3)
>>> l2
[1, 2, 3, 4, 5, 6, 7, 8]
>>> len(l2)
8
```

## delete

1. `del(l[i])` 或 `del l[i]`：从列表l中移除索引 i 处的元素；  

    > 当然也可以 `del l[i:j:k]` 移除切片子集

2. `l.pop(i)`：从列表l中移除索引 i 处元素，并弹出其值；  

    > 特殊地不指定索引 i，默认弹出刚刚 append 到队尾（栈顶）的元素。  
    > `l.pop(0)`，弹出队头（*栈底*）元素。  

---

以下总结 python 中的列表通用结构，按照栈和队列的惯用法：

- 栈 LIFO 惯例用法: `l.append(e)`, `e=l.pop()`  
- 队列 FIFO 惯例用法：`l.append(e)`, `e=l.pop(0)`  

如果需要频繁对序列做先出先进（FIFO）的操作，双端队列（collections.`deque`）的速度应该会更快。  
除了标准的 append/pop 接口，deque 还专门提供了 `appendleft`/`popleft` 接口。

- 双端队列标准惯用法：入队 **enqueue** - `dq.append(e)`, 出队 **dequeue** - `e=dq.popleft()`。

### remove

有时候，你不知道要从列表中删除的值所处的位置。
如果你只知道要删除的元素（的值），可调用 `list.remove(e)` 方法。

> Remove first occurrence of value. Raises *ValueError* if the value is not present.

```
>>> if e in l1:
...     l1.remove(e)
...     print(l1)
... else:
...     print("{} not in list".format(e))
```

当 e=4 在列表中时，被移除；当 e=9 不在列表中时，打印提示不在列表中。

## slice

切片的完整格式是 `[start:stop:step]`，对应 slice 函数的定义。  

一般省略默认step=1，简写为一个冒号区间形式 `[start:stop]`。  
甚至连start和stop都可不指定，简写一个冒号形式 `[:]`（等价于 `[::]`）。  

---

a = `[1,2,3,4,5,6,7]`，取切片 `a[1:3]` 索引范围 = [1,3)，取出的子集为 `[2, 3]`。

```
>>> a=[1,2,3,4,5,6,7]
>>> a[1:3]
[2, 3]
```

`a[:4]`：省略切片开始索引，默认为0，相当于 `a[0:4]`，取值 a[0]~a[3]。

```
>>> a[:4]
[1, 2, 3, 4]
```

`a[4:]`：省略切片结束索引，默认为len，相当于 `a[4:len(a)]`，取值 a[4]~a[len(a)-1]。

```
>>> a[4:]
[5, 6, 7]
```

`a[:]`：省略切片开始和结束索引，相当于 `a[0:len(a)]`，取值 a[0]~a[len(a)-1]。

```
>>> a[:] # 默认步长为1，等效于 a[::]、a[::1]
[1, 2, 3, 4, 5, 6, 7]

>>> a[::2] # 指定步长为2，取所有偶数索引位置的值
[1, 3, 5, 7]

>>> a[1::2] # 指定步长为2，指定起始索引为1，取所有奇数索引位置的值
[2, 4, 6]
```

---

也可以用内置的 **slice** 函数指定 start、stop 和 step，构造切片索引，对序列进行切片取值。

```
slice(start, stop[, step])
```

这样使得切片范围可编程定制化，更灵活的截取子集。

```
>>> s = slice(1,3)
>>> a[s] # 等效于 a[1:3] 和 a[1:3:1]
[2, 3]
```

特殊地有 `slice(None)`，连起始索引 start 都省略，等价于冒号 `:`，表示从头到尾。

```
>>> s=slice(None)
>>> a[s]
[1, 2, 3, 4, 5, 6, 7]
```

### copy slice

图解LeetCode初级算法插入排序中，用到了Python的切片赋值。

1. 从前子向量切片 [0:right]（结束索引为 right-1） 中查找比右子向量当前首元素 target 大的索引 left；  
2. 将从 left 开始比 right 大的切片 [left:right]（不包括 right 对应的 target 元素）整体向右移动一位；  

    > right 的值提前暂存到 target 中了，right 位置将被右移占用，左边 left 位置腾出插入 target 值。

```
def insertionSort(iList: list) -> list:
    if len(iList) <= 1:
        return iList
    for right in range(1, len(iList)):
        target = iList[right]
        for left in range(0, right):
            if target <= iList[left]:
                iList[left+1:right+1] = iList[left:right] #使用Python的切片赋值
                iList[left] = target
                break
        # print("第 %d 轮排序结果:" %(right), end="")
        # print(iList)
    return iList
```

### copy list

如果需要根据既有列表创建全新的列表，除了可以调用源列表的 `copy` 函数创建副本外，也可创建一个包含整个列表的切片（`[:]`），然后赋值给新列表变量，即达目的。

```
>>> b=a[:] # 深度复制 a 的副本
>>> b
[1, 2, 3, 4, 5, 6, 7]
>>> b.pop(0)
1
>>> b # b 弹出队首元素
[2, 3, 4, 5, 6, 7]
>>> a # b 的改动不影响 a，a 不变
[1, 2, 3, 4, 5, 6, 7]
```

### refs

[Python切片Slice](http://liao.cpython.org/07slice/)  
[python中切片（Slice）操作符](https://blog.csdn.net/xiaofeiyu321/article/details/82941765)  
[切片（Slice）在python中的运用](https://blog.csdn.net/dfshi198/article/details/80843175)  
[Python高级特性——切片（Slice）](https://www.cnblogs.com/hiwuchong/p/8052502.html)  
