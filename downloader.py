import requests
from datetime import datetime
import json
from templates import *
from pprint import pprint
from calendar import monthrange
import csv

all_fields_dict = {
    'case_court_type_cat': 'Уровень суда',
    'case_doc_subject_number': 'Код субъекта РФ',
    'case_common_doc_court': 'Наименование суда',
    'case_doc_district_rf': 'Округ РФ',
    'case_document_articles': 'Статьи закона',
    'case_common_event_result': 'Результат',
    'case_common_doc_result_date': 'Дата решения',
    'case_user_doc_result_date': 'Дата решения',
    'case_common_doc_number_rewrite': 'Номер дела',
    'case_common_parts_m2_search': 'Стороны по делу',
    'case_common_doc_entry_date': 'Дата поступления',
    'case_common_event_date': 'Дата события',
    'u_case_user_article': 'Статья УК РФ',
    'case_id': 'Идентификатор дела',
    'case_common_event_m2': 'Движение дела',
    'case_user_judge': 'Судья',
    'case_document_category_article': 'Статья или категория',
    'case_user_doc_entry_date': 'Дата поступления',
    'u_common_case_defendant_m_search': 'Лица',
    'case_common_event_name': 'Событие',
    'case_user_type': 'Тип дела',
    'case_doc_load_date': 'Дата загрузки дела',
    'case_user_doc_number': 'Номер дела (материала)',
    'name': 'Название',
    'case_doc_subject_rf': 'Субъект РФ',
    'case_doc_subject_rf_code': 'Субъект РФ (с кодом)',
    'case_user_doc_court': 'Наименование суда',
    'case_id_region': 'Идентификатор дела в субъекте',
    'case_common_entry_date': 'Дата поступления',
    'case_common_doc_result': 'Результат',
    'case_court_type': 'Уровень суда',
    'case_user_doc_number_rewrite': 'Номер дела',
    'case_common_parts_name': 'Сторона по делу',
    'case_doc_source': 'Источник',
    'case_doc_kind': 'Вид судопроизводства',
    'case_common_judge': 'Судья',
    'case_doc_vnkod': 'Код суда',
    'case_regbasenum': 'Уровень по субъекту',
    'case_common_parts_type': 'Вид участника производства',
    'timestamp': 'Дата индексирования',
    'u_common_case_defendant_m': 'Лица',
    'case_doc_kind_prefix': 'Префикс судопроизводства',
    'case_short_number': 'Порядковый номер дела',
    'u_common_case_defendant_name': 'ФИО',
    'case_doc_kind_short': 'Вид судопроизводства (короткое)',
    'case_common_type': 'Тип дела',
    'u_case_common_article': 'Статья УК РФ',
    'case_year': 'Год регистрации дела',
    'case_common_doc_number': 'Номер дела (материала)',
    'case_common_event_m2_search': 'Движение дела',
    'case_doc_instance': 'Инстанция',
    'case_user_entry_date': 'Дата поступления',
    'case_user_doc_result': 'Результат',
    'case_common_court_i': 'Передано из',
    'u_case_id': 'Идентификатор уголовного дела',
    'u2_33_case_court_i': 'Районныйсуд',
    'case_user_court_i': 'Передано из',
    'case_user_document_num': 'Дела с текстом судебного акта',
    'case_common_document_num': 'Количество судебных актов',
    'case_document_num_build': 'num_build',
    'case_document_publ_date': 'Дата публикации',
    'case_document_load_date': 'Дата загрузки судебного акта',
    'case_document_text': 'Текст документа',
    'case_user_document_text_tag': 'Текст документа',
    'case_document_id': 'Идентификатор судебного акта',
    'case_document_text3': 'Текст документа',
    'case_document_text2': 'Текст документа',
    'case_document_text4': 'Текст документа',
    'case_common_document_type': 'Тип документа',
    'case_user_document_type': 'Тип документа',
    'case_document_result_date': 'Дата судебного акта',
    'case_document_types': 'Типы документов',
    'case_common_doc_validity_date': 'Дата вступления в силу',
    'txt_exist': 'Наличие текста',
    'case_doc_source_table': 'Источник (префикс таблиц)',
    'case_user_doc_validity_date': 'Дата вступления в силу',
    'court_deside': 'Дела с решением',
    'case_common_document_article': 'Статья закона',
    'u33_case_writ_type': 'Вид обжалуемого судебного акта в порядке надзора',
    'u33_case_case_number_1': 'Номер производства по делу в суде 1-ой инстанции',
    'u33_case_vsrfid_notpost': 'Из Верховного суда',
    'case_document_result': 'Решение',
    'case_document_results': 'Решения',
    'case_common_parts_law_article': 'Статья КоАП, другой закон',
    'adm_case_user_name': 'Привлекаемое лицо',
    'adm_case_common_name': 'Привлекаемое лицо',
    'case_common_parts_breaking_law': 'Вид правонарушения',
    'adm_case_pr_number': 'Номер протокола (постановления) об АП',
    'adm_case_result': 'Результат рассмотрения (подготовки к рассмотрению) дела',
    'adm_case_id': 'Идентификатор дела об АП'
}
disabled_fields = [
    'case_court_type_cat',
    'case_user_document_text_tag',
    'case_document_text',
    'case_document_text3',
    'case_document_text2',
    'case_document_text4',
    'case_common_parts_m2_search',
    'case_common_event_m2',
    'u_common_case_defendant_m_search',
    'case_doc_subject_rf_code',
    'case_id_region',
    'case_court_type',
    'case_doc_source',
    'case_doc_vnkod',
    'case_regbasenum',
    'u_common_case_defendant_m',
    'case_common_event_m2_search',
    'case_user_type',
    'case_user_doc_number',
    'u33_case_vsrfid_notpost',
    'case_common_type',
    'case_common_document_num',
    'case_doc_subject_number',
    'adm_case_id',
    'case_document_id',
    'case_id',
    'case_common_parts_type',
    'case_short_number',
    'u_case_id',
    'case_document_num_build',
    'case_doc_kind_prefix',
    'adm_case_result',
    'case_common_parts_breaking_law',
    'u2_33_case_court_i',
    'u33_case_writ_type'
]
#case_document_articles
#case_common_doc_result

def createDocListFilter(date_from, date_to, paragraph):
    filt = json.loads(request_filter_templ)
    filt['typeRequests'][0]['fieldRequests'][0]['query'] = date_from.strftime("%Y-%m-%dT00:00:00")
    filt['typeRequests'][0]['fieldRequests'][0]['sQuery'] = date_to.strftime("%Y-%m-%dT00:00:00")
    filt['typeRequests'][0]['fieldRequests'][1]['query'] = paragraph
    return json.dumps(filt)


def getDocList(date_from, date_to, paragraph):
    request_list = json.loads(request_content_templ)
    request_list['request']['multiqueryRequest']['queryRequests'][0]['request'] = createDocListFilter(date_from, date_to, paragraph)
    return requests.post(doc_list_url, json=request_list).json()

totalNamesDict = dict()
def getDocDetail(id):
    global totalNamesDict
    request_doc = json.loads(request_doc_details_templ)
    request_doc["request"]["id"] = id
    ret = requests.post(doc_details_url, json=request_doc).json()['document']
    # print(ret['document']['id'])
    doc = {"type": ret['type'], "id": ret['id']}
    doc = dict()
    for f in ret['fields']:
        if f['name'] not in totalNamesDict:
            # print(f['name'], f['comment'])
            totalNamesDict[f['name']] = f['comment']
        if f['name'] in disabled_fields:
            continue
        name = f['name']
        if f['value']:
            doc[name] = f['value'].replace('"', "'")
        elif f['dateValue']:
            doc[name] = datetime.strptime(f['dateValue'], "%Y-%m-%dT%H:%M:%S")
        elif f['doubleValue']:
            doc[name] = f['doubleValue']
        elif f['longValue']:
            doc[name] = f['longValue']
        elif f['linkValue']:
            doc[name] = f['linkValue']
    return doc

paragraphs = [
    "Статья 282",
    # "Статья 280",
    "Статья 20.3 Часть",
    "Статья 20.2 Часть",
    # "Статья 148 Часть 1",
    # "Статья 6.21",
    # "Статья 20.29",
]


csv_fields = list(set(all_fields_dict.keys()) - set(disabled_fields))
csvfile = open('result.csv', 'w', newline='')
csvwriter = csv.DictWriter(csvfile, escapechar='$', quoting=csv.QUOTE_MINIMAL, strict=True, 
        fieldnames=csv_fields, extrasaction='ignore')
csvwriter.writeheader()
cnt = 0
for paragraph in paragraphs:
    for year in range(2017, 2019):
        for month in range(1, 13):
            _, maxday = monthrange(year, month)
            data = getDocList(datetime(year, month, 1), datetime(year, month, maxday), paragraph)
            print(f"{paragraph}, {year}.{month}: {len(data['searchResult']['documents'])}")
            documents = data['searchResult']['documents']
            for d in documents:
                doc = getDocDetail(d["id"])
                csvwriter.writerow(doc)
                cnt += 1
                print('     ', cnt)
csvfile.close()
