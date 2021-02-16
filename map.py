import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))


shp_path = "data/censusblocks/CensusBlocks2010.shp" 
sf = shp.Reader(shp_path)

def read_shapefile(sf):
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]    
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)    
    return df

df = read_shapefile(sf)
df.shape
df.sample(5)