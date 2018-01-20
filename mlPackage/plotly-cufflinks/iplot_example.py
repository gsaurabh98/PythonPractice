import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from plotly import __version__
import plotly.plotly as py
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import cufflinks as cf

init_notebook_mode(connected=True)
cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
print df.head()

df.iplot()
plt.show()