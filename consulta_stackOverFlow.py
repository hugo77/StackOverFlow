from googleapiclient.discovery import build
idBuscador="007470944933255819503:m3xkz985fk5"
keyApi="AIzaSyB2Fd2O9AnabZqjt8-D77d84OARpnjbgqI"


from googleapiclient.discovery import build

def google_results_count(query):
    service = build("customsearch", "v1",
                    developerKey="AIzaSyB2Fd2O9AnabZqjt8-D77d84OARpnjbgqI")

    result = service.cse().list(
            q=query,
            cx='007470944933255819503:m3xkz985fk5'
        ).execute()

    return result["items"]


def recorrer_items():
    items = google_results_count('java virtual machine')
    i=0;
    for item in items:
        print(i,"   -   " ,item["snippet"])
        i=i+1

recorrer_items()