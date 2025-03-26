import hashlib
import requests

# FILE_ID = "1bnmmu4Lonb2MmGReWojzSd2UuCgzsP9h"
# ACCESS_TOKEN = "你的_access_token"  # 在 OAuth Playground 复制的 token
ACCESS_TOKEN = 'ya29.a0AeXRPp7BJ-sdj1yT5vZ_fAdv9VxA4-S7wPrT1GHhM9mT8-TYbjpbPBIOgL96M_yurhWvslP09omdZW3noyWEIhz8EHfgEyHukN2sjwogdSVPD068-RFHc1Bo5THFrO5ziPEC6K7EeN47pudjEbBTfAb2a8dtsexqeWiSzn8caCgYKAf8SARESFQHGX2Mih_M0-g7yuU-VtL6YZWv5hg0175'

# OUTPUT_FILENAME = "downloaded_file"

def download(FILE_ID, OUTPUT_FILENAME, chunk_size):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    url = f"https://www.googleapis.com/drive/v3/files/{FILE_ID}?alt=media"

    response = requests.get(url, headers=headers, stream=True)
    md5 = hashlib.md5()
    size = 0

    if response.status_code == 200:
        with open(OUTPUT_FILENAME, "wb") as f:
            for chunk in response.iter_content(chunk_size << 10):
                f.write(chunk)
                md5.update(chunk)
                size += len(chunk)
        # print(f"文件下载成功: {OUTPUT_FILENAME}")
    else:
        print(f"下载失败: {response.status_code}, {response.text}")
        
    return size, md5
    # return size, md5.hexdigest()

if __name__ == "__main__":
    download("1bnmmu4Lonb2MmGReWojzSd2UuCgzsP9h", "./test.png", 128)