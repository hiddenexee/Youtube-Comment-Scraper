from os import system
from requests import get

def get_comments():
    next_id = ''
    while True:
        try:
            response = get(f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=1000&canReply=true&key={api_key}&pageToken={next_id}&textFormat=plainText&videoId={video_id}").json()
            for comment in response["items"]:
                comment = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                open("comments.txt", "a+", encoding="utf-8").write(comment + "\n")

            next_id = response["nextPageToken"]
        except:
            break

if __name__ == '__main__':
    api_key = ''
    video_id = 'pC1kLG_Mbds'

    system("cls")
    system("title Youtube Get Comments ^| @hiddenexe")

    get_comments()
