from telegram import *
from telegram.ext import *
from requests import *
import pandas as pd
import os

class TestBot:

    def __init__(self,input_dir=''):
        self.input_dir=input_dir
        self.token_given="5778362453:AAHkp63cZ75OMJ4X1ONWduWPDqcE-gDxoOU"
        bot_msg_data = pd.read_csv(input_dir + 'Bot Message Database.csv',encoding='cp1252')
        user_msg_data = pd.read_csv(input_dir + 'User Message Options.csv',encoding='cp1252')

        self.bot_msg = list(bot_msg_data['Bot Msg'].values)
        self.user_msg = list(user_msg_data['Button Msg'].values)
        self.context_block = 0

        self.updater = Updater(token=self.token_given)
        self.dispatcher = self.updater.dispatcher

    def startCommand(self,update: Update, context: CallbackContext):
        print("Command handler running")
        user_first_name = update.message.chat.first_name
        welcome_text = "Hi " + user_first_name + ',\n' + self.bot_msg[0]
        buttons = [[KeyboardButton(self.user_msg[0])],
                [KeyboardButton(self.user_msg[1])]]
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text,
                                reply_markup=ReplyKeyboardMarkup(buttons))
        context.bot.send_photo(chat_id=update.effective_chat.id,
                            photo=open(self.input_dir + 'Q7 All Plans Summary.jpeg', 'rb'))


    def messageHandler(self,update: Update, context: CallbackContext):
        # global context_block
        # if update.effective_chat.username not in allowedUsernames:
        #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
        #     return
        reply_text = update.message.text

        if reply_text == self.user_msg[0]:
            buttons = [[KeyboardButton(self.user_msg[2])],
                    [KeyboardButton(self.user_msg[3])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=self.bot_msg[1],
                                    reply_markup=ReplyKeyboardMarkup(buttons))

        elif reply_text == self.user_msg[1]:
            buttons = [[KeyboardButton(self.user_msg[5])],
                    [KeyboardButton(self.user_msg[6])],
                    [KeyboardButton(self.user_msg[4])]
                    ]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[2])
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                photo=open(self.input_dir + 'Q7 Premium Plans Summary.jpeg', 'rb'))

        elif reply_text == self.user_msg[2]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[4])]
                    ]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                text=self.bot_msg[3])

        elif reply_text == self.user_msg[3]:
            buttons = [[KeyboardButton(self.user_msg[9])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                text=self.bot_msg[4])

        elif reply_text == self.user_msg[4]:
            user_first_name = update.message.chat.first_name
            welcome_text = "Hi " + user_first_name + ',\n' + self.bot_msg[0]
            buttons = [[KeyboardButton(self.user_msg[0])],
                    [KeyboardButton(self.user_msg[1])]]
            context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text,
                            reply_markup=ReplyKeyboardMarkup(buttons))
            context.bot.send_photo(chat_id=update.effective_chat.id,
                            photo=open(self.input_dir + 'Q7 All Plans Summary.jpeg', 'rb'))
            

        elif reply_text == self.user_msg[5]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[5],parse_mode='html')

        elif reply_text == self.user_msg[6]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[6])

        elif reply_text == self.user_msg[7]:
            buttons = [[KeyboardButton(self.user_msg[14])],
                    [KeyboardButton(self.user_msg[15])],
                    [KeyboardButton(self.user_msg[16])],
                    [KeyboardButton(self.user_msg[17])],
                    [KeyboardButton(self.user_msg[18])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[7])

        elif reply_text == self.user_msg[8]:
            buttons = [[KeyboardButton(self.user_msg[19])],
                    [KeyboardButton(self.user_msg[20])],
                    [KeyboardButton(self.user_msg[21])],
                    [KeyboardButton(self.user_msg[22])],
                    [KeyboardButton(self.user_msg[23])],
                    [KeyboardButton(self.user_msg[24])],
                    [KeyboardButton(self.user_msg[25])],
                    [KeyboardButton(self.user_msg[26])],
                    [KeyboardButton(self.user_msg[27])],
                    [KeyboardButton(self.user_msg[28])],
                    [KeyboardButton(self.user_msg[29])],
                    [KeyboardButton(self.user_msg[30])],
                    [KeyboardButton(self.user_msg[31])],
                    [KeyboardButton(self.user_msg[32])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[8])

        elif reply_text == self.user_msg[9]:
            buttons = [[KeyboardButton(self.user_msg[47])],
                    [KeyboardButton(self.user_msg[48])],
                    [KeyboardButton(self.user_msg[49])],
                    [KeyboardButton(self.user_msg[50])],
                    [KeyboardButton(self.user_msg[51])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[43])

        elif reply_text == self.user_msg[10]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[49])

        elif reply_text == self.user_msg[11]:
            buttons = [[KeyboardButton(self.user_msg[4])],
                    [KeyboardButton(self.user_msg[10])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[9])

        elif reply_text == self.user_msg[12]:
            buttons = [[KeyboardButton(self.user_msg[33])],
                    [KeyboardButton(self.user_msg[34])],
                    [KeyboardButton(self.user_msg[35])],
                    [KeyboardButton(self.user_msg[36])],
                    [KeyboardButton(self.user_msg[37])],
                    [KeyboardButton(self.user_msg[38])],
                    [KeyboardButton(self.user_msg[39])],
                    [KeyboardButton(self.user_msg[40])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[10])

        elif reply_text == self.user_msg[13]:
            buttons = [[KeyboardButton(self.user_msg[52])],
                    [KeyboardButton(self.user_msg[53])],
                    [KeyboardButton(self.user_msg[54])],
                    [KeyboardButton(self.user_msg[55])],
                    [KeyboardButton(self.user_msg[56])],
                    [KeyboardButton(self.user_msg[57])],
                    [KeyboardButton(self.user_msg[58])],
                    [KeyboardButton(self.user_msg[59])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[11])

        elif reply_text == self.user_msg[14]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[12])

        elif reply_text == self.user_msg[15]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[13])

        elif reply_text == self.user_msg[16]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[14])

        elif reply_text == self.user_msg[17]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[15])

        elif reply_text == self.user_msg[18]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[16])

        elif reply_text == self.user_msg[19]:
            buttons = [[KeyboardButton(self.user_msg[41])],
                    [KeyboardButton(self.user_msg[42])],
                    [KeyboardButton(self.user_msg[43])],
                    [KeyboardButton(self.user_msg[44])],
                    [KeyboardButton(self.user_msg[45])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[4])]]
            # inline_button = [[InlineKeyboardButton(text="🔙 To Previous Options",callback_data='')]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[17])

        elif reply_text == self.user_msg[20]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[18])

        elif reply_text == self.user_msg[21]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[19])

        elif reply_text == self.user_msg[22]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[20])

        elif reply_text == self.user_msg[23]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[20])

        elif reply_text == self.user_msg[24]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[21])

        elif reply_text == self.user_msg[25]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[22])

        elif reply_text == self.user_msg[26]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[23])

        elif reply_text == self.user_msg[27]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[24])

        elif reply_text == self.user_msg[28]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[25])

        elif reply_text == self.user_msg[29]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[25])

        elif reply_text == self.user_msg[30]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[25])

        elif reply_text == self.user_msg[31]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[26])

        elif reply_text == self.user_msg[32]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[27])

        elif reply_text == self.user_msg[33]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[28])

        elif reply_text == self.user_msg[34]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[29])

        elif reply_text == self.user_msg[35]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[30])

        elif reply_text == self.user_msg[36]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[31])

        elif reply_text == self.user_msg[37]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[32])

        elif reply_text == self.user_msg[38]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[33])

        elif reply_text == self.user_msg[39]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[34])

        elif reply_text == self.user_msg[40]:
            buttons = [[KeyboardButton(self.user_msg[11])],
                    [KeyboardButton(self.user_msg[12])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[35])


        elif reply_text == self.user_msg[41]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[37])

        elif reply_text == self.user_msg[42]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[38])

        elif reply_text == self.user_msg[43]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[39])

        elif reply_text == self.user_msg[44]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[40])

        elif reply_text == self.user_msg[45]:
            buttons = [[KeyboardButton(self.user_msg[7])],
                    [KeyboardButton(self.user_msg[8])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[41])

        elif reply_text == self.user_msg[46]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[42])

        elif reply_text == self.user_msg[47]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[44])

        elif reply_text == self.user_msg[48]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[45])

        elif reply_text == self.user_msg[49]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[46])

        elif reply_text == self.user_msg[50]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[47])

        elif reply_text == self.user_msg[51]:
            buttons = [[KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[48])

        elif reply_text == self.user_msg[52]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[28])

        elif reply_text == self.user_msg[53]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[36])

        elif reply_text == self.user_msg[54]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[30])

        elif reply_text == self.user_msg[55]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[31])

        elif reply_text == self.user_msg[56]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[32])

        elif reply_text == self.user_msg[57]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[33])

        elif reply_text == self.user_msg[58]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[34])

        elif reply_text == self.user_msg[59]:
            buttons = [[KeyboardButton(self.user_msg[46])],
                    [KeyboardButton(self.user_msg[13])],
                    [KeyboardButton(self.user_msg[10])],
                    [KeyboardButton(self.user_msg[4])]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                    text=self.bot_msg[35])


        else:
            print('Invalid Input')
            buttons = [[InlineKeyboardButton("Main Menu", callback_data="start")]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                    text=self.bot_msg[50])


    def queryHandler(self,update: Update, context: CallbackContext):
        query = update.callback_query.data
        print('Starting Conversation From Callback...')
        print(query)
        if query == 'start':
            welcome_text = "Hi,\n" + self.bot_msg[0]
            buttons = [[KeyboardButton(self.user_msg[0])],
                    [KeyboardButton(self.user_msg[1])]]
            context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text,
                                    reply_markup=ReplyKeyboardMarkup(buttons))
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                photo=open(self.input_dir + 'Q7 All Plans Summary.jpeg', 'rb'))
            

        update.callback_query.answer()
    def run(self):
        self.dispatcher.add_handler(CommandHandler("start", self.startCommand))
        self.dispatcher.add_handler(MessageHandler(Filters.text,self.messageHandler))
        self.dispatcher.add_handler(CallbackQueryHandler(self.queryHandler))

        # self.updater.start_polling()
        self.updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=self.token_given,
                    webhook_url= + self.token_given)
        sentence = "\U0001f513 What's the capital requirement?"
        uc_sentence = sentence.encode('unicode-escape')
        dc_sentence = uc_sentence.decode("utf-8")
        print(dc_sentence)