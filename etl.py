from pandas import *
from streamlit import *

data = {    'Task' : ['ectract','transform','load'],
            'Status':['completed','inprogress','pending']
           }
write('AVD11')

df = DataFrame(data)
write('Etl pipeline execution status')
write(df)