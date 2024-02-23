# module ini di ambil dari repo bot https://t.me/FsubPremBot
# dibuat oleb: https://t.me/NorSodikin

from pykeyboard import InlineKeyboard
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton


def SUB_FOR_SUB(func):
    async def function(client, message):
        user = message.from_user
        rpk = f"<a href='tg://user?id={user.id}'>{user.first_name} {user.last_name or ''}</a>"
        vars = "-1001761436894"  # isi id gc atau username yg mau di pakai buat join member (bisa lebih dari 1 fsub nya)
        if not vars:
            return await func(client, message)
        try:
            for x in str(vars).split():
                await client.get_chat_member(int(x), user.id)
        except UserNotParticipant:
            buttons = InlineKeyboard(row_width=2)
            keyboard = []
            for x in str(vars).split():
                chat = await client.get_chat(int(x))
                invite_link = chat.invite_link
                keyboard.append(
                    InlineKeyboardButton(
                        text=f"• Join Channel •",
                        url=invite_link,
                    )
                )
            buttons.add(*keyboard)
            return await message.reply(
                f"""
<b>Hey 👋 {rpk} Untuk dapat memutar musik. Kamu harus Join Dulu Nih Ke Channel Terimakasih ❤️

Sfs Back PC <a href="tg://user?id=1365496750">ᴀɴᴀᴋɴʏᴀ ᴘᴀᴋ ʀᴛ⋆</a></b>
""",
                disable_web_page_preview=True,
                reply_markup=buttons,
            )
        return await func(client, message)

    return function
