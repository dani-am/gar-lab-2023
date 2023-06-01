import asyncio
import telegram
import subprocess
import re

# Configura el token del bot y el chat ID de destino
bot_token = '5723725362:AAHM-OxcJdcZSBEN-DA4wXSE13PPmND3irE'
chat_id = '-929326885'

# Crea el objeto bot
bot = telegram.Bot(token=bot_token)
process = None
command = "sudo docker-compose up" #comando a monitorizar
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

async def send_command_output():
    last_message = ""
    server_start_count = 31
    sending_count = 0
    message = ""

    while True:
        output = process.stdout.readline().decode().strip()
        print(output)
        if output == '' and process.poll() is not None:
            break
        if output:
            if output == last_message:
                continue
            if server_start_count > 0 and ("haproxy" in output or "backend" in output):
                server_start_count -= 1
            if server_start_count == 0 and ("haproxy" in output or "backend" in output) :
                if sending_count !=2 and (server_start_count == 0 and ("haproxy" in output or "backend" in output)):
                    sending_count += 1
                    message = message + "\n" + output
                if sending_count == 2 and (server_start_count == 0 and ("haproxy" in output or "backend" in output)):
                    sending_count = 0
                    try:
                        await bot.send_message(chat_id=chat_id, text=message)
                        message = ""
                    except telegram.error.TimedOut:
                        print("Timed out while sending message. Retrying in next iteration.")
                        await asyncio.sleep(10)
            last_message = output

    await asyncio.sleep(1)

while True:
    try:
        # Llama a la función asincrónica
        asyncio.run(send_command_output())
    except Exception as e:
        print(f"Error: {e}. Retrying in next iteration.")

