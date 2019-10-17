import pandas as pd


def remove_features(frame, list_of_columns):
    res = frame.drop(frame[list_of_columns], axis=1)
    return res




