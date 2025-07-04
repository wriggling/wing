import discord
import asyncio
import os
import time
from pystyle import Colors, Write, Colorate

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def set_title():
    os.system("title Wing" if os.name == "nt" else "")

def print_ascii_art():
    print(Colorate.Horizontal(Colors.rainbow, """
                                  ▓▓████▒▒
                                    ▓▓██████▒▒
                                        ░░██▓▓▓▓██
                                          ▓▓▓▓████░░
                                        ░░▓▓████████
                                        ▓▓██▓▓    ██
  ▒▒▒▒▒▒        ▒▒▒▒▒▒        ░░▒▒▒▒      ██        ██
  ▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒      ░░        ░░
  ▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒      ▓▓▒▒▒▒
  ▒▒▒▒▒▒    ░░▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒    ▒▒▒▒    ▒▒▒▒▒▒░░▒▒▒▒▓▓░░      ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▒▒▒▒▒▒    ▒▒▒▒░░▒▒▒▒  ░░▒▒▒▒▒▒    ░░▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
  ▒▒▒▒▒▒  ▒▒▒▒▒▒░░▒▒▒▒  ▒▒▒▒▒▒▒▒    ▒▒▒▒░░    ▒▒▒▒░░    ▒▒▒▒▒▒  ░░▒▒▒▒▒▒      ▒▒▒▒░░
  ▒▒▒▒▒▒░░▓▓▒▒    ▒▒▒▒░░▒▒▒▒▒▒      ▒▒▒▒    ░░▒▒▒▒      ▒▒▒▒▒▒  ▒▒▒▒▒▒      ░░▒▒▒▒           Dm @JC2 for any issues.
  ▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒░░      ▒▒▒▒    ▒▒▒▒▒▒      ▒▒▒▒▒▒  ▒▒▒▒▒▒      ▒▒▒▒▒▒
  ▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒      ░░▒▒▒▒    ▒▒▒▒▒▒    ░░▒▒▒▒░░  ▒▒▓▓▒▒      ▒▒▒▒▒▒
  ▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒
  ▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒          ▒▒▒▒▒▒  ▒▒▒▒▒▒      ▒▒▒▒▒▒    ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                                                                          ▒▒▒▒▒▒
                                                                          ▒▒▒▒▒▒
            Wing Checker: More Efficient, Easier, Better.               ░░▒▒▒▒░░
                            FEATURES BELOW:                             ▒▒▒▒
            type afk, lowmic, screenshare to trigger checker.         ▒▒▒▒
            type '.stop' to stop the checker.                     ░░▒▒░░
                                                                ▒▒
"""))

def print_menu():
    print(Colorate.Horizontal(Colors.rainbow, """
╔════════════════════════════════════════════════════════╗
║                      SOCIALS:                          ║
║          @jc2 on discord, @temp280 on tele             ║
╚════════════════════════════════════════════════════════╝
"""))

def clear_and_show_ascii():
    clear_screen()
    print_ascii_art()

def countdown_clear(seconds=5):
    for i in range(seconds, 0, -1):
        print(Colorate.Horizontal(Colors.yellow_to_green, f"Clearing in {i}... "), end='\r')
        time.sleep(1)
    clear_and_show_ascii()

spam_running = False
rate_limit_message_shown = False
mentioned_users_status = {}

async def spam_messages(client, channel, count, mentioned_users):
    global spam_running, rate_limit_message_shown, mentioned_users_status

    clear_and_show_ascii()
    spam_running = True
    rate_limit_message_shown = False
    mentioned_users_status = {user: False for user in mentioned_users}

    fast_rate = 0
    slow_rate = 1.7

    latency = round(client.latency * 1000)
    print(Colorate.Horizontal(Colors.blue_to_white,
        f"[{time.strftime('%H:%M:%S')}] Countdown started | Latency: {latency}ms | Number: {count}"
    ))

    i = count
    while i >= 0:
        if not spam_running:
            countdown_clear()
            return

        try:
            await channel.send(f"{i}")
            await asyncio.sleep(slow_rate if i < 30 else fast_rate)
            i -= 1
        except discord.errors.HTTPException as e:
            if e.status == 429:
                if not rate_limit_message_shown:
                    print(Colorate.Horizontal(Colors.red_to_white, "[!] Ratelimited, slowing down now."))
                    rate_limit_message_shown = True
                await asyncio.sleep(slow_rate)
                continue
            else:
                raise e

    if spam_running:
        Write.Print("Finished, now clearing.\n", Colors.blue, interval=0.05)
        await channel.send("Done with check.")
        countdown_clear()

    # PASSED / FAILED logs
    for user, responded in mentioned_users_status.items():
        tag = f"{user.name}#{user.discriminator}"
        if responded:
            print(Colorate.Horizontal(Colors.green_to_white, f"[+] {tag} | PASSED"))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f"[-] {tag} | FAILED"))

async def main():
    global spam_running, rate_limit_message_shown, mentioned_users_status

    set_title()
    clear_and_show_ascii()

    try:
        token = input(Colorate.Horizontal(Colors.rainbow, "Token = ")).strip()
        clear_and_show_ascii()
        count = int(input(Colorate.Horizontal(Colors.rainbow, "Check Number = ")).strip())
        clear_and_show_ascii()
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"[!] Input error: {e}"))
        input("Press ENTER to exit...")
        return

    spam_running = False
    rate_limit_message_shown = False
    mentioned_users_status = {}

    intents = discord.Intents.default()
    intents.messages = True
    intents.guilds = True
    if hasattr(intents, "message_content"):
        intents.message_content = True

    client = discord.Client(intents=intents)
    owner_id = None

    @client.event
    async def on_ready():
        nonlocal owner_id
        owner_id = client.user.id
        clear_and_show_ascii()
        print_menu()

    @client.event
    async def on_message(message):
        global spam_running, mentioned_users_status

        if message.author.bot:
            return

        # Track responses
        for user in mentioned_users_status:
            if user.id == message.author.id and not mentioned_users_status[user]:
                mentioned_users_status[user] = True
                print(Colorate.Horizontal(Colors.green_to_white,
                      f"[{time.strftime('%H:%M:%S')}] [+] User {user} responded."))
                break

        if message.author.id == owner_id:
            trigger_words = ["afk", "lowmic", "screenshare"]
            if any(word in message.content.lower() for word in trigger_words):
                mentioned_users = message.mentions if message.mentions else []
                await spam_messages(client, message.channel, count, mentioned_users)

            if ".stop" in message.content.lower():
                spam_running = False
                Write.Print("[!] Afk checker stopped by command, double clearing incase of extras.\n", Colors.yellow, interval=0.05)
                countdown_clear()

    try:
        await client.start(token, bot=False)
    except discord.LoginFailure:
        Write.Print(f"[-] Token invalid: {token}", Colors.red, interval=0.05)
    except Exception as e:
        Write.Print(f"[!] An error occurred: {e}", Colors.red, interval=0.05)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"[!] Unhandled exception: {e}"))
    input(Colorate.Horizontal(Colors.red_to_white, "Press ENTER to exit..."))