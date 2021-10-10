from video_info import *
import numpy as np
import pandas as pd
from decouple import config
import datetime   

# input: csv table with first col "VideoID" filled
# output: csv table with second col "ViewCount" filled
def fill_result_statistics(developer_key, csv_input_file, csv_output_file):
    VIDEOS_BATCH_SIZE = 39
    VIDEO_ID_COL_NAME = "VideoID"
    VIEWCOUNT_COL_NAME = "ViewCount"

    df = pd.read_csv(csv_input_file)
    df[VIEWCOUNT_COL_NAME] = df[VIDEO_ID_COL_NAME].astype(object)
    print(df)
    video_ids = []

    for index, row in df.iterrows():
        video_id_str = df.loc[index, VIDEO_ID_COL_NAME]
        if video_id_str[0] == "=":  # because Youtube gives us IDs containing "=" at the front, but this is not actually recognised as a symbol in its ID querying
            video_ids.append(video_id_str[1::])
        else:
            video_ids.append(video_id_str)
        if (index != 0) and (index % VIDEOS_BATCH_SIZE == 0):
            print(df.loc[index, VIDEO_ID_COL_NAME])
            print(video_ids)
            viewcounts = video_ids_to_viewcount(developer_key, video_ids, VIDEOS_BATCH_SIZE)
            for video_id_cols in range(index - VIDEOS_BATCH_SIZE + 1, index + 1):
                video_id_str = df.at[video_id_cols, VIDEO_ID_COL_NAME]
                if video_id_str[0] == "=":  # see above explanation
                    if video_id_str[1::] in viewcounts.keys():  # catch errors whereby dict key does not exist, so skip
                        df.at[video_id_cols, VIEWCOUNT_COL_NAME] = viewcounts[video_id_str[1::]]
                else:
                    if video_id_str in viewcounts.keys():
                        df.at[video_id_cols, VIEWCOUNT_COL_NAME] = viewcounts[video_id_str]
                video_ids = []
    df.to_csv(csv_output_file, index=False)
    return

# input: csv table with col "DateUploaded" filled
# output: csv table with second col "SamplingCategory" filled
def fill_date_aggregation(csv_input_file, csv_output_file):
    DATE_UPLOADED_COL_NAME = "DateUploaded"
    DATE_AGGREGATOR_COL_NAME = "SamplingCategory"

    df = pd.read_csv(csv_input_file)
    df[DATE_AGGREGATOR_COL_NAME] = df[DATE_UPLOADED_COL_NAME].astype(object)
    print(df)

    for index, row in df.iterrows():
        date_uploaded_str = df.loc[index, DATE_UPLOADED_COL_NAME][:-1]
        date_uploaded_dt = datetime.datetime.fromisoformat(date_uploaded_str)
        new_date_uploaded_str = date_uploaded_dt.strftime("%b_%Y")
        df.at[index, DATE_AGGREGATOR_COL_NAME] = new_date_uploaded_str
        if (index % 1000 == 0):
            print("{} completed".format(index))
    df.to_csv(csv_output_file, index=False)
    return

def main():
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return
    CSV_INPUT_FILE = "video_info_test.csv"
    CSV_OUTPUT_FILE = "video_output_test.csv"
    fill_result_statistics(DEVELOPER_KEY, CSV_INPUT_FILE, CSV_OUTPUT_FILE)
    # fill_date_aggregation(CSV_INPUT_FILE, CSV_OUTPUT_FILE)

if __name__ == "__main__":
    main()