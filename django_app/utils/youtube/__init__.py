import requests
from googleapiclient.discovery import build


def search_original(q):
    url_api_search = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'key': 'AIzaSyAQIMTkqwoO_CpDpzcizlInHeSrMhj_npo',
        'maxResults': '10',
        'type': 'video',
        'q': q,
    }
    # YouTube의 search api에 요청 응답받음
    response = requests.get(url_api_search, params=search_params)
    # 응답은 jason형태로 오며, json()메서드로 파이썬 객체 형식으로 변환
    data = response.json()
    return data


def search(q):
    # google api client를 사용
    youtube_api_service_name = "youtube"
    youtube_api_version = "v3"
    developer_key = "AIzaSyAQIMTkqwoO_CpDpzcizlInHeSrMhj_npo"

    youtube = build(
        youtube_api_service_name,
        youtube_api_version,
        developerKey=developer_key
    )

    search_response = youtube.search().list(
        q=q,
        part="snippet",
        maxResults=10,
        type='video'
    ).execute()

    data = search_response
    return data

