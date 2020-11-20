# PyTexCount
[![codebeat badge](https://codebeat.co/badges/54028854-7c45-4cd6-b1af-25842c2de1b5)](https://codebeat.co/projects/github-com-hobeedzc-pytexcount-master)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/HoBeedzc/PyTexCount)
![GitHub](https://img.shields.io/github/license/HoBeedzc/PyTexCount)

## What is PyTexCount ? 什么是PyTexCount？
Using Python to count the number of Chinese characters in LaTeX.
使用Python统计LaTeX正文中中文字符的个数。

构想：

复杂模式：


五种形式，包括：
- 形成标准 PyPi 第三方库
- Python 脚本
- GUI 界面操作
- Shell 命令行操作
- Web 应用程序

目标功能：
- 统计.tex文件中正文字符，不局限于中文字符
- 按需求统计字符
- 给出latex命令、字符统计信息、计算阅读时间
- 利用深度学习及神经网络自动化编写摘要和关键词
- 按章节统计字数

目前已实现功能：
- 统计.tex正文的字符，其中不包括中文字符。
- 统计.tex文件中使用的第三方程序包数目，并列出。(目前并未解决包含可选参数包名的统计)

简单模式：

如果要计算的.tex文件过于庞大，可使用简单模式进行字数统计。

简单模式使用迭代器加载文件，不会对内存造成压力，并且处理庞大文件时也会拥有较好的性能。

但由于使用了迭代器，功能上也会有所限制，目前仅可实现统计字数。

## Why PyTexCount ? 为什么要选择PyTexCount？



## How to get PyTexCount ? 如何获取PyTexCount？

From GitHub :
从Github：

https://github.com/HoBeedzc/PyTexCount

From PyPi :
从PyPi：

Not support now.暂不支持

## How to Use PyTexCount ? 怎么使用PyTexCount？


