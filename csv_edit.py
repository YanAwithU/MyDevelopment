from glob import glob
import pandas as pd

jsonData = pd.read_csv('train_labels.csv')
imgList = glob('*.jpg')

lastData=jsonData[jsonData.filename.isin(imgList)]

lastData.to_csv('fixed_train_labels.csv')

    
    
