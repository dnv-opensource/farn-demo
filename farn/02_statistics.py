#!/usr/bin/env python
#coding utf-8

import pandas as pd
import numpy as np
from pathlib import Path
from mvf.utils.tableTool import filter_reset
from mvf.statistic.chiSquare import chi_square_homogeneity
from old_not_used.statistic.statisticFunctions_not_used import statistic_summary
from dictIO.dictWriter import DictWriter
from mvf.utils.plotting import Plot, generate_3d_scatter_plot, generate_3d_bar_plot, generate_multivariate_plot

if __name__ == '__main__':
    # to be executed in farn root dir
    stats = dict({})
    statsFile = 'statistics'

    workDir = 'cases'

    dumpDir = 'dump'
    dumpDir = Path.cwd() / dumpDir
        
    resultDir = 'results'
    resultDir = Path.cwd() / resultDir
    resultDir.mkdir(parents=True, exist_ok=True)

    dumpFile = 'resultDataFrame.dump'

    df = pd.read_pickle(Path.joinpath(dumpDir, dumpFile), compression='gzip')
    
    '''
    # help finding header
    header = df.columns
    print (header)
    exit(0)
    header = ['caseIndex', 'minuend', 'subtrahend', 'dividend', 'quotient', 'difference']
    '''
    #reduced df to relevant values
    header = ['minuend', 'subtrahend', 'dividend', 'caseIndex']
   
    pdf = pd.DataFrame({'x%i:%s'%(i,s):df.loc[:,s] for i, s in enumerate(header)}) # i: number, s: name
    P = Plot()
    P.populate(
        pdf, marker='o', 
        marker_size=16, 
        label_size=6, 
        print_labels=True, 
        logscale_c=False
    )
    
    title = f'scatter points {" ".join(header)} {str(pdf.shape[0])} cases'
    generate_3d_scatter_plot(
        [P],
        title = title,
        path=resultDir,
        output='persist'
    )
    #exit(0)
    #header = ['caseIndex', 'minuend', 'subtrahend', 'dividend']
    header = ['caseIndex', 'minuend', 'subtrahend', 'dividend']

    pdf = pd.DataFrame({s:df.loc[:,s] for i, s in enumerate(header)}) # i: number, s: name
   
    # filter for caseIndex (all 2^n, caseIndex is not the index but from paramDict!)
    exceptList = [0, 1, 2, 3, 4, 5, 6, 7]
    pdf = filter_reset(pdf, query = f'caseIndex not in {exceptList}')
    
    # remove caseIndex
    header = ['minuend', 'subtrahend', 'dividend']
    pdf = pd.DataFrame({s:pdf.loc[:,s] for i, s in enumerate(header)})
    
    S = statistic_summary(pdf.to_numpy(), header=header)
    stats.update({'statistics': S})
    DictWriter.write(stats, Path.joinpath(resultDir, statsFile), mode='a')

    title = f'correlation errors {" ".join(header)} {str(pdf.shape[0])} cases'
    generate_3d_bar_plot(
        matrix=S['corrError'],
        title = title,
        path=resultDir,
        header=header,
        print_labels=True,
        color_range=[-1,1],
        output='persist'
    )
    exit(0)
