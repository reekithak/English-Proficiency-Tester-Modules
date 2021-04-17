import random
import string

sent_1 = "Nowadays, there is a huge amount of data that can be categorized as sequential. It is present in the form of audio, video, text, time series, sensor data, etc. A special thing about this type of data is that if two events are occurring in a particular time frame, the occurrence of event A before event B is an entirely different scenario as compared to the occurrence of event A after event B.".lower().split(" ")
sent_2 = "Text, a stream of characters lined up one after another, is a difficult thing to crack. This is because when handling text, a model may be trained to make very accurate predictions using the sequences that have occurred previously, but one wrong prediction has the potential to make the entire sentence meaningless. However, in case of a numerical sequence prediction problem, even if a prediction goes entirely south, it could still be considered a valid prediction (maybe with a high bias). But, it would not strike the eye.".lower().split(" ")


score_2_pos = 0
score_2_neg = 0 

def direct_comp(A,B):
    global score_2_pos,score_2_neg
    for x , y in zip(A,B):
        if x == y:
            score_2_pos+=1
        else:
            pass

def jaccard_sim(generated_text,input_text):
    intersection = set(generated_text).intersection(set(input_text))
    union = set(generated_text).union(set(input_text))
    return len(intersection)/len(union)

#score1 (15%) , score2 (85%)
def final_score(score_1,score_2):
    final_score = score_1*.15 + score_2*.85
    return final_score


def comparisor(generated_text , input_text):
    global score_2_pos,score_2_neg
    if len(sent_1)==len(sent_2):
        direct_comp(sent_1,sent_2)

    elif len(sent_1)>len(sent_2):
        count_ = len(sent_1)-len(sent_2)
        for iter_ in range(count_):
            letters = string.ascii_lowercase
            sent_2.append(letters)
            score_2_neg +=-0.25
        direct_comp(sent_1,sent_2)
    else:
        count_ = len(sent_2)-len(sent_1)
        for iter_ in range(count_):
            sent_2.pop(-1)
            score_2_neg +=-0.25

        direct_comp(sent_1,sent_2)



comparisor(sent_1,sent_2)
print("Positive Score:",score_2_pos,", Negative Score:",score_2_neg)
score_2 = ((score_2_pos+score_2_neg)/len(sent_1))*10
score_1 = jaccard_sim(sent_1,sent_2)
print("Final Score on 10 =",final_score(score_1,score_2))