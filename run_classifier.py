from argparse import ArgumentParser

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os 
import pickle 
from tqdm import tqdm
from collections import defaultdict 
from pprint import pprint


def extract_features_from_rrdata(data_root_dir): 
    """
    data_root_dir: path to directory containing to *.txt files
    """

    features = defaultdict(list) 
    txt_files = [x for x in sorted(os.listdir(data_root_dir)) if x.endswith('.txt')]

    for x in tqdm(txt_files, total=len(txt_files)): 
        if not x.endswith('.txt'): 
            continue 

        with open(os.path.join(data_root_dir, x), 'r') as f:
            rr_data = [float(y) for y in f.read().splitlines() if y]
        
        patient_age = rr_data[0] 
        full_data_array = np.array(rr_data[1:])

        subsections = np.array_split(full_data_array, len(full_data_array) // 3200)

        for data_array in subsections:
            q1 = np.percentile(data_array, 25)
            q3 = np.percentile(data_array, 75)
            iqr_rr = q3 - q1

            lower_bound = q1 - 1.5 * iqr_rr 
            upper_bound = q3 + 1.5 * iqr_rr 


            data_array = data_array[data_array <= upper_bound]
            data_array = data_array[data_array >= lower_bound]

            beats = len(data_array) 
            total = np.sum(data_array) 
            bpm = (beats / total) * 1000 * 60   
            mean_rr = np.mean(data_array) 
            range_rr = np.rint(np.max(data_array) - np.min(data_array))
            
            # Calculate the interquartile range (IQR)
            q1 = np.percentile(data_array, 25)
            q3 = np.percentile(data_array, 75)
            iqr_rr = q3 - q1

            # Calculate the variance
            var_rr = np.var(data_array)
            # Calculate the standard deviation
            std_rr = np.std(data_array)
            # Calculate the coefficient of variation
            cv_rr = std_rr / np.mean(data_array) * 100
            
            features['Age'].append(patient_age)
            features['BPM'].append(bpm)
            features['Mean'].append(mean_rr)
            features['Range'].append(range_rr)
            features['IQR'].append(iqr_rr)
            features['Variance'].append(var_rr)
            features['Std Dev'].append(std_rr)
            features['ID'].append(x.split('.txt')[0])
        
    return pd.DataFrame(features)


def classify(model, feature_dict: pd.DataFrame): 
    ids = feature_dict['ID'] 
    feature_dict = feature_dict.drop(['ID'], axis=1)
    y_pred = model.predict(feature_dict)
    
    results = defaultdict(bool)
    for uid in np.unique(ids): 
        results[uid] = y_pred[ids == uid].mean() > 0.5

    return results

# python3 run_classifier.py --root_dir=Data/Unprocessed/HealthyRR --model_path='model.pkl'
if __name__ == '__main__': 

    parser = ArgumentParser() 

    parser.add_argument('--root_dir', '-r', type=str, help="Path to directory containing RR peak data in .txt format.")   
    parser.add_argument('--model_path', '-m', type=str, help="Path to trained classifier.") 

    args = parser.parse_args() 

    feature_dict = extract_features_from_rrdata(args.root_dir)

    with open(args.model_path, 'rb') as f: 
        model = pickle.load(f)

    results = classify(model, feature_dict)