""" constant file
"""
COLUMNS_TO_CLEAN = ['medical_history_dia','medical_history_sud',
                    'medical_history_hbp','medical_history_ren',
                    'medical_history_tum','medical_history_anx',
                    'medical_history_mood',
                    'trt_anx', 'trt_con', 'trt_adt', 'trt_ssr',
                    'trt_the', 'trt_oth', 'symptom_1', 'symptom_2', 
                    'symptom_3', 'symptom_4', 'symptom_5']

CATEGORICAL_COLUMNS = [ 'medical_history_dia', 'medical_history_sud',
                        'medical_history_hbp',
       'medical_history_ren', 'medical_history_tum', 'medical_history_anx',
       'medical_history_mood', 'trt_anx', 'trt_con', 'trt_adt', 'trt_ssr',
       'trt_the', 'trt_oth', 'symptom_1', 'symptom_2', 'symptom_3',
       'symptom_4', 'symptom_5', 'cgis_adm', 'cgis_dis',
       'gaf_lv', 'gender', 'race', 'resident_status' ]  

DESCRIPTIONS = {
    'medical_history_dia': 'Diagnosis of diabetes',
    'medical_history_sud': 'Diagnosis of substance use disorder',
    'medical_history_hbp': 'Diagnosis of high blood pressure',
    'medical_history_ren': 'Diagnosis of renal failure',
    'medical_history_tum': 'Diagnosis of solid tumour',
    'medical_history_anx': 'Diagnosis of anxiety disorder',
    'medical_history_mood': 'Diagnosis of other mood disorders',
    'trt_anx': 'Current treatment of anxiolytics',
    'trt_con': 'Current treatment of anticonvulsants',
    'trt_adt': 'Current treatment of antidepressants',
    'trt_ssr': 'Current treatment of SSRI',
    'trt_the': 'Current treatment of psychotherapy',
    'trt_oth': 'Current treatment of other psychiatric medications',
    'symptom_1': 'Current presence of trouble sleeping',
    'symptom_2': 'Current presence of anhedonia',
    'symptom_3': 'Current poor appetite',
    'symptom_4': 'Currently feeling depressed',
    'symptom_5': 'Current presence of suicidal thoughts',
    'cgis_adm': 'Severity at admission',
    'cgis_dis': 'Severity at discharge',
    'gaf_lv': 'Global Assessment of Functioning'
}