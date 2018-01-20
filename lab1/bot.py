from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)

def hello(bot, trigger):
    print(trigger, trigger.nick)
    #bot.say('Hello, ' + trigger.nick)

def goodbye(bot, trigger);
    print(trigger, trigger.nick)
    #bot.say('Goodbye ' + trigger.nick)

def statement(bot, trigger):

