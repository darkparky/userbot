"""
Time In Profile Pic.....
Command: `.ahpp


#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/ee59dc8d80f42b689797c.jpg",
                         "https://telegra.ph/file/0b44260c071dc940deb0f.jpg",
                         "https://telegra.ph/file/b29084acee22e3c28629b.jpg",
                         "https://telegra.ph/file/7a2012343d53955e0ebcc.jpg",
                         "https://telegra.ph/file/745f6e31cfcc398ef7a3e.jpg",
                         "https://telegra.ph/file/ac3852ba1058420eea9c9.jpg",
                         "https://telegra.ph/file/e70d78e683d9d6b8bb98c.jpg",
                         "https://telegra.ph/file/d362954d77d3962e9858e.jpg",
                         "https://telegra.ph/file/8ee1fdbad05258961f7d0.jpg",
                         "https://telegra.ph/file/02b78a8b1870891de8279.jpg",
                         "https://telegra.ph/file/ca85641daf60aa9b01265.jpg",
                         "https://telegra.ph/file/2243b797c2b2820f71439.jpg",
                         "https://telegra.ph/file/d587f76be381cdb532e2d.jpg",
                         "https://telegra.ph/file/fb72a199a21f21afd7686.jpg",
                         "https://telegra.ph/file/041fdc859953b30be1ec7.jpg",
                         "https://telegra.ph/file/fab3332db920667c4987a.jpg",
                         "https://telegra.ph/file/bb2926daea218f405d5e6.jpg",
                         "https://telegra.ph/file/14ed50e3242ead423e596.jpg",
                         "https://telegra.ph/file/6262abd9aecde16bdc499.jpg",
                         "https://telegra.ph/file/56f5dd562d729b8afe573.jpg",
                         "https://telegra.ph/file/16b11558e3da34d697c87.jpg",
                         "https://telegra.ph/file/89cb3e99e466bfb32336f.jpg",
                         "https://telegra.ph/file/0ed9e06c3d44786aca1ae.jpg",
                         "https://telegra.ph/file/b0b55111becbf3d31698f.jpg",
                         "https://telegra.ph/file/d9a8c5ff61a17389a0681.jpg",
                         "https://telegra.ph/file/9dc924f291602f4d510b5.jpg",
                         "https://telegra.ph/file/85ca7917cf75002cbb104.jpg",
                         "https://telegra.ph/file/6bf445c5d8560ddd394d9.jpg",
                         "https://telegra.ph/file/b57ba3b7bb20567f759bd.jpg",
                         "https://telegra.ph/file/817c1d8eff3dbd1c58fdd.jpg",
                         "https://telegra.ph/file/14530dacce630e54ce6f7.jpg",
                         "https://telegra.ph/file/ea5cc411c7cc2fdc00521.jpg",
                         "https://telegra.ph/file/04088f90402fc689d1f17.jpg",
                         "https://telegra.ph/file/389ea7d551d69788bda2b.jpg",
                         "https://telegra.ph/file/fa5725380fc00bb1934be.jpg",
                         "https://telegra.ph/file/fbfcfa7fc71747a767cae.jpg",
                         "https://telegra.ph/file/26031bbbbbe3814b35a55.jpg",
                         "https://telegra.ph/file/3109a56babe99d014b189.jpg",
                         "https://telegra.ph/file/138eee250858d2b4a33c2.jpg",
                         "https://telegra.ph/file/7d9ff769818201343de86.jpg",
                         "https://telegra.ph/file/1e1423d75d477057bd1c5.jpg",
                         "https://telegra.ph/file/4a92b75016ac765ac6911.jpg",
                         "https://telegra.ph/file/e6f757e656f65c868f190.jpg",
                         "https://telegra.ph/file/4958764131e72f74ecadf.jpg",
                         "https://telegra.ph/file/a12c1053417bd9dcc040f.jpg",
                         "https://telegra.ph/file/e08e786c35fe65ea9a5e0.jpg",
                         "https://telegra.ph/file/7afb2d4569dbea3b339d3.jpg",
                         "https://telegra.ph/file/d52f3a1f37e774a588a5c.jpg",
                         "https://telegra.ph/file/1b1ee108a80e1379711fa.jpg",
                         "https://telegra.ph/file/75cfc840a81a0e14f5a51.jpg",
                         "https://telegra.ph/file/5c0ab0d2f25e423ee183d.jpg",
                         "https://telegra.ph/file/934eff84e56f15075d1f4.jpg",
                         "https://telegra.ph/file/7b780f0736f75d81333bc.jpg",
                         "https://telegra.ph/file/a6ef057807f6fb7d0bca6.jpg",
                         "https://telegra.ph/file/20d25834e0bab5147363e.jpg",
                         "https://telegra.ph/file/aa671136b796ffe89eb1c.jpg",
                         "https://telegra.ph/file/7b02e0029803e268167c6.jpg",
                         "https://telegra.ph/file/676f823326d5c47fcf4ea.jpg",
                         "https://telegra.ph/file/dadfeccf211b0a8c58369.jpg",
                         "https://telegra.ph/file/7df0e2a7d42f57203c40b.jpg",
                         "https://telegra.ph/file/2c72bff8dd48433effb79.jpg",
                         "https://telegra.ph/file/ff58d9a8822f4c22e5892.jpg",
                         "https://telegra.ph/file/5339345662d3a7a555dbc.jpg",
                         "https://telegra.ph/file/3b95613e91307958e7e8c.jpg"
                        ]
@borg.on(admin_cmd(pattern="ahpp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./ravana/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((200, 250), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(900)
        except:
            return
