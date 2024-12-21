from airflow_practice.download import download_file

FILES = [
    # 'CRNS0101-05-2020-AK_Aleknagik_1_NNE.txt',
    # 'CRNS0101-05-2020-AK_Bethel_87_WNW.txt',
    "CRNS0101-05-2020-AK_Aleknagik_1_NNE.txt",
    "CRNS0101-05-2020-AK_Cordova_14_ESE.txt",
]
for filename in FILES:
    download_file(filename, data_dir="./data/.raw")
