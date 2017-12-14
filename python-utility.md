# scale

> [python格式化输出](http://blog.csdn.net/wchoclate/article/details/42297173)  
> [Python print函数用法](http://blog.csdn.net/zanfeng/article/details/52164124)  

## 进制转换
python 内置的 `bin()`、`oct()`、`hex()` 函数支持将十进制数转换为对应的二进制、八进制、十六进制字符串。

```Shell
>>> bin(2017)
'0b11111100001'
>>> oct(2017)
'0o3741'
>>> print(hex(2017))
0x7e1
>>> print(0x7e1)
2017
```

或者通过 `print()` 函数的占位符 `%o`、`%x` 格式化输出十进制数对应的八进制和十六进制格式：

```Shell
>>> x=2017
>>> print('oct=%o' %(x))
oct=3741
>>> print('hex=%x' %(2017))
hex=7e1
```