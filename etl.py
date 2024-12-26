from pandas import *
from streamlit import *

data = {    'Task' : ['ectract','transform','load'],
            'Status':['completed','inprogress','pending']
           }
write('AVD112233444')

df = DataFrame(data)
write('Etl pipeline execution status')
write(df)