from pandas import *
from streamlit import *

data = {    'Task' : ['ectract','transform','load'],
            'Status':['completed','inprogress','pending']
           }
write('Welcome to AVD, MR Pandurang!')

df = DataFrame(data)
write('Etl pipeline execution status')
write(df)