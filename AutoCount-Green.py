from bs4 import BeautifulSoup
from time import sleep
from dateutil.relativedelta import relativedelta
from threading import Timer
from func import *

nowDataList = []
nextDataList = []

def getCarData(bs_html, carNumber):
    car_data = []
    car = bs_html.select_one(f'tr:nth-child({carNumber + 1})').findAll('td')
    for day_data in car:
        car_data.append(day_data.text)
    car_data[0] = ''
    return car_data

def crawling(time):
    if time == 'now':
        year, month = datetime.now().strftime('%Y-%m').split('-')
    elif time == 'next':
        year, month = (datetime.now() + relativedelta(months=1)).strftime('%Y-%m').split('-')
    else:
        raise ValueError('잘못된 args가 들어왔습니다. time args의 Data를 \'now\', \'next\'중으로 설정하시오.')

    url = {
        'now': f'https://greentrip.kr/Reserve/ReserveCalendar.aspx?year={year}&month={month}&CarArea=B',
        'next': f'https://greentrip.kr/Reserve/ReserveCalendar.aspx?year={year}&month={month}&CarArea=B'
    }

    html = requests.get(url[time])
    bs_html = BeautifulSoup(html.content, 'html.parser')

    car1_data = getCarData(bs_html, 1)
    car2_data = getCarData(bs_html, 2)

    dataList = [car1_data, car2_data]
    return dataList

def compare(time):
    if time == 'now':
        dataList = nowDataList
        month = datetime.now().strftime('%m')
    elif time == 'next':
        dataList = nextDataList
        month = (datetime.now() + relativedelta(months=1)).strftime('%m')
    else:
        raise ValueError('잘못된 args가 들어왔습니다. time args의 Data를 \'now\', \'next\'중으로 설정하시오.')

    if dataList[0] != dataList[1]:
        for i in range(len(dataList[0])):
            for j in range(len(dataList[0][i])):
                if dataList[0][i][j] == '' or dataList[1][i][j] == '':
                    continue
                if dataList[0][i][j] != dataList[1][i][j]:
                    postGreenData(f'`{month}월 {j}일`의 `{i + 1}`호차가 `{dataList[0][i][j]}`에서 `{dataList[1][i][j]}` 변경되었습니다.')
                    print(f'{now()} - 당월: {i + 1}호차 {j}일이 {dataList[0][i][j]}에서 {dataList[1][i][j]} 변경되었습니다.')
    del dataList[0]

def functioning():
    postGreenData(f'{now()} - 정상작동중 입니다.')
    print(f'{now()} - 정상작동중 입니다.')
    functioningRepeatTime = 60 * 60 * 24 # 1 = 1sec
    Timer(functioningRepeatTime, functioning).start()

if __name__ == '__main__':
    start = ['----------------------------------------------', f'{now()} - 프로그램이 시작되었습니다.', f'{now()} - {crawlingDelay}초마다 홈페이지에서 값을 불러와 비교합니다.']

    for i in start:
        print(i)
        postGreenData(i)

    functioning()

    nowDataList.append(crawling('now'))
    nextDataList.append(crawling('next'))

    sleep(1)
    while True:
        try:
            nowDataList.append(crawling('now'))
            compare('now')

            nextDataList.append(crawling('next'))
            compare('next')
            sleep(crawlingDelay)
        except Exception as e:
            postGreenData(e)
            print(e)
            sleep(1)