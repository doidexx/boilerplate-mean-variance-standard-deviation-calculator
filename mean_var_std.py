import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array([
        list[:3],
        list[3:6],
        list[6:]])

    calculations = {
        'mean' : [
            [float(mean) for mean in np.mean(arr, axis=0)], 
            [float(mean) for mean in np.mean(arr, axis=1)], 
            float(np.mean(arr.flatten()))],
        'variance' : [
            [float(var) for var in np.var(arr, axis=0)], 
            [float(var) for var in np.var(arr, axis=1)], 
            float(np.var(arr.flatten()))],
        'standard deviation' : [
            [float(std) for std in np.std(arr, axis=0)],
            [float(std) for std in np.std(arr, axis=1)],
            float(np.std(arr.flatten()))],
        'max' : [
            [float(max) for max in np.max(arr, axis=0)],
            [float(max) for max in np.max(arr, axis=1)],
            float(np.max(arr.flatten()))],
        'min' : [
            [float(min) for min in np.min(arr, axis=0)],
            [float(min) for min in np.min(arr, axis=1)],
            float(np.min(arr.flatten()))],
        'sum' : [
            [float(sum) for sum in np.sum(arr, axis=0)],
            [float(sum) for sum in np.sum(arr, axis=1)],
            float(np.sum(arr.flatten()))]
    }

    return calculations