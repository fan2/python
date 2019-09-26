
dir(builtins) 分类梳理一览

## id

builtins.dir  

builtins.id  
builtins.hash  
builtins.type  

builtins.isinstance  
builtins.issubclass  

## vars

builtins.vars  
builtins.locals  
builtins.globals  

## print & format

builtins.repr  
builtins.print  
builtins.format # help('FORMATTING')  

交互输入：

builtins.input

## types

### None

builtins.None  
builtins.Ellipsis # 省略号  

### bool

builtins.bool  
builtins.False  
builtins.True  

builtins.any # 一组值中只要有一个为 True

### Sequence Types

builtins.str - Text Sequence  

builtins.list  
builtins.tuple  
builtins.range  

builtins.slice  

### Mapping Types

builtins.map  
builtins.dict  

### Set Types

builtins.set  
builtins.frozenset  

### Binary Sequence Types

builtins.bytes  
builtins.bytearray  
builtins.memoryview  

## len & filter

builtins.len  

builtins.reversed  
builtins.filter  
builtins.sorted  

## enum & iter

builtins.enumerate  

builtins.iter  
builtins.next  

## utilities

### value

字符串转换为整形、浮点型：

builtins.int  
builtins.float  

进制转换：

builtins.bin  
builtins.hex  
builtins.oct  

### math

builtins.abs  
builtins.min  
builtins.max  
builtins.sum  

builtins.pow  
builtins.round  
builtins.divmod  

### ascii

builtins.ascii  
builtins.ord  
builtins.chr  

```
>>> ord('a')
97
>>> ord('A')
65
```

```
>>> chr(97)
'a'
>>> chr(65)
'A'
```

## open

builtins.open  
builtins.eval  
builtins.exec  

## warning/error

builtins.Warning  
builtins.UserWarning  

builtins.IndexError  
builtins.FileExistsError  
builtins.FileNotFoundError  

builtins.TypeError  
builtins.ValueError  
