# created by @eve_enryu

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="firmware(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = "firmware"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{firmware} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)



@poci_cmd(pattern="gas(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    well = "bypass"
    chat = "@ATBYPASSBOT"
    xx = await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/{well} {link}")
            await conv.get_response()
            response = await conv.get_response()
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{well} {link}")
            await conv.get_response()
            response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await xx.delete()

@poci_cmd(pattern="fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = "fastboot"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{fboot} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@poci_cmd(pattern="recovery(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = "recovery"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{recovery} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@poci_cmd(pattern="pb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = "pb"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{pitch} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@poci_cmd(pattern="of(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = "of"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{ofox} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@poci_cmd(pattern="eu(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    eu = "eu"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{eu} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{eu} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@poci_cmd(pattern="vendor(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    vendor = "vendor"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{vendor} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{vendor} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


@poci_cmd(pattern="specs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = "specs"
    chat = "@XiaomiGeeksBot"
    await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/{specs} {link}")
            response = await response
        else:
            await event.delete()
            await event.client.forward_messages(event.chat_id, response.message)


CMD_HELP.update(
    {
        "xiaomi": f"**Plugin : **`xiaomi`\
        \n\n  •  **Syntax :** `{cmd}firmware` (codename)\
        \n  •  **Function : **Get lastest Firmware.\
        \n\n  •  **Syntax :** `{cmd}pb` (codename)\
        \n  •  **Function : **Get latest PitchBlack Recovery.\
        \n\n  •  **Syntax :** `{cmd}specs` (codename)\
        \n  •  **Function : **Get quick spec information about device.\
        \n\n  •  **Syntax :** `{cmd}fastboot` (codename)\
        \n  •  **Function : **Get latest fastboot MIUI.\
        \n\n  •  **Syntax :** `{cmd}recovery` (codename)\
        \n  •  **Function : **Get latest recovery MIUI.\
        \n\n  •  **Syntax :** `{cmd}eu` (codename)\
        \n  •  **Function : **Get latest xiaomi.eu rom.\
        \n\n  •  **Syntax :** `{cmd}vendor` (codename)\
        \n  •  **Function : **fetches latest vendor.\
        \n\n  •  **Syntax :** `{cmd}of` (codename)\
        \n  •  **Function : **Get latest ORangeFox Recovery.\
    "
    }
)
