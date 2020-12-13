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

def solve_0b148d64(x):
    myList = [x]
    newList = []
    a = None
    a1 = 0
    b = None
    b1 = 0
    c = 0
    fIndex = 0
    lIndex = 0
    f_index = []
    l_index = []
    lastList = []

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

        rl = i[::-1]
        if rl.index(s) > lIndex:
            l_index.append(rl.index(s))
        else:
            pass
    fIndex = min(f_index)
    lIndex = min(l_index)
    lIndex = lIndex * -1

    print(fIndex)
    print(lIndex)  # Print for troubleshooting remove before submit

    for i in newList:
        i = i.tolist()
        if lIndex == -1:
            lastList.append(i[fIndex:])
        else:
            lastList.append(i[fIndex:lIndex])
    print(a1, b1, s, a, b)  # Print for troubleshooting remove before submit
    print(lastList)  # Print for troubleshooting remove before submit
    return lastList

def solve_0d3d703e(x):
    myList = [x]
    newList = []
    dic = {3: 4, 1: 5, 2: 6, 8: 9, 5: 1, 6: 2, 9: 8, 4: 3}

    for i in myList:
        for j in i:
            s_list = []
            for k in j:
                k = dic.get(k)
                s_list.append(k)
            newList.append(s_list)
    return newList

def solve_54d9e175(x):
    myList = [x]
    newList = []
    dic = {2: 7, 3: 8, 4: 9, 1: 6}
    ind = []
    f_list = []

    for i in myList:
        for j in i:
            s_list = []
            for k in j:
                if k == 0 or k == 5:
                    pass
                else:
                    ind.append(k)
        first = dic.get(ind[0])
        second = dic.get(ind[1])
        third = dic.get(ind[2])
        if len(x) > 3:
            fourth = dic.get(ind[3])
            fifth = dic.get(ind[4])
            sixth = dic.get(ind[5])
        else:
            pass

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
                print(f'S list at end {s_list}')
        else:
            pass

        print(f'ind {ind}')
        print(newList)
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
