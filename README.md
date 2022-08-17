# AutoCount-Green
초록여행 예약 현황 변경 사항 Slack 알림 봇

## Tech
* Python 3.8.9
* BeautifulSoup

## Introduction
AutoCount-Green Project는 초록여행 예약 현황 변경 사항을 Slack Bot을 통하여 알림을 보내주는 봇 입니다.  
초록여행 웹사이트를 Crawling 하여 데이터를 검사하여 변경 사항이 발생한다면, 변경사항을 Slack Bot을 통해 사용자에게 알림을 보내주게 됩니다.

## Getting Started

### Installing
* Slack Bot을 사용하기 위해 글 참고
[Slack Bot 토근 발급 방법](https://xsop.tistory.com/13)

발급한 토큰을 config.json 파일에 slackToken 입력

crawlingDelay는 초록여행 웹 사이트에서 정보를 가져오는 Refresh Delay 라고 생각하면 쉽다.   
crawlingDelay는 초(s) 기준으로 나타냅니다.

```
// config.json
{
  "slackToken": "",
  "crawlingDelay": 15
}
```
