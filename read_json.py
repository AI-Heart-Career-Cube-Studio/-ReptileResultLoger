import json ,write_in_sql,delete_invalid_data
import sys

def read_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data
def main(file_path):
    data = read_json(file_path)
    lst, unable_lst = delete_invalid_data.main(data)
    write_in_sql.link_to()
    for item in lst:
        write_in_sql.write_json(
                                item.get('name'),
                                " ".join(item.get('description')),
                                item.get('salary'),
                                item.get('location') if type(item.get('location')) == str else " ".join(item.get('location')),
                                item.get('job_type'),
                                item.get('education_required'),
                                " ".join(item.get('tags')),
                                item.get('company_name'),
                                item.get('company_size'),
                                item.get('url'))
    write_in_sql.close_conn()

