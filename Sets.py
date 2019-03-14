user_1 = {'hulk','ironman','baahubali','robot','URI','mask','batman','superman',
          'the ring','fukrey'}

user_2 = {'baahubali','robot','ironman','batman','fukrey','avengers','thor',
          'kgf','zero','sanju'}


intersection = user_1.intersection(user_2)
union = user_1.union(user_2)

# Jaccard Distance
dis = len(intersection) / len(union)
sim = 1 - dis
print("Similar Movies are",intersection)
print(sim * 100)
