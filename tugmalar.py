from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


menyu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Katalog', callback_data='catalog'),
        InlineKeyboardButton(text='Yordam', callback_data='help')
    ]
])


inline_katalog = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Anor", callback_data='anor'), 
        InlineKeyboardButton(text="Olma", callback_data='olma')
    ],    
    [
        InlineKeyboardButton(text="Anjir", callback_data='anjir'), 
        InlineKeyboardButton(text="Banan", callback_data='banan'), 
        InlineKeyboardButton(text="Uzum", callback_data='uzum')
    ],
    [
        InlineKeyboardButton(text='Bosh sahifa', callback_data='bosh_sahifa')
    ]
])


orqaga = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga')
    ]
])


orqaga_va_bosh = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
        InlineKeyboardButton(text='Bosh sahifa', callback_data='bosh_sahifa')
    ]
])


bosh_sahifa = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Bosh sahifa', callback_data='bosh_sahifa')
    ]
])


phone_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefon raqamni yuborish', request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
