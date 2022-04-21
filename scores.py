from collections import Counter
import numpy as np


# actual accuracy
def get_accuracy(p_data, t_data):
    sc = 0
    for i in range(len(p_data)):
        if p_data[i] == t_data[i]:
            sc += 1
    return sc / len(p_data)


# if all the digits where predicted, not just in the right order
def get_accuracy_order(p_data, t_data):
    sc = 0
    for i in range(len(p_data)):
        pred = str(int(p_data[i]))
        tru = str(t_data[i])
        # https://codereview.stackexchange.com/questions/140807/check-if-one-string-is-a-permutation-of-another-using-python
        if len(pred) == len(tru) and Counter(pred) == Counter(tru):
            sc += 1

    return sc / len(p_data)


# if at least 1 digit is correct
def get_accuracy_one(p_data, t_data):
    sc = 0
    for i in range(len(p_data)):
        pred = str(int(p_data[i]))
        tru = str(t_data[i])

        unique_pred = list(set(pred))
        unique_tru = list(set(tru))

        for u in unique_pred:
            if u in unique_tru:
                sc += 1
                break

    return sc / len(p_data)


# accuracy on the digits that in the testing set but not the training set
def get_accuracy_untrainable(p_data, t_data):
    # read in the unique digits
    with open("../results/untrainable_digits.txt", 'r') as g:
        y = np.asarray(list(map(int, g.readlines())))

    sc = 0
    ttl = 0
    for i in range(len(p_data)):
        if np.sum(y == t_data[i]) > 0:  # if the label is untrainable
            ttl += 1
            if p_data[i] == t_data[i]:
                sc += 1
    return sc / ttl
