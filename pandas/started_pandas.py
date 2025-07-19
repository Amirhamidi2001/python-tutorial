# Pandas Getting Started

import pandas as pd


# Import Pandas
import pandas

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pandas.DataFrame(mydataset)
print(myvar)

# Pandas as pd
mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)

# Checking Pandas Version
print(pd.__version__)
