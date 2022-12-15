#!/usr/bin/python3
def multiple_returns(sentence):
    # If the sentence is empty, the first character should be equal to None
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
