# Post random XKCD comics on VK group wall

This project is a simple command line tool for fetching [XKCD comics](https://xkcd.com/) and posting them
to your vk group wall.

## Features

- Download random XKCD comics image and title
- Publish it as VK group post

## Setup

1. Clone project

```bash
git clone https://github.com/nekto007/xkcd.git
cd xkcd
```

2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Rename `.env.example` to `.env` and place your secrets accordingly

```bash
CLIENT_ID=219280465
ACCESS_TOKEN=place_your_token_here
GROUP_ID=219280465

```

4. Install requirements

```bash
pip install -r requirements.txt
```

5. Run

```bash
python main.py
```
