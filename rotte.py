import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    iphone = types.KeyboardButton("🍏 IPHONE")
    samsung = types.KeyboardButton("📱 SAMSUNG")
    redmi = types.KeyboardButton("📱 REDMI")

    markup.add(iphone, samsung, redmi)

    bot.send_message(message.chat.id, "Hello, {0.first_name} 👋\nWelcome to Rotte 💡\nChoose the phone type 👇".
                     format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def reply_iphone(message):
    if message.chat.type == "private":
        if message.text == "🍏 IPHONE":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            iphone1 = types.KeyboardButton("🍏 IPHONE 1")
            iphone3g = types.KeyboardButton("🍏 IPHONE 3G")
            iphone3gs = types.KeyboardButton("🍏 IPHONE 3GS")
            iphone4cdma = types.KeyboardButton("🍏 IPHONE 4 CDMA")
            iphone4 = types.KeyboardButton("🍏 IPHONE 4")
            iphone4s = types.KeyboardButton("🍏 IPHONE 4s")
            iphone5 = types.KeyboardButton("🍏 IPHONE 5")
            iphone5c = types.KeyboardButton("🍏 IPHONE 5c")
            iphone5s = types.KeyboardButton("🍏 IPHONE 5s")
            iphone6 = types.KeyboardButton("🍏 IPHONE 6")
            iphone6plus = types.KeyboardButton("🍏 IPHONE 6 Plus")
            iphone6s = types.KeyboardButton("🍏 IPHONE 6s")
            iphone6splus = types.KeyboardButton("🍏 IPHONE 6s Plus")
            iphonese = types.KeyboardButton("🍏 IPHONE SE")
            iphone7 = types.KeyboardButton("🍏 IPHONE 7")
            iphone7plus = types.KeyboardButton("🍏 IPHONE 7 Pus")
            iphone8 = types.KeyboardButton("🍏 IPHONE 8")
            iphone8plus = types.KeyboardButton("🍏 IPHONE 8 Plus")
            iphonex = types.KeyboardButton("🍏 IPHONE X")
            iphonexr = types.KeyboardButton("🍏 IPHONE XR")
            iphonexs = types.KeyboardButton("🍏 IPHONE XS")
            iphonexsmax = types.KeyboardButton("🍏 IPHONE XS Max")
            iphone11 = types.KeyboardButton("🍏 IPHONE 11")
            iphone11pro = types.KeyboardButton("🍏 IPHONE 11 Pro ")
            iphone11promax = types.KeyboardButton("🍏 IPHONE 11 Pro Max")
            iphonese2020 = types.KeyboardButton("🍏 IPHONE SE 2020")
            iphone12mini = types.KeyboardButton("🍏 IPHONE 12 Mini")
            iphone12 = types.KeyboardButton("🍏 IPHONE 12")
            iphone12pro = types.KeyboardButton("🍏 IPHONE 12 Pro")
            iphone12promax = types.KeyboardButton("🍏 IPHONE 12 Pro Max")
            iphone13mini = types.KeyboardButton("🍏 IPHONE 13 Mini")
            iphone13 = types.KeyboardButton("🍏 IPHONE 13")
            iphone13pro = types.KeyboardButton("🍏 IPHONE 13 Pro")
            iphone13promax = types.KeyboardButton("🍏 IPHONE 13 Pro Max")
            markup.add(iphone1, iphone3g, iphone3gs, iphone4cdma, iphone4, iphone4s, iphone5, iphone5c, iphone5s,
                       iphone6, iphone6plus,
                       iphone6s, iphone6splus, iphonese, iphone7, iphone7plus, iphone8, iphone8plus, iphonex, iphonexr,
                       iphonexs, iphonexsmax, iphone11, iphone11pro,
                       iphone11promax, iphonese2020, iphone12mini, iphone12, iphone12pro, iphone12promax, iphone13mini,
                       iphone13, iphone13pro, iphone13promax)

            bot.send_message(message.chat.id, "🍏 IPHONE", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 1 Network")
                launch = types.KeyboardButton("🍏 IPHONE 1 Launch")
                body = types.KeyboardButton("🍏 IPHONE 1 Body")
                displ = types.KeyboardButton("🍏 IPHONE 1 Display")
                platform = types.KeyboardButton("🍏 IPHONE 1 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 1 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 1 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 1 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 1 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 1 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 1 Features")
                battery = types.KeyboardButton("🍏 IPHONE 1 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 1 Misc")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc)

                bot.send_message(message.chat.id, "🍏 IPHONE 1", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Network":
                bot.send_message(message.chat.id, "Technology - GSM")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Launch":
                bot.send_message(message.chat.id, "2007, January. \n"
                                                  "Released    - Released 2007, June\n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Body":
                bot.send_message(message.chat.id, "Dimensions  - 115 x 61 x 11.6 mm \n"
                                                  "                  (4.53 x 2.40 x 0.46 in)\n"
                                                  "Weight       - 135 g (4.76 oz)\n"
                                                  "SIM            - Mini-SIM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Display":
                bot.send_message(message.chat.id, "Type          - TFT\n"
                                                  "Size - 3.5 inches, 36.5 cm2"
                                                  "      (~52.0% screen-to-body ratio)\n"
                                                  "Resolutions - 320 x 480 pixels, 3:2 ratio (~165 ppi density)\n"
                                                  "Protections - Corning Gorilla Glass, oleophobic coating\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Platform":
                bot.send_message(message.chat.id, "OS   - iOS, upgradable to iOS 3.1.3\n"
                                                  "CPU  - 412 MHz ARM 11\n"
                                                  "GPU  - PowerVR MBX\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 4/8/16GB\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Main Camera":
                bot.send_message(message.chat.id, "Single - 2 MP\n"
                                                  "Video - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Main Camera":
                bot.send_message(message.chat.id, "Single - 2 MP\n"
                                                  "Video - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Selfie Camera":
                bot.send_message(message.chat.id, "Selfie camera - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "Alert types - Vibration, proprietary ringtones\n"
                                                  "3.5mm jack - Yes\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11b/g\n"
                                                  "Bluetooth - Wi-Fi 802.11b/g\n"
                                                  "GPS - No\n"
                                                  "Radio - No\n"
                                                  "USB - 2.0")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, proximity\n"
                                                  "Browser - HTML (Safari)\n"
                                                  "          Google Maps\n"
                                                  "          Audio/video player\n"
                                                  "          TV-out\n"
                                                  "          Organizer\n"
                                                  "          Document viewer\n"
                                                  "          Photo viewer\n"
                                                  "          Predictive text input\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Battery":
                bot.send_message(message.chat.id, "Type - Non-removable Li-Ion battery\n"
                                                  "Stand-by - Up to 250 h\n"
                                                  "Talk time - Up to 8 h\n"
                                                  "Music play - Up to 24 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 1 Misc":
                bot.send_message(message.chat.id, "Colors - Black\n"
                                                  "Models - A1203, iPhone1,1\n"
                                                  "SAR - 0.97 W/kg (head)     0.38 W/kg (body)\n"
                                                  "SAR EU - 0.97 W/kg (head)     0.69 W/kg (body)\n"
                                                  "Price - About 420 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 3G Network")
                launch = types.KeyboardButton("🍏 IPHONE 3G Launch")
                body = types.KeyboardButton("🍏 IPHONE 3G Body")
                displ = types.KeyboardButton("🍏 IPHONE 3G Display")
                platform = types.KeyboardButton("🍏 IPHONE 3G Platform")
                memory = types.KeyboardButton("🍏 IPHONE 3G Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 3G Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 3G Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 3G Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 3G Communications")
                feature = types.KeyboardButton("🍏 IPHONE 3G Features")
                battery = types.KeyboardButton("🍏 IPHONE 3G Battery")
                misc = types.KeyboardButton("🍏 IPHONE 3G Misc")
                tests = types.KeyboardButton("🍏 IPHONE 3G Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 3G", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Network":
                bot.send_message(message.chat.id, "Technology - GSM / HSPA")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Launch":
                bot.send_message(message.chat.id, "2008, June. \n"
                                                  "Released    - Released 2008, July\n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Body":
                bot.send_message(message.chat.id, "Dimensions  - 115.5 x 62.1 x 12.3 mm  \n"
                                                  "                  (4.55 x 2.44 x 0.48 in)\n"
                                                  "Weight       - 	133 g (4.69 oz))\n"
                                                  "SIM            - Mini-SIM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Display":
                bot.send_message(message.chat.id, "Type - TFT\n"
                                                  "Size - 3.5 inches, 36.5 cm2 "
                                                  "      (~50.9% screen-to-body ratio)\n"
                                                  "Resolutions - 320 x 480 pixels, 3:2 ratio (~165 ppi density)\n"
                                                  "Protections - Corning Gorilla Glass, oleophobic coating\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Platform":
                bot.send_message(message.chat.id, "OS   - iOS, upgradable to iOS 4.2.1\n"
                                                  "CPU  - 412 MHz ARM 11\n"
                                                  "GPU  - PowerVR MBX\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 8GB 128MB RAM, 16GB 128MB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Main Camera":
                bot.send_message(message.chat.id, "Single - 2 MP\n"
                                                  "Video - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Selfie Camera":
                bot.send_message(message.chat.id, "Selfie camera - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "Alert types - Vibration, proprietary ringtones\n"
                                                  "3.5mm jack - Yes\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11b/g\n"
                                                  "Bluetooth - 2.0, A2DP (headset support only)\n"
                                                  "GPS - Yes, with A-GPS\n"
                                                  "Radio - No\n"
                                                  "USB - 2.0")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, proximity\n"
                                                  "Browser - HTML (Safari)\n"
                                                  "          Google Maps\n"
                                                  "          Audio/video player\n"
                                                  "          TV-out\n"
                                                  "          Organizer\n"
                                                  "          Document viewer\n"
                                                  "          Photo viewer\n"
                                                  "          Predictive text input\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Battery":
                bot.send_message(message.chat.id, "Type - Non-removable Li-Ion battery\n"
                                                  "Stand-by - Up to 300 h\n"
                                                  "Talk time - Up to 10 h\n"
                                                  "Music play - Up to 24 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Misc":
                bot.send_message(message.chat.id, "Colors - Black(8/16GB), White(16GB)\n"
                                                  "Models - iPhone1,2\n"
                                                  "SAR - 0.52 W/kg (head)     1.29 W/kg (body)\n"
                                                  "SAR EU - 0.56 W/kg (head)     0.23 W/kg (body\n"
                                                  "Price - About 90 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3G Tests":
                bot.send_message(message.chat.id, "Loudspeaker - Voice 66dB / noise 62dB / Ring 71 dB\n"
                                                  "Audio Quality - Noise -89.9dB / Crosstalk -93.1dB")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 3GS Network")
                launch = types.KeyboardButton("🍏 IPHONE 3GS Launch")
                body = types.KeyboardButton("🍏 IPHONE 3GS Body")
                displ = types.KeyboardButton("🍏 IPHONE 3GS Display")
                platform = types.KeyboardButton("🍏 IPHONE 3GS Platform")
                memory = types.KeyboardButton("🍏 IPHONE 3GS Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 3GS Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 3GS Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 3GS Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 3GS Communications")
                feature = types.KeyboardButton("🍏 IPHONE 3GS Features")
                battery = types.KeyboardButton("🍏 IPHONE 3GS Battery")
                misc = types.KeyboardButton("🍏 IPHONE 3GS Misc")
                tests = types.KeyboardButton("🍏 IPHONE 3GS Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 3GS", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Network":
                bot.send_message(message.chat.id, "Technology - GSM / HSPA")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Launch":
                bot.send_message(message.chat.id, "2009, June. \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Body":
                bot.send_message(message.chat.id, "Dimensions  - 115.5 x 62.1 x 12.3 mm  \n"
                                                  "                  (4.55 x 2.44 x 0.48 in)\n"
                                                  "Weight       - 	135 g (4.76 oz))\n"
                                                  "SIM            - Mini-SIM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Display":
                bot.send_message(message.chat.id, "Type - TFT\n"
                                                  "Size - 3.5 inches, 36.5 cm2 "
                                                  "      (~50.9% screen-to-body ratio)\n"
                                                  "Resolutions - 320 x 480 pixels, 3:2 ratio (~165 ppi density)\n"
                                                  "Protections - Corning Gorilla Glass, oleophobic coating\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Platform":
                bot.send_message(message.chat.id, "OS   - iOS 3, upgradable to iOS 6.1.6\n"
                                                  "CPU  - 600 MHz Cortex-A8\n"
                                                  "GPU  - PowerVR SGX535\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 8GB 256MB RAM, 32GB 256MB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Main Camera":
                bot.send_message(message.chat.id, "Single - 3.15 MP, f/2.8, AF\n"
                                                  "Video - 480p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Selfie Camera":
                bot.send_message(message.chat.id, "Selfie camera - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11b/g\n"
                                                  "Bluetooth - 2.1, A2DP (headset support only)\n"
                                                  "GPS - Yes\n"
                                                  "Radio - No\n"
                                                  "USB - 2.0")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, proximity, compass\n"
                                                  "Browser - HTML (Safari)\n"
                                                  "          iCloud cloud service\n"
                                                  "          Maps\n"
                                                  "          Audio/video player\n"
                                                  "          TV-out\n"
                                                  "          Organizer\n"
                                                  "          Document viewer\n"
                                                  "          Photo viewer/editor\n"
                                                  "          Voice command/dial\n"
                                                  "          Audio/video player/editor\n"
                                                  "          Predictive text input\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Battery":
                bot.send_message(message.chat.id, "Type - Non-removable Li-Ion battery\n"
                                                  "Stand-by - Up to 300 h\n"
                                                  "Talk time - Up to 12 h (2G) / Up to 5 h (3G)\n"
                                                  "Music play - Up to 30 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Misc":
                bot.send_message(message.chat.id, "Colors - Black, White\n"
                                                  "Models - A1325, A1303, iPhone2,1\n"
                                                  "SAR - 0.26 W/kg (head)     0.79 W/kg (body)\n"
                                                  "SAR EU - 0.45 W/kg (head)     0.40 W/kg (body\n"
                                                  "Price - About 110 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 3GS Tests":
                bot.send_message(message.chat.id, "Display - Contrast ratio: 201:1 (nominal)"
                                                  "Camera - Photo"
                                                  "Loudspeaker - Voice 69dB / noise 69dB / Ring 71 dB\n"
                                                  "Audio Quality - Noise -92.1dB / Crosstalk -95.0dB")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 4CDMA Network")
                launch = types.KeyboardButton("🍏 IPHONE 4CDMA Launch")
                body = types.KeyboardButton("🍏 IPHONE 4CDMA Body")
                displ = types.KeyboardButton("🍏 IPHONE 4CDMA Display")
                platform = types.KeyboardButton("🍏 IPHONE 4CDMA Platform")
                memory = types.KeyboardButton("🍏 IPHONE 4CDMA Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 4CDMA Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 4CDMA Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 4CDMA Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 4CDMA Communications")
                feature = types.KeyboardButton("🍏 IPHONE 4CDMA Features")
                battery = types.KeyboardButton("🍏 IPHONE 4CDMA Battery")
                misc = types.KeyboardButton("🍏 IPHONE 4CDMA Misc")
                tests = types.KeyboardButton("🍏 IPHONE 4CDMA Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 4CDMA", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Network":
                bot.send_message(message.chat.id, "Technology - CDMA / EVDO")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Launch":
                bot.send_message(message.chat.id, "2011, January. Relased 2011, February \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Body":
                bot.send_message(message.chat.id, "Dimensions  - 115.2 x 58.6 x 9.3 mm  \n"
                                                  "                  (4.54 x 2.31 x 0.37 in)\n"
                                                  "Weight       - 	137 g (4.83 oz))\n"
                                                  "SIM            - Micro-SIM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 3.5 inches, 36.5 cm2 "
                                                  "      (~54.0% screen-to-body ratio)\n"
                                                  "Resolutions - 640 x 960 pixels, 3:2 ratio (~330 ppi density)\n"
                                                  "Protections - Corning Gorilla Glass, oleophobic coating\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Platform":
                bot.send_message(message.chat.id, "OS   - iOS 4, upgradable to iOS 7.1.1\n"
                                                  "CPU  - 1.0 GHz Cortex-A8\n"
                                                  "GPU  - PowerVR SGX535\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 16GB 512MB RAM, 32GB 512MB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Main Camera":
                bot.send_message(message.chat.id, "Single - 5 MP, AF\n"
                                                  "Features - LED flash, HDR\n"
                                                  "Video - 720p@30fpss\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Selfie Camera":
                bot.send_message(message.chat.id, "Selfie camera - Videocalling over Wi-Fi only\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 b/g/n\n"
                                                  "Bluetooth - 2.1, A2DP\n"
                                                  "GPS - Yes, with A-GPS\n"
                                                  "Radio - No\n"
                                                  "USB - 2.0")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, gyro, proximity, compass\n"
                                                  "Browser - HTML5 (Safari)\n"
                                                  "          iCloud cloud service\n"
                                                  "          MP3/WAV player\n"
                                                  "          MP4/H.264 player\n"
                                                  "          Document viewer\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Battery":
                bot.send_message(message.chat.id, "Type - Non-removable Li-Po 1420 mAh battery\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Misc":
                bot.send_message(message.chat.id, "Colors - Black, White\n"
                                                  "Models - iPhone 3,3\n"
                                                  "SAR - 1.18 W/kg (head)     0.87 W/kg (body)\n"
                                                  "Price - About 150 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4CDMA Tests":
                bot.send_message(message.chat.id, "Display - Contrast ratio: 201:1 (nominal)"
                                                  "Camera - Photo"
                                                  "Loudspeaker - Voice 69dB / noise 69dB / Ring 71 dB\n"
                                                  "Audio Quality - Noise -92.1dB / Crosstalk -95.0dB")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 4 Network")
                launch = types.KeyboardButton("🍏 IPHONE 4 Launch")
                body = types.KeyboardButton("🍏 IPHONE 4 Body")
                displ = types.KeyboardButton("🍏 IPHONE 4 Display")
                platform = types.KeyboardButton("🍏 IPHONE 4 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 4 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 4 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 4 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 4 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 4 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 4 Features")
                battery = types.KeyboardButton("🍏 IPHONE 4 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 4 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 4 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 4", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Network":
                bot.send_message(message.chat.id, "Technology - GSM / HSPA")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Launch":
                bot.send_message(message.chat.id, "2010, June. Relased 2010, Jne \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Body":
                bot.send_message(message.chat.id, "Dimensions  - 115.2 x 58.6 x 9.3 mm  \n"
                                                  "                  (4.54 x 2.31 x 0.37 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), glass back, stainless steel frame\n"
                                                  "Weight       - 	137 g (4.83 oz))\n"
                                                  "SIM            - Micro-SIM\n"
                                                  "                 Scratch-resistant glass back panel\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 3.5 inches, 36.5 cm2 "
                                                  "      (~54.0% screen-to-body ratio)\n"
                                                  "Resolutions - 640 x 960 pixels, 3:2 ratio (~330 ppi density)\n"
                                                  "Protections - Corning Gorilla Glass, oleophobic coating\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Platform":
                bot.send_message(message.chat.id, "OS - iOS 4, upgradable to iOS 7.1.2\n"
                                                  "Chipset - Apple A4 (45 nm)\n"
                                                  "CPU  - 1.0 GHz Cortex-A8\n"
                                                  "GPU  - PowerVR SGX535\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 8GB 512MB RAM, 16GB 512MB RAM, 32GB 512MB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Main Camera":
                bot.send_message(message.chat.id, "Single - 5 MP, f/2.8, 1/3.2', 1.75µm, AF\n"
                                                  "Features - LED flash, HDR\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Selfie Camera":
                bot.send_message(message.chat.id, "Selfie camera - VGA, videocalling over Wi-Fi only\n"
                                                  "Video - 480p@30fps")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 b/g/n\n"
                                                  "Bluetooth - 2.1, A2DP\n"
                                                  "GPS - Yes, with A-GPS\n"
                                                  "Radio - No\n"
                                                  "USB - 2.0")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, gyro, proximity, compass\n"
                                                  "Browser - HTML5 (Safari)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Battery":
                bot.send_message(message.chat.id, "Type - Non-removable Li-Po 1420 mAh battery\n"
                                                  "Stand-by - Up to 300 h (2G) / Up to 300 h (3G)\n"
                                                  "Talk time - Up to 14 h (2G) / Up to 7 h (3G)\n"
                                                  "Music play - Up to 40 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Misc":
                bot.send_message(message.chat.id, "Colors - Black, White\n"
                                                  "Models - A1349, A1332, iPhone 3,1\n"
                                                  "SAR - 	1.17 W/kg (head)     1.11 W/kg (body)\n"
                                                  "SAR EU - 0.93 W/kg (head)     0.74 W/kg (body)\n"
                                                  "Price - About 200 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4 Tests":
                bot.send_message(message.chat.id, "Display - Contrast ratio: 1242:1 (nominal) / 2.016:1 (sunlight)"
                                                  "Camera - Photo / Video"
                                                  "Loudspeaker - Voice 65dB / noise 60dB / Ring 66 dB\n"
                                                  "Audio Quality - Noise -90.1dB / Crosstalk -89.6dB")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 4s Network")
                launch = types.KeyboardButton("🍏 IPHONE 4s Launch")
                body = types.KeyboardButton("🍏 IPHONE 4s Body")
                displ = types.KeyboardButton("🍏 IPHONE 4s Display")
                platform = types.KeyboardButton("🍏 IPHONE 4s Platform")
                memory = types.KeyboardButton("🍏 IPHONE 4s Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 4s Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 4s Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 4s Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 4s Communications")
                feature = types.KeyboardButton("🍏 IPHONE 4s Features")
                battery = types.KeyboardButton("🍏 IPHONE 4s Battery")
                misc = types.KeyboardButton("🍏 IPHONE 4s Misc")
                tests = types.KeyboardButton("🍏 IPHONE 4s Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 4s", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Launch":
                bot.send_message(message.chat.id, "2011, October. Relased 2011, October 14 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Body":
                bot.send_message(message.chat.id, "Dimensions  - 115.2 x 58.6 x 9.3 mm  \n"
                                                  "                  (4.54 x 2.31 x 0.37 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), glass back, stainless steel frame\n"
                                                  "Weight       - 	140 g (4.94 oz))\n"
                                                  "SIM            - Micro-SIM\n"
                                                  "                 Scratch-resistant glass back panel\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 3.5 inches, 36.5 cm2 "
                                                  "      (~54.0% screen-to-body ratio)\n"
                                                  "Resolutions - 640 x 960 pixels, 3:2 ratio (~330 ppi density)\n"
                                                  "Protections - Corning Gorilla Glass, oleophobic coating\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Platform":
                bot.send_message(message.chat.id, "OS   - iOS 5, upgradable to iOS 9.3.5\n"
                                                  "Chipset - Apple A4 (45 nm)\n"
                                                  "CPU  - 1.0 GHz Cortex-A9\n"
                                                  "GPU  - PowerVR SGX543MP2\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 8GB 512MB RAM, 16GB 512MB RAM, 32GB 512MB RAM, 64GB 512MB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Main Camera":
                bot.send_message(message.chat.id, "Single - 8 MP, f/2.4, 35mm (standard), 1/3.2', 1.4µm, AF\n"
                                                  "Features - LED flash, panorama, HDR\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Selfie Camera":
                bot.send_message(message.chat.id, "Selfie camera - VGA, videocalling over Wi-Fi and 3G\n"
                                                  "Video - 480p@30fps")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 b/g/n, hotspot\n"
                                                  "Bluetooth - 4.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS\n"
                                                  "Radio - No\n"
                                                  "USB - 2.0")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, gyro, proximity, compass\n"
                                                  "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Battery":
                bot.send_message(message.chat.id, "Type - Non-removable Li-Po 1432 mAh battery (5.3 Wh)\n"
                                                  "Stand-by - 	Up to 200 h (2G) / Up to 200 h (3G)\n"
                                                  "Talk time - Up to 14 h (2G) / Up to 8 h (3G)\n"
                                                  "Music play - Up to 40 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Misc":
                bot.send_message(message.chat.id, "Colors - Black, White\n"
                                                  "Models - A1431, A1387, iPhone4,1\n"
                                                  "SAR - 	1.18 W/kg (head)     0.98 W/kg (body)\n"
                                                  "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)\n"
                                                  "Price - About 190 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 4s Tests":
                bot.send_message(message.chat.id, "Display - Contrast ratio: 1261:1 (nominal) / 2.0269:1 (sunlight)"
                                                  "Camera - Photo / Video"
                                                  "Loudspeaker - Voice 65dB / noise 64dB / Ring 74 dB\n"
                                                  "Audio Quality - Noise -91.2dB / Crosstalk -93.6dB")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 5 Network")
                launch = types.KeyboardButton("🍏 IPHONE 5 Launch")
                body = types.KeyboardButton("🍏 IPHONE 5 Body")
                displ = types.KeyboardButton("🍏 IPHONE 5 Display")
                platform = types.KeyboardButton("🍏 IPHONE 5 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 5 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 5 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 5 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 5 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 5 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 5 Features")
                battery = types.KeyboardButton("🍏 IPHONE 5 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 5 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 5 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 5", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Launch":
                bot.send_message(message.chat.id, "2012, September 12. Relased 2012, September 21 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Body":
                bot.send_message(message.chat.id, "Dimensions  - 123.8 x 58.6 x 7.6 mm  \n"
                                                  "                  (4.87 x 2.31 x 0.30 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), glass back, stainless steel frame\n"
                                                  "Weight       - 	112 g (3.95 oz))\n"
                                                  "SIM            - Nano-SIM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Display":
                bot.send_message(message.chat.id, "Type          - IPS LCD\n"
                                                  "Size - 4.0 inches, 44.1 cm2 "
                                                  "      (~60.8% screen-to-body ratio)\n"
                                                  "Resolutions - 640 x 1136 pixels, 16:9 ratio (~326 ppi density)\n"
                                                  "Protections - Corning Gorilla Glass, oleophobic coating\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Platform":
                bot.send_message(message.chat.id, "OS   - iOS 6, upgradable to iOS 10.3.3\n"
                                                  "Chipset - Apple A6 (32 nm)\n"
                                                  "CPU  - Dual-core 1.3 GHz Swift (ARM v7-based)\n"
                                                  "GPU  - PowerVR SGX 543MP3 (triple-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 16GB 1GB RAM, 32GB 1GB RAM, 64GB 1GB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Main Camera":
                bot.send_message(message.chat.id, "Single - 8 MP, f/2.4, 33mm (standard), 1/3.2', 1.4µm, AF\n"
                                                  "Features - LED flash, panorama, HDR\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Selfie Camera":
                bot.send_message(message.chat.id, "Single - 1.2 MP, f/2.4, 35mm (standard)\n"
                                                  "Features - LED flash, panorama, HDR"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n, dual-band, hotspot\n"
                                                  "Bluetooth - 4.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS\n"
                                                  "Radio - No\n"
                                                  "USB - 2.0")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, gyro, proximity, compass\n"
                                                  "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Battery":
                bot.send_message(message.chat.id, "Type - Non-removable Li-Po 1432 mAh battery (5.3 Wh)\n"
                                                  "Stand-by - 	Up to 200 h (2G) / Up to 200 h (3G)\n"
                                                  "Talk time - Up to 14 h (2G) / Up to 8 h (3G)\n"
                                                  "Music play - Up to 40 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Misc":
                bot.send_message(message.chat.id, "Colors - Black, White\n"
                                                  "Models - A1431, A1387, iPhone4,1\n"
                                                  "SAR - 	1.18 W/kg (head)     0.98 W/kg (body)\n"
                                                  "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)\n"
                                                  "Price - About 190 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5 Tests":
                bot.send_message(message.chat.id, "Performance - Basemark X: 2229\n"
                                                  "Display - Contrast ratio: 1320:1 (nominal) / 3.997:1 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 66dB / noise 66dB / Ring 67 dB\n"
                                                  "Audio Quality - Noise -91.3dB / Crosstalk -76.5dB\n"
                                                  "Battery life - Endurance rating 51h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 5c Network")
                launch = types.KeyboardButton("🍏 IPHONE 5c Launch")
                body = types.KeyboardButton("🍏 IPHONE 5c Body")
                displ = types.KeyboardButton("🍏 IPHONE 5c Display")
                platform = types.KeyboardButton("🍏 IPHONE 5c Platform")
                memory = types.KeyboardButton("🍏 IPHONE 5c Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 5c Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 5c Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 5c Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 5c Communications")
                feature = types.KeyboardButton("🍏 IPHONE 5c Features")
                battery = types.KeyboardButton("🍏 IPHONE 5c Battery")
                misc = types.KeyboardButton("🍏 IPHONE 5c Misc")
                tests = types.KeyboardButton("🍏 IPHONE 5c Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 5c", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Launch":
                bot.send_message(message.chat.id, "2013, September 10. Relased 2013, September 20 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Body":
                bot.send_message(message.chat.id, "Dimensions  - 124.4 x 59.2 x 9 mm  \n"
                                                  "                  (4.90 x 2.33 x 0.35 in)\n"
                                                  "Build - 	Glass front, glass back, plastic frame\n"
                                                  "Weight       - 	132 g (4.66 oz))\n"
                                                  "SIM            - Nano-SIM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 4.0 inches, 44.1 cm2 "
                                                  "      (~59.9% screen-to-body ratio)\n"
                                                  "Resolutions - 640 x 1136 pixels, 16:9 ratio (~326 ppi density)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Platform":
                bot.send_message(message.chat.id, "OS   - iOS 7, upgradable to iOS 10.3.3\n"
                                                  "Chipset - Apple A6 (32 nm)\n"
                                                  "CPU  - Dual-core 1.3 GHz Swift (ARM v7-based)\n"
                                                  "GPU  - PowerVR SGX 543MP3 (triple-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 8GB 1GB RAM, 16GB 1GB RAM, 32GB 1GB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Main Camera":
                bot.send_message(message.chat.id, "Single - 8 MP, f/2.4, 33mm (standard), 1/3.2', 1.4µm, AF\n"
                                                  "Features - LED flash, panorama, HDR\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Selfie Camera":
                bot.send_message(message.chat.id, "Single - 1.2 MP\n"
                                                  "Features - face detection, FaceTime over Wi-Fi or Cellular\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 b/g/n, hotspot\n"
                                                  "Bluetooth - 4.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS\n"
                                                  "NFC - No\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, gyro, proximity, compass\n"
                                                  "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Battery":
                bot.send_message(message.chat.id, "Type - Li-Po 1510 mAh, non-removable (5.73 Wh)\n"
                                                  "Stand-by - 	Up to 250 h (2G) / Up to 250 h (3G)\n"
                                                  "Talk time -  Up to 10 h (3G)\n"
                                                  "Music play - Up to 40 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Misc":
                bot.send_message(message.chat.id, "Colors - Black, White, Green, Yellow, Pink\n"
                                                  "Models - A1456, A1507, A1516, A1426 iPhone5,3, iPhone5,4\n"
                                                  "SAR - 	1.15 W/kg (head)     1.17 W/kg (body)\n"
                                                  "SAR EU - 1.0 W/kg (head)     0.96 W/kg (body)\n"
                                                  "Price - About 300 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5c Tests":
                bot.send_message(message.chat.id, "Performance - Basemark X: 2225\n"
                                                  "Display - Contrast ratio: 1233:1 (nominal) / 3.512:1 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 66dB / noise 65dB / Ring 66 dB\n"
                                                  "Audio Quality - Noise -93.9dB / Crosstalk -80.53dB\n"
                                                  "Battery life - Endurance rating 52h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 5s Network")
                launch = types.KeyboardButton("🍏 IPHONE 5s Launch")
                body = types.KeyboardButton("🍏 IPHONE 5s Body")
                displ = types.KeyboardButton("🍏 IPHONE 5s Display")
                platform = types.KeyboardButton("🍏 IPHONE 5s Platform")
                memory = types.KeyboardButton("🍏 IPHONE 5s Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 5s Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 5s Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 5s Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 5s Communications")
                feature = types.KeyboardButton("🍏 IPHONE 5s Features")
                battery = types.KeyboardButton("🍏 IPHONE 5s Battery")
                misc = types.KeyboardButton("🍏 IPHONE 5s Misc")
                tests = types.KeyboardButton("🍏 IPHONE 5s Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 5s", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Launch":
                bot.send_message(message.chat.id, "2013, September 10. Relased 2013, September 20 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Body":
                bot.send_message(message.chat.id, "Dimensions  - 123.8 x 58.6 x 7.6 mm  \n"
                                                  "                  (4.87 x 2.31 x 0.30 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	112 g (3.95 oz))\n"
                                                  "SIM            - Nano-SIM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 4.0 inches, 44.1 cm2 "
                                                  "      (~60.8% screen-to-body ratio)\n"
                                                  "Resolutions - 640 x 1136 pixels, 16:9 ratio (~326 ppi density)\n"
                                                  "Protection - Corning Gorilla Glass, oleophobic coating")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Platform":
                bot.send_message(message.chat.id, "OS   - iOS 7, upgradable to iOS 12.4.6\n"
                                                  "Chipset - Apple A7 (28 nm)\n"
                                                  "CPU  - Dual-core 1.3 GHz Cyclone (ARM v8-based)\n"
                                                  "GPU  - PowerVR G6430 (quad-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 16GB 1GB RAM, 32GB 1GB RAM, 64GB 1GB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Main Camera":
                bot.send_message(message.chat.id, "Single - 8 MP, f/2.2, 29mm (standard), 1/3', 1.5µm, AF\n"
                                                  "Features - Dual-LED dual-tone flash, HDR\n"
                                                  "Video - 1080p@30fps,  720p@120fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Selfie Camera":
                bot.send_message(message.chat.id, "Single - 1.2 MP,  f/2.4, 31mm (standard)\n"
                                                  "Features - face detection, FaceTime over Wi-Fi or Cellular\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 b/g/n, hotspot\n"
                                                  "Bluetooth - 4.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS\n"
                                                  "NFC - No\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, gyro, proximity, compass\n"
                                                  "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Battery":
                bot.send_message(message.chat.id, "Type - Li-Po 1560 mAh, non-removable (5.92 Wh)\n"
                                                  "Stand-by - 	Up to 250 h (2G) / Up to 250 h (3G)\n"
                                                  "Talk time -  Up to 10 h (3G) / Up to 10 h (3G)\n"
                                                  "Music play - Up to 40 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, White/Silver, Gold\n"
                                                  "Models - A1453, A1457, A1518, A1528, A1530, A1533, iPhone6,1, iPhone6,2\n"
                                                  "SAR - 	1.12 W/kg (head)     1.18 W/kg (body)\n"
                                                  "SAR EU - 	1.00 W/kg (head)     0.80 W/kg (body) \n"
                                                  "Price - About 330 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 5s Tests":
                bot.send_message(message.chat.id, "Performance - Basemark X: 14341\n"
                                                  "Display - Contrast ratio: 1219:1 (nominal) / 3.565:1 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 68dB / noise 66dB / Ring 69 dB\n"
                                                  "Audio Quality - Noise -93.6dB / Crosstalk -90.3dB\n"
                                                  "Battery life - Endurance rating 524\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 6 Network")
                launch = types.KeyboardButton("🍏 IPHONE 6 Launch")
                body = types.KeyboardButton("🍏 IPHONE 6 Body")
                displ = types.KeyboardButton("🍏 IPHONE 6 Display")
                platform = types.KeyboardButton("🍏 IPHONE 6 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 6 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 6 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 6 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 6 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 6 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 6 Features")
                battery = types.KeyboardButton("🍏 IPHONE 6 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 6 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 6 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 6", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Launch":
                bot.send_message(message.chat.id, "2014, September 9. Relased 2014, September 19 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Body":
                bot.send_message(message.chat.id, "Dimensions  - 138.1 x 67 x 6.9 mm  \n"
                                                  "                  (5.4 x 2.64 x 0.27 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	129 g (4.55 oz))\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 4.7 inches, 60.9 cm2\n"
                                                  "      (~65.8% screen-to-body ratio)\n"
                                                  "Resolutions - 750 x 1334 pixels, 16:9 ratio (~326 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Platform":
                bot.send_message(message.chat.id, "OS   - iOS 8, upgradable to iOS 12.4.6\n"
                                                  "Chipset - Apple A8 (20 nm)\n"
                                                  "CPU  - Dual-core 1.4 GHz Typhoon (ARM v8-based)\n"
                                                  "GPU - PowerVR GX6450 (quad-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 16GB 1GB RAM, 32GB 1GB RAM, 64GB 1GB RAM, 128GB 1GB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Main Camera":
                bot.send_message(message.chat.id, "Single - 8 MP, f/2.2, 29mm (standard), 1/3', 1.5µm, PDAF\n"
                                                  "Features - Dual-LED dual-tone flash, HDR\n"
                                                  "Video - 1080p@60fps,  720p@240fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Selfie Camera":
                bot.send_message(message.chat.id, "Single - 1.2 MP,  f/2.4, 31mm (standard)\n"
                                                  "Features - face detection, HDR, FaceTime over Wi-Fi or Cellular\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 4.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS\n"
                                                  "NFC - No\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Features":
                bot.send_message(message.chat.id, "Sensors - Accelerometer, gyro, proximity, compass\n"
                                                  "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Battery":
                bot.send_message(message.chat.id, "Type - Li-Po 1810 mAh, non-removable (6.9 Wh)\n"
                                                  "Stand-by - Up to 250 h (3G)\n"
                                                  "Talk time -  Up to 14 h (3G)\n"
                                                  "Music play - Up to 50 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, Silver, Gold\n"
                                                  "Models - A1549, A1586, A1589, A1522, A1524, A1593, iPhone7,2\n"
                                                  "SAR - 	1.18 W/kg (head)     1.18 W/kg (body)\n"
                                                  "SAR EU - 	0.98 W/kg (head)     0.97 W/kg (body) \n"
                                                  "Price - About 100 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Tests":
                bot.send_message(message.chat.id, "Performance - Basemark X: 15841\n"
                                                  "Display - Contrast ratio: 1213(nominal) / 3.838 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 66dB / noise 65dB / Ring 72 dB\n"
                                                  "Audio Quality - Noise -94dB / Crosstalk -73.4dB\n"
                                                  "Battery life - Endurance rating 61h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 6 Plus Network")
                launch = types.KeyboardButton("🍏 IPHONE 6 Plus Launch")
                body = types.KeyboardButton("🍏 IPHONE 6 Plus Body")
                displ = types.KeyboardButton("🍏 IPHONE 6 Plus Display")
                platform = types.KeyboardButton("🍏 IPHONE 6 Plus Platform")
                memory = types.KeyboardButton("🍏 IPHONE 6 Plus Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 6 Plus Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 6 Plus Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 6 Plus Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 6 Plus Communications")
                feature = types.KeyboardButton("🍏 IPHONE 6 Plus Features")
                battery = types.KeyboardButton("🍏 IPHONE 6 Plus Battery")
                misc = types.KeyboardButton("🍏 IPHONE 6 Plus Misc")
                tests = types.KeyboardButton("🍏 IPHONE 6 Plus Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 6 Plus", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Launch":
                bot.send_message(message.chat.id, "2014, September 9. Relased 2014, September 19 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Body":
                bot.send_message(message.chat.id, "Dimensions  - 158.1 x 77.8 x 7.1 mm  \n"
                                                  "                  (6.22 x 3.06 x 0.28 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	129 g (4.55 oz))\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 5.5 inches, 83.4 cm2\n"
                                                  "      (~67.8% screen-to-body ratio)\n"
                                                  "Resolutions - 1080 x 1920 pixels, 16:9 ratio (~401 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Platform":
                bot.send_message(message.chat.id, "OS   - iOS 8, upgradable to iOS 12.4.6\n"
                                                  "Chipset - Apple A8 (20 nm)\n"
                                                  "CPU  - Dual-core 1.4 GHz Typhoon (ARM v8-based)\n"
                                                  "GPU - PowerVR GX6450 (quad-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 16GB 1GB RAM, 64GB 1GB RAM, 128GB 1GB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Main Camera":
                bot.send_message(message.chat.id, "Single - 8 MP, f/2.2, 29mm (standard), 1/3', 1.5µm, PDAF\n"
                                                  "Features - Dual-LED dual-tone flash, HDR\n"
                                                  "Video - 1080p@60fps,  720p@240fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Selfie Camera":
                bot.send_message(message.chat.id, "Single - 1.2 MP,  f/2.4, 31mm (standard)\n"
                                                  "Features - face detection, HDR, FaceTime over Wi-Fi or Cellular\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 4.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Battery":
                bot.send_message(message.chat.id, "Type - Li-Po 2915 mAh, non-removable (11.1 Wh)\n"
                                                  "Stand-by - Up to 384 h (3G)\n"
                                                  "Talk time -  Up to 24 h (3G)\n"
                                                  "Music play - Up to 80 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, Silver, Gold\n"
                                                  "Models - A1522, A1524, iPhone7,1\n"
                                                  "SAR - 	1.19 W/kg (head)     1.19 W/kg (body)\n"
                                                  "SAR EU - 	0.99 W/kg (head)     0.91 W/kg (body) \n"
                                                  "Price - About 420 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6 Plus Tests":
                bot.send_message(message.chat.id, "Display - Contrast ratio: 1361(nominal) / 3.023 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 67dB / noise 65dB / Ring 66 dB\n"
                                                  "Audio Quality - Noise -94dB / Crosstalk -72dB\n"
                                                  "Battery life - Endurance rating 79h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 6s Network")
                launch = types.KeyboardButton("🍏 IPHONE 6s Launch")
                body = types.KeyboardButton("🍏 IPHONE 6s Body")
                displ = types.KeyboardButton("🍏 IPHONE 6s Display")
                platform = types.KeyboardButton("🍏 IPHONE 6s Platform")
                memory = types.KeyboardButton("🍏 IPHONE 6s Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 6s Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 6s Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 6S Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 6S Communications")
                feature = types.KeyboardButton("🍏 IPHONE 6s Features")
                battery = types.KeyboardButton("🍏 IPHONE 6s Battery")
                misc = types.KeyboardButton("🍏 IPHONE 6s Misc")
                tests = types.KeyboardButton("🍏 IPHONE 6s Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 6s", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Launch":
                bot.send_message(message.chat.id, "2015, September 9. Relased 2015, September 25 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Body":
                bot.send_message(message.chat.id, "Dimensions  - 138.3 x 67.1 x 7.1 mm\n"
                                                  "                  (5.44 x 2.64 x 0.28 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	129 g (4.55 oz))\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Display":
                bot.send_message(message.chat.id, "Type          - IPS LCD\n"
                                                  "Size -4.7 inches, 60.9 cm2\n"
                                                  "      (~65.6% screen-to-body ratio)\n"
                                                  "Resolutions - 750 x 1334 pixels, 16:9 ratio (~326 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating"
                                                  "             3D Touch\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Platform":
                bot.send_message(message.chat.id, "OS   - iOS 9, upgradable to iOS 15\n"
                                                  "Chipset - Apple A9 (14 nm)\n"
                                                  "CPU  - Dual-core 1.84 GHz Twister\n"
                                                  "GPU - PowerVR GT7600 (quad-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 16GB 2GB RAM, 32GB 2GB RAM, 64GB 2GB RAM, 128GB 2GB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/2.2, 29mm (standard), 1/3', 1.22µm, PDAF\n"
                                                  "Features - Dual-LED dual-tone flash, HDR\n"
                                                  "Video - 4K@30fps, 1080p@60fps, 1080p@120fps 720p@240fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Selfie Camera":
                bot.send_message(message.chat.id, "Single - 5 MP, f/2.2, 31mm (standard)\n"
                                                  "Features - face detection, HDR, panorama\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 4.2, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 1715 mAh, non-removable (6.91 Wh)\n"
                                                  "Stand-by - Up to 240 h (3G)\n"
                                                  "Talk time -  Up to 14 h (3G)\n"
                                                  "Music play - Up to 50 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, Silver, Gold, Rose Gold\n"
                                                  "Models - A1633, A1688, A1691, A1700 iPhone8,1\n"
                                                  "SAR - 	1.14 W/kg (head)     1.14 W/kg (body)\n"
                                                  "SAR EU - 	0.87 W/kg (head)     0.98 W/kg (body) \n"
                                                  "Price - About 230 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Tests":
                bot.send_message(message.chat.id, "Performance - Basemark OS  II 2.0: 2195\n"
                                                  "Display - Contrast ratio: 1481(nominal) / 3.783 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 66dB / noise 64dB / Ring 65 dB\n"
                                                  "Audio Quality - Noise -93.8dB / Crosstalk -73.2dB\n"
                                                  "Battery life - Endurance rating 62h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 6s Plus Network")
                launch = types.KeyboardButton("🍏 IPHONE 6s Plus Launch")
                body = types.KeyboardButton("🍏 IPHONE 6s Plus Body")
                displ = types.KeyboardButton("🍏 IPHONE 6s Plus Display")
                platform = types.KeyboardButton("🍏 IPHONE 6s Plus Platform")
                memory = types.KeyboardButton("🍏 IPHONE 6s Plus Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 6s Plus Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 6s Plus Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 6s Plus Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 6s Plus Communications")
                feature = types.KeyboardButton("🍏 IPHONE 6s Plus Features")
                battery = types.KeyboardButton("🍏 IPHONE 6s Plus Battery")
                misc = types.KeyboardButton("🍏 IPHONE 6s Plus Misc")
                tests = types.KeyboardButton("🍏 IPHONE 6s Plus Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 6s Plus", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Launch":
                bot.send_message(message.chat.id, "2015, September 9. Relased 2015, September 25 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Body":
                bot.send_message(message.chat.id, "Dimensions  - 158.2 x 77.9 x 7.3 mm\n"
                                                  "                  (6.23 x 3.07 x 0.29 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	129 g (4.55 oz))\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Display":
                bot.send_message(message.chat.id, "Type - IPS LCD\n"
                                                  "Size - 5.5 inches, 83.4 cm2\n"
                                                  "      (~67.7% screen-to-body ratio)\n"
                                                  "Resolutions - 1080 x 1920 pixels, 16:9 ratio (~401 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating"
                                                  "             3D Touch display\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Platform":
                bot.send_message(message.chat.id, "OS   - iOS 9, upgradable to iOS 15\n"
                                                  "Chipset - Apple A9 (14 nm)\n"
                                                  "CPU  - Dual-core 1.84 GHz Twister\n"
                                                  "GPU - PowerVR GT7600 (six-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 16GB 2GB RAM, 32GB 2GB RAM, 64GB 2GB RAM, 128GB 2GB RAM\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/2.2, 29mm (standard), 1/3', 1.22µm, PDAF, OIS\n"
                                                  "Features - Dual-LED dual-tone flash, HDR\n"
                                                  "Video - 4K@30fps, 1080p@60fps, 1080p@120fps 720p@240fps\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Selfie Camera":
                bot.send_message(message.chat.id, "Single - 5 MP, f/2.2, 31mm (standard)\n"
                                                  "Features - face detection, HDR, panorama\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 4.2, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2750 mAh, non-removable (10.45 Wh)\n"
                                                  "Stand-by - Up to 384 h (3G)\n"
                                                  "Talk time -  Up to 24 h (3G)\n"
                                                  "Music play - Up to 80 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, Silver, Gold, Rose Gold\n"
                                                  "Models - A1634, A1687, A1690, A1699, iPhone8,2\n"
                                                  "SAR - 	1.12W/kg (head)     1.14 W/kg (body)\n"
                                                  "SAR EU - 0.93 W/kg (head)     0.98 W/kg (body) \n"
                                                  "Price - About 240 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 6s Plus Tests":
                bot.send_message(message.chat.id, "Performance - Basemark OS  II 2.0: 2261\n"
                                                  "Display - Contrast ratio: 1382:1(nominal) / 3.530 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 65dB / Noise 65dB / Ring 64 dB\n"
                                                  "Audio Quality - Noise -93.4dB / Crosstalk -71.1dB\n"
                                                  "Battery life - Endurance rating 85h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE SE Network")
                launch = types.KeyboardButton("🍏 IPHONE SE Launch")
                body = types.KeyboardButton("🍏 IPHONE SE Body")
                displ = types.KeyboardButton("🍏 IPHONE SE Display")
                platform = types.KeyboardButton("🍏 IPHONE SE Platform")
                memory = types.KeyboardButton("🍏 IPHONE SE Memory")
                maincam = types.KeyboardButton("🍏 IPHONE SE Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE SE Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE SE Sounds")
                comms = types.KeyboardButton("🍏 IPHONE SE Communications")
                feature = types.KeyboardButton("🍏 IPHONE SE Features")
                battery = types.KeyboardButton("🍏 IPHONE SE Battery")
                misc = types.KeyboardButton("🍏 IPHONE SE Misc")
                tests = types.KeyboardButton("🍏 IPHONE SE Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE SE", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Launch":
                bot.send_message(message.chat.id, "2016, March 21. Released 2016, March 31 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Body":
                bot.send_message(message.chat.id, "Dimensions  - 123.8 x 58.6 x 7.6 mm\n"
                                                  "                  ((4.87 x 2.31 x 0.30 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	113 g (3.99 oz)\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Display":
                bot.send_message(message.chat.id, "Type          - IPS LCD\n"
                                                  "Size - 4.0 inches, 44.1 cm2\n"
                                                  "      (~60.8% screen-to-body ratio)\n"
                                                  "Resolutions - 640 x 1136 pixels, 16:9 ratio (~326 ppi density)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Platform":
                bot.send_message(message.chat.id, "OS   - iOS 9.3.2, upgradable to iOS 15\n"
                                                  "Chipset - Apple A9 (14 nm)\n"
                                                  "CPU  - Dual-core 1.84 GHz Twister\n"
                                                  "GPU - PowerVR GT7600 (six-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 16GB 2GB RAM, 32GB 2GB RAM, 64GB 2GB RAM, 128GB 2GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/2.2, 29mm (standard), 1/3', 1.22µm, PDAF, OIS\n"
                                                  "Features - Dual-LED dual-tone flash, HDR\n"
                                                  "Video - 4K@30fps, 1080p@60fps, 1080p@120fps 720p@240fps\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Selfie Camera":
                bot.send_message(message.chat.id, "Single - 1.2 MP, f/2.4, 31mm (standard)\n"
                                                  "Features - face detection, HDR, panorama\n"
                                                  "Video - 720p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes\n"
                                                  "3.5mm jack - Yes\n"
                                                  "16-bit/44.1kHZ audio\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, hotspot\n"
                                                  "Bluetooth - 4.2, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Plus Battery":
                bot.send_message(message.chat.id, "Type - Li-Po 1624 mAh, non-removable (6.21 Wh)\n"
                                                  "Stand-by - Up to 240 h (2G) / Up to 240 h (3G)\n"
                                                  "Talk time -  Up to 14 h (3G)\n"
                                                  "Music play - Up to 50 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, Silver, Gold, Rose Gold\n"
                                                  "Models - A1662, A1723, A1724, iPhone8,4\n"
                                                  "SAR - 	1.17W/kg (head)     1.19 W/kg (body)\n"
                                                  "SAR EU - 0.72 W/kg (head)     0.97 W/kg (body) \n"
                                                  "Price - About 140 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE Tests":
                bot.send_message(message.chat.id, "Performance - Basemark OS  II 2.0: 2163\n"
                                                  "Display - Contrast ratio: 804:1(nominal) / 3.681 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 66dB / Noise 65dB / Ring 69 dB\n"
                                                  "Audio Quality - Noise -93.0dB / Crosstalk -72.9dB\n"
                                                  "Battery life - Endurance rating 73h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 7 Network")
                launch = types.KeyboardButton("🍏 IPHONE 7 Launch")
                body = types.KeyboardButton("🍏 IPHONE 7 Body")
                displ = types.KeyboardButton("🍏 IPHONE 7 Display")
                platform = types.KeyboardButton("🍏 IPHONE 7 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 7 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 7 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 7 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 7 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 7 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 7 Features")
                battery = types.KeyboardButton("🍏 IPHONE 7 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 7 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 7 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 7", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Launch":
                bot.send_message(message.chat.id, "2016, September 7. Released 2016, September 16 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Body":
                bot.send_message(message.chat.id, "Dimensions  - 138.3 x 67.1 x 7.1 mm\n"
                                                  "                  (5.44 x 2.64 x 0.28 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	138 g (4.87 oz)\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Display":
                bot.send_message(message.chat.id, "Type - Retina IPS LCD, 625 nits (typ)\n"
                                                  "Size -   4.7 inches, 60.9 cm2\n"
                                                  "       (~65.6% screen-to-body ratio)\n"
                                                  "Resolutions - 750 x 1334 pixels, 16:9 ratio (~326 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating\n"
                                                  "Wide color gamut\n"
                                                  "3D Touch display & home button\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Platform":
                bot.send_message(message.chat.id, "OS   - iOS 10.0.1, upgradable to iOS 15\n"
                                                  "Chipset - Apple A10 Fusion (16 nm)\n"
                                                  "CPU  - Quad-core 2.34 GHz (2x Hurricane + 2x Zephyr)\n"
                                                  "GPU - PowerVR Series7XT Plus (six-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 32GB 2GB RAM, 128GB 2GB RAM, 256GB 2GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/1.8, 28mm (wide), 1/3', PDAF, OIS\n"
                                                  "Features - Quad-LED dual-tone flash, HDR\n"
                                                  "Video - 4K@30fps, 1080p@30/60/120fps, 720p@240fps\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Selfie Camera":
                bot.send_message(message.chat.id, "Single - 7 MP, f/2.2, 32mm (standard)\n"
                                                  "Features - Face detection, HDR, panorama\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 4.2, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO. QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7  Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 1960 mAh, non-removable (7.45 Wh)\n"
                                                  "Stand-by - Up to 14 h (3G)\n"
                                                  "Music play - Up to 40 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Misc":
                bot.send_message(message.chat.id, "Colors - Jet Black, Black, Silver, Gold, Rose Gold, Red\n"
                                                  "Models - A1660, A1778, A1779, A1780, A1853, A1866, iPhone9,1, iPhone9,3\n"
                                                  "SAR - 	1.19W/kg (head)     1.19 W/kg (body)\n"
                                                  "SAR EU - 1.38 W/kg (head)     1.34 W/kg (body) \n"
                                                  "Price - About 180 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Tests":
                bot.send_message(message.chat.id, "Performance - Basemark OS  II 2.0: 3416\n"
                                                  "Display - Contrast ratio: 1603:1(nominal) / 3.964 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 67dB / Noise 73dB / Ring 75 dB\n"
                                                  "Audio Quality - Noise -92.4dB / Crosstalk -80.9dB\n"
                                                  "Battery life - Endurance rating 61h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 7 Plus Network")
                launch = types.KeyboardButton("🍏 IPHONE 7 Plus Launch")
                body = types.KeyboardButton("🍏 IPHONE 7 Plus Body")
                displ = types.KeyboardButton("🍏 IPHONE 7 Plus Display")
                platform = types.KeyboardButton("🍏 IPHONE 7 Plus Platform")
                memory = types.KeyboardButton("🍏 IPHONE 7 Plus Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 7 Plus Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 7 Plus Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 7 Plus Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 7 Plus Communications")
                feature = types.KeyboardButton("🍏 IPHONE 7 Plus Features")
                battery = types.KeyboardButton("🍏 IPHONE 7 Plus Battery")
                misc = types.KeyboardButton("🍏 IPHONE 7 Plus Misc")
                tests = types.KeyboardButton("🍏 IPHONE 7 Plus Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 7 Plus", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Launch":
                bot.send_message(message.chat.id, "2016, September 7. Released 2016, September 16 \n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Body":
                bot.send_message(message.chat.id, "Dimensions -  158.2 x 77.9 x 7.3 mm\n"
                                                  "                  (6.23 x 3.07 x 0.29 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), aluminum back, aluminum frame\n"
                                                  "Weight       - 	188 g (6.63 oz)\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "IP67 dust/water resistant (up to 1m for 30 mins"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Display":
                bot.send_message(message.chat.id, "Type - Retina IPS LCD, 625 nits (typ)\n"
                                                  "Size -   5.5 inches, 83.4 cm2 \n"
                                                  "       (~67.7% screen-to-body ratio)\n"
                                                  "Resolutions - 1080 x 1920 pixels, 16:9 ratio (~401 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating\n"
                                                  "Wide color gamut\n"
                                                  "3D Touch display & home button\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Platform":
                bot.send_message(message.chat.id, "OS   - iOS 10.0.1, upgradable to iOS 15\n"
                                                  "Chipset - Apple A10 Fusion (16 nm)\n"
                                                  "CPU  - Quad-core 2.34 GHz (2x Hurricane + 2x Zephyr)\n"
                                                  "GPU - PowerVR Series7XT Plus (six-core graphics)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 32GB 3GB RAM, 128GB 3GB RAM, 256GB 3GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Main Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/1.8, 28mm (wide), 1/3', PDAF, OIS\n"
                                                  "12 MP, f/2.8, 56mm (telephoto), 1/3.6', AF, 2x optical zoom"
                                                  "Features - Quad-LED dual-tone flash, HDR\n"
                                                  "Video - 4K@30fps, 1080p@30/60/120fps, 720p@240fps\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Selfie Camera":
                bot.send_message(message.chat.id, "Single - 7 MP, f/2.2, 32mm (standard)\n"
                                                  "Features - Face detection, HDR, panorama\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 4.2, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO. QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2900 mAh, non-removable (11.1 Wh\n"
                                                  "Stand-by - Up to 384h (3G)\n"
                                                  "Music play - Up to 60 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Misc":
                bot.send_message(message.chat.id, "Colors - Jet Black, Black, Silver, Gold, Rose Gold, Red\n"
                                                  "Models - A1661, A1784, A1785, A1786, iPhone9,4\n"
                                                  "SAR - 	1.19W/kg (head)     1.19 W/kg (body)\n"
                                                  "SAR EU - 1.24 W/kg (head)     1.00 W/kg (body) \n"
                                                  "Price - About 320 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 7 Plus Tests":
                bot.send_message(message.chat.id, "Performance - Basemark OS  II 2.0: 3796\n"
                                                  "Display - Contrast ratio: 1398:1(nominal) / 3.588 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 68dB / Noise 72dB / Ring 72 dB\n"
                                                  "Audio Quality - Noise -93.1dB / Crosstalk -80.5dB\n"
                                                  "Battery life - Endurance rating 75h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 8 Network")
                launch = types.KeyboardButton("🍏 IPHONE 8 Launch")
                body = types.KeyboardButton("🍏 IPHONE 8 Body")
                displ = types.KeyboardButton("🍏 IPHONE 8 Display")
                platform = types.KeyboardButton("🍏 IPHONE 8 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 8 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 8 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 8 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 8 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 8 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 8 Features")
                battery = types.KeyboardButton("🍏 IPHONE 8 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 8 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 8 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 8", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Network":
                bot.send_message(message.chat.id, "Technology - GSM / HSPA / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Launch":
                bot.send_message(message.chat.id, "2017, September 12\n"
                                                  "Status        - Available. Released 2017, September 22\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Body":
                bot.send_message(message.chat.id, "Dimensions  - 138.4 x 67.3 x 7.3 mm\n"
                                                  "                  (5.45 x 2.65 x 0.29 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame\n"
                                                  "Weight       - 	148 g (5.22 oz)\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "IP67 dust/water resistant (up to 1m for 30 mins"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Display":
                bot.send_message(message.chat.id, "Type          - Retina IPS LCD, 625 nits (typ)\n"
                                                  "Size -   4.7 inches, 60.9 cm2\n"
                                                  "       ((~65.4% screen-to-body ratio)\n"
                                                  "Resolutions - 750 x 1334 pixels, 16:9 ratio (~326 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating\n"
                                                  "Wide color gamut\n"
                                                  "3D Touch display & home button\n"
                                                  "True-tone\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Platform":
                bot.send_message(message.chat.id, "OS   - iOS 11, upgradable to iOS 15\n"
                                                  "Chipset - Apple A11 Bionic (10 nm)\n"
                                                  "CPU  - Hexa-core 2.34 GHz (2x Monsoon + 4x Mistral)\n"
                                                  "GPU - PowerVR Series7XT Plus (six-core graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 64GB 2GB RAM, 128GB 2GB RAM, 256GB 2GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/1.8, 28mm (wide), 1/3', PDAF, OIS\n"
                                                  "Features - Quad-LED dual-tone flash, HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Selfie Camera":
                bot.send_message(message.chat.id, "Single - 7 MP, f/2.2\n"
                                                  "Features - Face detection, HDR, panorama\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 4.2, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO. QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 1821 mAh, non-removable (6.96 Wh)\n"
                                                  "Charging - Fast charging 15W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 14 h (3G)"
                                                  "Music play - Up to 40 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Misc":
                bot.send_message(message.chat.id, "Colors - Silver, Gold, Space Grey, Red\n"
                                                  "Models - A1863, A1905, A1906, A1907, iPhone10,1, iPhone10,4\n"
                                                  "SAR - 	1.32W/kg (head)     1.36 W/kg (body)\n"
                                                  "SAR EU - 1.19 W/kg (head)     1.17 W/kg (body) \n"
                                                  "Price - About 210 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Tests":
                bot.send_message(message.chat.id, "Performance - AnTuTu: 237594 (v7)\n"
                                                  "              GeekBench: 10214 (v4.4)\n"
                                                  "              GFXBench: 20fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: 1395:1(nominal) / 3.957 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 71dB / Noise 77dB / Ring 80 dB\n"
                                                  "Audio Quality - Noise -93.5dB / Crosstalk -80.4dB\n"
                                                  "Battery life - Endurance rating 66h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 8 Plus Network")
                launch = types.KeyboardButton("🍏 IPHONE 8 Plus Launch")
                body = types.KeyboardButton("🍏 IPHONE 8 Plus Body")
                displ = types.KeyboardButton("🍏 IPHONE 8 Plus Display")
                platform = types.KeyboardButton("🍏 IPHONE 8 Plus Platform")
                memory = types.KeyboardButton("🍏 IPHONE 8 Plus Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 8 Plus Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 8 Plus Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 8 Plus Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 8 Plus Communications")
                feature = types.KeyboardButton("🍏 IPHONE 8 Plus Features")
                battery = types.KeyboardButton("🍏 IPHONE 8 Plus Battery")
                misc = types.KeyboardButton("🍏 IPHONE 8 Plus Misc")
                tests = types.KeyboardButton("🍏 IPHONE 8 Plus Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 8 Plus", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Network":
                bot.send_message(message.chat.id, "Technology - GSM / HSPA / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Launch":
                bot.send_message(message.chat.id, "2017, September 12. Released 2017, September 22\n"
                                                  "Status        - Discontinued\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Body":
                bot.send_message(message.chat.id, "Dimensions  - 158.4 x 78.1 x 7.5 mm\n"
                                                  "                  (6.24 x 3.07 x 0.30 in)\n"
                                                  "Build - 	Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame\n"
                                                  "Weight       - 	148 g (5.22 oz)\n"
                                                  "SIM            - Nano-SIM\n"
                                                  "IP67 dust/water resistant (up to 1m for 30 mins"
                                                  "Apple Pay (Visa, MasterCard, AMEX certified)\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Display":
                bot.send_message(message.chat.id, "Type          - Retina IPS LCD, 625 nits (typ)\n"
                                                  "Size -   5.5 inches, 83.4 cm2\n"
                                                  "       (~67.4% screen-to-body ratio)\n"
                                                  "Resolutions - 1080 x 1920 pixels, 16:9 ratio (~401 ppi density)\n"
                                                  "Protection - Ion-strengthened glass, oleophobic coating\n"
                                                  "Wide color gamut\n"
                                                  "3D Touch display & home button\n"
                                                  "True-tone\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Platform":
                bot.send_message(message.chat.id, "OS   - iOS 11, upgradable to iOS 15\n"
                                                  "Chipset - Apple A11 Bionic (10 nm)\n"
                                                  "CPU  - Hexa-core 2.34 GHz (2x Monsoon + 4x Mistral)\n"
                                                  "GPU - Apple GPU (three-core graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Intternal - 64GB 3GB RAM, 128GB 3GB RAM, 256GB 3GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/1.8, 28mm (wide), 1/3', PDAF, OIS\n"
                                                  "Features - Quad-LED dual-tone flash, HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Selfie Camera":
                bot.send_message(message.chat.id, "Single - 7 MP, f/2.2, 32mm (standard)\n"
                                                  "Features - Face detection, HDR, panorama\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO. QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2691 mAh, non-removable (10.28 Wh)\n"
                                                  "Charging - Fast charging 15W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 21 h (3G)"
                                                  "Music play - Up to 60 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Misc":
                bot.send_message(message.chat.id, "Colors - Silver, Gold, Space Grey, Red\n"
                                                  "Models - A1864, A1897, A1898, , A1899, iPhone10,2, iPhone10,5\n"
                                                  "SAR - 	1.19W/kg (head)     1.19 W/kg (body)\n"
                                                  "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body) \n"
                                                  "Price - About 340 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 8 Plus Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 10037 (v4.4)\n"
                                                  "Display - Contrast ratio: 1395:1(nominal) / 3.957 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 76dB / Noise 74dB / Ring 79 dB\n"
                                                  "Audio Quality - Noise -93.5dB / Crosstalk -80.2dB\n"
                                                  "Battery life - Endurance rating 81h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE X Network")
                launch = types.KeyboardButton("🍏 IPHONE X Launch")
                body = types.KeyboardButton("🍏 IPHONE X Body")
                displ = types.KeyboardButton("🍏 IPHONE X Display")
                platform = types.KeyboardButton("🍏 IPHONE X Platform")
                memory = types.KeyboardButton("🍏 IPHONE X Memory")
                maincam = types.KeyboardButton("🍏 IPHONE X Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE X Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE X Sounds")
                comms = types.KeyboardButton("🍏 IPHONE X Communications")
                feature = types.KeyboardButton("🍏 IPHONE X Features")
                battery = types.KeyboardButton("🍏 IPHONE X Battery")
                misc = types.KeyboardButton("🍏 IPHONE X Misc")
                tests = types.KeyboardButton("🍏 IPHONE X Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE X", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Network":
                bot.send_message(message.chat.id, "Technology - GSM / HSPA / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Launch":
                bot.send_message(message.chat.id, "Announced - 2017, September 12\n"
                                                  "Status - Aviable. Released 2017, November 3\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Body":
                bot.send_message(message.chat.id, "Dimensions - 143.6 x 70.9 x 7.7 mm\n"
                                                  "             (5.65 x 2.79 x 0.30 in)\n"
                                                  "Weight - 174 g (6.14)\n"
                                                  "Build - Glass front (Gorilla Glass), glass black (Gorilla Black), stainless steel frame\n"
                                                  "SIM - Nano-SIM\n"
                                                  "IP67 dust/water resistant (up to 1m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Display":
                bot.send_message(message.chat.id, "Type - Super Retina OLED, HDR10, Dolby Vision , 625 nits (typ)\n"
                                                  "Size - 5.8 inches, 84.4 cm2 (~82.9% screen-to-body ratio)\n"
                                                  "Resolution - 1125 x 2436 pixels, 19.5:9 ratio (~458 ppi density)\n"
                                                  "Protection - scratch-resistant glass, opleophobic coating\n"
                                                  "Wide color gamut\n"
                                                  "3D Touch\n"
                                                  "True-tone\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Platform":
                bot.send_message(message.chat.id, "OS - iOS 11.1.1, upgradable to iOS 15\n"
                                                  "Chipset - Apple A11 Bionic (10 nm)\n"
                                                  "CPU - Hexa-core 2.39 GHz (2x Monsoon + 4x Mistral)\n"
                                                  "GPU - Apple GPU (three-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 3GB RAM, 256 GB 3GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Main Camera":
                bot.send_message(message.chat.id,
                                 "Single - 12 MP, f/1.8, 28mm (wide), 1/3', 1.22µm, dual pixel PDAF, OIS\n"
                                 "12 MP, f/2.4, 52mm (telephoto), 1/3.4', 1.0µm, PDAF, OIS, 2x optical zoom\n"
                                 "Features - Quad-LED dual-tone flash, HDR  (photo/panorama), panorama, HDR\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Selfie Camera":
                bot.send_message(message.chat.id, "Single - 7 MP, f/2.2, 32mm (standard)\n"
                                                  "Features - Face detection, HDR, panorama\n"
                                                  "Video - 1080p@30fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2716 mAh, non-removable (10.35 Wh)\n"
                                                  "Charging - Fast charging 15W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 21 h (3G)"
                                                  "Music play - Up to 60 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Misc":
                bot.send_message(message.chat.id, "Colors - Silver, Gold, Space Grey, Red\n"
                                                  "Models - A1864, A1897, A1898, , A1899, iPhone10,2, iPhone10,5\n"
                                                  "SAR - 	1.19W/kg (head)     1.19 W/kg (body)\n"
                                                  "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body) \n"
                                                  "Price - About 340 EUR\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE X Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 10037 (v4.4)\n"
                                                  "AnTuTu: 233100 (v7)\n"
                                                  "GFXBench: 28fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinity(nominal) / 5.013 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 68dB / Noise 74dB / Ring 76 dB\n"
                                                  "Audio Quality - Noise -93.7dB / Crosstalk -82.8dB\n"
                                                  "Battery life - Endurance rating 74h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE XR Network")
                launch = types.KeyboardButton("🍏 IPHONE XR Launch")
                body = types.KeyboardButton("🍏 IPHONE XR Body")
                displ = types.KeyboardButton("🍏 IPHONE XR Display")
                platform = types.KeyboardButton("🍏 IPHONE XR Platform")
                memory = types.KeyboardButton("🍏 IPHONE XR Memory")
                maincam = types.KeyboardButton("🍏 IPHONE XR Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE XR Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE XR Sounds")
                comms = types.KeyboardButton("🍏 IPHONE XR Communications")
                feature = types.KeyboardButton("🍏 IPHONE XR Features")
                battery = types.KeyboardButton("🍏 IPHONE XR Battery")
                misc = types.KeyboardButton("🍏 IPHONE XR Misc")
                tests = types.KeyboardButton("🍏 IPHONE XR Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE XR", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Launch":
                bot.send_message(message.chat.id, "Announced - 2018, September 12\n"
                                                  "Status - Available. Released 2018, October 26\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Body":
                bot.send_message(message.chat.id, "Dimensions - 150.9 x 75.7 x 8.3 mm\n"
                                                  "             ((5.94 x 2.98 x 0.33 in)\n"
                                                  "Weight - 194 g (6.84)\n"
                                                  "Build - Glass front (Gorilla Glass), glass black (Gorilla Black), stainless steel frame\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for\n"
                                                  "China\n"
                                                  "IP67 dust/water resistant (up to 1m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Display":
                bot.send_message(message.chat.id, "Type - Liquid Retina IPS LCD, 625 nits (typ)\n"
                                                  "Size - 6.1 inches, 90.3 cm2 (~79.0% screen-to-body ratio)\n"
                                                  "Resolution - 828 x 1792 pixels, 19.5:9 ratio (~326 ppi density)\n"
                                                  "Protection - Scratch-resistant glass, oleophobic coating\n"
                                                  "True-tone\n"
                                                  "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Platform":
                bot.send_message(message.chat.id, "OS - iOS 12, upgradable to iOS 15\n"
                                                  "Chipset - Apple A12 Bionic (7 nm)\n"
                                                  "CPU - Hexa-core (2x2.5 GHz Vortex + 4x1.6 GHz Tempest)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 3GB RAM, 128GB 3GB RAM, 256GB 3GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/1.8, 26mm (wide), 1/2.55', 1.4µm, PDAF, OIS\n"
                                                  "Features - Quad-LED dual-tone flash, HDR  (photo/panorama)\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, stereo sound rec.\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Selfie Camera":
                bot.send_message(message.chat.id, "Single - 7 MP, f/2.2, 32mm (standard)\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 1080p@60fps\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2942 mAh, non-removable (11.16 Wh)\n"
                                                  "Charging - Fast charging 15W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 16 h (3G)"
                                                  "Music play - Up to 65 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Misc":
                bot.send_message(message.chat.id, "Colors - Black, Red, Yellow, Blue, Coral, White\n"
                                                  "Models - A2105, A1984, A2107, A2108, A2106, iPhone11,8\n"
                                                  "SAR - 	1.13W/kg (head)     1.16 W/kg (body)\n"
                                                  "Price -  $ 303.89 / € 358.24 / £ 274.90 / ₹ 42.99\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XR Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 11437 (v4.4), 2690 (v5.1)\n"
                                                  "AnTuTu: 341196 (v7), 422465 (v8)\n"
                                                  "GFXBench: 58fps (ES 3.1 onscreen)\n"
                                                  "Battery life - Endurance rating 78h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE XS Network")
                launch = types.KeyboardButton("🍏 IPHONE XS Launch")
                body = types.KeyboardButton("🍏 IPHONE XS Body")
                displ = types.KeyboardButton("🍏 IPHONE XS Display")
                platform = types.KeyboardButton("🍏 IPHONE XS Platform")
                memory = types.KeyboardButton("🍏 IPHONE XS Memory")
                maincam = types.KeyboardButton("🍏 IPHONE XS Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE XS Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE XS Sounds")
                comms = types.KeyboardButton("🍏 IPHONE XS Communications")
                feature = types.KeyboardButton("🍏 IPHONE XS Features")
                battery = types.KeyboardButton("🍏 IPHONE XS Battery")
                misc = types.KeyboardButton("🍏 IPHONE XS Misc")
                tests = types.KeyboardButton("🍏 IPHONE XS Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE XS", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Launch":
                bot.send_message(message.chat.id, "Announced - 2018, September 12\n"
                                                  "Status - Available. Released 2018, September 21\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Body":
                bot.send_message(message.chat.id, "Dimensions - 143.6 x 70.9 x 7.7 mm\n"
                                                  "             (5.65 x 2.79 x 0.30 in)\n"
                                                  "Weight - 177 g (6.24)\n"
                                                  "Build - Glass front (Gorilla Glass), glass black (Gorilla Black), stainless steel frame\n"
                                                  "SIM - Nano-SIM, eSIM\n"
                                                  "IP68 dust/water resistant (up to 2m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Display":
                bot.send_message(message.chat.id, "Type - Super Retina OLED, HDR10, Dolby Vision, 625 nits (typ)\n"
                                                  "Size - 5.8 inches, 84.4 cm2 (~82.9% screen-to-body ratio)\n"
                                                  "Resolution - 1125 x 2436 pixels, 19.5:9 ratio (~458 ppi density)\n"
                                                  "Protection - Scratch-resistant glass, oleophobic coating\n"
                                                  "3D Touch\n"
                                                  "True-tone\n"
                                                  "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Platform":
                bot.send_message(message.chat.id, "OS - iOS 12, upgradable to iOS 15\n"
                                                  "Chipset - Apple A12 Bionic (7 nm)\n"
                                                  "CPU - Hexa-core (2x2.5 GHz Vortex + 4x1.6 GHz Tempest)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 256GB 4GB RAM, 512GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/1.8, 26mm (wide), 1/2.55', 1.4µm, PDAF, OIS\n"
                                                  "12 MP, f/2.4, 52mm (telephoto), 1/3.4', 1.0µm, PDAF, OIS, 2x optical zoom\n"
                                                  "Features - Quad-LED dual-tone flash, HDR  (photo/panorama)\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, stereo sound rec.\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 7 MP, f/2.2, 32mm (standard)\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 1080p@60fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2658 mAh, non-removable (10.13 Wh)\n"
                                                  "Charging - Fast charging 15W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 14 h (3G)"
                                                  "Music play - Up to 60 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, Silver, Gold\n"
                                                  "Models - A2097, A1920, A2100, A2098, Phone11,2\n"
                                                  "SAR - 1.19 W/kg (head)     1.18 W/kg (body)\n"
                                                  "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)"
                                                  "Price -  $ 365.00 / € 385.00 / £ 281.99\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 11472 (v4.4)\n"
                                                  "AnTuTu: 346379 (v7)\n"
                                                  "GFXBench: 47fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal), 5.171 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 71dB / Noise 75dB / Ring 78dB\n"
                                                  "Audio quality - Noise -93.7dB / Crosstalk -82.8dB\n"
                                                  "Battery life - Endurance rating 72h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE XS Max Network")
                launch = types.KeyboardButton("🍏 IPHONE XS Max Launch")
                body = types.KeyboardButton("🍏 IPHONE XS Max Body")
                displ = types.KeyboardButton("🍏 IPHONE XS Max Display")
                platform = types.KeyboardButton("🍏 IPHONE XS Max Platform")
                memory = types.KeyboardButton("🍏 IPHONE XS Max Memory")
                maincam = types.KeyboardButton("🍏 IPHONE XS Max Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE XS Max Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE XS Max Sounds")
                comms = types.KeyboardButton("🍏 IPHONE XS Max Communications")
                feature = types.KeyboardButton("🍏 IPHONE XS Max Features")
                battery = types.KeyboardButton("🍏 IPHONE XS Max Battery")
                misc = types.KeyboardButton("🍏 IPHONE XS Max Misc")
                tests = types.KeyboardButton("🍏 IPHONE XS Max Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE XS Max", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Launch":
                bot.send_message(message.chat.id, "Announced - 2018, September 12\n"
                                                  "Status - Available. Released 2018, September 21\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Body":
                bot.send_message(message.chat.id, "Dimensions - 157.5 x 77.4 x 7.7 mm\n"
                                                  "             (6.20 x 3.05 x 0.30 in)\n"
                                                  "Weight - 208 g (7.44)\n"
                                                  "Build - Glass front (Gorilla Glass), glass black (Gorilla Black), stainless steel frame\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for\n"
                                                  "China\n"
                                                  "IP68 dust/water resistant (up to 2m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Display":
                bot.send_message(message.chat.id, "Type - Super Retina OLED, HDR10, Dolby Vision, 625 nits (typ)\n"
                                                  "Size - 6.5 inches, 102.9 cm2 (~84.4% screen-to-body ratio)\n"
                                                  "Resolution - 1242 x 2688 pixels, 19.5:9 ratio (~458 ppi density)\n"
                                                  "Protection - Scratch-resistant glass, oleophobic coating\n"
                                                  "3D Touch\n"
                                                  "True-tone\n"
                                                  "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Platform":
                bot.send_message(message.chat.id, "OS - iOS 12, upgradable to iOS 15\n"
                                                  "Chipset - Apple A12 Bionic (7 nm)\n"
                                                  "CPU - Hexa-core (2x2.5 GHz Vortex + 4x1.6 GHz Tempest)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 256GB 4GB RAM, 512GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Main Camera":
                bot.send_message(message.chat.id, "Single - 12 MP, f/1.8, 26mm (wide), 1/2.55', 1.4µm, PDAF, OIS\n"
                                                  "         12 MP, f/2.4, 52mm (telephoto), 1/3.4', 1.0µm, PDAF, OIS, 2x optical zoom\n"
                                                  "Features - Quad-LED dual-tone flash, HDR  (photo/panorama)\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, stereo sound rec.\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 7 MP, f/2.2, 32mm (standard)\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 1080p@30/60fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2658 mAh, non-removable (10.13 Wh)\n"
                                                  "Charging - Fast charging 15W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 16 h (3G)"
                                                  "Music play - Up to 65 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Misc":
                bot.send_message(message.chat.id, "Colors - Space Gray, Silver, Gold\n"
                                                  "Models - A1921, A2101, A2102, A2104, Phone11,6\n"
                                                  "SAR - 1.16 W/kg (head)     1.17 W/kg (body)\n"
                                                  "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)"
                                                  "Price -  $ 390.00 / £ 337.70\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE XS Max Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 11432 (v4.4)\n"
                                                  "AnTuTu: 353210 (v7)\n"
                                                  "GFXBench: 47fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal), 4.516 (sunlight)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 70dB / Noise 74dB / Ring 84dB\n"
                                                  "Audio quality - Noise -93.7dB / Crosstalk -82.8dB\n"
                                                  "Battery life - Endurance rating 79h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 11 Network")
                launch = types.KeyboardButton("🍏 IPHONE 11 Launch")
                body = types.KeyboardButton("🍏 IPHONE 11 Body")
                displ = types.KeyboardButton("🍏 IPHONE 11 Display")
                platform = types.KeyboardButton("🍏 IPHONE 11 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 11 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 11 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 11 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 11 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 11 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 11 Features")
                battery = types.KeyboardButton("🍏 IPHONE 11 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 11 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 11 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 11", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Launch":
                bot.send_message(message.chat.id, "Announced - 2019, September 10\n"
                                                  "Status - Available. Released 2019, September 20\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Body":
                bot.send_message(message.chat.id, "Dimensions - 150.9 x 75.7 x 8.3 mm\n"
                                                  "             (5.94 x 2.98 x 0.33 in)\n"
                                                  "Weight - 194 g (6.84)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame (7000 series)\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for\n"
                                                  "China\n"
                                                  "IP68 dust/water resistant (up to 2m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Display":
                bot.send_message(message.chat.id, "Type - Liquid Retina IPS LCD, 625 nits (typ)\n"
                                                  "Size - 6.1 inches, 90.3 cm2 (~79.0% screen-to-body ratio)\n"
                                                  "Resolution - 828 x 1792 pixels, 19.5:9 ratio (~326 ppi density)\n"
                                                  "Protection - Scratch-resistant glass, oleophobic coating\n"
                                                  "True-tone\n"
                                                  "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Platform":
                bot.send_message(message.chat.id, "OS - iOS 13, upgradable to iOS 15\n"
                                                  "Chipset - Apple A13 Bionic (7 nm+)\n"
                                                  "CPU - Hexa-core (2x2.65 GHz Lightning + 4x1.8 GHz Thunder)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 128GB 4GB RAM, 256GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Main Camera":
                bot.send_message(message.chat.id,
                                 "Dual - 12 MP, f/1.8, 26mm (wide), 1/2.55', 1.4µm, dual pixel PDAF, OIS\n"
                                 "       12 MP, f/2.4, 120˚, 13mm (ultrawide), 1/3.6\n"
                                 "Features - Quad-LED dual-tone flash, HDR  (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, stereo sound rec.\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 3110 mAh, non-removable (11.91 Wh)\n"
                                                  "Charging - Fast charging 18W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 17 h (multimedia)"
                                                  "Music play - Up to 65 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Misc":
                bot.send_message(message.chat.id, "Colors - Black, Green, Yellow, Purple, Red, White\n"
                                                  "Models - A2221, A2111, A2223, iPhone12,1\n"
                                                  "SAR - 1.09 W/kg (head)     1.18 W/kg (body)\n"
                                                  "SAR EU - 0.95 W/kg (head)     0.99 W/kg (body)"
                                                  "Price -  $ 474.00 / € 509.00 / £ 396.98 / ₹ 49.900\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 13882 (v4.4)\n"
                                                  "AnTuTu: 419453 (v7)\n"
                                                  "GFXBench: 60fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: 1505:1 (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - Voice 70dB / Noise 72dB / Ring 76dB\n"
                                                  "Audio quality - Noise -94.2dB / Crosstalk -80.8dB\n"
                                                  "Battery life - Endurance rating 94h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 11 Pro Network")
                launch = types.KeyboardButton("🍏 IPHONE 11 Pro Launch")
                body = types.KeyboardButton("🍏 IPHONE 11 Pro Body")
                displ = types.KeyboardButton("🍏 IPHONE 11 Pro Display")
                platform = types.KeyboardButton("🍏 IPHONE 11 Pro Platform")
                memory = types.KeyboardButton("🍏 IPHONE 11 Pro Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 11 Pro Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 11 Pro Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 11 Pro Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 11 Pro Communications")
                feature = types.KeyboardButton("🍏 IPHONE 11 Pro Features")
                battery = types.KeyboardButton("🍏 IPHONE 11 Pro Battery")
                misc = types.KeyboardButton("🍏 IPHONE 11 Pro Misc")
                tests = types.KeyboardButton("🍏 IPHONE 11 Pro Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 11 Pro", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Launch":
                bot.send_message(message.chat.id, "Announced - 2019, September 10\n"
                                                  "Status - Available. Released 2019, September 20\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Body":
                bot.send_message(message.chat.id, "Dimensions - 144 x 71.4 x 8.1 mm\n"
                                                  "             (5.67 x 2.81 x 0.32 in)\n"
                                                  "Weight - 188 g (6.63)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame (7000 series)\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for\n"
                                                  "China\n"
                                                  "IP68 dust/water resistant (up to 4m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 800 nits (typ), 1200 nits (peak)\n"
                                 "Size - 5.8 inches, 84.4 cm2 (~82.1% screen-to-body ratio)\n"
                                 "Resolution - 1125 x 2436 pixels, 19.5:9 ratio (~458 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Platform":
                bot.send_message(message.chat.id, "OS - iOS 13, upgradable to iOS 15\n"
                                                  "Chipset - Apple A13 Bionic (7 nm+)\n"
                                                  "CPU - Hexa-core (2x2.65 GHz Lightning + 4x1.8 GHz Thunder)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 128GB 4GB RAM, 256GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Main Camera":
                bot.send_message(message.chat.id,
                                 "Triple - 12 MP, f/1.8, 26mm (wide), 1/2.55', 1.4µm, dual pixel PDAF, OIS\n"
                                 "         12 MP, f/2.0, 52mm (telephoto), 1/3.4', 1.0µm, PDAF, OIS, 2x optical zoom\n"
                                 "         12 MP, f/2.4, 120˚, 13mm (ultrawide), 1/3.6\n"
                                 "Features - Quad-LED dual-tone flash, HDR  (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, stereo sound rec.\n"
                                 )

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 3046 mAh, non-removable (11.67 Wh)\n"
                                                  "Charging - Fast charging 18W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 18 h (multimedia)"
                                                  "Music play - Up to 65 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Matte Space Gray, Matte Silver, Matte Gold, Matte Midnight Green\n"
                                 "Models - A2215, A2160, A2217, iPhone12,3\n"
                                 "SAR - 1.18 W/kg (head)     1.16 W/kg (body)\n"
                                 "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)"
                                 "Price -  $ 899.00 / € 661.48 / £ 444.95\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 13829 (v4.4)\n"
                                                  "              AnTuTu: 460784 (v7)\n"
                                                  "              GFXBench: 57fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - -24.3 LUFS (Very good)\n"
                                                  "Audio quality - Noise -94.2dB / Crosstalk -81.0dB\n"
                                                  "Battery life - Endurance rating 86h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 11 Pro Max Network")
                launch = types.KeyboardButton("🍏 IPHONE 11 Pro Max Launch")
                body = types.KeyboardButton("🍏 IPHONE 11 Pro Max Body")
                displ = types.KeyboardButton("🍏 IPHONE 11 Pro Max Display")
                platform = types.KeyboardButton("🍏 IPHONE 11 Pro Max Platform")
                memory = types.KeyboardButton("🍏 IPHONE 11 Pro Max Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 11 Pro Max Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 11 Pro Max Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 11 Pro Max Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 11 Pro Max Communications")
                feature = types.KeyboardButton("🍏 IPHONE 11 Pro Max Features")
                battery = types.KeyboardButton("🍏 IPHONE 11 Pro Max Max Battery")
                misc = types.KeyboardButton("🍏 IPHONE 11 Pro Max Misc")
                tests = types.KeyboardButton("🍏 IPHONE 11 Pro Max Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 11 Pro Max", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Launch":
                bot.send_message(message.chat.id, "Announced - 2019, September 10\n"
                                                  "Status - Available. Released 2019, September 20\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Body":
                bot.send_message(message.chat.id, "Dimensions - 158 x 77.8 x 8.1 mm\n"
                                                  "             (6.22 x 3.06 x 0.32 in)\n"
                                                  "Weight - 188 g (7.97)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame (7000 series)\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for\n"
                                                  "China\n"
                                                  "IP68 dust/water resistant (up to 4m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 800 nits (typ), 1200 nits (peak)\n"
                                 "Size - 6.5 inches, 102.9 cm2 (~83.7% screen-to-body ratio)\n"
                                 "Resolution - 1242 x 2688 pixels, 19.5:9 ratio (~458 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Platform":
                bot.send_message(message.chat.id, "OS - iOS 13, upgradable to iOS 15\n"
                                                  "Chipset - Apple A13 Bionic (7 nm+)\n"
                                                  "CPU - Hexa-core (2x2.65 GHz Lightning + 4x1.8 GHz Thunder)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 128GB 4GB RAM, 256GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Main Camera":
                bot.send_message(message.chat.id,
                                 "Triple - 12 MP, f/1.8, 26mm (wide), 1/2.55', 1.4µm, dual pixel PDAF, OIS\n"
                                 "         12 MP, f/2.0, 52mm (telephoto), 1/3.4', 1.0µm, PDAF, OIS, 2x optical zoom\n"
                                 "         12 MP, f/2.4, 120˚, 13mm (ultrawide), 1/3.6\n"
                                 "Features - Quad-LED dual-tone flash, HDR  (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 3969 mAh, non-removable (15.04 Wh)\n"
                                                  "Charging - Fast charging 18W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           Qi wireless charging\n"
                                                  "Talk time - Up to 20 h (multimedia)"
                                                  "Music play - Up to 80 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Matte Space Gray, Matte Silver, Matte Gold, Matte Midnight Green\n"
                                 "Models - A2218, A2161, A2220, iPhone12.5\n"
                                 "SAR - 1.16 W/kg (head)     1.17 W/kg (body)\n"
                                 "SAR EU - 0.95 W/kg (head)     0.99 W/kg (body)"
                                 "Price -  $ 648.96 / € 1,149.00 / £ 537.46 / ₹ 96.899\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 11 Pro Max Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 13829 (v4.4)\n"
                                                  "              AnTuTu: 460784 (v7)\n"
                                                  "              GFXBench: 57fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - -24.3 LUFS (Very good)\n"
                                                  "Audio quality - Noise -94.2dB / Crosstalk -81.0dB\n"
                                                  "Battery life - Endurance rating 86h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE SE 2020 Network")
                launch = types.KeyboardButton("🍏 IPHONE SE 2020 Launch")
                body = types.KeyboardButton("🍏 IPHONE SE 2020 Body")
                displ = types.KeyboardButton("🍏 IPHONE SE 2020 Display")
                platform = types.KeyboardButton("🍏 IPHONE SE 2020 Platform")
                memory = types.KeyboardButton("🍏 IPHONE SE 2020 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE SE 2020 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE SE 2020 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE SE 2020 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE SE 2020 Communications")
                feature = types.KeyboardButton("🍏 IPHONE SE 2020 Features")
                battery = types.KeyboardButton("🍏 IPHONE SE 2020 Battery")
                misc = types.KeyboardButton("🍏 IPHONE SE 2020 Misc")
                tests = types.KeyboardButton("🍏 IPHONE SE 2020 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE SE 2020", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Launch":
                bot.send_message(message.chat.id, "Announced - 2020, April 15\n"
                                                  "Status - Available. Released 2020, April 24\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Body":
                bot.send_message(message.chat.id, "Dimensions - 138.4 x 67.3 x 7.3 mm\n"
                                                  "             (5.45 x 2.65 x 0.29 in)\n"
                                                  "Weight - 148 g (5.22 oz)\n"
                                                  "Build - Glass front, glass back, aluminum frame\n"
                                                  "SIM - Nano-SIM and/or eSIM\n"
                                                  "IP67 dust/water resistant (up to 1m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Display":
                bot.send_message(message.chat.id,
                                 "Type - Retina IPS LCD, 625 nits (typ)\n"
                                 "Size - 4.7 inches, 60.9 cm2 (~65.4% screen-to-body ratio)\n"
                                 "Resolution - 750 x 1334 pixels, 16:9 ratio (~326 ppi density)\n"
                                 "Protection - Ion-strengthened glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Platform":
                bot.send_message(message.chat.id, "OS - iOS 13, upgradable to iOS 15\n"
                                                  "Chipset - Apple A13 Bionic (7 nm+)\n"
                                                  "CPU - Hexa-core (2x2.65 GHz Lightning + 4x1.8 GHz Thunder)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 3GB RAM, 128GB 3GB RAM, 256GB 3GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Main Camera":
                bot.send_message(message.chat.id,
                                 "Single - 12 MP, f/1.8 (wide), PDAF, OIS\n"
                                 "Features - Quad-LED dual-tone flash, HDR  (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, OIS, stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Selfie Camera":
                bot.send_message(message.chat.id, "Single - 7 MP, f/2.2\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 1080p@30fps; gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 1821 mAh, non-removable (6.96 Wh)\n"
                                                  "Charging - Fast charging 18W, 50% in 30 min (advertised)\n"
                                                  "           Qi wireless charging\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Black, White, Red\n"
                                 "Models - A2275, A2296, A2298, iPhone12,8\n"
                                 "SAR - 1.17 W/kg (head)     1.16 W/kg (body)\n"
                                 "SAR EU - 0.98 W/kg (head)     0.99 W/kg (body)\n"
                                 "Price -  $ 219.99 / € 320.80 / £ 279.99n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE SE 2020 Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 3237 (v5.1)\n"
                                                  "              AnTuTu: 462253 (v8)\n"
                                                  "Display - Contrast ratio: 1544:1 (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - -24.1 LUFS (Very good)\n"
                                                  "Battery life - Endurance rating 59h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 12 Mini Network")
                launch = types.KeyboardButton("🍏 IPHONE 12 Mini Launch")
                body = types.KeyboardButton("🍏 IPHONE 12 Mini Body")
                displ = types.KeyboardButton("🍏 IPHONE 12 Mini Display")
                platform = types.KeyboardButton("🍏 IPHONE 12 Mini Platform")
                memory = types.KeyboardButton("🍏 IPHONE 12 Mini Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 12 Mini Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 12 Mini Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 12 Mini Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 12 Mini Communications")
                feature = types.KeyboardButton("🍏 IPHONE 12 Mini Features")
                battery = types.KeyboardButton("🍏 IPHONE 12 Mini Battery")
                misc = types.KeyboardButton("🍏 IPHONE 12 Mini Misc")
                tests = types.KeyboardButton("🍏 IPHONE 12 Mini Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 12 Mini", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Launch":
                bot.send_message(message.chat.id, "Announced - 2020, October 13\n"
                                                  "Status - Available. Released 2020, November 13\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Body":
                bot.send_message(message.chat.id, "Dimensions - 131.5 x 64.2 x 7.4 mm\n"
                                                  "             (5.18 x 2.53 x 0.29 in)\n"
                                                  "Weight - 135 g (4.76 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame (7000 series)\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by)\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 625 nits (typ), 1200 nits (peak)\n"
                                 "Size - 5.4 inches, 71.9 cm2 (~85.1% screen-to-body ratio)\n"
                                 "Resolution - 1080 x 2340 pixels, 19.5:9 ratio (~476 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Platform":
                bot.send_message(message.chat.id, "OS - iOS 14.1, upgradable to iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 128GB 4GB RAM, 256GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Main Camera":
                bot.send_message(message.chat.id,
                                 "Dual - 12 MP, f/1.6, 26mm (wide), 1.4µm, dual pixel PDAF, OIS\n"
                                 "       12 MP, f/2.4, 13mm, 120˚ (ultrawide), 1/3.6'\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, Dolby Vision HDR (up to 30fps),\n"
                                 "stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2227 mAh, non-removable (8.57 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 15 h (multimedia)"
                                                  "Music play - Up to 50 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Black, White, Red, Green, Blue, Purple\n"
                                 "Models - A2399, A2176, A2398, A2400, A2399, iPhone13,1\n"
                                 "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)\n"
                                 "Price -  $ 549.00 / € 632.91 / £ 519.00 / ₹ 56.999\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Mini Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 4174 (v5.1)\n"
                                                  "              AnTuTu: 589616 (v8)\n"
                                                  "              GFXBench: 60fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - -24.6 LUFS (Very good)\n"
                                                  "Battery life - Endurance rating 69h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 12 Network")
                launch = types.KeyboardButton("🍏 IPHONE 12 Launch")
                body = types.KeyboardButton("🍏 IPHONE 12 Body")
                displ = types.KeyboardButton("🍏 IPHONE 12 Display")
                platform = types.KeyboardButton("🍏 IPHONE 12 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 12 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 12 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 12 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 12 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 12 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 12 Features")
                battery = types.KeyboardButton("🍏 IPHONE 12 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 12 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 12 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 12", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Launch":
                bot.send_message(message.chat.id, "Announced - 2020, October 13\n"
                                                  "Status - Available. Released 2020, October 23\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Body":
                bot.send_message(message.chat.id, "Dimensions - 146.7 x 71.5 x 7.4 mm\n"
                                                  "             (5.78 x 2.81 x 0.29 in)\n"
                                                  "Weight - 164 g (5.78 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame (7000 series)\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for China\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 625 nits (typ), 1200 nits (peak)\n"
                                 "Size - 6.1 inches, 90.2 cm2 (~86.0% screen-to-body ratio)\n"
                                 "Resolution - 1170 x 2532 pixels, 19.5:9 ratio (~460 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Platform":
                bot.send_message(message.chat.id, "OS - iOS 14.1, upgradable to iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 128GB 4GB RAM, 256GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Main Camera":
                bot.send_message(message.chat.id,
                                 "Dual - 12 MP, f/1.6, 26mm (wide), 1.4µm, dual pixel PDAF, OIS\n"
                                 "       12 MP, f/2.4, 13mm, 120˚ (ultrawide), 1/3.6'\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, Dolby Vision HDR (up to 30fps),\n"
                                 "stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2815 mAh, non-removable (10.78 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 17 h (multimedia)"
                                                  "Music play - Up to 65 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Black, White, Red, Green, Blue, Purple\n"
                                 "Models - A2403, A2172, A2402, A2404, iPhone13,2\n"
                                 "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)\n"
                                 "Price -  $ 699.00 / € 724.99 / £ 589.99 / ₹ 63.999\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 4067 (v5.1)\n"
                                                  "              AnTuTu: 568674 (v8)\n"
                                                  "              GFXBench: 58fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - -24.4 LUFS (Very good)\n"
                                                  "Battery life - Endurance rating 84h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 12 Pro Network")
                launch = types.KeyboardButton("🍏 IPHONE 12 Pro Launch")
                body = types.KeyboardButton("🍏 IPHONE 12 Pro Body")
                displ = types.KeyboardButton("🍏 IPHONE 12 Pro Display")
                platform = types.KeyboardButton("🍏 IPHONE 12 Pro Platform")
                memory = types.KeyboardButton("🍏 IPHONE 12 Pro Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 12 Pro Pro Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 12 Pro Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 12 Pro Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 12 Pro Communications")
                feature = types.KeyboardButton("🍏 IPHONE 12 Pro Features")
                battery = types.KeyboardButton("🍏 IPHONE 12 Pro Battery")
                misc = types.KeyboardButton("🍏 IPHONE 12 Pro Misc")
                tests = types.KeyboardButton("🍏 IPHONE 12 Pro Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 12 Pro", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Launch":
                bot.send_message(message.chat.id, "Announced - 2020, October 13\n"
                                                  "Status - Available. Released 2020, October 23\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Body":
                bot.send_message(message.chat.id, "Dimensions - 146.7 x 71.5 x 7.4 mm\n"
                                                  "             (5.78 x 2.81 x 0.29 in)\n"
                                                  "Weight - 164 g (5.78 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame (7000 series)\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for China\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 625 nits (typ), 1200 nits (peak)\n"
                                 "Size - 6.1 inches, 90.2 cm2 (~86.0% screen-to-body ratio)\n"
                                 "Resolution - 1170 x 2532 pixels, 19.5:9 ratio (~460 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Platform":
                bot.send_message(message.chat.id, "OS - iOS 14.1, upgradable to iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 64GB 4GB RAM, 128GB 4GB RAM, 256GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Main Camera":
                bot.send_message(message.chat.id,
                                 "Quad - 12 MP, f/1.6, 26mm (wide), 1.4µm, dual pixel PDAF, OIS\n"
                                 "       12 MP, f/2.0, 52mm (telephoto), 1/3.4', 1.0µm, PDAF, OIS, 2x optical zoom\n"
                                 "       12 MP, f/2.4, 13mm, 120˚ (ultrawide), 1/3.6'\n"
                                 "       TOF 3D LiDAR scanner (depth)\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, 10‑bit HDR, Dolby Vision HDR (up to 60fps), stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2815 mAh, non-removable (10.78 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 17 h (multimedia)"
                                                  "Music play - Up to 65 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Silver, Graphite, Gold, Pacific Blue\n"
                                 "Models - A2407, A2341, A2406, A2408, iPhone13,3\n"
                                 "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)\n"
                                 "Price -  $ 999.00 / £ 769.00 / ₹ 99.990\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 4056 (v5.1)\n"
                                                  "              AnTuTu: 596244 (v8)\n"
                                                  "              GFXBench: 58fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - -24.2 LUFS (Very good)\n"
                                                  "Battery life - Endurance rating 81h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 12 Pro Max Network")
                launch = types.KeyboardButton("🍏 IPHONE 12 Pro Max Launch")
                body = types.KeyboardButton("🍏 IPHONE 12 Pro Max Body")
                displ = types.KeyboardButton("🍏 IPHONE 12 Pro Max Display")
                platform = types.KeyboardButton("🍏 IPHONE 12 Pro Max Platform")
                memory = types.KeyboardButton("🍏 IPHONE 12 Pro Max Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 12 Pro Max Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 12 Pro Max Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 12 Pro Max Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 12 Pro Max Communications")
                feature = types.KeyboardButton("🍏 IPHONE 12 Pro Max Features")
                battery = types.KeyboardButton("🍏 IPHONE 12 Pro Max Battery")
                misc = types.KeyboardButton("🍏 IPHONE 12 Pro Max Misc")
                tests = types.KeyboardButton("🍏 IPHONE 12 Pro Max Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 12 Pro Max", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Launch":
                bot.send_message(message.chat.id, "Announced - 2020, October 13\n"
                                                  "Status - Available. Released 2020, November 13\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Body":
                bot.send_message(message.chat.id, "Dimensions - 160.8 x 78.1 x 7.4 mm\n"
                                                  "             (6.33 x 3.07 x 0.29 in)\n"
                                                  "Weight - 228 g (8.04 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), stainless steel frame\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for China\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 800 nits (HBM), 1200 nits (peak)\n"
                                 "Size - 6.7 inches, 109.8 cm2 (~87.4% screen-to-body ratio)\n"
                                 "Resolution - 1284 x 2778 pixels, 19.5:9 ratio (~458 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Platform":
                bot.send_message(message.chat.id, "OS - iOS 14.1, upgradable to iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 128GB 6GB RAM, 256GB 6GB RAM, 512GB 6GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Main Camera":
                bot.send_message(message.chat.id,
                                 "Quad - 12 MP, f/1.6, 26mm (wide), 1.4µm, dual pixel PDAF, OIS\n"
                                 "       12 MP, f/2.0, 52mm (telephoto), 1/3.4', 1.0µm, PDAF, OIS, 2.5x optical zoom\n"
                                 "       12 MP, f/2.4, 13mm, 120˚ (ultrawide), 1/3.6'\n"
                                 "       TOF 3D LiDAR scanner (depth)\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, 10‑bit HDR, Dolby Vision HDR (up to 60fps), stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 3687 mAh, non-removable (14.13 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 20 h (multimedia)"
                                                  "Music play - Up to 80 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Silver, Graphite, Gold, Pacific Blue\n"
                                 "Models - A2411, A2342, A2410, A2412, iPhone13,4\n"
                                 "SAR EU - 0.99 W/kg (head)     0.99 W/kg (body)\n"
                                 "Price -  $ 998.00 / € 1.107.00 / £ 869.99 / ₹ 109.999\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 12 Pro Max Tests":
                bot.send_message(message.chat.id, "Performance - GeekBench: 4240 (v5.1)\n"
                                                  "              AnTuTu: 638584 (v8)\n"
                                                  "              GFXBench: 55fps (ES 3.1 onscreen)\n"
                                                  "Display - Contrast ratio: Infinite (nominal)\n"
                                                  "Camera - Photo / Video\n"
                                                  "Loudspeaker - -23.8 LUFS (Very good)\n"
                                                  "Battery life - Endurance rating 95h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 13 Mini Network")
                launch = types.KeyboardButton("🍏 IPHONE 13 Mini Launch")
                body = types.KeyboardButton("🍏 IPHONE 13 Mini Body")
                displ = types.KeyboardButton("🍏 IPHONE 13 Mini Display")
                platform = types.KeyboardButton("🍏 IPHONE 13 Mini Platform")
                memory = types.KeyboardButton("🍏 IPHONE 13 Mini Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 13 Mini Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 13 Mini Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 13 Mini Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 13 Mini Communications")
                feature = types.KeyboardButton("🍏 IPHONE 13 Mini Features")
                battery = types.KeyboardButton("🍏 IPHONE 13 Mini Battery")
                misc = types.KeyboardButton("🍏 IPHONE 13 Mini Misc")
                tests = types.KeyboardButton("🍏 IPHONE 13 Mini Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 13 Mini", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Launch":
                bot.send_message(message.chat.id, "Announced - 2021, September 24\n"
                                                  "Status - Available. Released 2021, September 24\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Body":
                bot.send_message(message.chat.id, "Dimensions - 131.5 x 64.2 x 7.7 mm\n"
                                                  "             (5.18 x 2.53 x 0.30 in)\n"
                                                  "Weight - 141 g (4.97 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), stainless steel frame\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for China\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 800 nits (HBM), 1200 nits (peak)\n"
                                 "Size - 5.4 inches, 71.9 cm2 (~85.1% screen-to-body ratio)\n"
                                 "Resolution - 1080 x 2340 pixels, 19.5:9 ratio (~476 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Platform":
                bot.send_message(message.chat.id, "OS - iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.22 GHz Avalanche + 4xX.X GHz Blizzard)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 128GB 4GB RAM, 256GB 4GB RAM, 512GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Main Camera":
                bot.send_message(message.chat.id,
                                 "Dual - 12 MP, f/1.6, 26mm (wide), 1.7µm, dual pixel PDAF, sensor-shift OIS\n"
                                 "       12 MP, f/2.4, 120˚, 13mm (ultrawide)\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, Dolby Vision HDR (up to XXfps), stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/25/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 2438 mAh, non-removable (9.34 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 17 h (multimedia)"
                                                  "Music play - Up to 55 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Mini Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Starlight, Midnight, Blue, Pink, Red\n"
                                 "Models - A2399, A2176, A2398, 2400, A2630\n"
                                 "Price -  $ 699.99 / € 781.03 / £ 679.99 / ₹ 69.900\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 13 Network")
                launch = types.KeyboardButton("🍏 IPHONE 13 Launch")
                body = types.KeyboardButton("🍏 IPHONE 13 Body")
                displ = types.KeyboardButton("🍏 IPHONE 13 Display")
                platform = types.KeyboardButton("🍏 IPHONE 13 Platform")
                memory = types.KeyboardButton("🍏 IPHONE 13 Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 13 Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 13 Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 13 Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 13 Communications")
                feature = types.KeyboardButton("🍏 IPHONE 13 Features")
                battery = types.KeyboardButton("🍏 IPHONE 13 Battery")
                misc = types.KeyboardButton("🍏 IPHONE 13 Misc")
                tests = types.KeyboardButton("🍏 IPHONE 13 Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 13", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Launch":
                bot.send_message(message.chat.id, "Announced - 2021, September 14\n"
                                                  "Status - Available. Released 2021, September 24\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Body":
                bot.send_message(message.chat.id, "Dimensions - 146.7 x 71.5 x 7.7 mm\n"
                                                  "             (5.78 x 2.81 x 0.30 in)\n"
                                                  "Weight - 174 g (6.14 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), stainless steel frame\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for China\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 800 nits (HBM), 1200 nits (peak)\n"
                                 "Size - 6.1 inches, 90.2 cm2 (~86.0% screen-to-body ratio)\n"
                                 "Resolution - 1170 x 2532 pixels, 19.5:9 ratio (~460 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Platform":
                bot.send_message(message.chat.id, "OS - iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.22 GHz Avalanche + 4xX.X GHz Blizzard)\n"
                                                  "GPU - Apple GPU (4-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 128GB 4GB RAM, 256GB 4GB RAM, 512GB 4GB RAM\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Main Camera":
                bot.send_message(message.chat.id,
                                 "Dual - 12 MP, f/1.6, 26mm (wide), 1.7µm, dual pixel PDAF, sensor-shift OIS\n"
                                 "       12 MP, f/2.4, 120˚, 13mm (ultrawide)\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, Dolby Vision HDR (up to XXfps), stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/25/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 3240 mAh, non-removable (12.41 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 19 h (multimedia)"
                                                  "Music play - Up to 75 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Misc":
                bot.send_message(message.chat.id,
                                 "Colors - Starlight, Midnight, Blue, Pink, Red\n"
                                 "Models - A2633, A2482, A2631, A2634, A2635\n"
                                 "Price -  $ 799.99 / € 899.00 / £ 779.00 / ₹ 79.900\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Tests":
                bot.send_message(message.chat.id, "Loudspeaker - -25.5 LUFS (Very good)")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 13 Pro Network")
                launch = types.KeyboardButton("🍏 IPHONE 13 Pro Launch")
                body = types.KeyboardButton("🍏 IPHONE 13 Pro Body")
                displ = types.KeyboardButton("🍏 IPHONE 13 Pro Display")
                platform = types.KeyboardButton("🍏 IPHONE 13 Pro Platform")
                memory = types.KeyboardButton("🍏 IPHONE 13 Pro Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 13 Pro Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 13 Pro Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 13 Pro Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 13 Pro Communications")
                feature = types.KeyboardButton("🍏 IPHONE 13 Pro Features")
                battery = types.KeyboardButton("🍏 IPHONE 13 Pro Battery")
                misc = types.KeyboardButton("🍏 IPHONE 13 Pro Misc")
                tests = types.KeyboardButton("🍏 IPHONE 13 Pro Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 13 Pro", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Launch":
                bot.send_message(message.chat.id, "Announced - 2021, September 14\n"
                                                  "Status - Available. Released 2021, September 24\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Body":
                bot.send_message(message.chat.id, "Dimensions - 146.7 x 71.5 x 7.7 mm\n"
                                                  "             (5.78 x 2.81 x 0.30 in)\n"
                                                  "Weight - 204 g (7.20 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), stainless steel frame\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for China\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 800 nits (HBM), 1200 nits (peak)\n"
                                 "Size - 6.1 inches, 90.2 cm2 (~86.0% screen-to-body ratio)\n"
                                 "Resolution - 1170 x 2532 pixels, 19.5:9 ratio (~460 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Platform":
                bot.send_message(message.chat.id, "OS - iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.22 GHz Avalanche + 4xX.X GHz Blizzard)\n"
                                                  "GPU - Apple GPU (5-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 128GB 6GB RAM, 256GB 6GB RAM, 512GB 6GB RAM, 1TB\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Main Camera":
                bot.send_message(message.chat.id,
                                 "Quad - 12 MP, f/1.5, 26mm (wide), 1.9µm, dual pixel PDAF, sensor-shift OIS\n"
                                 "       12 MP, f/2.8, 77mm (telephoto), PDAF, OIS, 3x optical zoom\n"
                                 "       12 MP, f/1.8, 13mm, 120˚ (ultrawide), PDAF\n"
                                 "       TOF 3D LiDAR scanner (depth)\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, 10‑bit HDR, Dolby Vision HDR (up to 60fps),\n"
                                 "ProRes, Cinematic mode, stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/25/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 3095 mAh, non-removable (12.11 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 22 h (multimedia)"
                                                  "Music play - Up to 75 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Misc":
                bot.send_message(message.chat.id, "Colors - Graphite, Gold, Silver, Sierra Blue\n"
                                                  "Models - A2638, A2483, A2636, A2639, A2640, iPhone14,2\n"
                                                  "Price -  $ 999.00 / € 1.091.30 / £ 948.99\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                network = types.KeyboardButton("🍏 IPHONE 13 Pro Max Network")
                launch = types.KeyboardButton("🍏 IPHONE 13 Pro Max Launch")
                body = types.KeyboardButton("🍏 IPHONE 13 Pro Max Body")
                displ = types.KeyboardButton("🍏 IPHONE 13 Pro Max Display")
                platform = types.KeyboardButton("🍏 IPHONE 13 Pro Max Platform")
                memory = types.KeyboardButton("🍏 IPHONE 13 Pro Max Memory")
                maincam = types.KeyboardButton("🍏 IPHONE 13 Pro Max Main Camera")
                selfcam = types.KeyboardButton("🍏 IPHONE 13 Pro Max Selfie Camera")
                sound = types.KeyboardButton("🍏 IPHONE 13 Pro Max Sounds")
                comms = types.KeyboardButton("🍏 IPHONE 13 Pro Max Communications")
                feature = types.KeyboardButton("🍏 IPHONE 13 Pro Max Features")
                battery = types.KeyboardButton("🍏 IPHONE 13 Pro Max Battery")
                misc = types.KeyboardButton("🍏 IPHONE 13 Pro Max Misc")
                tests = types.KeyboardButton("🍏 IPHONE 13 Pro Max Tests")

                markup.add(network, launch, body, displ, platform, memory, maincam, selfcam, sound, comms, feature,
                           battery, misc, tests)

                bot.send_message(message.chat.id, "🍏 IPHONE 13 Pro", reply_markup=markup)

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Network":
                bot.send_message(message.chat.id, "Technology - GSM / CDMA / HSPA / EVDO / LTE / 5G")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Launch":
                bot.send_message(message.chat.id, "Announced - 2021, September 14\n"
                                                  "Status - Available. Released 2021, September 24\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Body":
                bot.send_message(message.chat.id, "Dimensions - 160.8 x 78.1 x 7.7 mm\n"
                                                  "             (6.33 x 3.07 x 0.30 in)\n"
                                                  "Weight - 240 g (8.47 oz)\n"
                                                  "Build - Glass front (Gorilla Glass), glass back (Gorilla Glass), stainless steel frame\n"
                                                  "SIM - Single SIM (Nano-SIM and/or eSIM) or Dual SIM (Nano-SIM, dual stand-by) - for China\n"
                                                  "IP68 dust/water resistant (up to 6m for 30 mins)\n"
                                                  "Apple Pay (Visa, Master Card, AMEX certified\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Display":
                bot.send_message(message.chat.id,
                                 "Type - Super Retina XDR OLED, HDR10, Dolby Vision, 1000 nits (HBM), 1200 nits (peak)\n"
                                 "Size - 6.7 inches, 109.8 cm2 (~87.4% screen-to-body ratio)\n"
                                 "Resolution - 1284 x 2778 pixels, 19.5:9 ratio (~458 ppi density)\n"
                                 "Protection - Scratch-resistant glass, oleophobic coating\n"
                                 "True-tone\n"
                                 "Wide color gamut\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Platform":
                bot.send_message(message.chat.id, "OS - iOS 15\n"
                                                  "Chipset - Apple A14 Bionic (5 nm)\n"
                                                  "CPU - Hexa-core (2x3.22 GHz Avalanche + 4xX.X GHz Blizzard)\n"
                                                  "GPU - Apple GPU (5-core-graphics)\n")
        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Memory":
                bot.send_message(message.chat.id, "Card slot - No\n"
                                                  "Internal - 128GB 6GB RAM, 256GB 6GB RAM, 512GB 6GB RAM, 1TB\n"
                                                  "NVMe\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Main Camera":
                bot.send_message(message.chat.id,
                                 "Quad - 12 MP, f/1.5, 26mm (wide), 1.9µm, dual pixel PDAF, sensor-shift OIS\n"
                                 "       12 MP, f/2.8, 77mm (telephoto), PDAF, OIS, 3x optical zoom\n"
                                 "       12 MP, f/1.8, 13mm, 120˚ (ultrawide), PDAF\n"
                                 "       TOF 3D LiDAR scanner (depth)\n"
                                 "Features - Dual-LED dual-tone flash, HDR (photo/panorama)\n"
                                 "Video - 4K@24/30/60fps, 1080p@30/60/120/240fps, 10‑bit HDR, Dolby Vision HDR (up to 60fps),\n"
                                 "ProRes, Cinematic mode, stereo sound rec.\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Selfie Camera":
                bot.send_message(message.chat.id, "Dual - 12 MP, f/2.2, 23mm (wide), 1/3.6'\n"
                                                  "SL 3D, (depth/biometrics sensor)\n"
                                                  "Features - HDR\n"
                                                  "Video - 4K@24/25/30/60fps, 1080p@30/60/120fps, gyro-EIS\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Sounds":
                bot.send_message(message.chat.id, "Loudspeaker - Yes, with stereo speakers\n"
                                                  "3.5mm jack - No\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Communications":
                bot.send_message(message.chat.id, "WLAN - Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, hotspot\n"
                                                  "Bluetooth - 5.0, A2DP, LE\n"
                                                  "GPS - Yes, with A-GPS, GLONASS, GALILEO, QZSS\n"
                                                  "NFC - Yes (Apple Pay only)\n"
                                                  "Radio - No\n"
                                                  "USB - Lightning, USB 2.0\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Features":
                bot.send_message(message.chat.id,
                                 "Sensors - Face ID, accelerometer, gyro, proximity, compass, barometer\n"
                                 "Siri natural language commands and dictation\n"
                                 "Ultra Wideband (UWB) support\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Battery":
                bot.send_message(message.chat.id, "Type - Li-Ion 4352 mAh, non-removable (16.75 Wh)\n"
                                                  "Charging - Fast charging 20W, 50% in 30 min (advertised)\n"
                                                  "           USB Power Delivery 2.0\n"
                                                  "           MagSafe wireless charging 15W\n"
                                                  "           Qi magnetic fast wireless charging 7.5W\n"
                                                  "Talk time - Up to 28 h (multimedia)"
                                                  "Music play - Up to 95 h\n")

        if message.chat.type == "private":
            if message.text == "🍏 IPHONE 13 Pro Max Misc":
                bot.send_message(message.chat.id, "Colors - Graphite, Gold, Silver, Sierra Blue\n"
                                                  "Models - A2638, A2483, A2636, A2639, A2640, iPhone14,2\n"
                                                  "Price -  $ 1.099.00 / € 1.207.64 / £ 1.049.00\n")


bot.polling(none_stop=True)