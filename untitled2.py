# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:58:21 2024

@author: student
"""

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "是一個偶數。")
    else:
        print(number, "不是一個偶數。")

def main():
    # 輸入一個整數
    number = int(input("請輸入一個整數: "))

    # 判斷是否為偶數
    check_even_odd(number)

if __name__ == "__main__":
    main()
