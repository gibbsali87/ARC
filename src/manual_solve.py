#!/usr/bin/python

import os, sys
import json
from typing import Optional

import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

#Student Name: Arshad Ali
#Student ID: 20236061
#GitHub Repo: https://github.com/gibbsali87/ARC
"""
In this solution, we have input data where one side of the data set is different from the rest. 
However, it was effortless to see on the Visual website for a human. It was a bit of challenge to code 
that but I enjoyed it.
In the start, I took the approach of dividing the data into two sets and then take the set, 
which including the solution. Although it did work for some fo the Grids it was not the right solution, 
so I had to change my approach. Furthermore, I looked for the index where the data change started and ended. 
This was a much better approach and solved all the Grids.

In all of the solution, I have used pure python. I have used a dictionary in two of the three solutions.
All the grids are returning True for the three solution solved.
"""
def solve_0b148d64(x):
    myList = [x]
    newList = []
    a = None
    a1 = 0
    b = None
    b1 = 0
    c = 0
    lIndex = 0
    f_index = []
    l_index = []
    lastList = []

    # For loop to extract the indexes where the change is starting and ending.
    for i in myList:
        for j in i:
            for k in j:
                if a is None and b is None and k != 0:
                    a = k
                elif b is None and k != a and k != 0:
                    b = k
                elif k == a:
                    a1 = a1 + 1
                elif k == b:
                    b1 = b1 + 1
                elif k == c:
                    pass  # Do nothing
                else:
                    pass  # Do nothing
    if a1 < b1:
        s = a
    else:
        s = b
    for i in x:
        if s in i:
            if s in i:
                newList.append(i)
            else:
                pass

    for i in newList:
        i = i.tolist()
        f_index.append(i.index(s))

        rl = i[::-1]  # Reversing the list to get the last index where the data change has occurred.
        if rl.index(s) > lIndex:
            l_index.append(rl.index(s))
        else:
            pass
    fIndex = min(f_index)
    lIndex = min(l_index)
    lIndex = lIndex * -1  # Multiplying by -1 as I had reverse the list to get the last index

    for i in newList:
        i = i.tolist()
        if lIndex == -1:
            lastList.append(i[fIndex:])
        else:
            lastList.append(i[fIndex:lIndex])
    return lastList
"""
The output required in this solution is exchanging the index with a corresponding 
number that represents the corresponding colour.
The Approach I have taken is to store the colour values in a Dictionary 
and then replace it as required to form the correct output.
"""
def solve_0d3d703e(x):
    myList = [x]
    newList = []
    dic = {3: 4, 1: 5, 2: 6, 8: 9, 5: 1, 6: 2, 9: 8, 4: 3}
    # Nested for loop to exchange the current value with corresponding value
    # with the help of already created dictionary.
    for i in myList:
        for j in i:
            s_list = []
            for k in j:
                k = dic.get(k)
                s_list.append(k)
            newList.append(s_list)
    return newList

"""
This solution requires filling the surrounding squares with the colour of the 
corresponding square in the middle. There are two solution types required one 
for 3 x 11 Grid and one for 7 x 11 grid. 
The Approach I have taken is to store the colour square number and then create 
a list of the corresponding colour that I can match from a dictionary 
already created.
"""
def solve_54d9e175(x):
    # Variables and Objects
    myList = [x]
    newList = []
    dic = {2: 7, 3: 8, 4: 9, 1: 6}
    ind = []
    # Below nested for loops, extracts the number that I can match for the colour,
    # and storing it in a list.
    # Then I query the dictionary and assign the correct colour to a variable
    # for later use.
    for i in myList:
        for j in i:
            for k in j:
                if k == 0 or k == 5:
                    pass
                else:
                    ind.append(k)
        first = dic.get(ind[0])
        second = dic.get(ind[1])
        third = dic.get(ind[2])
        # Checking if 3x11 or 7x11 Grid is required.
        if len(x) > 3:
            fourth = dic.get(ind[3])
            fifth = dic.get(ind[4])
            sixth = dic.get(ind[5])
        else:
            pass
        # Below nested while loops create the required output.
        while len(newList) < 3:
            s_list = []
            while len(s_list) < 3:
                s_list.append(first)
            s_list.append(5)
            while len(s_list) < 7:
                s_list.append(second)
            s_list.append(5)
            while len(s_list) < 11:
                s_list.append(third)
            newList.append(s_list)

        # Checking if 3x11 or 7x11 Grid is required.
        if len(x) > 3:

            f_list = []
            while len(f_list) < 11:
                f_list.append(5)
            newList.append(f_list[:12])

            while len(newList) < 7:
                s_list = []
                while len(s_list) < 3:
                    s_list.append(fourth)
                s_list.append(5)
                while len(s_list) < 7:
                    s_list.append(fifth)
                s_list.append(5)
                while len(s_list) < 11:
                    s_list.append(sixth)
                newList.append(s_list)
        else:
            pass
    return newList

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)
        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()
