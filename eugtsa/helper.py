import re
import numpy as np
import pandas as pd
from tqdm import tqdm


def sort_df_cols_by(all_data, match_to_sort=re.compile(r'.[1-5]_xp'), suffixes_to_sort=r'[1-5]_(de|go|it|ki|lh|xp|he).*'):
    for cols_with_rad_heroes_nums in [re.compile(r'r'+suffixes_to_sort),re.compile(r'd'+suffixes_to_sort)]:

        cols_to_sort_rad = [col for col in all_data.columns if cols_with_rad_heroes_nums.match(col)]
        df_data_to_sort_radiants = all_data[cols_to_sort_rad]

        cols_sort_by = [c for c in cols_to_sort_rad if match_to_sort.match(c)]
        print('sorting by {}'.format(cols_sort_by))

        cols_vals = np.array([0,0,0,0,0])
        argsorted_rad_array = np.zeros((len(df_data_to_sort_radiants),len(cols_to_sort_rad)+1),dtype=int)
        block_len_to_sort = len(cols_to_sort_rad)

        sort_by_indexes = [i+1 for i,v in enumerate(cols_to_sort_rad) if match_to_sort.match(v)]

        sorted_row_indexes = np.array([0 for i in range(len(cols_to_sort_rad)+1)])

        def propagate_sort_by_indexes(cur_df_index,sort_by,propagate_num=int(len(cols_to_sort_rad)/len(cols_sort_by))):
            sorted_row_indexes[0] = 0
            for ind_0,ind in enumerate(sort_by):
                sorted_row_indexes[1+ind_0*propagate_num:1+(ind_0+1)*propagate_num] = np.arange(1+ind*propagate_num,1+(ind+1)*propagate_num)
            return sorted_row_indexes

        for df_tuple in tqdm(df_data_to_sort_radiants.itertuples()):
            tuple_array = np.array(df_tuple)
            cols_vals[:] = tuple_array[sort_by_indexes]

            argsorted = np.argsort(cols_vals)
            cur_df_index = df_tuple[0]
            argsorted_rad_array[cur_df_index,0] = cur_df_index
            argsorted_rad_array[cur_df_index,:] = tuple_array[propagate_sort_by_indexes(cur_df_index,argsorted)]

        for ind,col in enumerate(cols_to_sort_rad):
            all_data[col] = pd.Series(index=argsorted_rad_array[:,0],data=argsorted_rad_array[:,ind+1])
    return all_data