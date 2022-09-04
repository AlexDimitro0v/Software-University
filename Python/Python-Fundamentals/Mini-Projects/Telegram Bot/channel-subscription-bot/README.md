## Telegram Channel Subscription Membership Management Bot

channel-subscription-bot

Written by dashezup (fiverr, FO71D325EA9C5)

### Requirements

Based on [aiogram](https://aiogram.dev)

- Python 3.7 or higher
  <!-- https://github.com/aiogram/aiogram/blob/dev-2.x/setup.py#L47 -->
- A [Telegram bot token](https://t.me/BotFather)

```
apt update
apt upgrade
apt autoremove
apt install tmux python3-pip
cd /path/to/project
# tmux
pip3 install -U -r requirements.txt
cp sample_config.py config.py
nano config.py
python3 -m bot
```

### Set Up

Copy `sample_config.py` as `config.py` and edit `config.py` with your own values,
and then run the bot with `python3 -m bot`

You can get chat (private/group/supergroup/channel) ID with `/id` command for
`channel_id` and `log_chat_id`. `owner` can be your username or user ID which is
the chat ID of the PM (private) you have with the bot.

### Usage

`/id` for get chat ID
`/help` (owner only) for showing owner commands

### Test Telegram Bot Payments API with 'Stripe TEST MODE' Provider

[Bot Payments API](https://core.telegram.org/bots/payments#the-payments-api)

> **Getting a Token**
> - Use the /mybots command in the chat with BotFather and choose the @merchantbot that will be offering goods or services.
> - Go to Bot Settings > Payments.
> - Choose a provider, and you will be redirected to the relevant bot.
> - Enter the required details so that the payments provider is connected successfully, go back to the chat with Botfather.
> - The message will now show available providers. Each will have a name, a token, and the date the provider was connected.
> - You will use the token when working with the Bot API.

[Testing | Stripe Documentation](https://stripe.com/docs/testing#cards)

> **Testing interactively**
> When testing interactively, use a card number, such as 4242 4242 4242 4242.
> - Use a valid future date, such as 12/34.
> - Use any three-digit CVC (four digits for American Express cards).
> - Use any value you like for other form fields.
