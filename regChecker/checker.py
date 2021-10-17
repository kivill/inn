import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote


def check_dobro_mail(name):
    response = requests.get(f"https://dobro.mail.ru/funds/search/?query={name}") 
    soup = BeautifulSoup(response.content, 'html.parser') 
    name = name.lower()

    found = False
    for span in soup.find_all('span', class_='link__text'):
        span_text = span.get_text().lower()
        if re.search(rf'{name}', span_text):
            found = True
    
    return found


def check_nuzhnapomosh(name):
    params = {
        'np_name': name,
    }
    response = requests.post(f"https://nuzhnapomosh.ru/wp-content/plugins/nuzhnapomosh/funds.php", data=params) 
    soup = BeautifulSoup(response.content, 'html.parser') 
    name = name.lower()

    found = False
    for h4 in soup.find_all('h4', class_='np-card__title'):
        h4_text = h4.get_text().lower()
        if re.search(rf'{name}', h4_text):
            found = True
    
    return found


def check_together(name):
    response = requests.get(f"https://wse-wmeste.ru/?s={name}") 
    soup = BeautifulSoup(response.content, 'html.parser') 
    name = name.lower()

    found = False
    for a in soup.find_all('a'):
        a_title = a.get('title')
        if a_title is not None:
            a_title = a_title.lower()
            if re.search(rf'{name}', a_title):
                found = True
    return found


def check_minjust(name):
    payload = f'filter_regions_text=%A0&selected_pdg_items=&pdg_pdg_sort_col=full_name&pdg_pdg_sort_ord=ASC&pdg_pdg_record_count=18&hd_frame_id=Unknown&ctl02_dummy_calendar_past_date=False&__VIEWSTATE=%2FwEPDwULLTEzNzYyNTUxMTkPZBYCZg9kFgICAQ9kFgQCBQ9kFgICAQ8QZA8WJmYCAQICAgMCBAIFAgYCBwIIAgkCCgILAgwCDQIOAg8CEAIRAhICEwIUAhUCFgIXAhgCGQIaAhsCHAIdAh4CHwIgAiECIgIjAiQCJRYmEAUK0LvRjtCx0LDRj2VnEAVI0JDQstGC0L7QvdC%2B0LzQvdCw0Y8g0L3QtdC60L7QvNC80LXRgNGH0LXRgdC60LDRjyDQvtGA0LPQsNC90LjQt9Cw0YbQuNGPBQQxNDA1ZxAFO9CQ0LTQstC%2B0LrQsNGC0YHQutC40LUg0L%2FQsNC70LDRgtGLINGB0YPQsdGK0LXQutGC0L7QsiDQoNCkBQQxNDE4ZxAFH9CQ0LTQstC%2B0LrQsNGC0YHQutC%2B0LUg0LHRjtGA0L4FBDE0MjRnEAVV0JDRgdGB0L7RhtC40LDRhtC40Y8g0LrRgNC10YHRgtGM0Y%2FQvdGB0LrQuNGFICjRhNC10YDQvNC10YDRgdC60LjRhSkg0YXQvtC30Y%2FQudGB0YLQsgUEMTQwN2cQBULQkNGB0YHQvtGG0LjQsNGG0LjRjyDRjdC60L7QvdC%2B0LzQuNGH0LXRgdC60L7Qs9C%2BINGA0LDQt9Cy0LjRgtC40Y8FBDE0MTFnEAUz0JPQvtGB0YPQtNCw0YDRgdGC0LLQtdC90L3QsNGPINC60L7RgNC%2F0L7RgNCw0YbQuNGPBQQxNDAyZxAFTNCT0L7RgdGD0LTQsNGA0YHRgtCy0LXQvdC90L4t0L7QsdGJ0LXRgdGC0LLQtdC90L3QvtC1INC%2B0LHRitC10LTQuNC90LXQvdC40LUFBDEyMDhnEAU80JjQvdGL0LUg0L3QtdC60L7QvNC80LXRgNGH0LXRgdC60LjQtSDQvtGA0LPQsNC90LjQt9Cw0YbQuNC4BQQxNDE2ZxAFH9Ca0LDQt9Cw0YfRjNC1INC%2B0LHRidC10YHRgtCy0L4FBDE1MDFnEAUj0JrQvtC70LvQtdCz0LjRjyDQsNC00LLQvtC60LDRgtC%2B0LIFBDE0MTdnEAU%2B0J3QsNGG0LjQvtC90LDQu9GM0L3Qvi3QutGD0LvRjNGC0YPRgNC90LDRjyDQsNCy0YLQvtC90L7QvNC40Y8FBDEyMTBnEAVA0J3QtdCz0L7RgdGD0LTQsNGA0YHRgtCy0LXQvdC90YvQuSDQv9C10L3RgdC40L7QvdC90YvQuSDRhNC%2B0L3QtAUEMTQyM2cQBSXQndC10LrQvtC80LzQtdGA0YfQtdGB0LrQuNC5INGE0L7QvdC0BQQxNDAxZxAFM9Cd0LXQutC%2B0LzQvNC10YDRh9C10YHQutC%2B0LUg0L%2FQsNGA0YLQvdC10YDRgdGC0LLQvgUEMTQwM2cQBSXQndC%2B0YLQsNGA0LjQsNC70YzQvdCw0Y8g0L%2FQsNC70LDRgtCwBQQxNDEzZxAFL9Ce0LHRidC10YHRgtCy0LXQvdC90LDRjyDQvtGA0LPQsNC90LjQt9Cw0YbQuNGPBQQxMjAxZxAFZdCe0LHRidC10YHRgtCy0LXQvdC90L4t0LPQvtGB0YPQtNCw0YDRgdGC0LLQtdC90L3QvtC1INC%2B0LHRidC10YHRgtCy0LXQvdC90L7QtSDQvtCx0YrQtdC00LjQvdC10L3QuNC1BQQxMjA5ZxAFKdCe0LHRidC10YHRgtCy0LXQvdC90L7QtSDQtNCy0LjQttC10L3QuNC1BQQxMjAyZxAFLdCe0LHRidC10YHRgtCy0LXQvdC90L7QtSDRg9GH0YDQtdC20LTQtdC90LjQtQUEMTIwNGcQBSHQntCx0YnQtdGB0YLQstC10L3QvdGL0Lkg0YTQvtC90LQFBDEyMDNnEAU20J7QsdGJ0LjQvdCwINC80LDQu9C%2B0YfQuNGB0LvQtdC90L3Ri9GFINC90LDRgNC%2B0LTQvtCyBQQxNDIyZxAFMdCe0LHRitC10LTQuNC90LXQvdC40LUg0YDQsNCx0L7RgtC%2B0LTQsNGC0LXQu9C10LkFBDE0MTJnEAUp0J7QsdGK0LXQtNC40L3QtdC90LjRjyDQsNC00LLQvtC60LDRgtC%2B0LIFBDE0MTRnEAVV0J7QsdGK0LXQtNC40L3QtdC90LjRjyAo0YHQvtGO0LcsINCw0YHRgdC%2B0YbQuNCw0YbQuNGPKSDRjtGA0LjQtNC40YfQtdGB0LrQuNGFINC70LjRhgUEMTQwNmcQBUTQntGA0LPQsNC9INC%2B0LHRidC10YHRgtCy0LXQvdC90L7QuSDRgdCw0LzQvtC00LXRj9GC0LXQu9GM0L3QvtGB0YLQuAUEMTIwNWcQBSXQn9C%2B0LvQuNGC0LjRh9C10YHQutCw0Y8g0L%2FQsNGA0YLQuNGPBQQxMjA2ZxAFKdCf0YDQvtGE0LXRgdGB0LjQvtC90LDQu9GM0L3Ri9C5INGB0L7RjtC3BQQxMjExZxAFLdCg0LXQu9C40LPQuNC%2B0LfQvdCw0Y8g0L7RgNCz0LDQvdC40LfQsNGG0LjRjwUEMTEwMWcQBYgB0KHQsNC00L7QstC%2B0LTRh9C10YHQutC40LUsINC%2B0LPQvtGA0L7QtNC90LjRh9C10YHQutC40LUsINC00LDRh9C90YvQtSDQuCDQuNC90YvQtSDQvdC10LrQvtC80LzQtdGA0YfQtdGB0LrQuNC1INGC0L7QstCw0YDQuNGJ0LXRgdGC0LLQsAUEMTQxMGcQBXrQodCw0LTQvtCy0L7QtNGH0LXRgdC60L7QtSwg0L7Qs9C%2B0YDQvtC00L3QuNGH0LXRgdC60L7QtSwg0LTQsNGH0L3QvtC1INC90LXQutC%2B0LzQvNC10YDRh9C10YHQutC%2B0LUg0L7QsdGK0LXQtNC40L3QtdC90LjQtQUEMTQxOWcQBXrQodCw0LTQvtCy0L7QtNGH0LXRgdC60L7QtSwg0L7Qs9C%2B0YDQvtC00L3QuNGH0LXRgdC60L7QtSwg0LTQsNGH0L3QvtC1INC90LXQutC%2B0LzQvNC10YDRh9C10YHQutC%2B0LUg0L%2FQsNGA0YLQvdC10YDRgdGC0LLQvgUEMTQyMGcQBTzQodC%2B0LLQtdGCINC80YPQvdC40YbQuNC%2F0LDQu9GM0L3Ri9GFINC%2B0LHRgNCw0LfQvtCy0LDQvdC40LkFBDE0MjFnEAVP0KHQvtGO0LcgKNCw0YHRgdC%2B0YbQuNCw0YbQuNGPKSDQvtCx0YnQtdGB0YLQstC10L3QvdGL0YUg0L7QsdGK0LXQtNC40L3QtdC90LjQuQUEMTIwN2cQBVTQotC10YDRgNC40YLQvtGA0LjQsNC70YzQvdC%2B0LUg0L7QsdGJ0LXRgdGC0LLQtdC90L3QvtC1INGB0LDQvNC%2B0YPQv9GA0LDQstC70LXQvdC40LUFBDE0MDhnEAU%2B0KLQvtCy0LDRgNC40YnQtdGB0YLQstC%2BINGB0L7QsdGB0YLQstC10L3QvdC40LrQvtCyINC20LjQu9GM0Y8FBDE0MDlnEAU00KLQvtGA0LPQvtCy0L4t0L%2FRgNC%2B0LzRi9GI0LvQtdC90L3QsNGPINC%2F0LDQu9Cw0YLQsAUEMTIxMmcQBRTQo9GH0YDQtdC20LTQtdC90LjQtQUEMTQwNGdkZAIGD2QWAgIBDw8WDB4IU3RhcnRQb3MoKVlTeXN0ZW0uSW50NjQsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OQEwHgdTb3J0Q29sBQlmdWxsX25hbWUeB1NvcnRPcmQFA0FTQx4HZGJtc19pZAspW1JMLkRCV3JhcHBlci5EYm1zSWQsIERhdGFVdGlsaXRpZXMsIFZlcnNpb249MS4wLjEwMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGwCHhFjb25uZWN0aW9uX3N0cmluZwV2VXNlciBJRD1OT05DT01NRVJDSUFMX0RBVEEwMURCO3Bhc3N3b3JkPU5DT19EQVRBMDFEQjtEYXRhIFNvdXJjZT1PUkFEQjAxO1BlcnNpc3QgU2VjdXJpdHkgSW5mbz1GYWxzZTtNYXggUG9vbCBTaXplPTMwMB4FcXVlcnkFqAogU0VMRUNUIGQuaWQsIAkJQ0FTRSAgCQkJV0hFTiBkLnR5cGUgPSAxIFRIRU4gJ9Cd0LXQutC%2B0LzQvNC10YDRh9C10YHQutC40LUg0L7RgNCz0LDQvdC40LfQsNGG0LjQuCcgCQkJV0hFTiBkLnR5cGUgPSAyIFRIRU4gJ9Cg0LXQu9C40LPQuNC%2B0LfQvdGL0LUg0L7RgNCz0LDQvdC40LfQsNGG0LjQuCcgCQkJV0hFTiBkLnR5cGUgPSAzIFRIRU4gJ9Ca0LDQt9Cw0YfRjNC4INC%2B0LHRidC10YHRgtCy0LAnIAkJCVdIRU4gZC50eXBlID0gNCBUSEVOICfQmNC90L7RgdGC0YDQsNC90L3Ri9C1INC90LXQutC%2B0LzQvNC10YDRh9C10YHQutC40LUg0J3Qn9CeJyAJCQlXSEVOIGQudHlwZSA9IDUgVEhFTiAn0JrQsNC30LDRh9GM0Lgg0L7QsdGK0LXQtNC40L3QtdC90LjRjycgCQkJV0hFTiBkLnR5cGUgPSA2IFRIRU4gJ9Ce0LHRidC10YHRgtCy0LXQvdC90YvQtSDQvtCx0YrQtdC00LjQvdC10L3QuNGPJyAJCUVORCBBUyByZWVzdHIsICAgIAkJZC5yZWdfbnVtLCBkLmZ1bGxfbmFtZSwgZC5vZ3JuLCBkLmVncnVsX2RhdGUsIGQuYWRkcmVzcywgdi5kZXNjcmlwdGlvbiBBUyBvcGYsIGMuZGVzY3JpcHRpb24gQVMgcmVnaW9uLCAJCUNBU0UgCQkJV0hFTiBkLnN0YXR1c19mbGFnID0gMiBUSEVOICfQl9Cw0YDQtdCz0LjRgdGC0YDQuC08YnI%2B0YDQvtCy0LDQvdCwJyAJCQlXSEVOIGQuc3RhdHVzX2ZsYWcgPSAzIFRIRU4gJ9CY0YHQutC70Y4tPGJyPtGH0LXQvdCwJyAJCUVORCBBUyBzdGF0dXMsIAkJMC8qKFNFTEVDVCBNQVgoZGVwYXJ0X2lkKSBGUk9NIHJfc3ltYm9sb2d5IHJzIElOTkVSIEpPSU4gcl9zeW1ib2xvZ3lfc3RhdGVtZW50IHN0IE9OIHJzLmlkPXN0LnN5bWJvbG9neV9pZCBBTkQgc3QuZXZlbnRfdHlwZT0yMzAwMiBXSEVSRSBycy5kZXBhcnRfaWQ9ZC5pZCkqLyBBUyBsb2dvLCAJCWQuc3RhdGVfcmVnaXN0cmF0aW9uX251bSwgZC5yZWdpc3RyYXRpb25fZGF0ZSBBUyBzdGF0ZV9yZWdpc3RyYXRpb25fZGF0ZSBGUk9NIHJfZGVwYXJ0bWVudGFsIGQgCUxFRlQgT1VURVIgSk9JTiBjbGFzc2lmaWNhdG9yX3ZhbHVlIGMgT04gZC5zdWJqZWN0ID0gYy5pZCAJTEVGVCBPVVRFUiBKT0lOIHZyX2NsYXNzaWZpY2F0b3JfdmFsdWUgdiBPTiBkLm9yZ19mb3JtID0gdi5pZCBXSEVSRSBkLnR5cGUgTk9UIElOKDcsIDgsIDkpIEFORCBkLnN0YXR1c19mbGFnIElOKDIsIDMpIEFORCBOT1QoZC50eXBlPTQgQU5EIGQuc3ViZGl2aXNpb25fdHlwZSBJTig0NjA1LCA0NjA2KSkgQU5EIFVQUEVSKGQuZnVsbF9uYW1lKSBMSUtFIFVQUEVSKCcl0KHQvtGE0LjRjyUnKSBBTkQgZC5vcmdfZm9ybT0xNDAxIEFORCBkLnN0YXR1c19mbGFnPTJkFgQCBQ8PFgIeB1Zpc2libGVoZGQCBg8PFgIfBmhkZGThtPxi4qvdO2fEWgdOcHibUh3nXirKlnnKnw8B7AdYeQ%3D%3D&__VIEWSTATEGENERATOR=9AA81B59&__EVENTTARGET=&__EVENTARGUMENT=&mode=refresh&affiliate=&filter_region_selected=&filter_oktmo_selected=&err_msg= \
    &filter_org_name={name.encode("utf-8")} \
    &filter_opf=1401&filter_status=2&filter_oktmo_pattern=%C2%E2%E5%E4%E8%F2%E5+%EA%EE%E4+%E8%EB%E8+%ED%E0%E7%E2%E0%ED%E8%E5+%EC%F3%ED%E8%F6%E8%EF%E0%EB%FC%ED%EE%E3%EE+%EE%E1%F0%E0%E7%EE%E2%E0%ED%E8%FF&filter_regions=%ED%E5+%E2%FB%E1%F0%E0%ED&filter_reg_num=&filter_ogrn='


    headers = {
        'Host': 'unro.minjust.ru',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://unro.minjust.ru',
        'Referer': 'http://unro.minjust.ru/NKOs.aspx',
    }

    response = requests.post(f"http://unro.minjust.ru/NKOs.aspx", 
        data=payload,
        headers=headers, verify=False)

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', id="pdg")

    name = name.lower()

    found = False

    return found


def check_nalog(name):
    headers = {
        'Host': 'egrul.nalog.ru',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://egrul.nalog.ru',
        'Referer': 'https://egrul.nalog.ru/index.html',
    }

    data = {
        'query': name
    }

    response = requests.post(f"https://egrul.nalog.ru/", data=data, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser') 
    name = name.lower()

    found = False

    '''
    for a in soup.find_all('a', class_='op-excerpt'):
        a_text = a.get('title').lower()
        print(a_text)
        if re.search(rf'{name}', a_text) and re.search(r'благотворительный фонд', a_text):
            found = True
    '''

    return found


def main(name):
    check_results = {
        'dobro_mail': False,
        'nuzhnapomosh': False,
        'together': False,
        #'minjust': False,
        #'nalog': False,
    }

    check_results['dobro_mail'] = check_dobro_mail(name)
    check_results['nuzhnapomosh'] = check_nuzhnapomosh(name)
    check_results['together'] = check_together(name)

    return check_results
    #check_results['minjust'] = check_minjust(name)
    #check_results['nalog'] = check_nalog(name)