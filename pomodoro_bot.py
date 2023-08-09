import telebot
import time


bot = telebot.TeleBot("YOUR API TOKEN")

@bot.message_handler(commands=["start", "help"])
def start(message):
  bot.send_message(message.chat.id, "Welcome to the Pomodoro Timer bot! To start a timer, type /pomodoro <minutes>.For example, to start a 25-minute timer,type /pomodoro 25.And for breaktime type /breaktime 5  To stop timer type /stop .Please take pomodoro timer Greater than 5 and breaktime greater than 3. ")

@bot.message_handler(commands=["pomodoro"])
def pomodoro(message):
  
  if len(message.text.split(" ")) < 2:
    bot.send_message(message.chat.id, "Please enter a number of minutes after the /pomodoro command.")
    return
  
  minutes = int(message.text.split(" ")[1])
  if minutes <5:
    bot.send_message(message.chat.id, "Please enter a number of minutes greater than  or equal to 5.")
    return

  bot.send_message(message.chat.id, "Starting pomodoro timer for {} minutes.".format(minutes))
  bot.send_message(message.chat.id, "⏳")
  global timer_running
  
  timer_running = True

  while timer_running:
    time.sleep(60)
    minutes -= 1
    if minutes == 0:
      bot.send_message(message.chat.id, "Pomodoro timer finished! Would you like to take a break? Reply with /breaktime <minutes>")
      timer_running = False
      user_reply = bot.send_message(message.chat.id, "What would you like to do?")
    #   if user_reply.text == "/breaktime":
    #     breaktime(message, minutes)

    elif timer_running == False:
      bot.send_message(message.chat.id,"To restart press /start ")

    elif minutes <=0:  
      bot.send_message(message.chat.id, "Timer stopped sequences".format(minutes))
    elif minutes%4==1:  
      bot.send_message(message.chat.id, "{} minutes remaining.".format(minutes))


@bot.message_handler(commands=["breaktime"])
def breaktime(message):
  if len(message.text.split(" ")) < 2:
    bot.send_message(message.chat.id, "Please enter a number of minutes after the /breaktime command.")
    return
  
  minutes = int(message.text.split(" ")[1])
  if minutes <=3:
    bot.send_message(message.chat.id, "Please enter a number of minutes greater than  3 .")
    return

  bot.send_message(message.chat.id, "Okay, starting breaktime for {} minutes.".format(minutes))
  bot.send_message(message.chat.id, "⏳")
  global timer_running
  
  timer_running = True


  while timer_running:
    time.sleep(60)
    minutes -= 1
    if minutes == 0:

      bot.send_message(message.chat.id, "breaktime timer finished! . To start again type /pomodoro <minutes> ")
      timer_running = False
      
    elif timer_running == False:
      bot.send_message(message.chat.id,"To restart press /start ")

    elif minutes <=0:  
      bot.send_message(message.chat.id, "Timer stopped sequences".format(minutes))
    elif minutes%4==1:  
      bot.send_message(message.chat.id, "{} minutes remaining.".format(minutes))


@bot.message_handler(commands=["stop"])
def stop(message):
  
  global timer_running
  timer_running = False
  bot.send_message(message.chat.id, "Timer Stopped")


@bot.message_handler(commands=["start", "help"])
def help(message):
  bot.send_message(message.chat.id, "Welcome to the Help Section . The Commands are - 1] /pomodoro <minutes> - To set time for Your Work  2] /breaktime <minutes> - To set break time after session 3] /stop - To stop the  timer in case of emergency")

bot.polling()
