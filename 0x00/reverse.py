#!/usr/bin/env python
# encoding: utf-8


# 方法一：将list作为stack使用，将字符串倒序输出
def reverse_1(str):
    stack = list(str)
    li = []

    for i in range(len(stack)):
        li.append(stack.pop())
    return "".join(li)

# 方法二： 利用list的反向切片功能实现字符串反转
def reverse_2(str):
    return str[::-1]

# 方法三：递归
def reverse_3(str):
    if len(str) < 2: return str
    return reverse_3(str[1:]) + str[0]



if __name__ == "__main__":
    str = "I am a string"
    print reverse_3(str)
