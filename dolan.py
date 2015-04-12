import JustIRC
import translator
import commands
import time
import json
import random

def get_time_string():
  return time.strftime("[%d-%m-%Y %H:%M:%S]")


class Dolan:
  def __init__(self):
    self.bot = JustIRC.IRCConnection()
    self.config = json.loads(open("config.json").read())
    self.channels = self.config["channels"]
    self.log_level = 1
    
    self.initBot()
  
  def initBot(self):
    self.bot.on_connect.append(self.onConnect)
    self.bot.on_welcome.append(self.onWelcome)
    self.bot.on_public_message.append(self.onMessage)
    self.bot.on_private_message.append(self.onPrivateMessage)
    self.bot.connect("irc.freenode.net")
    self.bot.run_loop()
  
  def onConnect(self, bot):
    self.log("Connected!", 2)
    self.bot.set_nick("Dolan")
    self.bot.send_user_packet("Dolan")
    
  def onWelcome(self, bot):
    self.log("Welcome message sent.", 1)
    for channel in self.channels:
        self.bot.join_channel(channel)
        self.bot.send_message(channel, translator.translate("Hello kids, Donald is back"))
  
  def onPrivateMessage(self, bot, sender, message):
    self.onMessage(bot, random.choice(self.channels), sender, message)
  
  def onMessage(self, bot, channel, sender, message):
    if len(message.split()) == 0: #Stops people from crashing bot with " "
      message = "."
    
    self.log("{} {} {}".format(channel, sender, message))
    if message.split()[0].startswith("!"):
      command_name = message.split()[0][1:]
      if command_name in commands.commands:
        messageParts = message.split()
        messageParts.pop(0)
        message = " ".join(messageParts)
        commands.commands[command_name](bot, channel, sender, message)

  def log(self, message, level=1):
    if self.log_level <= level:
      print("{} {}".format(get_time_string(), message))

bot = Dolan()
