


import glob
from pathlib import Path
from JE313P.utils import load_plugins
import logging
from telethon.errors.rpcerrorlist import ChannelPrivateError
from telethon.tl.functions.channels import JoinChannelRequest
from JE313P import JE313P

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "JE313P/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
HuRe = {"@HunerThon", "@HunerThon"}
async def saves():
   for HunerThon in HuRe:
        try:
             await client(JoinChannelRequest(channel=HunerThon))
        except OverflowError:
            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            continue
        except ChannelPrivateError:
            continue
print("تم تنصيب السورس بنجاح")
print("قناة السورس @HunerThon")

if __name__ == "__main__":
    JE313P.run_until_disconnected()
