import ConfigParser
import zipfile
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
Config = ConfigParser.ConfigParser()
Config.read("limpieza.ini");

def carga_archivo(ruta_zip,nombre):

    columnas    = Config.get(nombre,"columnas")
    columnas    = columnas.split(',')
    extencion   = Config.get(nombre,"extencion")

    zip_ = zipfile.ZipFile(ruta_zip, 'r')
    zip_.extract(ruta_zip.split('/')[-1][:-4],"tmp/")
    zip_.close()

    if extencion == ".xlsx":
        df = pd.read_excel(ruta_zip[:-4])
    elif extencion == ".csv":
        df = pd.read_csv(ruta_zip[:-4])
    elif extencion == ".hd5":
        df = pd.read_hdf(ruta_zip[:-4])
    else:
        return(0,"Tipo de archivo no conocido")
    
    columnas_file=[]
    for i in df.columns:
        columnas_file.append(i)
    
    if columnas_file != columnas:
        return(0,"Las columnas no corresponden a las acordadas")

    df = df.drop_duplicates() # registros duplicados
    df=df.reset_index(drop=True)
   
    return 1,df
