# TikTok Streak Auto

# Environment Variables

Create a `.env` file in the root directory and declare the following variables:

```
CAPTCHA_API_KEY="api_key_ocacaptcha"
TIKTOK_USERNAME="username"
TIKTOK_PASSWORD="password"
```


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
