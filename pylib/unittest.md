[TOC]

# unittest

[unittest — Unit testing framework — Python 3.12.2 documentation](https://docs.python.org/3/library/unittest.html)
[unittest --- 单元测试框架 — Python 3.12.2 文档](https://docs.python.org/zh-cn/3/library/unittest.html#)

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages.

The unittest module provides a rich set of tools for constructing and running tests.

## TestCase

In unittest, test cases are represented by `unittest.TestCase` instances. To make your own test cases you must write subclasses of `TestCase` or use FunctionTestCase.

**test case**:

A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. 
unittest provides a base class,` TestCase`, which may be used to create new test cases.
A testcase is created by subclassing `unittest.TestCase`. 

### test/helper

以上代码 class NameTestCase 继承 `unittest.TestCase` 创建了一个测试样例。

测试方法都以 `test` 开头命名，该前缀告诉测试框架哪些方法是需要运行的测试用例。unittest 运行起来后，会执行所有以 `test` 开头的测试用例。

> The three individual tests are defined with methods whose names start with the letters `test`.
> This naming convention informs the test runner about which methods **represent** tests.

如果多个测试用例，测试流程基本相同，仅仅是部分测试参数差异。此时，可考虑将公共部分提取为辅助函数。然后，每个测试用例都调用这个辅助函数。

> 如果想要定义辅助函数，只要命名不以 test 开头的 [Non-test methods](https://stackoverflow.com/questions/6961099/non-test-methods-in-a-python-testcase) 即可。

### setUp/tearDown

通过 setUp() 和 tearDown() 方法，可以设置测试开始前与完成后需要执行的指令。

运行每个以 `test` 开头命名的测试用例，都会先执行 setUp()；用例执行完，会执行 tearDown()。

1. Tests can be numerous, and their set-up can be repetitive. Luckily, we can factor out set-up code by implementing a method called `setUp`(), which the testing framework will automatically call for every single test we run.
2. Similarly, we can provide a `tearDown`() method that tidies up after the test method has been run.

Tests share setup and shutdown code: The `setUp`() and `tearDown`() methods allow you to define instructions that will be executed before and after **each** test method.

可在 `__init__` 中初始化成员变量，挂靠到self上，后续测试用例中通过 self.var 形式引用这些成员变量。
但 `__init__` 不止初始化一次，调用次数同 setUp/tearDown。

A new TestCase instance is created as a unique test fixture used to execute each individual test method. Thus `setUp`(), `tearDown`(), and `__init__`() will be called once per test.

如果想初始化成员变量，且只初始化一次，可考虑调用类方法 `setUpClass` 和 `tearDownClass`。

```Python
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()
```

在测试用例中，可通过 `self._connection` 引用这个成员变量。

### assert methods

每个测试的关键是使用断言来管理预期：

- 调用 assertEqual 或 assertNotEqual 来检查预期的输出（check for an expected result）；
- 调用 assertTrue 或 assertFalse 来验证一个条件（verify a condition）；
- 调用 assertIs 或 assertIsNot 来验证是否同一对象；
- 调用 assertIsNone 或 assertIsNotNone 来验证对象是否有效；
- 调用 assertIn 或 assertNotIn 来验证包含情况；
- 调用 assertIsInstance 或 assertNotIsInstance 来验证对象和是否是类的实例；

这些断言方法都支持 msg 参数，如果指定了该参数，它将被用作测试失败时的错误消息。

使用这些方法而不是 `assert` 语句是为了让测试运行者能聚合所有的测试结果并产生结果报告。

> These methods are used instead of the assert statement so the test runner can accumulate all test results and produce a report.

the list of assert methods:

方法 | 检查对象 | 引入版本
----|---------|-----------
assertEqual(a, b) | a == b
assertNotEqual(a, b) | a != b
assertTrue(x) | bool(x) is True
assertFalse(x) | bool(x) is False
assertIs(a, b) | a is b | 3.1
assertIsNot(a, b) | a is not b | 3.1
assertIsNone(x) | x is None | 3.1
assertIsNotNone(x) | x is not None | 3.1
assertIn(a, b) | a in b | 3.1
assertNotIn(a, b) | a not in b | 3.1
assertIsInstance(a, b) | isinstance(a, b) | 3.2
assertNotIsInstance(a, b) | not isinstance(a, b) | 3.2

还有 assertGreater/assertGreaterEqual、assertLess/assertLessEqual、assertRegex/assertNotRegex、assertCountEqual 等断言方法。

还可以使用下列方法来检查异常、警告和日志消息的产生:

方法 | 检查对象 | 引入版本
----|---------|-----------
assertRaises(exc, fun, *args, **kwds) | `fun(*args, **kwds)` 引发了 exc
assertRaisesRegex(exc, r, fun, *args, **kwds) | `fun(*args, **kwds)` 引发了 exc 并且消息可与正则表达式 r 相匹配 | 3.1
assertWarns(warn, fun, *args, **kwds) | `fun(*args, **kwds)` 引发了 warn | 3.2
assertWarnsRegex(warn, r, fun, *args, **kwds) | `fun(*args, **kwds)` 引发了 warn 并且消息可与正则表达式 r 相匹配 | 3.2
assertLogs(logger, level) | `with` 代码块在 logger 上使用了最小的 level 级别写入日志 | 3.4
assertNoLogs(logger, level) | `with` 代码块没有在 logger 上使用最小的 level 级别写入日志 | 3.10

### subTest

Distinguishing test iterations using subtests

When there are very small differences among your tests, for instance some parameters, unittest allows you to distinguish them inside the body of a test method using the `subTest`() context manager.

```Python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
```

Without using a subtest, execution would **stop** after the *first* failure, and the error would be less easy to diagnose because the value of `i` wouldn’t be displayed.

对于以上 test_even 用例中的 for 循环，如果不添加 subTest，那么i=1时，用例即立即宣告失败并退出。
实际上，我们希望跑完for循环，并将失败的循环变量i打印出来，添加 subTest 可满足这种需求。

## skip

Unittest supports skipping individual test methods and even whole classes of tests.

Skipping a test is simply a matter of using the skip() decorator or one of its conditional variants:

```Python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
```

Classes can be skipped just like methods:

```Python
@unittest.skip("MyTestCase")
class MyTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

    def test_nothing(self):
        self.fail("shouldn't happen")
```

## main run TestCase

```Python
unittest.main(module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=unittest.defaultTestLoader, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None, warnings=None)

A command-line program that loads a set of tests from module and runs them; this is primarily for making test modules conveniently executable.
```

The simplest use for this function is to include the following line at the end of a test script:

```Python
if __name__ == '__main__':
    unittest.main()
```

You can run tests with more detailed information by passing in the verbosity argument:

```Python
if __name__ == '__main__':
    unittest.main(verbosity=2)
```

考虑在 vscode 中使用 Jupyter Notebook 情景。

假设Cell 1中定义了一个函数：

```Python
def add(a, b):
    return a + b
```

可在Cell 2中编写测试Cell 1中add函数的单测用例：

- 运行Cell2之前，必须先运行Cell1使之加载。

```Python
import unittest

class TestNotebook(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
```

**注意**：测试框架入口函数 unittest.main() 在 ipykernel 下需要指定 `argv` 和 `exit` 参数，否则运行报错！

[用单元测试让你的python代码更靠谱测试函数单元测试和测试用例测试类-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1347180)

假设 name_function.py 文件中定义了 get_formatted_name 函数：

```Python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
```

test_name_function.py 单测 name_function 中的 get_formatted_name 函数：

```Python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
```

在控制台中运行单元测试用例脚本：

```Shell
$ python3 test_name_function.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

测试框架入口函数 unittest.main() 默认 verbosity=1，可修改为2，以便打印更详细的单测过程：

```Shell
# unittest.main(verbosity=2)
$ python3 test_name_function.py #or
$ python -m unittest test_name_function.py #or
$ python -m unittest -v test_name_function.py

test_first_last_middle_name (__main__.NameTestCase.test_first_last_middle_name) ... ok
test_first_last_name (__main__.NameTestCase.test_first_last_name) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## TextTestRunner run TestSuite

**test suite**

A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

```Python
class unittest.TextTestRunner(stream=None, descriptions=True, verbosity=1, failfast=False, buffer=False, resultclass=None, warnings=None, *, tb_locals=False, durations=None)

A basic test runner implementation that outputs results to a stream. If stream is None, the default, sys.stderr is used as the output stream. This class has a few configurable parameters, but is essentially very simple. Graphical applications which run test suites should provide alternate implementations. Such implementations should accept **kwargs as the interface to construct runners changes when features are added to unittest.

run(test)
    This method is the main public interface to the TextTestRunner. This method takes a TestSuite or TestCase instance.
```

以下示例中，TestStringMethods 定义了三个 test 用例，TestSuite addTest 添加两个用例，然后调用 unittest.TextTestRunner run TestSuite。

```Python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

# if __name__ == '__main__':
    # unittest.main(argv=[''], verbosity=2, exit=False)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
```

## main or TextTestRunner?

采用 `unittest.main` 作为测试入口点时，会启动执行当前模块（Python File或Jupyter Notebook）中的所有TestCase测试用例。

1. Python File 包含多个 TestCase
2. Jupyter Code Cell 中包含多个 TestCase
3. Jupyter 包含多个包含 TestCase 的 Code Cell

如果不想执行所有的测试用例，最好将不同的测试用例分散到独立的模块中，保证每个Python File或者Jupyter Notebook中只有一个TestCase测试用例。
也可创建 TestSuite 按需添加指定 TestCase 的测试用例，改用 `unittest.TextTestRunner` 加载 TestSuite，再调用 run 启动测试用例。
