
## [re](https://docs.python.org/3/library/re.html)

### help

```Shell
>>> import re
>>> help(re)

Help on module re:

NAME
    re - Support for regular expressions (RE).

DESCRIPTION
    This module provides regular expression matching operations similar to
    those found in Perl.  It supports both 8-bit and Unicode strings; both
    the pattern and the strings being processed can contain null bytes and
    characters outside the US ASCII range.

    Regular expressions can contain both special and ordinary characters.
    Most ordinary characters, like "A", "a", or "0", are the simplest
    regular expressions; they simply match themselves.  You can
    concatenate ordinary characters, so last matches the string 'last'.
```

### howto

[regex-howto](https://docs.python.org/3/howto/regex.html#regex-howto)

The sequence

```Python
prog = re.compile(pattern)
result = prog.match(string)
```

is equivalent to

```
result = re.match(pattern, string)
```

### flags

- `re.I`(re.IGNORECASE): Perform case-insensitive matching;  
- `re.M`(re.MULTILINE): When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character '$' matches at the end of the string and at the end of each line (immediately preceding each newline).
- `re.S`(re.DOTALL): Make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline. Corresponds to the inline flag (`?s`).  

`re.I` 和 `re.M` 分别对应 javascript RegExp 中的 `/i` 和 `/m` 标志。

正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(`|`) 来指定。
如 `re.I | re.M` 被设置成 I 和 M 标志。

### APIs

#### search

```
re.search(pattern, string, flags=0)
```

re.search 扫描整个字符串并返回 **第一个** 成功的匹配。

匹配成功将返回一个匹配的对象 [match object](https://docs.python.org/3/library/re.html#match-objects)，否则返回 None。
我们可以使用 group(num) 或 groups() 匹配对象函数来获取匹配表达式。

[Detecting Chinese Characters in Unicode Strings](https://medium.com/the-artificial-impostor/detecting-chinese-characters-in-unicode-strings-4ac839ba313a)
[regex - Python: Check if a string contains chinese character?](https://stackoverflow.com/questions/34587346/python-check-if-a-string-contains-chinese-character)

To check if a string contains Chinese characters in Python, several methods can be employed:

1. Using Unicode Ranges:

> Chinese characters fall within specific Unicode ranges. You can iterate through the string and check if any character's Unicode value falls within these ranges.

```python
def contains_chinese(text) -> bool:
    for char in text:
        # Common Chinese character ranges
        if '\u4E00' <= char <= '\u9FFF' or \
           '\u3400' <= char <= '\u4DBF' or \
           '\uF900' <= char <= '\uFAFF': # CJK Compatibility Ideographs
            return True
    return False

# Example usage
xinhua_en="xinhuanet.com"
xinhua_cn="新华网.cn"
xinhua_hz="新华网.中国"

print(f"'{xinhua_en}' contains Chinese: {contains_chinese(xinhua_en)}")
print(f"'{xinhua_cn}' contains Chinese: {contains_chinese(xinhua_cn)}")
print(f"'{xinhua_hz}' contains Chinese: {contains_chinese(xinhua_hz)}")
```

2. Using Regular Expressions with re Module:

> The `re` module can be used to search for patterns matching Chinese characters.



#### match

```
re.match(pattern, string, flags=0)
re.fullmatch(pattern, string, flags=0)
```

- re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话就返回 None。  
- re.fullmatch 匹配整个字符串。  

> re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；  
> 而 re.search 则匹配整个字符串，直到找到一个匹配。  

#### search vs. match

Python offers different primitive operations based on regular expressions:

- `re.match()` checks for a match only at the beginning of the string
- `re.search()` checks for a match anywhere in the string (this is what Perl does by default)
- `re.fullmatch()` checks for entire string to be a match

#### split

```
re.split(pattern, string, maxsplit=0, flags=0)
```

split 方法按照能够匹配的子串将字符串分割后返回列表。

#### findall

```
re.findall(pattern, string, flags=0)
```

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配 **一次**，findall 则是匹配 **所有**。

[Find all Chinese text in a string using Python and Regex](https://stackoverflow.com/questions/2718196/find-all-chinese-text-in-a-string-using-python-and-regex)

```python
import re

hello_shijie = "Hello World/你好世界"
xinhuanet="xinhuanet.com/新华网.cn/新华网.中国/"

# Define the regex pattern for Chinese characters
# The range \u4e00-\u9fff covers most common Chinese characters
chinese_pattern = re.compile(r"[\u4e00-\u9fff]+")
matches = chinese_pattern.findall(xinhuanet)
print(matches)
```

[Check if csv contains Chinese characters in python then output](https://stackoverflow.com/questions/72757444/check-if-csv-contains-chinese-characters-in-python-then-output)

This code output the lines that contains the chinese character and save those into a file named "detected.txt".

```python
import re

characters=[]
i = 0
with open('01.csv','r',encoding='utf-8') as file: #Open CSV file
    with open('detected.txt', 'r+') as f: #Open file to write

        for line in file.readlines(): #Read each line of CSV file
            #If there is no Chinese character in the line
            if re.findall(r'[\u4e00-\u9fff]+', line) == []:
                pass
            else:
                #Append the Chinese character to the list
                characters.append(re.findall(r'[\u4e00-\u9fff]+', line))
                #If the Chinese character is in the line
                if str(characters[i][0]) in line:
                    f.write(line) #Append the line to the file
                i+=1
```

#### sub

```
re.sub(pattern, repl, string, count=0, flags=0)
re.subn(pattern, repl, string, count=0, flags=0)
```

## log_line_extractor

传入日志第一行，正则匹配猜测出平台类型。

```
log_line_ios = '2019-09-29 14:46:49.301 Debug|1031|23627|:96|IMPDT_MBR_Engine||start: role = 1'
log_line_android = '19-09-22 15:09:09|1569136148648[4600]4794|W|VasQuickUpdateEngine_Native|[2019-09-22 15:09:08][1569136148648][debug   ][unnamed thread:4794][MBR_Engine:96]: start: role = 1'
log_line_windows = r'''"36098","2","2019/09/29 17:12:44:884","183323671","XP.MSGBAK.MBR_Engine","start: role = 1","10400","18892","95"'''
```

暂不考虑日期及时间的合法性，从行首匹配各个平台的日志格式。

### test cases

```
log_line_i_m = 'test 2019-09-29 14:46:49.301 mid'
log_line_i_e = 'test end 2019-09-29 14:46:49.301'
log_line_i = '2019-09-29 14:46:49.301 Debug|1031|23627|:96|IMPDT_MBR_Engine||start: role = 1'

log_line_a_m = 'test 19-09-22 15:09:09| mid'
log_line_a_e = 'test end 19-09-22 15:09:09|'
log_line_a = '19-09-22 15:09:09|1569136148648[4600]4794|W|VasQuickUpdateEngine_Native|[2019-09-22 15:09:08][1569136148648][debug   ][unnamed thread:4794][MBR_Engine:96]: start: role = 1'

log_line_w_m = r'''test ,"2019/09/29 17:12:44:884", mid'''
log_line_w_e = r'''test end ,"2019/09/29 17:12:44:884",'''
log_line_w = r'''"36098","2","2019/09/29 17:12:44:884","183323671","XP.MSGBAK.MBR_Engine","start: role = 1","10400","18892","95"'''
```

### RegExp

以下为 javascript 对应的 literal expression，可在 vscode 中利用 Regex Previewer 插件进行 Test Regex：

```TypeScript
let irem = /(?:^)\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} /m
let iren = /(?:^|\n)\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} /
let arem = /(?:^)\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\|/m
let aren = /(?:^|\n)\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\|/
let wre = /,"\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}\:\d{3}",/ // 可匹配中部
let wrem = /(?:^)"\d+","\d","\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}\:\d{3}",/m
```

### re

从行首 match 匹配各个平台的日志格式。

由于 re 中的 match 本身就是从行首开始匹配，故无需指定 `re.M` 匹配行头 `(?:^)`。

```Python
#moi = re.match(r'(?:^)\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} ', log_line_i, re.M)
#roi = re.compile(r'(?:^|\n)\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} ')
roi = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} ')
moi = roi.match(log_line_i)     # not None, non-group, moi.group(0)
moi_m = roi.match(log_line_i_m) # None
moi_e = roi.match(log_line_i_e) # None

roa = re.compile(r'\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\|')
moa = roa.match(log_line_a)     # not None, non-group, moi.group(0)
moa_m = roa.match(log_line_a_m) # None
moa_e = roa.match(log_line_a_e) # None

row = re.compile(r'"\d+","\d","\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}\:\d{3}",')
mow = row.match(log_line_w)     # not None, non-group, moi.group(0)
mow_m = row.match(log_line_w_m) # None
mow_e = row.match(log_line_w_e) # None
```

提取为 `try_to_guess_platform` 函数：

```Python
import enum
import re


class PLATFORM(enum.Enum):
    ios = 0
    android = 1
    windows = 2


def try_to_guess_platform(log_line: str) -> int:
    roi = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} ')
    roa = re.compile(r'\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\|')
    row = re.compile(r'"\d+","\d","\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}\:\d{3}",')
    if (roi.match(log_line)):
        return PLATFORM.ios.value
    if (roa.match(log_line)):
        return PLATFORM.android.value
    if (row.match(log_line)):
        return PLATFORM.windows.value
    return -1
```

以下为测试代码：

```
try_to_guess_platform(log_line_i)   # 0: ios
try_to_guess_platform(log_line_i_m) # -1
try_to_guess_platform(log_line_i_e) # -1

try_to_guess_platform(log_line_a)   # 1: android
try_to_guess_platform(log_line_a_m) # -1
try_to_guess_platform(log_line_a_e) # -1

try_to_guess_platform(log_line_w)   # 2: windows
try_to_guess_platform(log_line_w_m) # -1
try_to_guess_platform(log_line_w_e) # -1
```

## refs

[用python正则表达式提取字符串](https://blog.csdn.net/liao392781/article/details/80181088)  
[通用正则表达式与python中的正则匹配](http://pelhans.com/2018/06/22/liunx-regex/)  
