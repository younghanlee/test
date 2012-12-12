#!/usr/bin/python
#-*- coding: utf-8 -*-

def sort_dict_by_key(adict):
  keys = adict.keys()
  keys.sort()
  return [adict[key] for key in keys]

def sort_dict_by_value(adict):
  values = adict.values()
  return values.sort()

def sort_case_insensitive(string_list):
  temp_list = [(x.lower(), x) for x in string_list)]
  temp_list.sort()
  return [x[1] for x in temp_list]
