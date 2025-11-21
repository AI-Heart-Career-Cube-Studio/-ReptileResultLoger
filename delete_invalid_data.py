
def main(data):
    lst = []
    unable_lst = []
    for item in data:
        dict_temp = {}
        url = False
        for j in  (item.get('event_url') ,item.get('apply_url') , item.get('contact').get('email') , item.get('contact').get('phone')):
            if j:
                url = j
                break
        if url:
            dict_temp['url'] = url
            dict_temp['tags'] = item.get('job_categories')
            dict_temp['company_name'] = item.get('publisher')
            for i in item.get('positions'):
                dict_temp['description'] = i.get('responsibilities')
                dict_temp['name'] = i.get('name')
                dict_temp['salary'] = i.get('salary')
                dict_temp['location'] = i.get('location')
                dict_temp['job_type'] = i.get('type')
                dict_temp['education_required'] = i.get('degree')
                lst.append(dict_temp)
        else:
            unable_lst.append(item)
            continue

    return lst, unable_lst
