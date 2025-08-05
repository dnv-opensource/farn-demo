#!/usr/bin/env python
#coding utf-8

import pandas as pd
import pandasgui
from pathlib import Path

    
workDir = 'cases'
dumpDir = 'dump'
fName = 'resultDataFrame.dump'
fPath = Path.cwd() / dumpDir / fName

df = pd.read_pickle(fPath, compression='gzip')

pandasgui.show(df, settings={'block': True})


