# TikTok Streak Auto

# Environment Variables

Create a `.env` file in the root directory and declare the following variables:

```
CAPTCHA_API_KEY="api_key_ocacaptcha"
TIKTOK_USERNAME="username"
TIKTOK_PASSWORD="password"
MESSAGE="auto send message"
```


> **Note:** Instead of a username, you can use an email for the `TIKTOK_USERNAME` variable.

> **Note:** The `MESSAGE` variable is the message that will be sent to all friends.


## Get All Friends

To get all friends, run the `my-friends.py` file:

```sh
python my-friends.py
```


## Manage Friends List

You can add or remove your friends in the `friends.csv` file. This file contains the list of friends to whom messages will be sent.


## Send Message to All Friends

To send a message to all friends listed in the `friends.csv` file, run the `main.py` file:

```sh
python main.py
```
