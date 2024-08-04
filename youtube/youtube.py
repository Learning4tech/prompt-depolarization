from googleapiclient.discovery import build

# Authenticate to YouTube
youtube = build('youtube', 'v3', developerKey='your_api_key')

# Collect comments
request = youtube.commentThreads().list(part='snippet', videoId='your_video_id', maxResults=100)
response = request.execute()

for item in response['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
