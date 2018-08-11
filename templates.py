doc_list_url = "https://bsr.sudrf.ru/bigs/s.action"


request_content_templ = """
{
    "request":
    {
        "type": "MULTIQUERY",
        "multiqueryRequest":
        {
            "queryRequests": [
            {
                "type": "Q",
                "request": "",
                "operator": "AND",
                "queryRequestRole": "CATEGORIES"
            }]
        },
        "sorts": [
        {
            "field": "score",
            "order": "desc"
        }],
        "simpleSearchFieldsBundle": "default00",
        "start": 0,
        "rows": 1000,
        "uid": "",
        "noOrpho": false,
        "facet":
        {
            "field": ["type"]
        },
        "facetLimit": 21,
        "additionalFields": ["court_document_documentype1", "court_case_entry_date", "court_case_result_date", "court_subject_rf", "court_name_court", "court_document_law_article", "court_case_result", "case_user_document_type", "case_user_doc_entry_date", "case_user_doc_result_date", "case_doc_subject_rf", "case_user_doc_court", "case_document_category_article", "case_user_doc_result", "case_user_entry_date", "m_case_user_type", "m_case_user_sub_type", "ora_main_law_article"],
        "hlFragSize": 1000,
        "groupLimit": 3,
        "woBoost": false
    },
    "doNotSaveHistory": false
}
"""

request_filter_templ = """
{
    "mode": "EXTENDED",
    "typeRequests": [{
        "fieldRequests": [{
            "name": "case_user_doc_entry_date",
            "operator": "B",
            "query": "2018-08-01T00:00:00",
            "sQuery": "2018-08-10T00:00:00"
        }, {
            "name": "case_document_category_article_cat",
            "operator": "SEW",
            "query": "Статья 20.3 Часть 1"
        }],
        "mode": "AND",
        "name": "common",
        "typesMode": "AND"
    }]
}
"""

request_doc_details_templ = """
{
    "request": {
        "start": 0,
        "rows": 10,
        "uid": "",
        "type": "MULTIQUERY",
        "multiqueryRequest": {
            "queryRequests": [{
                "type": "Q",
                "request": "",
                "operator": "AND",
                "queryRequestRole": "CATEGORIES"
            }]
        },
        "sorts": [{
            "field": "score",
            "order": "desc"
        }],
        "simpleSearchFieldsBundle": "default00",
        "noOrpho": false,
        "groupLimit": 3,
        "woBoost": false,
        "facet": {
            "field": ["type"]
        },
        "facetLimit": 21,
        "additionalFields": ["court_document_documentype1", "court_case_entry_date", "court_case_result_date", "court_subject_rf", "court_name_court", "court_document_law_article", "court_case_result", "case_user_document_type", "case_user_doc_entry_date", "case_user_doc_result_date", "case_doc_subject_rf", "case_user_doc_court", "case_document_category_article", "case_user_doc_result", "case_user_entry_date", "m_case_user_type", "m_case_user_sub_type", "ora_main_law_article"],
        "hlFragSize": 1000,
        "id": "13c2b9805614b159fa023869cc80a807",
        "shards": ["Все дела"],
        "hlColors": ["searchHL0"]
    },
    "saveBoostQuery": true
}
"""

doc_details_url = "https://bsr.sudrf.ru/bigs/showDocument.action"
