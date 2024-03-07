# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:56:42 2024

@author: student
"""


def collect_user_data():
    # 輸入用戶資料
    name = input("請輸入您的姓名: ")
    age = int(input("請輸入您的年齡: "))
    height = float(input("請輸入您的身高（米）: "))
    favorite_color = input("請輸入您喜愛的顏色: ")

    # 建立用戶資料字典
    user_data = {
        "姓名": name,
        "年齡": age,
        "身高": height,
        "喜愛的顏色": favorite_color
    }

    return user_data

def format_user_summary(user_data):
    # 格式化用戶資料摘要
    summary = "{name}, {age}歲, 身高{height}米, 喜愛的顏色是{color}。".format(
        name=user_data["姓名"],
        age=user_data["年齡"],
        height=user_data["身高"],
        color=user_data["喜愛的顏色"]
    )

    return summary

def main():
    # 收集用戶資料
    user_data = collect_user_data()

    # 格式化用戶資料摘要並輸出
    user_summary = format_user_summary(user_data)
    print("用戶資料摘要:", user_summary)

if __name__ == "__main__":
    main()
