from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

"""-------------------------------------------------------------------------------"""

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, r_j))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from a boat of a banana tree
            buttons = [[
                InlineKeyboardButton('πππΏπΏπΎππ', url=f'https://t.me/{SUPPORT_CHAT}')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>α΄Κα΄α΄ Ι΄α΄α΄ α΄ΚΚα΄α΄‘α΄α΄\n\nπΌπ π°π³πΌπΈπ½π π·π°π ππ΄ππππΈπ²ππ΄π³ πΌπ΄ π΅ππΎπΌ ππΎππΊπΈπ½πΆ π·π΄ππ΄ !πΈπ΅ ππΎπ ππ°π½π ππΎ πΊπ½πΎπ πΌπΎππ΄ π°π±πΎππ πΈπ π²πΎπ½ππ°π²π πΎππ½π΄π...</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
            InlineKeyboardButton('π·πΎπ ππΎ πππ΄ πΌπ΄', url=f"https://t.me/PlusTechzBots"),
            InlineKeyboardButton('Κα΄α΄s | α΄α΄α΄α΄α΄α΄s', url='https://t.me/PlusTechz')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>βΊβΊ ππ·π°π½πΊπ ππΎ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ. {message.chat.title} β£οΈ\nβΊβΊ π³πΎπ½'π π΅πΎππΆπ΄π ππΎ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½.\nβΊβΊ πΈf π°π½π π³πΎππ±ππ π°π±πΎππ πππΈπ½πΆ πΌπ΄ π²π»πΈπ²πΊ π±π΄π»πΎπ π±ππππΎπ½..β‘β‘.</b>",
            reply_markup=reply_markup)
    else:
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            for u in message.new_chat_members:
                if (temp.MELCOW).get('welcome') is not None:
                    try:
                        await (temp.MELCOW['welcome']).delete()
                    except:
                        pass
                temp.MELCOW['welcome'] = await message.reply_video(
                video="https://telegra.ph/file/03691465baa774e46506d.mp4",                                               
                                                 caption=f'<b>Κα΄Κ, {u.mention} ππ»\nα΄‘α΄Κα΄α΄α΄α΄ α΄α΄ α΄α΄Κ Ι’Κα΄α΄α΄ {message.chat.title}\n\nFind Any Media ! if you need any movie then then enter the movie name + years. π\n\nGuys Enter Only movie Or Webseries Name like This π\nPushpa β\nPushpa 2021 β\nPushpa in Hindi β\nLucifer β\nLucifer S01 β\nLucifer all season β</b>',
                                                 reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton('β­ α΄α΄α΄ Ιͺα΄s | α΄α΄α΄α΄α΄α΄s β­', url='https://t.me/HDFlims4U') ],
                                                                                      [ InlineKeyboardButton('π₯  β­Κα΄α΄s | α΄α΄α΄α΄α΄α΄sβ­  π₯', url='https://t.me/PlusTechz') ]
                                                                                    ] )
                )

@Client.on_message(filters.command('Κα΄α΄α΄ α΄') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Ι’Ιͺα΄ α΄ α΄α΄ α΄Κα΄α΄ Ιͺα΄')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('πππΏπΏπΎππ', url='t.me/TeamShadowXD')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Κα΄ΚΚα΄ ?ΚΙͺα΄Ι΄α΄s, \nα΄Κ α΄α΄α΄ΙͺΙ΄ Κα΄s α΄α΄Κα΄ α΄α΄ α΄α΄ Κα΄α΄α΄ α΄ ?Κα΄α΄ Ι’Κα΄α΄α΄ sα΄ Ιͺ Ι’α΄! Ιͺ? Κα΄α΄ α΄‘α΄Ι΄Ι΄α΄ α΄α΄α΄ α΄α΄ α΄Ι’α΄ΙͺΙ΄ α΄α΄Ι΄α΄α΄α΄α΄ α΄Κ sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"left the chat `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Ι’Ιͺα΄ α΄ α΄α΄ α΄ α΄ α΄ΚΙͺα΄ α΄Κα΄α΄ Ιͺα΄')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("α΄Κα΄α΄ Ι΄α΄α΄ ?α΄α΄Ι΄α΄ ΙͺΙ΄ α΄Κ")
    if cha_t['is_disabled']:
        return await message.reply(f"α΄ΚΙͺs α΄Κα΄α΄ Ιͺs α΄ΚΚα΄α΄α΄Κ α΄Ιͺsα΄ΚΚα΄α΄:\nΚα΄α΄sα΄Ι΄-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('α΄Κα΄α΄ sα΄α΄α΄α΄ss?α΄ΚΚΚ α΄Ιͺsα΄ΚΚα΄α΄')
    try:
        buttons = [[
            InlineKeyboardButton('πππΏπΏπΎππ', url='t.me/TeamShadowXD}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>Κα΄ΚΚα΄ ?ΚΙͺα΄Ι΄α΄s, \nα΄Κ α΄α΄α΄ΙͺΙ΄ Κα΄s α΄α΄Κα΄ α΄α΄ α΄α΄ Κα΄α΄α΄ α΄ ?Κα΄α΄ Ι’Κα΄α΄α΄ sα΄ Ιͺ Ι’α΄! Ιͺ? Κα΄α΄ α΄‘α΄Ι΄Ι΄α΄ α΄α΄α΄ α΄α΄ α΄Ι’α΄ΙͺΙ΄ α΄α΄Ι΄α΄α΄α΄α΄ α΄Κ sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄.</Κ> \nΚα΄α΄sα΄Ι΄ : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Ι’Ιͺα΄ α΄ α΄α΄ α΄ α΄Κα΄α΄ Ιͺα΄')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Ι’Ιͺα΄ α΄ α΄α΄ α΄ α΄ α΄ΚΙͺα΄ α΄Κα΄α΄ Ιͺα΄')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("α΄Κα΄α΄ Ιͺα΄ Ι΄α΄α΄ ?α΄α΄Ι΄α΄ ΙͺΙ΄ α΄Κ !")
    if not sts.get('is_disabled'):
        return await message.reply('α΄ΚΙͺs α΄Κα΄α΄ Ιͺs Ι΄α΄α΄ Κα΄α΄ α΄Ιͺsα΄ΚΚα΄α΄')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Chat Successfully re-enabled")


@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('<b>π°π²π²π΄πππΈπ½πΆ πππ°πππ π³π΄ππ°πΈπ»π...</b>')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(script.STATUS_TXT.format(files, total_users, totl_chats, size, free))


# a function for trespassing into others groups, Inspired by a Vazha
# Not to be used , But Just to showcase his vazhatharam.
# @Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Invite Link Generation Failed, Iam Not Having Sufficient Rights")
    except Exception as e:
        return await message.reply(f'α΄ΚΚα΄Κ {e}')
    await message.reply(f'Here is your Invite Link {link.invite_link}')

@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # https://t.me/GetTGLink/4185
    if len(message.command) == 1:
        return await message.reply('Ι’Ιͺα΄ α΄ α΄α΄ α΄ α΄sα΄Κ Ιͺα΄ / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Ι΄α΄ Κα΄α΄sα΄Ι΄ α΄Κα΄α΄ Ιͺα΄α΄α΄"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("α΄ΚΙͺs Ιͺs α΄Ι΄ ΙͺΙ΄α΄ α΄ΚΙͺα΄ α΄sα΄Κ, α΄α΄α΄α΄ sα΄Κα΄ Ιͺα΄ Κα΄α΄ α΄ α΄α΄α΄ ΚΙͺα΄ Κα΄?α΄Κα΄.")
    except IndexError:
        return await message.reply("α΄ΚΙͺs α΄ΙͺΙ’Κα΄ Κα΄ α΄ α΄Κα΄Ι΄Ι΄α΄Κ, α΄α΄α΄α΄ sα΄Κα΄ Ιͺα΄s α΄ α΄sα΄Κ.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} Ιͺs α΄ΚΚα΄α΄α΄Κ Κα΄Ι΄Ι΄α΄α΄\nΚα΄α΄sα΄Ι΄: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"sα΄α΄α΄α΄ss?α΄ΚΚΚ Κα΄Ι΄Ι΄α΄α΄  {k.mention}")


    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Ι’Ιͺα΄ α΄ α΄α΄ α΄ α΄sα΄Κ Ιͺα΄ / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Ι΄α΄ Κα΄α΄sα΄Ι΄ α΄Κα΄α΄ Ιͺα΄α΄α΄"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("Thismight be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} is not yet banned.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"sα΄α΄α΄α΄ss?α΄ΚΚΚ α΄Ι΄Κα΄Ι΄Ι΄α΄α΄ {k.mention}")


    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Ι’α΄α΄α΄ΙͺΙ΄Ι’ ΚΙͺsα΄ α΄? α΄sα΄Κs')
    users = await db.get_all_users()
    out = "α΄sα΄Κs sα΄α΄ α΄α΄ ΙͺΙ΄ α΄Κ α΄Κα΄:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Banned User )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="ΚΙͺsα΄ α΄? α΄sα΄Κs")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Ι’α΄α΄α΄ΙͺΙ΄Ι’ ΚΙͺsα΄ α΄? α΄Κα΄α΄s')
    chats = await db.get_all_chats()
    out = "α΄Κα΄α΄ sα΄α΄ α΄α΄ ΙͺΙ΄ α΄Κ α΄Κα΄:\n\n"
    async for chat in chats:
        out += f"**Title:** `{chat['title']}`\n**- ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += '( Disabled Chat )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="ΚΙͺsα΄ α΄? α΄Κα΄α΄")
