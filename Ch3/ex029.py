# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
import ex028
import urllib.request as ur
import urllib.parse as up
import json

def get_url_national_flag():
    info_dict = ex028.simplify_info_dict()
    file_name = info_dict['国旗画像']
    url = 'https://commons.wikimedia.org/w/api.php?'
    params = {'action': 'query', 'titles': 'File:{}'.format(file_name),
              'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json'}
    params = up.urlencode(params)
    params = params.encode('utf-8')
    req = ur.Request(url, params)
    with ur.urlopen(req) as response:
        json_data = response.read().decode("utf-8")
    _, value = list(json.loads(json_data)['query']['pages'].items())[0]
    return value['imageinfo'][0]['url']


def main():
    print(get_url_national_flag())


if __name__ == '__main__':
    main()
