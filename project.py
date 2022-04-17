import pandas as pd 
import plotly.express as pe 

df = pd.read_csv("score.csv")

score = df["TOEFL Score"].tolist()

Chance_of_Admission = df["Chance of Admit "].tolist() 

graph = pe.scatter(x = score, y = Chance_of_Admission) 
# graph.show()


# --------------------------- using hit and trial method (m= 0.01 , c=-2.5) -------------------------------------
# y = mx + c

m = 0.01
c = -2.5 
y = [] 

for x in score:
    y_val = m * x + c
    y.append(y_val)

graph = pe.scatter( x = score, y = Chance_of_Admission)

graph.update_layout(shapes = [
    dict(
        type = "line",
        y0 = min(y), y1 = max(y),
        x0 = min(score), x1 = max(score),

    )
])
#graph.show()


x = 250
y = m * x + c

print("Chances of admission of someone with 250 Toefl Score using hit and trial: " , y)


# ------------------------------------ using the algorithm will get the value of m & c----------------------------------

import numpy as np

score_array = np.array(score)
Chance_of_Admission_array = np.array(Chance_of_Admission)

m,c = np.polyfit(score_array , Chance_of_Admission_array ,  1)

y = [] 

for x in score_array:
    y_val = m * x + c
    y.append(y_val)

graph = pe.scatter( x = score_array, y = Chance_of_Admission_array)

graph.update_layout(shapes = [
    dict(
        type = "line",
        y0 = min(y), y1 = max(y),
        x0 = min(score_array), x1 = max(score_array),

    )
])
#graph.show()


x = 250
y = m * x + c

print("Chances of admission of someone with 250 Toefl Score using Algo : " , y)









