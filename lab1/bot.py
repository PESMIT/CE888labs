from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()

@module.rule('')
def main(bot, trigger):
	print(trigger, trigger.nick)

	# Variables
	botName = trigger.nick
	botTrigger = trigger
	happyCounter = 0
	sadCounter = 0
	#print(botName + " " + botTrigger + " " + str(userInput))
	
	# Splitter
	chatInput = botTrigger.lower()
	chatInputList = chatInput.split()
	print(str(chatInputList)) 
	for x in chatInputList:
		if(x == "happy"):
			happyCounter += 1
		if(x == "sad"):
			sadCounter += 1
	print("Happy Counter = " + str(happyCounter))
	print("Sad Counter = " + str(sadCounter))
			
    #bot.say('Hi, ' + trigger.nick)

