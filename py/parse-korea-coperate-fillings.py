#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
从 [韩国上市公司财报](https://dart.fss.or.kr/dsac001/mainY.do) PDF中提取指定章节表格中匹配关键字所在行

III. 재무에 관한 사항 (level 1 title fixed)
3. 연결재무제표 주석   (level 2 title fixed)

匹配 row-title = 평균유효세율，提取输出 column 1 和 column 2。

【运行说明】：

1. 需安装 python3（及配套包管理器 pip3）；
2. 需安装 pdfminer 和 pdfplumber，具体安装方式：pip3 install pdfminer, pip3 install pdfplumber；
3. 查看脚本帮助：-h
    python3 parse-korea-coperate-fillings.py -h
4. 运行脚本，携带PDF文件路径（相对或绝对路径）作为位置参数：
    python3 parse-korea-coperate-fillings.py ~/Downloads/korea-coperate-fillings-2021.08.17.pdf
5. 打开调试开关：-v，输出更多调试信息
    python3 parse-korea-coperate-fillings.py -v ~/Downloads/korea-coperate-fillings-2021.08.17.pdf

【TODO】：

1. 若章节中不存在表格，而是在文字中包含行标题关键字（평균유효세율），可考虑用正则提取。
2. 可考虑将位置参数从文件路径修改为财报PDF存储目录，逐个扫描目录下的PDF进行分析提取，
然后将各个文件处理结果都输出（append）到result.txt中：

    2021.08.17.pdf 32.5 23.5
    2021.10.25.pdf 32.6 23.6
    2021.10.26.pdf 32.7 23.7

【参考】：

1. [Programming with PDFMiner](https://www.unixuser.org/~euske/python/pdfminer/programming.html)
2. [coolioxlr/ziply](https://github.com/coolioxlr/ziply/blob/master/libs/pdfminer/tools/dumppdf.py)

"""

import argparse
import os

import pdfplumber
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfdocument import (PDFDocument, PDFNoOutlines,
                                  PDFTextExtractionNotAllowed)
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1
from pdfminer.psparser import PSLiteral


def resolveTOCDest(dest, doc: PDFDocument) -> list:
    if isinstance(dest, str):
        dest = resolve1(doc.get_dest(dest))
    elif isinstance(dest, PSLiteral):
        dest = resolve1(doc.get_dest(dest.name))
    if isinstance(dest, dict):
        dest = dest['D']
    return dest


# 返回一级标题下的二级标题章节内容的页码区间[start, end)
def findTOCPages(document: PDFDocument, level1title: str, level2title: str, debug: bool = False) -> tuple:
    # 建立PDFPage映射：pageid->pageno(zero-based)
    pageid2pageno = dict((page.pageid, pageno) for (pageno, page)
                         in enumerate(PDFPage.create_pages(document)))
    # 获取PDF文档大纲（TOC）及其页码
    level2pageno1 = 0
    level2pageno2 = len(pageid2pageno)
    try:
        findLevel1 = False
        findLevel2Start = False
        findLevel2End = False
        outlines = document.get_outlines()
        for (level, title, dest, a, se) in outlines:
            pageno = None
            if dest:
                objRefNode = resolveTOCDest(dest, document)
                pageno = pageid2pageno[objRefNode[0].objid]
            elif a:
                action = a.resolve()
                if isinstance(action, dict):
                    subtype = action.get('S')
                    if subtype and repr(subtype) == '/GoTo' and action.get('D'):
                        dest = resolveTOCDest(action['D'])
                        pageno = pageid2pageno[dest[0].objid]
            # dump PDF Outlines
            # print(level, title, pageno)
            if level == 1:
                if not findLevel1:
                    if level1title in title:
                        if debug:
                            print(title + ' = ' + str(pageno))
                        findLevel1 = True
                elif findLevel1:
                    # not found next level 2, end
                    # 可能 level2title 是该章最后一节，下一章作为结尾页
                    if findLevel2Start and not findLevel2End:
                        findLevel2End = True
                        level2pageno2 = pageno
                        if debug:
                            print(title + ' = ' + str(pageno))
                    # find next level 1, exit
                    break
            elif level == 2:
                if findLevel1:
                    if level2title in title:
                        findLevel2Start = True
                        level2pageno1 = pageno
                        if debug:
                            print(title + ' = ' + str(pageno))
                        # FIXME: 可能是最后一章最后一节，则结束页码可取总页数
                    elif findLevel2Start:
                        # find next level 2, end
                        findLevel2End = True
                        level2pageno2 = pageno
                        if debug:
                            print(title + ' = ' + str(pageno))
                        break
                    if findLevel2Start and findLevel2End:
                        break  # 都找到了
    except PDFNoOutlines as exc:
        print(exc)
        pass
    return (level2pageno1, level2pageno2)


# 返回指定页面区间内（唯一）匹配关键字的页面页码
def locateKeywordPage(document: PDFDocument, keyword: str, pageno1: int, pageno2: int, debug: bool = False) -> int:
    matchedPageNumber = None
    # 创建pdf资源管理器 来管理共享资源
    resource = PDFResourceManager()
    # 参数分析器
    laParam = LAParams()
    # 创建一个聚合器
    device = PDFPageAggregator(resource, laparams=laParam)
    # 创建pdf页面解释器
    interpreter = PDFPageInterpreter(resource, device)

    # 循环遍历列表，每次处理一个page的内容
    for pageno, page in enumerate(PDFPage.create_pages(document)):
        if pageno >= pageno1 and pageno < pageno2:
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象，里面存放着这个 page 解析出的各种对象
            # 包括 LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    textBox = x.get_text().strip()
                    if keyword in textBox:
                        matchedPageNumber = pageno
                        break
    return matchedPageNumber


# 打印匹配关键字（行标题）的行内容
def locateRowOfTableInPage(filepath: str, pageno: int, rowtitle: str, debug: bool = False) -> str:
    pdf = pdfplumber.open(filepath)
    page = pdf.pages[pageno]
    targetRow = None
    for table in page.extract_tables():
        for row in table:
            if rowtitle in row:
                if debug:
                    print(row)
                targetRow = row
                break
    pdf.close()
    return targetRow


def main(filepath: str, debug: bool):
    if debug:
        (filePath, fileName) = os.path.split(filepath)
        print('filePath = {} \nfileName = {}\n'.format(filePath, fileName))

    # 打开PDF文档（只读、二进制模式）
    with open(filepath, 'rb') as fp:
        # 创建PDF文档分析器
        parser = PDFParser(fp)
        # 创建一个PDF文档
        document = PDFDocument(parser)
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed

        # 1. 找出指定章节的页码范围[start, end)
        pageRange = findTOCPages(document, '재무에 관한 사항', '연결재무제표 주석', debug)
        print('pageRange =', pageRange)

        # 2. 在页码范围内查找关键词所在的具体页面
        keyword = '평균유효세율'
        matchedPageNo = locateKeywordPage(
            document, keyword, pageRange[0], pageRange[1])
        print('matchedPageNo =', matchedPageNo)

        # 3. 解析具体页面中的表格，并定位关键词所在表格的行
        targetRow = locateRowOfTableInPage(
            filepath, matchedPageNo, keyword, debug)
        col1 = targetRow[1]
        col2 = targetRow[2]
        print(col1[:-2], col2[:-2])  # 不打印尾部百分号


# main entry
if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        description="korea's coperate fillings parser",
        formatter_class=argparse.
        RawTextHelpFormatter,
        epilog='melody')
    argparser.version = '1.0'
    argparser.add_argument('-V', '--version', action='version')
    argparser.add_argument('filepath', type=str, help='path of PDF')
    argparser.add_argument('-v', '--verbose', dest='debug',
                           action='store_true', help='print debug verbose')
    args_namespace = argparser.parse_args()
    # print(vars(args_namespace))

    if not os.path.isfile(args_namespace.filepath):
        print('please input valid PDF filepath')
    else:
        main(args_namespace.filepath, args_namespace.debug)

else:
    # print('I am being imported from another module')
    pass
