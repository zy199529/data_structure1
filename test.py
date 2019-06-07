#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-03 18:18:29
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-03 18:37:50


class Fruit(object):
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):
        print(self.__color)

    @staticmethod
    def getPrice():
        print(Fruit.price)

    def __getPrice():
        Fruit.price = Fruit.price + 10
        print(Fruit.price)
    count =staticmethod(__getPrice)
if __name__ == "__main__":
    print(Fruit.price)
    apple = Fruit()
    apple.getColor
    Fruit.count()
    banana = Fruit()
    Fruit.count

