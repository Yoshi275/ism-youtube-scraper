import os
import pandas as pd
import spacy
from google.cloud import language

### COMMANDS TO RUN THIS:
### pip install -r requirements.txt
### if using spacy model, run: "python -m spacy download en_core_web_lg"
### python entity_recognition_model.py (ensure input file path is valid)

from enum import Enum
class Model(Enum):
    GOOGLE_MODEL = "google_nlp"
    SPACY_MODEL = "spacy"

ENTITY_RECOGNITION_MODEL = Model.GOOGLE_MODEL     # options: google_nlp, spacy

if (ENTITY_RECOGNITION_MODEL == Model.GOOGLE_MODEL):
    # ensure that containing folder contains a file named gservice_account.json, storing the service account key info. Follow https://cloud.google.com/natural-language/docs/quickstart-client-libraries
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gservice_account.json"
    # language = "en"     # setting the language for the entity recogniser
    client = language.LanguageServiceClient()
elif (ENTITY_RECOGNITION_MODEL == Model.SPACY_MODEL):
    spacy_entity_rec = spacy.load("en_core_web_lg")
isFirstVideoAnalysis = True

FILE_TYPE = ".csv"
INPUT_CSV_FILE_NAME = "test_videos"
INPUT_CSV_FILE_PATH = INPUT_CSV_FILE_NAME + FILE_TYPE
OUTPUT_CSV_FILE_PATH = INPUT_CSV_FILE_NAME + "_entities_new" + FILE_TYPE

print("Generating entity results at {}".format(OUTPUT_CSV_FILE_PATH))

def analyze_text_entities_for_video(video_id, text):
    global isFirstVideoAnalysis
    entities_df = pd.DataFrame(columns=['VideoID', 'Name', 'Type', 'Salience'])     # global dataframe to store all entity models wuhu
    if (ENTITY_RECOGNITION_MODEL == Model.GOOGLE_MODEL):
        document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
        response = client.analyze_entities(document=document)
        for entity in response.entities:
            new_row = {
                'VideoID': video_id,
                'Name': entity.name,
                'Type': entity.type_.name,
                'Salience': f"{entity.salience:.1%}"
            }
            print(new_row)
            entities_df = entities_df.append(new_row, ignore_index=True)
    elif (ENTITY_RECOGNITION_MODEL == Model.SPACY_MODEL):
        response = spacy_entity_rec(text)
        for entity in response.ents:
            new_row = {
                'VideoID': video_id,
                'Name': entity.text,
                'Type': entity.label_
            }
            print(new_row)
            entities_df = entities_df.append(new_row, ignore_index=True)
    if isFirstVideoAnalysis:
        entities_df.to_csv(OUTPUT_CSV_FILE_PATH, index=False, encoding='utf-8-sig', mode='a')
        isFirstVideoAnalysis = False
    else:
        entities_df.to_csv(OUTPUT_CSV_FILE_PATH, index=False, header=False, encoding='utf-8-sig', mode='a')
    print("Entities found and added for video ID {}".format(video_id))

def run_entity_recogniser_on_csv():
    SELECTED_COLS = ["Title", "Description"]
    VIDEO_ID_COL_NAME = "VideoID"
    
    print("Selected Columns to Run ER Model on: {}".format(",".join(SELECTED_COLS)))

    df = pd.read_csv(INPUT_CSV_FILE_PATH)
    for index, row in df.iterrows():
        selected_text = ""
        for column in SELECTED_COLS:
            new_text = df.loc[index, column]
            if type(new_text) == str:
                selected_text += " " + new_text
        selected_video_id = df.loc[index, VIDEO_ID_COL_NAME]
        try:
            analyze_text_entities_for_video(selected_video_id, selected_text)
        except Exception as e:
            print("Entity recognition failed for video {}".format(selected_video_id))
            print(e)

if __name__ == "__main__":
    run_entity_recogniser_on_csv()