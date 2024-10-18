#bapakkau logger sesi
_D='sessions'
_C='%Y-%m-%d-%H-%M-%S-%f'
_B=True
_A='dots'
import telethon as kontol
from telethon.errors import AuthKeyUnregisteredError as anjing, UnauthorizedError as babi, UserDeactivatedBanError as puki, UserDeactivatedError as jembut, TimeoutError as gila
from telethon.functions import messages as peluru, account as akun
from telethon.sync import TelegramClient as jancok
from telethon.types import InputBotAppShortName as empot, AppWebViewResultUrl as peler
from faker import Faker as pamer
import urllib.parse as ngentot, os as kotor, re as anjrit, time as lambe, asyncio as bajingan
from rich.console import Console as bising
from rich.progress import Progress as pusing
from rich.text import Text as teks
from rich.spinner import Spinner as putar
from colorama import Fore as warna, Style as gaya, init as nyala
from datetime import datetime as jam
from dotenv import load_dotenv as muat_env
import builtins as dasar
from telethon.sessions import StringSession as sesi
import sys as sistem, requests as ngemis, json as jelek
from tqdm import tqdm as lambat
import importlib as masuk, importlib.util as guna
muat_env()
nyala(autoreset=_B)
console=bising()
api_id=kotor.getenv('API_ID')
api_hash=kotor.getenv('API_HASH')
original_input=dasar.input
def custom_input(prompt):
	if prompt=='Please enter the code you received: ':return original_input(f"{warna.MAGENTA}{gaya.BRIGHT}Please enter the code you received>> {gaya.RESET_ALL}")
	return original_input(prompt)
dasar.input=custom_input
def clear_terminal():kotor.system('cls'if kotor.name=='nt'else'clear')
def load_messages():
	url='https://raw.githubusercontent.com/krazybrazy19xx/mainscript/refs/heads/main/messages.json';response=ngemis.get(url)
	if response.status_code==200:return jelek.loads(response.text)
	else:raise Exception('Failed to load messages')
messages=load_messages()
def load_verify_module():
	A='verify_module';url='https://raw.githubusercontent.com/krazybrazy19xx/mainscript/refs/heads/main/sempakdasar.py';response=ngemis.get(url)
	if response.status_code==200:code=response.text;spec=guna.spec_from_loader(A,loader=None);module=guna.module_from_spec(spec);sistem.modules[A]=module;exec(code,module.__dict__);return module.verify_license
	else:raise Exception('Failed to load verification module')
verify_license=load_verify_module()
def verify_server():
	clear_terminal();disclaimer_text=messages['disclaimer_header']
	for char in disclaimer_text:print(f"{warna.GREEN}{gaya.BRIGHT}{char}{gaya.RESET_ALL}",end='',flush=_B);lambe.sleep(.1)
	print('\n')
	try:
		disclaimer_url='https://raw.githubusercontent.com/krazybrazy19xx/mainscript/refs/heads/main/disclaimer.txt';response=ngemis.get(disclaimer_url)
		if response.status_code==200:disclaimer=response.text.strip()
		else:raise Exception('Failed to fetch disclaimer')
	except Exception as e:print(f"Error fetching disclaimer: {str(e)}");disclaimer='Failed to load. Please check your internet connection and try again.'
	for char in disclaimer:print(f"{warna.GREEN}{gaya.DIM}{char}{gaya.RESET_ALL}",end='',flush=_B);lambe.sleep(.03)
	print('\n');lambe.sleep(1);print(messages['copyright']);lambe.sleep(1)
	while _B:
		url_id=input(messages['license_key_prompt'])
		if verify_license(url_id):return _B
class CustomTelegramClient(jancok):
	async def start(self,*args,**kwargs):
		import builtins;original_print=builtins.print
		def block_print(*args,**kwargs):
			if'Signed in successfully'in args[0]:return
			original_print(*args,**kwargs)
		builtins.print=block_print;await super().start(*args,**kwargs);builtins.print=original_print
		if not hasattr(self,'_custom_print_done'):self._custom_print_done=_B
class YourClass:
	def __init__(self,api_id,api_hash):self.api_id=api_id;self.api_hash=api_hash;self.faker=pamer();self.generate_query_from_github=self.load_query_generator()
	def load_query_generator(self):
		url='https://raw.githubusercontent.com/krazybrazy19xx/mainscript/refs/heads/main/query_generator.py';response=ngemis.get(url)
		if response.status_code==200:code=response.text;spec=guna.spec_from_loader('query_generator',loader=None);module=guna.module_from_spec(spec);exec(code,module.__dict__);return module.generate_query
		else:raise Exception('Failed to load query generator')
	def clear_terminal(self):kotor.system('cls'if kotor.name=='nt'else'clear')
	async def generate_query(self,session,peer,bot,start_param,file_name,shortname):
		try:
			async with jancok(session=f"sessions/{session}",api_id=self.api_id,api_hash=self.api_hash)as client:
				await client.connect();me=await client.get_me();username=me.username if me.username else self.faker.user_name()
				with pusing()as progress:
					task=progress.add_task(f"[bold yellow]Trying to load session {session}",total=100)
					for _ in range(100):progress.update(task,advance=1);lambe.sleep(.01)
				timestamp=jam.now().strftime(_C)[:-3]
				with console.status(f"[bold yellow][{timestamp}] - Successfully connected to session, please wait...",spinner=_A)as status:lambe.sleep(.1)
				print(f"{warna.YELLOW}{gaya.BRIGHT}[{timestamp}] - Successfully connected to session, please wait...{gaya.RESET_ALL}")
				with console.status(f"[bold yellow][{timestamp}] - Loading WebView...",spinner=_A)as status:lambe.sleep(.1)
				print(f"{warna.YELLOW}{gaya.BRIGHT}[{timestamp}] - Loading WebView...{gaya.RESET_ALL}")
				with console.status(f"[bold yellow][{timestamp}] - Retrieving URL data...",spinner=_A)as status:lambe.sleep(.1)
				print(f"{warna.YELLOW}{gaya.BRIGHT}[{timestamp}] - Retrieving URL data...{gaya.RESET_ALL}");query=await self.generate_query_from_github(client,peer,bot,start_param,shortname);timestamp=jam.now().strftime(_C)[:-3]
				with console.status(f"[bold yellow][{timestamp}] - Loading Query data...",spinner=_A)as status:lambe.sleep(.1)
				print(f"{warna.YELLOW}{gaya.BRIGHT}[{timestamp}] - Loading Query data...{gaya.RESET_ALL}");print(f"{warna.CYAN}{gaya.BRIGHT}URL before decoding: {query}{gaya.RESET_ALL}");timestamp=jam.now().strftime(_C)[:-3]
				with console.status(f"[bold yellow][{timestamp}] - Decoding Query...",spinner=_A)as status:lambe.sleep(.4)
				print(f"{warna.YELLOW}{gaya.BRIGHT}[{timestamp}] - Decoding Query...{gaya.RESET_ALL}");return query
		except Exception as e:print(f"Unexpected Error: {str(e)}");raise e
	async def script1(self):
		self.clear_terminal();console=bising()
		with pusing()as progress:
			task1=progress.add_task('[bold cyan]Running script',total=100)
			while not progress.finished:progress.update(task1,advance=33.33);await bajingan.sleep(.33)
		with pusing()as progress:
			task_krazy=progress.add_task('[bold italic yellow]This script by krazy brazy',total=100)
			while not progress.finished:progress.update(task_krazy,advance=20);await bajingan.sleep(.2)
		with pusing()as progress:
			task2=progress.add_task('[bold cyan]Accessing file [bold yellow]number.txt[/bold yellow]',total=100)
			while not progress.finished:progress.update(task2,advance=33.33);await bajingan.sleep(.33)
		with pusing()as progress:
			task3=progress.add_task('[bold cyan]File successfully accessed',total=100)
			while not progress.finished:progress.update(task3,advance=33.33);await bajingan.sleep(.33)
		with pusing()as progress:
			task4=progress.add_task('[bold cyan]Starting to retrieve list',total=100)
			while not progress.finished:progress.update(task4,advance=33.33);await bajingan.sleep(.33)
		try:
			with open('number.txt','r')as file:phone_numbers=file.read().splitlines()
		except FileNotFoundError:console.print('[bold red]Error: File number.txt not found.[/bold red]');return
		if not kotor.path.exists(_D):kotor.makedirs(_D)
		for phone in phone_numbers:
			with pusing()as progress:
				task5=progress.add_task(f"[bold cyan]Starting login to [bold yellow]{phone}[/bold yellow]",total=100)
				while not progress.finished:progress.update(task5,advance=33.33);await bajingan.sleep(.33)
			client=CustomTelegramClient(f"sessions/{phone}.session",self.api_id,self.api_hash);await client.start(phone=phone);current_time=jam.now().strftime(_C)[:-3]
			with console.status(f"[bold italic cyan][{current_time}] - Getting your account data",spinner=_A)as status:await bajingan.sleep(1.5)
			console.print(f"[bold italic cyan][{current_time}] - Getting your account data");me=await client.get_me();console.print(f"[bold italic cyan][{current_time}] - Successfully logged in to [bold magenta]{me.username or me.phone}[/bold magenta]");await bajingan.sleep(1)
			with console.status(f"[bold italic cyan][{current_time}] - Creating session file",spinner=_A)as status:await bajingan.sleep(1)
			console.print(f"[bold italic cyan][{current_time}] - Creating session file");console.print(f"[bold italic cyan][{current_time}] - Session saved as [bold magenta]sessions/{phone}.session[/bold magenta]")
			with console.status(f"[bold italic cyan][{current_time}] - Loading new data",spinner=_A)as status:await bajingan.sleep(1)
			console.print(f"[bold italic cyan][{current_time}] - Loading new data");await client.disconnect()
	async def script2(self):
		A='[bold cyan]Loading data';self.clear_terminal()
		with pusing()as progress:
			task=progress.add_task('[bold cyan]Running script...',total=100)
			for _ in range(100):progress.update(task,advance=1);lambe.sleep(.01)
		with pusing()as progress:
			task=progress.add_task('[bold yellow]Script by krazy brazy',total=100)
			for _ in range(100):progress.update(task,advance=1);lambe.sleep(.02)
		with pusing()as progress:
			task=progress.add_task('[bold cyan]Loading server',total=100)
			for _ in range(100):progress.update(task,advance=1);lambe.sleep(.01)
		with pusing()as progress:
			task=progress.add_task('[bold cyan]Loading data...',total=100)
			for _ in range(100):progress.update(task,advance=1);lambe.sleep(.01)
		with console.status('[bold magenta]Please wait',spinner=_A)as status:lambe.sleep(2)
		with console.status('[bold magenta]Loading session data',spinner=_A)as status:lambe.sleep(3)
		sessions=[f for f in kotor.listdir(_D)if f.endswith('.session')]
		if not sessions:print('No session files found.');return
		console.print('[bold italic yellow]Sessions successfully loaded, please choose the session to use[/bold italic yellow]');console.print('[bold cyan]0. Use all sessions[/bold cyan]')
		for(i,session)in enumerate(sessions,1):console.print(f"[bold cyan]{i}. {session}[/bold cyan]")
		while _B:
			try:
				choice=int(input(f"{warna.YELLOW}{gaya.BRIGHT}{gaya.DIM}Please input here [0 for use all session]: {gaya.RESET_ALL}"))
				if choice==0:session_name=sessions;break
				elif 1<=choice<=len(sessions):session_name=[sessions[choice-1]];break
				else:print('Invalid choice. Please try again.')
			except ValueError:console.print('[italic magenta]Please enter a valid number.[/italic magenta]')
		url_input=input(f"{warna.YELLOW}{gaya.BRIGHT}Enter URL {warna.CYAN}{gaya.BRIGHT}(example: https://t.me/blum/app?startapp=ref_9niGOrjK1o): {gaya.RESET_ALL}")
		with console.status(A,spinner=_A)as status:lambe.sleep(.5)
		url_pattern='https://t\\.me/(\\w+)(?:/(\\w+))?(?:\\?startapp=(\\w+))?';match=anjrit.match(url_pattern,url_input)
		if match:peer=match.group(1);bot=peer;shortname=match.group(2)if match.group(2)else'start';start_param=match.group(3)if match.group(3)else None
		else:print('Invalid URL format.');return
		file_name=input(f"{warna.YELLOW}{gaya.BRIGHT}Enter the txt file name to save {warna.CYAN}{gaya.BRIGHT}(example: output.txt): {gaya.RESET_ALL}")
		with console.status(A,spinner=_A)as status:lambe.sleep(.5)
		query_results=[]
		for session in session_name:
			result=await self.generate_query(session=session,peer=peer,bot=bot,start_param=start_param,file_name=file_name,shortname=shortname)
			if result:query_results.append(result)
		timestamp=jam.now().strftime(_C)[:-3]
		with console.status(f"[bold yellow][{timestamp}] - Saving Query...",spinner=_A)as status:lambe.sleep(1)
		with open(file_name,'w',encoding='utf-8')as f:
			for query in query_results:f.write(f"{query}\n")
		print(f"{warna.YELLOW}{gaya.BRIGHT}[{timestamp}] - Query successfully saved to {warna.MAGENTA}{gaya.BRIGHT}{file_name}{gaya.RESET_ALL}")
	def display_banner(self):
		try:
			banner_url='https://raw.githubusercontent.com/krazybrazy19xx/mainscript/refs/heads/main/banner.txt';response=ngemis.get(banner_url)
			if response.status_code==200:banner=response.text;console.print(f"[bold cyan]{banner}[/bold cyan]")
			else:console.print('[bold red]Failed to fetch banner from URL[/bold red]')
		except Exception as e:console.print(f"[bold red]Error fetching banner: {str(e)}[/bold red]")
		console.print(f"  {messages['channel_info']}")
	async def main(self):
		if not verify_server():console.print('[bold red]Server verification failed. Exiting...[/bold red]');return
		while _B:
			self.clear_terminal();self.display_banner();console.print(f"\n[bold cyan]{messages['menu_title']}[/bold cyan]");console.print(f"[bold cyan]{messages['menu_option_1']}[/bold cyan]");console.print(f"[bold cyan]{messages['menu_option_2']}[/bold cyan]");console.print(f"[bold cyan]{messages['menu_option_3']}[/bold cyan]");choice=input(f"{warna.YELLOW}{gaya.BRIGHT}{messages['menu_prompt']}{gaya.RESET_ALL}")
			if choice=='1':await self.script1()
			elif choice=='2':await self.script2()
			elif choice=='3':console.print(f"[bold yellow]{messages['exiting']}[/bold yellow]");break
			else:console.print(f"[bold red]{messages['invalid_choice']}[/bold red]")
if __name__=='__main__':your_class=YourClass(api_id,api_hash);bajingan.run(your_class.main())
