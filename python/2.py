import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
#登录后才能访问的网页
url = 'https://etax.hebei.chinatax.gov.cn/login-web/auth/hb/queryQySmrzxx.do'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'yfx_c_g_u_id_10003708=_ck19041013404111085361344218432; yfx_f_l_v_t_10003708=f_t_1554874841093__r_t_1554874841093__v_t_1554874841093__r_c_0; yfx_mr_10003708=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10003708=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10003708=; UM_distinctid=16a956c68816e-07bbb83f4d192e-65567528-100200-16a956c688269e; yfx_c_g_u_id_10003706=_ck19050811111113823366805347767; yfx_f_l_v_t_10003706=f_t_1557285071374__r_t_1557285071374__v_t_1557285071374__r_c_0; yfx_mr_10003706=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10003706=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10003706=; AD_RS_COOKIE=20110973; DZSWJ_TGC=0d146c7c7a4a4ab88e2e57e6f53eaf0e; SSO_LOGIN_TGC=0b83f508456a46fe86ddc6fa1c896d37; TGC=TGT-183580-vSz997HKZ3TuL3ctuYJloXCP00kUbCcdsoCcLh01IvG6hhzohF-hbdzswj;JSESSIONID=qrubPRUu9L-rZP9ImLdpdt03EV_wANwPqSQJp8kgLLwzY7yVK7y9!1151974382'
#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
 key, value = line.split('=', 1)
 cookies[key] = value

proxy={'http':'http://192.168.10.167:8888','https':'https://127.0.0.1:8888'}

data = {'djxh':'10111306010000130883'}

 #设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
#在发送get请求时带上请求头和cookies
resp = requests.post(url,data, headers = headers, cookies = cookies,proxies=proxy,verify=False)
print(resp.content.decode('utf-8'))

setc = resp.headers['Set-Cookie'].split(';',1)[0]
ckey,cvalue = setc.split('=', 1)
cookies[ckey] = cvalue

print(cookies)

url="https://etax.hebei.chinatax.gov.cn/bszm-web/api/desktop/todoList/get"

resp = requests.get(url, headers = headers, cookies = cookies,proxies=proxy,verify=False)
print(resp.content.decode('utf-8'))
