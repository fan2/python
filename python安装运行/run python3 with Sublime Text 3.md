
## Run python with SublimeText
[How do I run Python code from Sublime Text 2?](https://stackoverflow.com/questions/8551735/how-do-i-run-python-code-from-sublime-text-2)  
[Run python with SublimeText](https://dotblogs.com.tw/larrynung/2013/05/12/103533)  
[sublime运行python文件简单配置与安装](http://blog.csdn.net/u012905422/article/details/52526640)  

On macOS, save your file with a `.py` extension. Press <kbd>⌘</kbd> + <kbd>B</kbd>. It runs in a window below.

@img ![⌘+B](https://i.stack.imgur.com/Ic2T8.png)  

如果出现中文乱码，可在文件开头加入：`# -*- coding: utf-8 -*-` 或者 `#coding=utf-8`。  

要实现 python 交互，可考虑安装 [**SublimeREPL**](https://packagecontrol.io/packages/SublimeREPL) 插件。

### Python3 Build System
[**在Sublime Text中使用不同的python版本**](https://wslark.wordpress.com/2016/07/27/sublime-text-%e5%9c%a8sublime-text%e4%b8%ad%e4%bd%bf%e7%94%a8%e4%b8%8d%e5%90%8c%e7%9a%84python%e7%89%88%e6%9c%ac/)  

> Tools > Build System > New Build System 新建 Python3

```json
{
    "path": "/usr/local/bin/",
    "cmd": ["python3", "-u", "$file"], // -i?
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python", // source.python3?
    "encoding": "utf8", // 可选 "env": {"LANG": "en_US.UTF-8"}
}
```

> which python3: /usr/local/bin/python3。  
> 由于 python3 已经加入了 PATH，因此第一行 path 可略去。  

save as `~/Library/Application Support/Sublime Text 3/Packages/User/Python3.sublime-build`

Tools > Build System 菜单下已有的 Python 下将多出 **Python3**。  

默认 `Automatic`，将调用 python2 编译 py 脚本；  
显式选中 `Python3`，再按下 <kbd>⌘</kbd> + <kbd>B</kbd>，则调用 python3 编译 py 脚本。  

按下 <kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>B</kbd> 弹出 Build With 菜单，其下将多出 Python3，可选 Python 或 Python3。

### python_version

> [python 代码获取当前 Python 版本](http://www.cnblogs.com/ifantastic/p/4183496.html)  
> [python - 在输出中打印Python版本](https://ask.helplib.com/python/post_317974)  

```python
#coding=utf-8

#from platform import python_version
#print(python_version())

import platform
print(platform.python_version())
print('\n' * 1)

import sys
print(sys.version)

print('\n' * 1)

print(sys.version_info)
print('\n' * 1)

print("The Python version is %s.%s.%s" % sys.version_info[:3])
```

可分别 Build With Python 和 Python3 查看具体执行版本信息。

## references
[Set up Python 3 build system with Sublime Text 3](https://stackoverflow.com/questions/23730866/set-up-python-3-build-system-with-sublime-text-3) - Windows  
[How to link Sublime Text Build system to Python 3](https://gist.github.com/zaemiel/4fbd8b5125fda7a140be)  
[为 Sublime Text 3 添加 Python 3 和 JavaScript 的 build system](http://movii.github.io/blog/2014/12/04/sublime-add-python3-and-javascript-build-system/)  

[sublime text中用python3运行文件](http://blog.csdn.net/yelyyely/article/details/40890871)  
[Sublime Text 3 配置 python3编译环境](http://blog.csdn.net/zxgdll/article/details/69524635)  
[使用 Sublime Text 方便的运行 Python 代码](https://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/001434018642537aa6d1ad772a445d99ed07e7691cd6d14000)  
在Sublime Text 3中配置Python3的开发环境（Build System）: [cnblogs](http://www.cnblogs.com/zhangqinwei/p/6886600.html) / [csdn](http://blog.csdn.net/Aaroun/article/details/78263512)  

[Mac 配置 sublime text 3 的python3.5环境](http://www.jianshu.com/p/6ec3d1b9c9d6)  
[Mac下Sublime Text3配置Python3开发环境](http://blog.csdn.net/qq_33304418/article/details/63337602)  
[Mac Sublime Text 3 配置Python环境及安装插件](http://www.cnblogs.com/zhanglinfeng/p/7359102.html)  
