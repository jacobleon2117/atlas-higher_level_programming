#!/usr/bin/python3

def best_score(a_dict):
    if a_dict is None:
        return None
    if len(a_dict) == 0:
        return None
    return max(a_dict, key=a_dict.get)