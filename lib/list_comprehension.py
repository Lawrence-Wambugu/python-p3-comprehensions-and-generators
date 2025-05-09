#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens  # Ensure the function returns the list of even numbers

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]  # Return a new list with exclamation marks
