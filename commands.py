import translator
import json
import requests

def greet_command(bot, channel, sender, message):
  nick = sender
  if len(message.split()) >= 1:
    nick = message.split()[0]
  bot.send_message(channel, translator.translate("Hello there {}. I am Donald".format(nick)))

def change_nick_command(bot, channel, sender, message):
  if len(message.split()) == 1:
    bot.set_nick(message.split()[0])

def dolanify_command(bot, channel, sender, message):
  bot.send_message(channel, translator.translate(message))
  
def christmas_command(bot, channel, sender, message):
  song = "Oh the weather outside is frightful , But the fire is so delightful , And since we've no place to go , Let It Snow ! Let It Snow ! Let It Snow !"
  bot.send_message(channel, translator.translate(song))
  
def shoot_command(bot, channel, sender, message):
  if len(message.split()) >= 1:
    target = message.split()[0]
    bot.send_action_message(channel, translator.translate("shoots {} in the face".format(target)))

def help_command(bot, channel, sender, message):
  commandNames = []
  for cmd in commands:
    commandNames.append("!{}".format(cmd))
  bot.send_message(channel, ", ".join(commandNames))
  
def video_command(bot, channel, sender, message):
  search_command(bot, channel, sender, "inurl:youtube.com/watch %s" % message)
  
def search_command(bot, channel, sender, message):
  results = search(message)
  if len(results) == 0:
    bot.send_message(channel, translator.translate("nothing found"))
  else:
    res = results[0]
    msg = "{} [ {} ]".format(translator.translate(res["titleNoFormatting"]), res["unescapedUrl"])
    bot.send_message(channel, msg)

def search(query):
  url = 'http://ajax.googleapis.com/ajax/services/search/web'
  search_response = requests.get(url, params={ 'q': query, 'v': '1.0'})
  search_results = search_response.json()
  return search_results["responseData"]["results"]

commands = {
  "greet": greet_command,
  "nick": change_nick_command,
  "dolanify": dolanify_command,
  "christmas": christmas_command,
  "shoot": shoot_command,
  "help": help_command,
  "halp": help_command,
  "search": search_command,
  "video": video_command
}