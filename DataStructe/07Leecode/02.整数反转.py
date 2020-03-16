# -*- coding: utf-8 -*-
# Author: Hao Zhao

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
    输入: 123
    输出: 321

def func1(x):
    temp = 0
    s = str(x)
    for i in range(len(s))
        temp = temp + s[len(s) - i]
    return temp

示例 2:
    输入: -123
    输出: -321

示例 3:
    输入: 120
    输出: 21

注意:假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

"""
class Solution:
    def reverse(self, x: int) -> int:
        # x // max(1,abs(x)) 判定正负符号
        # int(str(abs(x))[::-1]) 先字符串切片（取反）；然后转换成整形去"0"
        r = x // max(1, abs(x)) * int(str(abs(x))[::-1])
        # 三元运算
        return r if -2 ** 31 <= r <= 2 ** 31 - 1 else 0

# 测试
obj = Solution()
print(obj.reverse(123))
print(obj.reverse(-123))
print(obj.reverse(120))
