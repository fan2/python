[PEP 0 -- Index of Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/)  

This PEP contains the index of all Python Enhancement Proposals, known as PEPs.

## [PEP8](https://www.python.org/dev/peps/pep-0008/) - Style Guide for Python Code

```shell
faner@MBP-FAN:~|⇒  pip3 search pep8
autopep8 (1.3.4)                  - A tool that automatically formats Python code to conform
                                    to the PEP 8 style guide

pep8-naming (0.5.0)               - Check PEP-8 naming conventions, plugin for flake8
ulint-pep8 (0.2)                  - PEP8 linter for ulint
pytest-pep8 (1.0.6)               - pytest plugin to check PEP8 requirements
pep8 (1.7.1)                      - Python style guide checker
pepper8 (1.1.1)                   - Transforms pep8 or flake8 output into an HTML report.

```

[autopep8](https://github.com/hhatto/autopep8)  
[PEP8 online check](http://pep8online.com/)  
[Python PEP8 Autoformat](https://packagecontrol.io/packages/Python%20PEP8%20Autoformat)  

[PEP8 Python 编码规范](https://www.jianshu.com/p/52f4416c267d)  
[PEP 8——Python编码风格指南](https://lizhe2004.gitbooks.io/code-style-guideline-cn/content/python/python-pep8.html)  

## Anaconda PEP8 lint error

- `Anaconda: Disable linting on this file`，选中后将不再进行 PEP8 错误标识。  

	> 选中 **Disable** 禁止 PEP8 错误提示后，将多出相应的 **Enable** 项可恢复提示。  

- `Anaconda: Show error list`：浮窗列出 PEP8 错误列表。  
- `Anaconda: Next/Previous lint error`：查看下/上 PEP8 错误。  

- `Anaconda: Autoformat PEP8 Errors`：按PEP8风格自动排版代码

### common PEP8 errors

1. [W] PEP8 (E265): block comment should start with ‘#’

	> 独行顶格注释：`#` 后需要一个（或以上）空格和注释文字隔开。

2. E261 & E262

	- [W] PEP8 (E261): at least two spaces before inline comment
	- [W] PEP8 (E262): inline comment should start with ‘#’

	> 行末跟随注释：`#` 前距离代码结尾两个（或以上）空格，  
	> `#` 后需要一个（或以上）空格和注释文字隔开。

3. [W] PEP8 (E703): statement ends with a semicolon

	> 从 C++ 等其他编程语言转过来，习惯在代码行末增加分号以示结束。  
	> 但 python 代码是以自然行作为组织单元，末尾无需添加分号。  

4. [W] PEP8 (E225): missing whitespace around operator

	> 逻辑运算符（`==`, `!=`）和算数运算符（`+`,`*`）前后都要留空格。

5. [W] PEP8 (E302): expected 2 blank lines, found 1

	> 函数定义（`def function():`）上面应预留两空行，当前只有一个空行。

6. [W] PEP8 (E305): expected 2 blank lines after class or function definition, found 1

	> 类或函数定义下面应预留两空行，当前只有一个空行。

7. [W] PEP8 (E303): too many blank lines(N)

	> E302/E305，补充空行数 N 超过两行，不能少也不能多。
