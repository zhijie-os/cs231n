def classify_image(image):
    # some magic here
    # unlike sorting a list of numbers
    # no obvious way to hard-code the algorithm for recognizing a cat or other classes
    return class_label

'''
data-driven approach:
    1. Collect a dataset of images and labels
    2. Use machine learning to train a classifier
    3. Evaluate the classifier on new images
'''

def train(images, labels):
    # machine learning
    return model

def predict(model, test_images):
    # use model to predict labels
    return test_labels


'''
first classifier: Nearest Neighbor
'''

def train(images, labels):
    # machine -> memorize all data and labels
    return model

def predict(model, test_images):
    # predict the label of the most similar training model  
    return test_labels

'''
hyperparameters - knn:

what is the best value of k to use

what is the best distance to use

Very problem-dependent
Must try them all out and see what works best
'''

'''
idea #1: choose hyperparameters that work best on the data

BAD: k = 1 always works perfectly on training data
|-----train------|

idea #2: split data into training and test, choose
hyperparameters that work best on test data

BAD: No idea how algorithm will perform on new data
|---train---|test|

idea #3: split data into train, val, and test;
choose hyperparameters on val and evaluate on test

|--train--|val|test|, test is touched last for reporting

idea #4: cross-validation: split data into
folds, try each fold as validation and average
the results

|f1|f2|f3|f4|v|t|
|f1|f2|f3|v|f5|t|
|f1|f2|v|f4|f5|t|

k-nearest neighbor on images never used

- very slow at test time
- distance metrics on pixels are not informative
'''





image - array of 32*32*3 numbers -> f(x,W) -> 10 numbers giving class scores

W parameters or weights