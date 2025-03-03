# -*- coding: cp1251 -*-

import datetime
import calendar
from art import *

def get_birthday():
    day = int(input("������� ���� ��������: "))
    month = int(input("������� ����� ��������: "))
    year = int(input("������� ��� ��������: "))
    return day, month, year

def day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")

def is_leap_year(year):
    return calendar.isleap(year)

def calculate_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def display_date_as_stars(day, month, year):
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    date_str = f"{day_str} {month_str} {year_str}"
    print(text2art(date_str))

def main():
    day, month, year = get_birthday()
    print(f"�� �������� � {day_of_week(day, month, year)}.")
    print(f"��� ��� �������� {year} {'����������' if is_leap_year(year) else '�� ����������'}.")
    print(f"��� ������ {calculate_age(day, month, year)} ���.")
    print("���� ���� �������� � ������� �� �� ����:")
    display_date_as_stars(day, month, year)

if __name__ == "__main__":
    main()