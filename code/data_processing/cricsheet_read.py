
# this code reads in cricsheet.org data downloaded previously by cricsheet_fetch.

#---------------standard packages------------------
import numpy as np
import pandas as pd
import datetime as dt
from tqdm import tqdm
import os

#----------------league dictionary-----------------
league_dict = {'ntb':'Vitality Blast', 'ipl':'Indian Premier League',
               'cpl':'Carribean Premier League', 'psl':'Pakistan Super League',
               'bbl':'Big Bash League', 't20s':'T20 Internationals'}

#------------------cricsheet read------------------
def cricsheet_read(leagues = ['ntb', 'ipl', 'cpl', 'psl', 'bbl', 't20s']):
    
    data_directory = os.getcwd().split('gayle')[0] + 'gayle\\data\\master\\'

    league_df = pd.DataFrame.from_dict(league_dict, orient='index', columns=['league'])
    league_list = league_df[league_df.index.isin(leagues)]['league']
            
    master_stack=pd.read_csv(data_directory + 'master_data.csv', dtype={'ball':str, 'match_id':str}, parse_dates=['start_date'], low_memory = False)
    master_stack = master_stack[master_stack['league'].isin(league_list)] #league filter

    master_results = pd.read_csv(data_directory + 'master_results.csv', dtype = {0:str}).set_index('Unnamed: 0').rename_axis(index=None)
    master_results = master_results[master_results.index.isin(master_stack['match_id'].unique())] #get only matches in master_stack

    return master_stack, master_results