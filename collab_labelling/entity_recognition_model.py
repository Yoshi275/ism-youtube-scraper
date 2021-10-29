# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:24:39 2021

@author: kokil
"""
#https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3#4
##https://cloud.google.com/natural-language/docs/analyzing-entities#language-entities-string-python
import os
import csv
import spacy
import logging
import traceback
# from google.cloud import language_v1
def clean(content):
    content = content.replace('\n','')
    content = content.replace('\t','')
    content = content.replace(',','')
    content = content.replace('\r','')
    return content
# We setup the global variable for GCP service account credentials

# We specify the path to the file we want to load
FOLDER_PATH = "C:/Users/chery/Downloads/ism-youtube-gcp-entity"
INPUT_OUTPUT_FILE_TYPE = ".csv"
INPUT_FILE_NAME = "test_videos"
OUTPUT_FILE_NAME = INPUT_FILE_NAME + "_entities"
INPUT_FILE_PATH = FOLDER_PATH + "/" + INPUT_FILE_NAME + INPUT_OUTPUT_FILE_TYPE
OUTPUT_FILE_PATH = FOLDER_PATH + "/" + OUTPUT_FILE_NAME + INPUT_OUTPUT_FILE_TYPE
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FOLDER_PATH + "/trendingminer-6c690a782ce5.json"
spacy_entity_rec = spacy.load("en_core_web_lg")

## UNUSED
filepath = r'D:/Dropbox/python_workspace/2021/ism-youtube-gcp-entity/full_video_list.csv'

# Instantiate the Google Translation API Client

# entity_client = language_v1.LanguageServiceClient()

 # text_content = 'California is a state.'

 # Available types: PLAIN_TEXT, HTML
# type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
language = "en"
# from google.cloud import language


def analyze_text_entities(index,text):
    # client = language.LanguageServiceClient()
    # text = clean(str(text))
    # document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = spacy_entity_rec(text)
    with open(OUTPUT_FILE_PATH, 'a', encoding='utf-8') as f:
            


        for entity in response.ents:
            namee=entity.text
            label = entity.label_
            # typee=entity.start_char
            # salience=f"{entity.salience:.1%}"
            print(str(index) + '\t' + namee + '\t' + label)
            f.write(str(index) + '\t' + namee + '\t' + label + '\n')
            # print(str(index) + '\t'  + namee + '\t' + typee+ '\t' + salience)
            # f.write(str(index) + '\t'   + namee + '\t' + typee+ '\t' + salience + '\n')
        f.close()
            

    
output = []
print(INPUT_FILE_PATH)
with open(INPUT_FILE_PATH,encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                        print(row)
                        try:
                            index = row[0]
                            title = row[1]
                            #print(title)
                            desc = row[6]
                            #print(desc)
                            text_content = title + " " + desc
                            print(text_content)
                            analyze_text_entities(index,text_content)
#                            f.write(str(index) + '\t' + clean(str(text)) +'\t'  + str(response['attributeScores']['ATTACK_ON_AUTHOR@2']['summaryScore']['value']) +'\t'  + str(response['attributeScores']['UNSUBSTANTIAL@2']['summaryScore']['value']) +'\t'  + str(response['attributeScores']['SEXUALLY_EXPLICIT@2']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['TOXICITY@6']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['LIKELY_TO_REJECT@2']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['INSULT@2']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['ATTACK_ON_COMMENTER@2']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['FLIRTATION@2']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['SEVERE_TOXICITY@2']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['SPAM@1']['summaryScore']['value'])+'\t'  + str(response['attributeScores']['OBSCENE@2']['summaryScore']['value']) +'\t'  + str(response['attributeScores']['PROFANITY@2']['summaryScore']['value']) +'\t'  + str(response['attributeScores']['THREAT@2']['summaryScore']['value']) +'\t'  + str(response['attributeScores']['INFLAMMATORY@2']['summaryScore']['value']) +'\t'  + str(response['attributeScores']['INCOHERENT@2']['summaryScore']['value'])+'\n')
                        except Exception as e:
#                            f.write(str(index) + '\t' + clean(str(text))   + 'NA'+ '\n')
                            print("didnt work")
                            logging.error(traceback.format_exc)
            
