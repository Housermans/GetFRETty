import pandas as pd
from glob import glob

YFP_path = glob('../Input/*YFP.csv')[0]
CFP_path = glob('../Input/*CFP.csv')[0]

YFP = pd.read_csv(YFP_path, sep=',', index_col=0)
YFP.index.name = 'ObjectID'
YFP.rename(columns={'Mean':'Mean_YFP', 'TrackN':'TrackID', 'Area':'Area_YFP'}, inplace=True)

CFP = pd.read_csv(CFP_path, sep=',', index_col=0)
CFP.index.name = 'ObjectID'
CFP.rename(columns={'Mean':'Mean_CFP', 'Area':'Area_CFP'}, inplace=True)

YFP_table = YFP[['TrackID', 'Mean_YFP',  'Area_YFP', 'Slice']]
CFP_table = CFP[['Mean_CFP', 'Area_CFP']]
result = pd.concat([YFP_table, CFP_table], axis=1, join='inner')
result.sort_values(by=['TrackID', 'Slice'], ascending=True, inplace=True)

result['YFP/CFP_Ratio'] = result.Mean_YFP/result.Mean_CFP

result.to_csv('../Output/FRET_ratio.csv', sep=',')