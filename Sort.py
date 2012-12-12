#!/usr/bin/python
#-*- coding: utf-8 -*-

def sortDictByKey(adict):
  keys = adict.keys()
  keys.sort()
  return [adict[key] for key in keys]

def sortDictByValue(adict):
  values = adict.values()
  return values.sort()

def sortCI(string_list):
  temp_list = [(x.lower(), x) for x in string_list)]
  temp_list.sort()
  return [x[1] for x in temp_list]
