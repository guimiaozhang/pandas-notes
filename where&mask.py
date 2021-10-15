# In[1]
import pandas as pd
import numpy as np

# In[2]
s = pd.Series(range(5))
print(s)

# In[3]
#  df.where(condition, other=nan, inplace=False, 
#           axis=None, level=None, errors='raise', try_cast=NoDefault.no_default)[source]¶
print(s.where(s > 0))
print(s.mask(s > 0)) 

print(s.where(s > 0, 10)) #F --> 10
print(s.mask(s > 0, 10)) # T --> 10

# In[4]
df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])

df

# In[5]
m = df % 3 == 0 # 1%3 = 1
print(m)
df.where(m, -df)

# In[6]
np.where(m, df, -df)
#  numpy.where(condition[, x, y]) cond T -> x, F -> y
df.where(m, -df) == np.where(m, df, -df)

# In[7]
df.where(m, -df) == df.mask(~m, -df)
# ~m: not m

