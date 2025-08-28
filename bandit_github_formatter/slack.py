from slack_sdk import WebClient
import os

# Sends message to Slack channel with given message
def send_message(message: dict, SLACK_CHANNEL: str) -> dict:
    SLACK_TOKEN = os.getenv("INPUT_SLACK_TOKEN", "none")
    SLACK_USERNAME = os.getenv("INPUT_SLACK_USERNAME")
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=SLACK_CHANNEL, 
        blocks=message, 
        username=SLACK_USERNAME
    )

def notify(pr_link: str,comment_url: str,repo_name: str) -> str:
    SLACK_CHANNEL = os.getenv("INPUT_SLACK_CHANNEL")
    message_blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Bandit was triggred in a PR on "+ repo_name,
                "emoji": True
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Pull request link:"
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Github",
                    "emoji": True
                },
                "value": "link1",
                "url": pr_link or "https://github.com/#missing-pr-url-error",
                "action_id": "button-action"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Bandit findings:"
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Github",
                    "emoji": True
                },
                "value": "link2",
                "url": comment_url or "https://github.com/#missing-bandit-comment-error",
                "action_id": "button-action"
            }
        },
        {
            "type": "divider"
        }
    ]
    send_message(message_blocks, SLACK_CHANNEL)