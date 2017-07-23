# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 14:48:06 2017

@author: Ashish Kumar Jayant
"""
class Singleton(object):
    _instance = None
    age = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    @classmethod
    def makevariable(cls,x):
        cls.age = x

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    Singleton.makevariable(20)  #assigning values to the singleton class variable
    print(id(s1)==id(s2))
    print(s1,s2)
    print(Singleton.age)