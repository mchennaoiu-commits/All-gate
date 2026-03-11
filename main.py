from reg import reg
from gates import *
from datetime import datetime, timedelta
from faker import Faker
import threading
import telebot
import requests
import json
import random
import time
from multiprocessing import Process
import string
from telebot import types
import re
stopuser = {}
token = '7306815535:AAG2OikNtpPQk29z_eSnna7CLIZjq5emAcw'#TOKEN
admin=5168499996

bot=telebot.TeleBot(token,parse_mode="HTML")

command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}

@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="المالك", url="https://t.me/")
			bu2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/cc_chk")
			keyboard.add(contact_button)
			photo_url = 'https://t.me/O_An6/30231'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''𝑯𝑬𝑳𝑳𝑶 ♡   {name}   𝗛𝗶 𝗖𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗵𝗲 𝗔𝘂𝘁𝗵 𝗚𝗮𝘁𝗲𝘀 𝗼𝗿 𝗖𝗵𝗮𝗿𝗴𝗲 𝗚𝗮𝘁𝗲𝘀.
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="المطور", url="https://t.me/")
		bu2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/O_An6/30231'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝑯𝑬𝑳𝑳𝑶 ♡   {name}   𝗛𝗶 𝗖𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗵𝗲 𝗔𝘂𝘁𝗵 𝗚𝗮𝘁𝗲𝘀 𝗼𝗿 𝗖𝗵𝗮𝗿𝗴𝗲 𝗚𝗮𝘁𝗲𝘀.
 ''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
def code(id):
 def my_function():
  print(id)
  #if not id ==admin:
  # return
  try:
   h=24
   with open('data.json', 'r') as json_file:
    existing_data = json.load(json_file)
   characters = string.ascii_uppercase + string.digits
   pas ='VIP-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
   current_time = datetime.now()
   ig = current_time + timedelta(hours=h)
   plan='𝗩𝗜𝗣'
   parts = str(ig).split(':')
   ig = ':'.join(parts[:2])
   with open('data.json', 'r') as json_file:
    existing_data = json.load(json_file)
   new_data = {
    pas : {
   "plan": plan,
   "time": ig,
   }
   }
   existing_data.update(new_data)
   with open('data.json', 'w') as json_file:
    json.dump(existing_data, json_file, ensure_ascii=False, indent=4) 
   msg=f'''<b> ✅
𝗞𝗘𝗬 ➜ <code>/redeem {pas}</code>
 [𝗞𝗘𝗬]</b>'''
   bot.send_message(id, msg)
  except Exception as e:
   print('ERROR : ',e)
   bot.reply_to(message,e,parse_mode="HTML")
 my_thread = threading.Thread(target=my_function)
 my_thread.start()


 
###$#########بدايه الدفع
@bot.message_handler(commands=["buy"])
def process_payment(message):
    SERVICE_COST = 100
    prices = [
        LabeledPrice(label="خدمة البوت", amount=SERVICE_COST * 1)
    ]  

    bot.send_invoice(
        chat_id=message.chat.id,
        title="خدمة البوت",
        description=f"ادفع {SERVICE_COST} نجمة للاستفادة من كود 24 ساعه في البوت",
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload="Star-Payment-Payload",
    )

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    id=message.chat.id
    bot.send_message(message.chat.id, "تم الدفع بنجاح! انتظر و سيتم ارسال لك الكود الذي اشتريته الان")
    code(id)	
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f" {BL} ",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗛𝗘𝗦𝗘 𝗔𝗥𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 
━━━━━━━━━━━━
━━━━━━━
[ϟ] Name: Brantree Auth 1
[ϟ] Format: /chk card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
━━━━━━━
[ϟ] Name: OTP PAYLAL
[ϟ] Format: /vbv card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: strip chareg 6$ 
[ϟ] Format: /ss card|month|year|cvv
[ϟ] Condition: ON✅
[ϟ] Type: Only-Vip-User

@i7cy7
</b>
''',reply_markup=keyboard)

@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text=" 𝗢𝗪𝗡𝗘𝗥  ", url="https://t.me/")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>
𝑯𝑬𝑳𝑳𝑶 {name} sorry you can not Use The Bot
</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text=" 𝗢𝗪𝗡𝗘𝗥  ", url="https://t.me/x")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>
𝑯𝑬𝑳𝑳𝑶 {name} sorry you can not Use The Bot</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text=" 𝗢𝗪𝗡𝗘𝗥  ", url="https://t.me/")
#			b2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/")
			keyboard.row(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		vvb = types.InlineKeyboardButton(text=f"ϟ - Bruntree Auth ✨",callback_data='vbv')
		vvbv = types.InlineKeyboardButton(text=f"ϟ - OTP Paypal",callback_data='vbv1')		
		wwwa = types.InlineKeyboardButton(text=f" Stripe Charge $6 $💀",callback_data='zoza')		
		keyboard.row(vvb)
		keyboard.row(vvbv)		
		keyboard.row(wwwa)		
		bot.reply_to(message, text=f'click start for start chk',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		abdo = (f"com{id}.txt")
		with open(abdo, "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'vbv')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth '
		cooo = (f"com{id}.txt")
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @i7cy7')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>''', reply_markup=mes)
					
					msg=f'''<b>Approved ✅
#Braintree_Auth 🔥[/chk]
[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @i7cy7⚡</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last or 'try agen' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(3)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @i7cy7')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()	
	
@bot.callback_query_handler(func=lambda call: call.data == 'vbv1')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='OTP PayPal V1 '
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		abdo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(abdo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @i7cy7')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(vbv(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙋𝘼𝙎𝙎𝙋✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝙊𝙏𝙋 💚  ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱  ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>''', reply_markup=mes)
					
					msg=f'''<b>Passed ✅
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -><code> {last}</code>
card Info -> <code>{card_type} </code>- <code>{brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Bot by : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b> ϟ - OTP Card ✅
#OTP
<a href='tg://user?id=5268530944'>[⌥]</a>Card ->  <code>{cc}</code>
<a href='tg://user?id=5268530944'>[⌥]</a> Status -> {last}
<a href='tg://user?id=5268530944'>[⌥]</a> Gate -> {gate}

card Info -> <code>{card_type} </code>- <code>{brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

<a href='tg://user?id=5268530944'>[⌥]</a> Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
<a href='tg://user?id=5268530944'>[⌥]</a> Programmer -> @i7cy7⚡</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️-
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -><code> {last}</code>
card Info -> <code>{card_type} </code>- <code>{brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Bot by : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>𝘿𝙍𝙂𝘼𝙢</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'Successful' in last:
						ch += 1
						#bot.send_message(call.from_user.id, msg)
					elif "funjfbjds" in last:
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif 'Required' in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(1)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @i7cy7')#علي الاقل اذكى المصدر
	my_thread = threading.Thread(target=my_function)
	my_thread.start()				

@bot.callback_query_handler(func=lambda call: call.data == 'zoza')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		cooo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @i7cy7')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Telev(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>''', reply_markup=mes)
					
					msg=f'''<b>Approved ✅
[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @i7cy7⚡</b>'''
					if "Charged !✅" in last or "The card's security code is incorrect." in last or 'Payment success' in last or 'success' in last or 'Payment Completed.' in last or 'Approved' in last or 'CVV' in last or 'Success'in last or 'CHARGED' in last or 'Payment has been made' in last or 'CHARGED 1$' in last or 'successfully' in last or 'INVALID_BILLING_ADDRESS' in last or 'Your payment has already been processed' in last or 'Thank You For Donation.' in last or 'status": "succeeded' in last or 'NEED_CREDIT_CARD' in last or 'Insufficient Funds' in last or 'Payment Successful' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last or 'try agen' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(3)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @i7cy7')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()		
	

@bot.message_handler(func=lambda message: message.text.lower().startswith('.ss') or message.text.lower().startswith('/ss'))
def respond_to_vbv(message):
	gate='stripe charge'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_pNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Telev(cc))
	except Exception as e:
		last='Error'
		print(e)
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msgd=f'''<b>ϟ -  Not valid ❌
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @i7cy7⚡</b>'''
	msg=f'''<b> Approved ✅
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @i7cy7⚡</b>'''
	msgc=f'''<b>𝑪𝑪𝑵 ☑️
	
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgf=f'''<b> Approved ✅
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @i7cy7⚡</b>'''
	if 'success' in last or 'Thank you for your order.' in last or 'Thank you' in last or 'Charged' in last or 'Charged !✅' in last or 'success' in last or 'Success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "funds" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgf)
	elif "card's security" in last or 'ccn' in last or 'cvv' in last or 'Insufficient funds' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)		

			
@bot.message_handler(func=lambda message: message.text.lower().startswith('.otp') or message.text.lower().startswith('/otp') or message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv') or message.text.lower().startswith('/vb') or message.text.lower().startswith('.vb'))
def respond_to_vbv(message):
	gate='Brantree OTP 3D'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/i_PnP")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/i_pnp1")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/i_pnp")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/i_pnp")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/i_pnp")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/i_pnp1")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(vbv(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b> 𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
#3D
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='strip Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>Approved ✅
#Braintree
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @i7cy7⚡</b>'''
	msgd=f'''<b>Invalid ❌
#Braintree
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'success' in last or 'Success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)	



@bot.message_handler(func=lambda message: message.text.lower().startswith('.ua') or message.text.lower().startswith('/ua'))
def respond_to_vbv(message):
	gate='strip Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>Approved ✅
#Braintree
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @i7cy7⚡</b>'''
	msgd=f'''<b>Invalid ❌
#Braintree
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'success' in last or 'Success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)	







@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>ÃBĐO 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()#x8xt8
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='i7cy7-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
	
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>/redeem {pas}</code>
 [𝗞𝗘𝗬]BY : @i7cy7</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
	


@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print("ERORR")
#bot.polling()
