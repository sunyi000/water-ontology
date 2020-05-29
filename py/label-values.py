import configparser
import pandas as pd

def main():
    cp = configparser.RawConfigParser()
    configFile = r'config.ini'
    cp.read(configFile)

    data = pd.read_csv("C:/Users/ysun/Documents/griffith/water-data/data-all-1.csv.o")
    templbl = []
    disOxylbl =[]
    orplbl = []
    condlbl = []
    turblbl = []
    pHlbl =[]

    for i,row in data.iterrows():

        if float(row["temperature"]) > float(cp.get('threshold','temperature')):
            templbl.append('high')
        else:
            templbl.append('low')

        if float(row["conductivity"]) > float(cp.get('threshold','conductivity')):
            condlbl.append('high')
        else:
            condlbl.append('low')

        if float(row["disOxy"]) > float(cp.get('threshold','disOxy')):
            disOxylbl.append('high')
        else:
            disOxylbl.append('low')

        if float(row["orp"]) > float(cp.get('threshold','orp')):
            orplbl.append('high')
        else:
            orplbl.append('low')

        if float(row["pH"]) > float(cp.get('threshold','pH')):
            pHlbl.append('high')
        else:
            pHlbl.append('low')

        if float(row["turbidity"]) > float(cp.get('threshold','turbidity')):
            turblbl.append('high')
        else:
            turblbl.append('low')

    data['tempFlag']=templbl
    data['condFlag'] = condlbl
    data['DOFlag'] = disOxylbl
    data['ORPFlag'] = orplbl
    data['pHFlag'] = pHlbl
    data['turbFlag'] = turblbl

    print (data)
    data.to_csv('new.csv')

if __name__ == "__main__":
    main()