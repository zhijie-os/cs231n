'''
Todo:
1. define a loss function that quantifiers our unahappiness with
the scores across the training data
2. come up with a way of efficiently finding the parameters that minimize the loss 
function (optimization)

L = 1/N acc_i Li(f(x_i, W), y_i)

multiple class SVM

x_i = the image
y_i = the (integer) label

L_i = acc_j!=yi{0 (if s_yi >= s_j + 1), s_j - s_y + 1(otherwise)}
    = acc_j!=yi(max(0, s_j - s_yi + 1))
    = max(0, 2.2 - (-3.1) + 1)
    = 3
'''


