def get_min_max_score(*scores):
    li = [score for score in scores]
    return min(li), max(li)

def get_average(korean=None, english=None, math=None, science=None):
    li = [korean, english, math, science]
    li = [i for i in li if i != None]
    print(li)
    return sum(li) / (len(li) + 1)

(kor, eng, math, science) = [int(i) for i in input().split()]

min_score, max_score = get_min_max_score(kor, eng, math, science)
average_score = get_average(korean=kor, english=eng,
                            math=math, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(eng, science)
average_score = get_average(english=eng, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))