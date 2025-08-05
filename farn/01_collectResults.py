#!/usr/bin/env python
#coding utf-8

import shutil
import pandas as pd
from pathlib import Path
from mvf.utils.tableTool import collect_data_frame_from_paths


# collect convPlots in bash
# for i in 2022-11-16_cases/lhsVar_* ; do cp $i/results/watchDict-simulinkResults.png 2022-11-16_results/convPlots/${i/2022-11-16_cases'/'/}_watchDict-simulinkResults.png ; done

# rename files to same ame
# for i in 2023-04-20_cases/fixedLayer_*/lhsLayer_*/results ; do s=$i/*target.png ; t=$(echo $s |sed 's/_changerate.*/_target.png/') ; cp $s $t ; done

# delete a file
# for i in 2023-04-20_cases/fixedLayer_*/lhsLayer_*/results/2023-04-20_gunnerus-dp_wp-gen.png ; do rm $i ; done

if __name__ == '__main__':
    
    caseDir = Path('cases') # leave it relative!
    #caseDir = Path.cwd() / caseDir
    
    dumpDir = 'dump'
    dumpDir = Path.cwd() / dumpDir
    dumpDir.mkdir(parents=True, exist_ok=True)
    
    dumpFile = 'resultDataFrame.dump'
    
    resultDir = 'results'
    resultDir = Path.cwd() / resultDir
    resultDir.mkdir(parents=True, exist_ok=True)
    
### INPUTS ###
    pathTemplate = f'{caseDir}/lhsVar_*'
    dictionary = 'paramDict'
    
    pathList = list(Path.cwd().glob(pathTemplate))
   
    map = {
        'caseIndex':{'key':'_case:index'},
        'minuend':{'key':'minuend'},
        'subtrahend':{'key':'subtrahend'},   
        'dividend':{'key':'dividend'},   
    }
    
    (dfI, style) = collect_data_frame_from_paths(
        pathList,
        dictionary,
        map,
        use_path_as_index = False
    )
    dfI.dropna()
    
    #repair strange automatic to_datetime issue
    dfI = dfI.apply(pd.to_numeric, errors='ignore')   
    
### RESULTS ###
    pathTemplate = f'{caseDir}/lhsVar_*/results'
    dictionary = 'watchDict-farn_demo-resultDict'

    pathList = list(Path.cwd().glob(pathTemplate))
    
    map = {
        'quotient':{'key':'quotient|quotient.OUT:latestValue', 'unit':'1'},
        'difference':{'key':'difference|difference.OUT:latestValue', 'unit':'1'},
    }

    #add path to columns
    (dfR, style) = collect_data_frame_from_paths(
        pathList,
        dictionary,
        map,
        use_path_as_index = False
    )
    dfR.dropna()
   
    #repair strange automatic to_datetime issue
    dfR = dfR.apply(pd.to_numeric, errors='ignore')
        
    df = pd.concat((dfI, dfR), axis=1, sort=False)
    #df = pd.concat([dfI, dfR.drop(['path'], axis=1)], axis=1, sort=False)
        
    #df = dfI
    #if containing voids
    #dfs = [dfI, dfR]
    #df = reduce(lambda  left,right: pd.merge(left,right,on=['Steps'], how='outer'), dfs).fillna(0)
    
    df.to_pickle(Path.joinpath(dumpDir, dumpFile), compression='gzip', protocol=5)
    
    exit(0)
    



