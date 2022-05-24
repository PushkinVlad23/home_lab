'GUF'
import pandas as pd
import matplotlib.pyplot as plt

courses = pd.read_csv('udemy_courses.csv')
pd.read_csv('udemy_courses.csv',delimiter=',',index_col=False)
sort = courses.sort_values(by='subject')
courses = pd.DataFrame(sort)
sum_con_dur_subject = courses.groupby('subject').content_duration.sum()
sum_con_dur_subject.plot.bar(x='subject',y='content_duration',color='grey',
                             rot=0,subplots=True,figsize=(8,5))
plt.show()
sum_lec_subject = courses.groupby('subject').num_lectures.sum()
sum_lec_subject.plot.bar(x='subject',y='num_lectures',color='g',
                         rot=0,subplots=True)
plt.show()
