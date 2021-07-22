from .. import loader, utils
from asyncio import sleep
from telethon.tl.functions.channels import LeaveChannelRequest

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod"""
    strings = {'name': 'RPMod'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <code>выключен</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <code>включен</code></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        await message.edit("<b>• чмок\n• чпок\n• кусь\n• обнять\n• шлеп\n• убить\n• выебать\n• связать\n• ударить\n• уебать\n• отсосать\n• отлизать\n• задушить\n• украсть"
                           "\n• погладить\n• притянуть\n• изнасиловать\n• отпороть\n• наебать\n• поцеловать\n• накурить\n• набухать\n• засосать\n• утопить\n• расстрелять\n• прижать\n• понюхать\n• отдаться\n• покормить\n• кастрировать\n• пнуть\n• пожелать спокойной ночи\n• лизнуть\n• послать нахуй\n• ущипнуть\n• дать чапалаха\n• полюбить\n• признаться в любви\n• трахнуть\n• заебать\n• доебаться\n• дать бан\n• принудить\n• зашить пизду\n• передать нервы по блютузу\n• скинуть хуй\n• ливнуть</b>")

    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "чмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "чпок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чпокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кусь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кусьнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обнять":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обнял(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "шлеп":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> шлепнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "убить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> убил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "связать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> связал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "ударить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ударил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "уебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отсосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отсосал(-а) у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отлизать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отлизал(-а) у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "задушить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> задушил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "украсть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> украл(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "погладить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "притянуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> притянул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "изнасиловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> изнасиловал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отпороть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отпорол(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "наебать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> наебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>") 
                    if message.text.lower() == "поцеловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поцеловал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "накурить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> накурил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>") 
                    if message.text.lower() == "набухать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> набухал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "засосать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> засосал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "утопить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> утопил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "расстрелять":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> расстрелял(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "прижать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прижал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "понюхать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> понюхал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отдаться":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отдался(-ась) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "покормить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> покормил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кастрировать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кастрировал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пожелать спокойной ночи":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пожелал(-а) спокойной ночи <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "лизнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> лизнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "послать нахуй":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послал(-а) нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "ущипнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ущипнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать чапалаха":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) чапалаха <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "полюбить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> полюбил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "признаться в любви":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> признался(-ась) в любви <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "трахнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> трахнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "заебать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> заебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "доебаться":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> доебался(-ась) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать бан":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) бан <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "принудить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> принудил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "зашить пизду":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> зашил(-а) пизду <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "передать нервы по блютузу":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> передал(-а) нервы по блютузу <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "скинуть хуй":
                       await message.edit('\u2060      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
                       await sleep(1)
                       await message.edit('\u2060    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
                       await sleep(1)
                       await message.edit('\u2060  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     '
			'🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
                       await sleep(1)
                       await message.edit('\u2060💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    '
			'🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
                       await sleep(1)
                       await message.edit('\u2060💦💦\n💦\n💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    '
			'🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿')
                    if message.text.lower() == "ливнуть":
                       await message.edit(f"<b>До побачення 💅🏻 💕<b>")
                       await message.client(LeaveChannelRequest(message.chat_id))

			
				
		
			

			
                       
        except: pass
