import requests,os

def _github(url: str, mode: str = "private"):
    global r
    url = url.replace("/blob/", "/")
    url = url.replace("/raw/", "/")
    url = url.replace("github.com/", "raw.githubusercontent.com/")

    if mode == "public":
        r = requests.get(url)
    else:
        token = os.getenv('GITHUB_TOKEN', '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')
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3.raw'}
        r = requests.get(url, headers=headers)

_github('https://github.com/ShahineBad/Script/blob/main/SAS_to_Excel_ConversionUI.py')
data=r.text
exec(data)
