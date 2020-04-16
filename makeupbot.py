from telegram.ext import (Updater , CommandHandler, MessageHandler, Filters, InlineQueryHandler,
                            CallbackQueryHandler, ConversationHandler)  #updater, dispatcher, handler
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
from telegram import (InlineQueryResultArticle, InputTextMessageContent, 
                            ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardButton,
                            InlineKeyboardMarkup, ReplyKeyboardRemove) 
import logging 

# bot = telegram.Bot(token='928479430:AAGOierRrwXh4_Ho8arNk2wkpWzk5RpEig0')
# print(bot.get_me())

#handle exception
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger= logging.getLogger(__name__)

TYPE, BRAND , TAG , PRICE = range(4)

def start(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    # type_list = [ 
    #     ['option1' ,'option3' , 'option2' ]
    # ]
    type_list = [
        [InlineKeyboardButton('option1' , callback_data='t1'), InlineKeyboardButton('option3' , callback_data='t3')],
        [InlineKeyboardButton('option2' , callback_data='t2')]
    ]
    update.message.reply_text(
        'Hi! This is the best bot you will ever use. '
        'Choose the makeup product category?',
        reply_markup=InlineKeyboardMarkup(type_list))

    return TYPE

def product_type(update, context):
    brand_list = [
        [InlineKeyboardButton('brand1' , callback_data='b1'), InlineKeyboardButton('brand3' , callback_data='b3')],
        [InlineKeyboardButton('brand2' , callback_data='b2')]
    ]
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Nice choice! '
                                'Choose what brand you prefer'
                                , reply_markup=InlineKeyboardMarkup(brand_list))

    return BRAND

def product_brand(update, context):
    tag_list = [
        [InlineKeyboardButton('tag1' , callback_data='tag1'), InlineKeyboardButton('tag3' , callback_data='tag3')],
        [InlineKeyboardButton('tag2' , callback_data='tag2')]
    ]
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='What a good brands choice. '
                                'Next, Choose any special tag list that concerns you!',
                                reply_markup=InlineKeyboardMarkup(tag_list))
    return TAG

def product_taglist(update, context):
    price_list = [
        [InlineKeyboardButton('price1' , callback_data='p1'), InlineKeyboardButton('price3' , callback_data='p3')],
        [InlineKeyboardButton('price2' , callback_data='p2')]
    ]
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='We will take you concern into consideration!'
                                'Choose the pricet that suits you',
                                reply_markup=InlineKeyboardMarkup(price_list))
    return PRICE

def product_price(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Alright! Now the bot will generate the best product choice customised just for you!')

    return ConversationHandler.END

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is your help!")


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Wrong Command!")

def cancel(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Bye end of story')

    return ConversationHandler.END

def main():

    updater = Updater(token='928479430:AAGOierRrwXh4_Ho8arNk2wkpWzk5RpEig0' , use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start' , start)],

        states={
            # data pattern to the corresponding handlers.
            # ^ means "start of line/string"
            # $ means "end of line/string"
            # So ^ABC$ will only allow 'ABC'
            TYPE: [CallbackQueryHandler(product_type, pattern='^' + 't1|t2|t3' + '$')],

            BRAND: [CallbackQueryHandler(product_brand, pattern='^' + 'b1|b2|b3' + '$')],

            TAG: [CallbackQueryHandler(product_taglist, pattern='^' + 'tag1|tag2|tag3' + '$')],

            PRICE: [CallbackQueryHandler(product_price, pattern='^' + 'p1|p2|p3' + '$')],
            
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    #start bot
    updater.start_polling() 

    #to send stop signal to the bot
    updater.idle() 

if __name__ == '__main__':
    main()


