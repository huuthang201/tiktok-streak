from utils import init_browser, login_tiktok, auto_send_message
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    browser, wait = init_browser()
    login_tiktok(browser, wait, os.getenv("TIKTOK_USERNAME"), os.getenv("TIKTOK_PASSWORD"))
    auto_send_message(browser, wait)
