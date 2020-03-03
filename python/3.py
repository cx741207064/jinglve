import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

captchCode='24'

data = {'userName':'d083f784b64f22a00ca6adbc2ada3c26902f53060fe7c4f0f0cee20c9193cd8662e0f6f8fdcd2696db4397f667a2463841de48bfdaf7b343dcd2043a67dbb2b805b6cb0862972782ca43807bebe1e0244ddc4bc1c36105fdb687b21e0a7062b6fe12789cb1a9106c055c5e15bb877bdc1d3bcbbe7367f5ea4c998a7d1582862e', 
 'passWord':'985d721f99ae477706e59dea3a7c151c6b947be3be42c8a0e5310dbf3972f75e2ad7dba5a53da1c57fc1a3ed8d590b860db031a5bfce8de7a316eefe0d25381cb7531575ed45480a0bc4f0779d4c2c78bb9fb9d27a88cc221a50413a5faeacd0b1b1a14abcf9928a505a4546da7231c9442be16c5c252ec90e7e701907ff9ef9', 
 'authencationHandler':'UsernamePasswordAuthencationHandler', 
 'lt':'LT-500574-dcRdNbwhRduPuxM6yDT4-hbdzswj'
 ,'_eventId':'submit'
 ,'execution':'17a6dd54-d0d3-4a7b-b718-e015032a7be5_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuV0ZCMGVXVTBkemxhT1ZsWVFtVjVhWE5EVDFoVmRrdEhaMU55YmxBdldIcFVaMGhoVjNvMU5HVlhZWGQxTDNRMGNVcFhkMjF0T1hGcmNsbGpZVlYwV1hSTmJHcG5ibko1Tkc5UFRHVklWbGh1TDBaVFVsVjRjVEJ1WkV4VFoxUk9kV3A0UjAxRVEybFNjRWQyU0V4cWNUQk9UV3BRYTBzMk1rcGFlVzkwU25aaFRqbE1USEJKVG14Q2NrazJRUzlOVUVKbVRWQTBkVkptZFc1MGVFdFJOR3BNZFhwSVZGTjBaalJTT0dGWVZIQXJialEyWXpSTFJHZDJaSEkxVGtGTFoxcEZObkFyUVU5MldYRjFhVUV3WW1WeE9VTjVaMmQxYkdGUGRsRjFUbEZxVlZsR1VtcEdVVkJzTnpSQmNWRlRjRTgyTmtaVlYyNVdZMXBXTVN0V1UyRXpTbmRSVGpKUVVtSkJRek5zWmxJNWVFWjNiVWxyYldZeFZrVm1TR1JrUTJWNGNqbExXbEoyZEhKUVRrNW9ka0l4TTBaTWFGRnNTSGx3Unpob1drRmhMMnRRYVZjNWFuZDJNR05KVm5GeFptUlZkUzlGZVdzMGVtY3lXVkV6VEZwcGFXNDBaRGhuY0d4RlpFTTBjMEZvWkRKS1NFRlZialZ2UzJoSk4xaGhWVEpIVFM5M1lreEdXRGh6YUdJeFpVbEVUelZSTXpCaVduUkRjWEpFVDNGemFVZFVaMDVRV0ZRck5rMHhPV056T0V4WVYyWlVVbkZQWlZJcmJrOWFSRE5JVUhOM1FuTlVlbkk1YTBOYWRqbEdNaTlGT1dGQmVIQmtaSEZDWlRVNVdXaDFWVkkwU0ZCQlRuUmhhbU5uVmxSck5IbENUbFYxYm1ZNWIxcHpNWFY0ZGk5VGFsZzFiM3BZZGpWYVlYZFhWMHBLVUVKRE1FcDNXRlUwU2tKT1VtOXFlU3RxT0ZST2QxZHVja1J0YmxFMVptVnRkR3RCVW1rNWEwSktXVkV3TW5GRFlqUnVRMVZOVlVWMVVYWTNLMjQ1TjJwelprTk5SMVpOVUhKQlRqSmxkbE56VUZwU1kzbGlWaXRaZGt0eFZVUlZObE5UZFZvek9XeDFSR00xT0N0WlMwb3JhMnR4ZVdsc1lVdHVSbFZHUWpSeE5GcHFaMEpIYW1KbE5qWmhkR2hvTkVkSVFVOWxOV3BHTHpVd05XSlhTVEFyYjFGaVZFUnRhRmhVYjJWcmRFcFFNQ3RxVGxkU1ZubENVbU5vTldGRlVtTlVRbFJEUkZsNll6UjNTemt3U2pFM1JHRmljbmR2YUVKeU0zVldZbVZwYkVwT2RHTk5la3hVU0VONVlYUkhiSFV5ZGpCT1NUVk9UV3N3VkZwbmVFaFZVVUowVFhCcVMzVjRabFJwYUdaMk1tcGxibU5tWkRWaGFYSklZbU5aT0ZkVFJYZHRiVE5OU21OUldrWTNiMHhwVGk5SVlXb3JSMjlrTVVOallVWlJUQ3R0TUZWbmNHbHRVM1IxUzJObE9UWkpZM0JGVUhwbFMweHlkRFYyUjNScWJUbGFSRUZsZHpSVFRHbHdXVU01UTJaTlJFMUdZVmRsV1dsS1pqZFVUak5EU0VkSmFVNUliSEU0T1Zsa1pYbDBLM3BYUlROR1FqUmhOMUpzVFdZd2ExbElMMGRWT1ZacGQzUkxlVlpGYWxKYU1UZFhjMHcyYzNBNVNqRXZiVFFyZFRaa1ZWbGhkaTl6ZVZOTmNtVnljWE5aUVM4eVJuSTBXVUp1Y1hSSFlXMXFTa0psV21FME9URXZkMEZXY1RkdFNGbzBjVVkzYW5GU04wRnhaMnN2WWlzclVVOW5XV1oxTXpaV2FsRjVlRVJvY1dGRWFucFhNalo0UmpKd1EzZzBkbVJHVWtKNmRXOW5lRGRCUkhsRVpFUlZkRFF2TW5CMk0xTkJlVkZXT0hOaVpuSlJSbkpqYjAxUmJuRjRVSGRoU2s4eVZXdGhVa1JhWjBkd1NqQkdiWEpSYUdaS1JGSlVXVVJELlk0cjhDRGd3cWY2aXpsQmw3LVpNOEtQUy10MERCTkVGSzIwT0JKeFZWNjk1ZTNRWDdZTElSWEUyZkFvNDRhLXJfSnpZSWFTZEg4a25na3hJMWRCa1Zn'
 ,'captchCode':captchCode
 ,'qd':''
 }

 #设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

cookie_str = r'yfx_c_g_u_id_10003708=_ck19041013404111085361344218432; yfx_f_l_v_t_10003708=f_t_1554874841093__r_t_1554874841093__v_t_1554874841093__r_c_0; yfx_mr_10003708=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10003708=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10003708=; UM_distinctid=16a956c68816e-07bbb83f4d192e-65567528-100200-16a956c688269e; yfx_c_g_u_id_10003706=_ck19050811111113823366805347767; yfx_f_l_v_t_10003706=f_t_1557285071374__r_t_1557285071374__v_t_1557285071374__r_c_0; yfx_mr_10003706=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10003706=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10003706=; AD_RS_COOKIE=20110973; DZSWJ_TGC=0d146c7c7a4a4ab88e2e57e6f53eaf0e; SSO_LOGIN_TGC=0b83f508456a46fe86ddc6fa1c896d37; TGC=TGT-183580-vSz997HKZ3TuL3ctuYJloXCP00kUbCcdsoCcLh01IvG6hhzohF-hbdzswj;JSESSIONID=qrubPRUu9L-rZP9ImLdpdt03EV_wANwPqSQJp8kgLLwzY7yVK7y9!1151974382'
#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
 key, value = line.split('=', 1)
 cookies[key] = value

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'https://etax.hebei.chinatax.gov.cn/login-web/login'
#构造Session
session = requests.Session()

print(session.cookies.get_dict())

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url,verify=False,headers=headers,data=data)
#登录后才能访问的网页
url = 'https://etax.hebei.chinatax.gov.cn/login-web/auth/checkLoginState.do'
#url = 'https://etax.hebei.chinatax.gov.cn/bszm-web/apps/views-zj/home/home.html'
#发送访问请求
print(resp.content.decode('utf-8'))
print(session.cookies.get_dict())

#resp = session.post(url,verify=False,headers=headers)
#print(resp.content.decode('utf-8'))

#登录后才能访问的网页
url = 'https://etax.hebei.chinatax.gov.cn/bszm-web/api/desktop/todoList/get'

data = {'djxh':'10111306010000130883'}

