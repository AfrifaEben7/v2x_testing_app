import pandas as pd

def calculate_differences():
    # read the csv file into a pandas dataframe
    df = pd.read_csv('mylog.csv')

    # create two separate dataframes based on ObjId
    df_obj0 = df[df['ObjId'] == 0]
    df_obj1 = df[df['ObjId'] == 1]

    time_col = df.pop('Time')
    time_col = time_col.drop_duplicates()
    time_col.reset_index(drop=True)

    df_0 = df_obj0.drop(['ObjId'], axis=1)
    df_1 = df_obj1.drop(['ObjId'], axis=1)


    df_0 = df_0.reset_index(drop=True)
    df_1 = df_1.reset_index(drop=True)

    # create an empty dataframe to store the differences
    diff_df = pd.DataFrame(columns=["Time",'diff_s', 'diff_x', 'diff_y', 'diff_heading', 'diff_speed'])

    # iterate over the rows of the dataframes and calculate the differences
    for idx, row in df_0.iterrows():
        diff_s = abs(row['s'] - df_1.loc[idx, 's'])
        diff_x = abs(row['x'] - df_1.loc[idx, 'x'])
        diff_y = abs(row['y'] - df_1.loc[idx, 'y'])
        diff_heading = abs(row['heading'] - df_1.loc[idx, 'heading'])
        diff_speed = abs(row['speed'] - df_1.loc[idx, 'speed'])
        time = df_0["Time"][idx]

        # add the differences to the diff_df dataframe
        diff_df.loc[idx] = [time, diff_s, diff_x, diff_y, diff_heading, diff_speed]

    deed = diff_df.describe()
    deed.to_csv('summary.csv', index=False)
    # Write the diff_df dataframe to a CSV file
    diff_df.to_csv('diff_df.csv', index=False)
