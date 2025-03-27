#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import random
import requests
from datetime import datetime
from colorama import Fore, Back, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Kelas untuk menyimpan banner dan utilitas tampilan
class Display:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def show_banner():
        banner = f"""
{Fore.CYAN}██╗███╗   ██╗██████╗  ██████╗ ███╗   ██╗██████╗ ███████╗ ██╗ ██╗██╗
{Fore.CYAN}██║████╗  ██║██╔══██╗██╔═████╗████╗  ██║╚════██╗██╔════╝███║███║██║
{Fore.CYAN}██║██╔██╗ ██║██║  ██║██║██╔██║██╔██╗ ██║ █████╔╝███████╗╚██║╚██║██║
{Fore.MAGENTA}██║██║╚██╗██║██║  ██║████╔╝██║██║╚██╗██║██╔═══╝ ╚════██║ ██║ ██║╚═╝
{Fore.MAGENTA}██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║███████╗███████║ ██║ ██║██╗
{Fore.MAGENTA}╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═╝ ╚═╝╚═╝
{Fore.RED}███████╗ █████╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗    ██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
{Fore.RED}██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗╚██╗ ██╔╝    ╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
{Fore.RED}███████╗███████║██║  ██║██████╔╝██║   ██║ ╚████╔╝      ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   
{Fore.RED}╚════██║██╔══██║██║  ██║██╔══██╗██║   ██║  ╚██╔╝       ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   
{Fore.RED}███████║██║  ██║██████╔╝██████╔╝╚██████╔╝   ██║       ██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   
{Fore.RED}╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
{Fore.GREEN}   • {Fore.YELLOW}Bug Bounty Dork Finder Tool v2.0{Fore.GREEN} •
{Fore.BLUE}   • {Fore.WHITE}Powered by IND0N3S14 S4DB0Y XPL01T Team{Fore.BLUE} •
{Fore.RED}   • {Fore.WHITE}Use responsibly and ethically{Fore.RED} •
"""
        print(banner)
    
    @staticmethod
    def show_menu():
        menu = f"""
{Fore.YELLOW}╔═══════════════════════════════════════════╗
{Fore.YELLOW}║{Fore.WHITE}             MENU UTAMA                    {Fore.YELLOW}║
{Fore.YELLOW}╠═══════════════════════════════════════════╣
{Fore.YELLOW}║ {Fore.GREEN}[1]{Fore.WHITE} Cross-Site Scripting (XSS)            {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[2]{Fore.WHITE} SQL Injection                         {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[3]{Fore.WHITE} Local/Remote File Inclusion (LFI/RFI) {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[4]{Fore.WHITE} Server-Side Request Forgery (SSRF)    {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[5]{Fore.WHITE} Command Injection                     {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[6]{Fore.WHITE} Open Redirect                         {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[7]{Fore.WHITE} Information Disclosure                {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[8]{Fore.WHITE} XML External Entity (XXE)             {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[9]{Fore.WHITE} Cari Dork Berdasarkan Keyword         {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[10]{Fore.WHITE} Bantuan & Referensi                  {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[11]{Fore.WHITE} Tentang Alat Ini                     {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.GREEN}[12]{Fore.WHITE} Keluar                               {Fore.YELLOW}║
{Fore.YELLOW}╚═══════════════════════════════════════════╝
"""
        print(menu)

    @staticmethod
    def loading_animation(message="Memuat...", duration=2):
        chars = "|/-\\"
        for _ in range(int(duration * 10)):
            for char in chars:
                sys.stdout.write(f'\r{Fore.YELLOW}{message} {char}')
                sys.stdout.flush()
                time.sleep(0.1)
        print()

# Kelas untuk mengelola database dork
class DorkDatabase:
    def __init__(self):
        self.db_file = "dorks_database.json"
        self.dorks = self.load_database()
    
    def load_database(self):
        # Jika database tidak ada, buat default
        if not os.path.exists(self.db_file):
            self.create_default_database()
        
        try:
            with open(self.db_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Gagal membaca database: {e}")
            return self.create_default_database()
    
    def create_default_database(self):
        default_db = {
            "xss": [
                {"dork": "inurl:search.php?q=", "description": "Potensial XSS pada parameter pencarian", "risk": "Medium"},
                {"dork": "inurl:php?id=", "description": "Parameter id tidak terfilter dengan baik", "risk": "High"},
                {"dork": "inurl:php?feedback=", "description": "Form feedback rentan XSS", "risk": "Medium"},
                {"dork": "inurl:view.php?page=", "description": "Parameter page potensial XSS", "risk": "High"},
                {"dork": "inurl:product.php?pid=", "description": "Parameter product id tidak terfilter", "risk": "Medium"},
                {"dork": "inurl:result.php?search=", "description": "Parameter pencarian rentan XSS", "risk": "Medium"},
                {"dork": "inurl:preview.php?file=", "description": "Parameter file rentan XSS", "risk": "High"},
                {"dork": "inurl:news.php?title=", "description": "Parameter title rentan XSS", "risk": "Medium"}
            ],
            "sql": [
                {"dork": "inurl:product.php?id=", "description": "Potensial SQL Injection pada ID produk", "risk": "Critical"},
                {"dork": "inurl:category.php?id=", "description": "Parameter kategori rentan SQL Injection", "risk": "High"},
                {"dork": "inurl:news.php?id=", "description": "ID berita tidak terfilter dengan baik", "risk": "Critical"},
                {"dork": "inurl:item.php?itemid=", "description": "Parameter item id rentan SQL Injection", "risk": "High"},
                {"dork": "inurl:view_product.php?id=", "description": "View product rentan SQL Injection", "risk": "Critical"},
                {"dork": "inurl:shop.php?cat=", "description": "Parameter kategori shop rentan", "risk": "High"},
                {"dork": "inurl:shopdisplayproducts.cfm?id=", "description": "Parameter produk ColdFusion rentan", "risk": "Critical"},
                {"dork": "inurl:ViewProduct.asp?prodID=", "description": "Produk ASP rentan SQL Injection", "risk": "High"}
            ],
            "lfi": [
                {"dork": "inurl:include_file=", "description": "Include file tidak terfilter", "risk": "Critical"},
                {"dork": "inurl:show.php?file=", "description": "Parameter file rentan LFI", "risk": "High"},
                {"dork": "inurl:download.php?path=", "description": "Path download tidak terfilter", "risk": "Critical"},
                {"dork": "inurl:index.php?page=", "description": "Parameter page rentan LFI", "risk": "High"},
                {"dork": "inurl:main.php?inc=", "description": "Parameter include rentan", "risk": "Critical"},
                {"dork": "inurl:index.php?content=", "description": "Content include rentan LFI", "risk": "High"},
                {"dork": "inurl:index.php?open=", "description": "Parameter open rentan LFI", "risk": "Critical"},
                {"dork": "inurl:index.php?from_market=", "description": "Parameter from_market rentan", "risk": "Medium"}
            ],
            "ssrf": [
                {"dork": "inurl:proxy.php?url=", "description": "Proxy URL rentan SSRF", "risk": "Critical"},
                {"dork": "inurl:fetch.php?url=", "description": "Parameter fetch rentan SSRF", "risk": "High"},
                {"dork": "inurl:redirect.php?url=", "description": "Redirect URL rentan SSRF", "risk": "Critical"},
                {"dork": "inurl:connect.php?url=", "description": "Parameter koneksi rentan", "risk": "High"},
                {"dork": "inurl:api/fetch?url=", "description": "API fetch rentan SSRF", "risk": "Critical"}
            ],
            "command_injection": [
                {"dork": "inurl:execute.php?cmd=", "description": "Command execution langsung", "risk": "Critical"},
                {"dork": "inurl:ping.php?host=", "description": "Ping command rentan injeksi", "risk": "High"},
                {"dork": "inurl:shell.php?command=", "description": "Shell command tidak terfilter", "risk": "Critical"},
                {"dork": "inurl:exec.php?command=", "description": "Exec command tidak terfilter", "risk": "Critical"}
            ],
            "open_redirect": [
                {"dork": "inurl:redirect.php?url=", "description": "Redirect URL tidak tervalidasi", "risk": "Medium"},
                {"dork": "inurl:return.php?site=", "description": "Return parameter rentan", "risk": "Medium"},
                {"dork": "inurl:exit.php?url=", "description": "Exit URL tidak tervalidasi", "risk": "Medium"},
                {"dork": "inurl:out.php?link=", "description": "Out link parameter rentan", "risk": "Medium"}
            ],
            "info_disclosure": [
                {"dork": "intitle:\"Index of /admin\"", "description": "Directory listing admin", "risk": "High"},
                {"dork": "intitle:\"Index of /backup\"", "description": "Directory listing backup", "risk": "High"},
                {"dork": "intitle:\"Index of /config\"", "description": "Directory listing config", "risk": "High"},
                {"dork": "intext:\"sql dump\" filetype:sql", "description": "SQL dump files exposed", "risk": "Critical"},
                {"dork": "inurl:/phpinfo.php", "description": "PHP info exposed", "risk": "High"},
                {"dork": "filetype:env intext:DB_PASSWORD", "description": "Env files dengan password DB", "risk": "Critical"}
            ],
            "xxe": [
                {"dork": "inurl:xml.php?file=", "description": "Parameter XML file tidak terfilter", "risk": "High"},
                {"dork": "inurl:process.php?xml=", "description": "XML processing tidak aman", "risk": "Critical"},
                {"dork": "inurl:upload.php filetype:xml", "description": "Upload XML rentan XXE", "risk": "High"}
            ]
        }
        
        # Simpan database default
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(default_db, f, indent=4)
        
        return default_db
    
    def get_dorks(self, category):
        return self.dorks.get(category, [])
    
    def search_dorks(self, keyword):
        results = []
        for category, dorks in self.dorks.items():
            for dork in dorks:
                if keyword.lower() in dork["dork"].lower() or keyword.lower() in dork["description"].lower():
                    # Tambah kategori untuk pencarian
                    dork_with_category = dork.copy()
                    dork_with_category["category"] = category
                    results.append(dork_with_category)
        return results
    
    def add_dork(self, category, dork, description, risk="Medium"):
        if category not in self.dorks:
            self.dorks[category] = []
        
        self.dorks[category].append({
            "dork": dork,
            "description": description,
            "risk": risk
        })
        
        self.save_database()
    
    def save_database(self):
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(self.dorks, f, indent=4)

# Kelas untuk pencarian dan testing dork
class DorkFinder:
    def __init__(self, database):
        self.db = database
        self.results_folder = "hasil_dork"
        self.ensure_results_folder()
    
    def ensure_results_folder(self):
        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)
    
    def display_dorks(self, category):
        dorks = self.db.get_dorks(category)
        if not dorks:
            print(f"{Fore.RED}[ERROR] Kategori '{category}' tidak ditemukan")
            return
        
        category_titles = {
            "xss": "Cross-Site Scripting (XSS)",
            "sql": "SQL Injection",
            "lfi": "Local/Remote File Inclusion (LFI/RFI)",
            "ssrf": "Server-Side Request Forgery (SSRF)",
            "command_injection": "Command Injection",
            "open_redirect": "Open Redirect",
            "info_disclosure": "Information Disclosure",
            "xxe": "XML External Entity (XXE)"
        }
        
        title = category_titles.get(category, category.upper())
        
        print(f"\n{Fore.YELLOW}╔{'═' * (len(title) + 12)}╗")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}DORK {title} {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}╠{'═' * (len(title) + 12)}╣")
        
        for i, dork in enumerate(dorks, 1):
            risk_color = Fore.GREEN
            if dork["risk"] == "Medium":
                risk_color = Fore.YELLOW
            elif dork["risk"] == "High":
                risk_color = Fore.RED
            elif dork["risk"] == "Critical":
                risk_color = Fore.MAGENTA
                
            print(f"{Fore.YELLOW}║ {Fore.GREEN}[{i}]{Fore.WHITE} {dork['dork']}")
            print(f"{Fore.YELLOW}║   {Fore.BLUE}• Deskripsi: {Fore.WHITE}{dork['description']}")
            print(f"{Fore.YELLOW}║   {Fore.BLUE}• Risiko: {risk_color}{dork['risk']}")
            print(f"{Fore.YELLOW}╠{'─' * (len(title) + 12)}╣")
        
        print(f"{Fore.YELLOW}╚{'═' * (len(title) + 12)}╝")
    
    def display_search_results(self, results, keyword):
        if not results:
            print(f"\n{Fore.RED}[!] Tidak ada dork yang ditemukan dengan keyword '{keyword}'")
            return
        
        print(f"\n{Fore.YELLOW}╔{'═' * 60}╗")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}HASIL PENCARIAN UNTUK: '{Fore.WHITE}{keyword}{Fore.CYAN}' {Fore.YELLOW}{' ' * (38 - len(keyword))}║")
        print(f"{Fore.YELLOW}╠{'═' * 60}╣")
        
        for i, dork in enumerate(results, 1):
            risk_color = Fore.GREEN
            if dork["risk"] == "Medium":
                risk_color = Fore.YELLOW
            elif dork["risk"] == "High":
                risk_color = Fore.RED
            elif dork["risk"] == "Critical":
                risk_color = Fore.MAGENTA
            
            category_name = dork["category"].replace("_", " ").upper()
            
            print(f"{Fore.YELLOW}║ {Fore.GREEN}[{i}]{Fore.WHITE} {dork['dork']}")
            print(f"{Fore.YELLOW}║   {Fore.BLUE}• Kategori: {Fore.WHITE}{category_name}")
            print(f"{Fore.YELLOW}║   {Fore.BLUE}• Deskripsi: {Fore.WHITE}{dork['description']}")
            print(f"{Fore.YELLOW}║   {Fore.BLUE}• Risiko: {risk_color}{dork['risk']}")
            print(f"{Fore.YELLOW}╠{'─' * 60}╣")
        
        print(f"{Fore.YELLOW}╚{'═' * 60}╝")
    
    def save_dorks_to_file(self, category):
        dorks = self.db.get_dorks(category)
        if not dorks:
            print(f"{Fore.RED}[ERROR] Kategori '{category}' tidak ditemukan")
            return
        
        category_titles = {
            "xss": "Cross-Site Scripting (XSS)",
            "sql": "SQL Injection",
            "lfi": "Local/Remote File Inclusion (LFI/RFI)",
            "ssrf": "Server-Side Request Forgery (SSRF)",
            "command_injection": "Command Injection",
            "open_redirect": "Open Redirect",
            "info_disclosure": "Information Disclosure",
            "xxe": "XML External Entity (XXE)"
        }
        
        title = category_titles.get(category, category.upper())
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.results_folder}/dork_{category}_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=== DORK {title} ===\n")
            f.write(f"Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for i, dork in enumerate(dorks, 1):
                f.write(f"[{i}] {dork['dork']}\n")
                f.write(f"    • Deskripsi: {dork['description']}\n")
                f.write(f"    • Risiko: {dork['risk']}\n\n")
        
        print(f"\n{Fore.GREEN}[+] Dork berhasil disimpan ke file: {Fore.WHITE}{filename}")
    
    def test_url(self, url, category):
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        print(f"\n{Fore.YELLOW}[*] Menguji URL: {Fore.WHITE}{url}")
        try:
            response = requests.get(url, timeout=10, verify=False)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] URL dapat diakses (Status 200 OK)")
                
                # Test untuk berbagai kategori
                if category == "xss":
                    test_payload = "<script>alert('XSS')</script>"
                    print(f"{Fore.YELLOW}[*] Mencoba payload XSS: {test_payload}")
                    
                elif category == "sql":
                    test_payload = "' OR '1'='1"
                    print(f"{Fore.YELLOW}[*] Mencoba payload SQL Injection: {test_payload}")
                    
                elif category == "lfi":
                    test_payload = "../../../etc/passwd"
                    print(f"{Fore.YELLOW}[*] Mencoba payload LFI: {test_payload}")
                
                # Tambahkan warning untuk mengingatkan penggunaan etis
                print(f"\n{Fore.RED}[!] PERINGATAN: {Fore.WHITE}Pengujian lanjutan harus dilakukan hanya pada sistem yang Anda memiliki izin untuk diuji.")
                
            else:
                print(f"{Fore.RED}[!] URL tidak dapat diakses (Status {response.status_code})")
        except Exception as e:
            print(f"{Fore.RED}[!] Gagal menguji URL: {e}")

# Kelas utama aplikasi
class BugBountyDorkFinder:
    def __init__(self):
        self.display = Display()
        self.db = DorkDatabase()
        self.dork_finder = DorkFinder(self.db)
    
    def show_references(self):
        print(f"\n{Fore.YELLOW}╔{'═' * 60}╗")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}BANTUAN & REFERENSI {Fore.YELLOW}{' ' * 41}║")
        print(f"{Fore.YELLOW}╠{'═' * 60}╣")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}Google Dorking adalah teknik pencarian lanjutan untuk {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}menemukan informasi spesifik yang tidak mudah diakses. {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}Dalam konteks keamanan, dork dapat membantu menemukan {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}situs yang berpotensi rentan.{Fore.YELLOW}{' ' * 27}║")
        print(f"{Fore.YELLOW}╠{'═' * 60}╣")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}OPERATOR PENCARIAN GOOGLE {Fore.YELLOW}{' ' * 35}║")
        print(f"{Fore.YELLOW}╠{'═' * 60}╣")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}intitle:{Fore.WHITE} Mencari halaman dengan kata tertentu di judul {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}inurl:{Fore.WHITE} Mencari URL yang mengandung kata tertentu {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}intext:{Fore.WHITE} Mencari halaman dengan teks tertentu {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}site:{Fore.WHITE} Membatasi pencarian ke domain tertentu {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}filetype:{Fore.WHITE} Mencari file dengan ekstensi tertentu {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}╠{'═' * 60}╣")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}KEAMANAN & ETIKA {Fore.YELLOW}{' ' * 43}║")
        print(f"{Fore.YELLOW}╠{'═' * 60}╣")
        print(f"{Fore.YELLOW}║ {Fore.RED}• {Fore.WHITE}Gunakan alat ini hanya untuk tujuan legal {Fore.YELLOW}{' ' * 18}║")
        print(f"{Fore.YELLOW}║ {Fore.RED}• {Fore.WHITE}Selalu dapatkan izin sebelum menguji situs {Fore.YELLOW}{' ' * 16}║")
        print(f"{Fore.YELLOW}║ {Fore.RED}• {Fore.WHITE}Laporkan kerentanan secara bertanggung jawab {Fore.YELLOW}{' ' * 14}║")
        print(f"{Fore.YELLOW}║ {Fore.RED}• {Fore.WHITE}Jangan menyalahgunakan informasi yang ditemukan {Fore.YELLOW}{' ' * 12}║")
        print(f"{Fore.YELLOW}╚{'═' * 60}╝")

    def show_about(self):
        print(f"\n{Fore.YELLOW}╔{'═' * 60}╗")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}TENTANG ALAT INI {Fore.YELLOW}{' ' * 42}║")
        print(f"{Fore.YELLOW}╠{'═' * 60}╣")
        print(f"{Fore.YELLOW}║ {Fore.RED}IND0N3S14 S4DB0Y XPL01T {Fore.WHITE}proudly presents:                  {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}Bug Bounty Dork Finder adalah alat canggih untuk           {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}membantu peneliti keamanan dan bug hunter menemukan        {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}target potensial untuk program bug bounty.                 {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE} {Fore.YELLOW}{' ' * 59}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}Fitur: {Fore.YELLOW}{' ' * 53}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}• {Fore.WHITE}Database dork untuk berbagai jenis kerentanan {Fore.YELLOW}{' ' * 13}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}• {Fore.WHITE}Pencarian dork berdasarkan kata kunci {Fore.YELLOW}{' ' * 23}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}• {Fore.WHITE}Menyimpan hasil pencarian ke file {Fore.YELLOW}{' ' * 26}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}• {Fore.WHITE}Pengujian URL sederhana {Fore.YELLOW}{' ' * 35}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}• {Fore.WHITE}Referensi dan panduan penggunaan {Fore.YELLOW}{' ' * 27}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE} {Fore.YELLOW}{' ' * 59}║")
        print(f"{Fore.YELLOW}║ {Fore.RED}PENGGUNAAN BERTANGGUNG JAWAB: {Fore.YELLOW}{' ' * 31}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}Alat ini dibuat untuk tujuan pendidikan dan harus {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.WHITE}digunakan secara bertanggung jawab dan etis. {Fore.YELLOW}{' ' * 21}║")
        print(f"{Fore.YELLOW}╚{'═' * 60}╝")
    
    def handle_category_menu(self, category):
        while True:
            self.display.clear_screen()
            self.dork_finder.display_dorks(category)
            
            submenu = f"""
{Fore.YELLOW}╔{'═' * 40}╗
{Fore.YELLOW}║ {Fore.CYAN}MENU AKSI {Fore.YELLOW}{' ' * 29}║
{Fore.YELLOW}╠{'═' * 40}╣
{Fore.YELLOW}║ {Fore.GREEN}[1]{Fore.WHITE} Simpan dork ke file {Fore.YELLOW}{' ' * 19}║
{Fore.YELLOW}║ {Fore.GREEN}[2]{Fore.WHITE} Uji URL dengan dork {Fore.YELLOW}{' ' * 18}║
{Fore.YELLOW}║ {Fore.GREEN}[3]{Fore.WHITE} Tambah dork baru {Fore.YELLOW}{' ' * 22}║
{Fore.YELLOW}║ {Fore.GREEN}[4]{Fore.WHITE} Kembali ke menu utama {Fore.YELLOW}{' ' * 17}║
{Fore.YELLOW}╚{'═' * 40}╝
"""
            print(submenu)
            
            action = input(f"{Fore.GREEN}[?] {Fore.WHITE}Pilih aksi (1-4): ")
            
            if action == "1":
                self.dork_finder.save_dorks_to_file(category)
                input(f"\n{Fore.CYAN}[*] {Fore.WHITE}Tekan Enter untuk melanjutkan...")
            
            elif action == "2":
                url = input(f"\n{Fore.GREEN}[?] {Fore.WHITE}Masukkan URL untuk diuji: ")
                self.dork_finder.test_url(url, category)
                input(f"\n{Fore.CYAN}[*] {Fore.WHITE}Tekan Enter untuk melanjutkan...")
            
            elif action == "3":
                print(f"\n{Fore.CYAN}[*] {Fore.WHITE}Tambah Dork Baru ke Kategori {category.upper()}")
                dork = input(f"{Fore.GREEN}[?] {Fore.WHITE}Masukkan dork: ")
                description = input(f"{Fore.GREEN}[?] {Fore.WHITE}Deskripsi: ")
                
                risk_options = f"""
{Fore.YELLOW}[1] {Fore.GREEN}Low
{Fore.YELLOW}[2] {Fore.GREEN}Medium
{Fore.YELLOW}[3] {Fore.RED}High
{Fore.YELLOW}[4] {Fore.MAGENTA}Critical
"""
                print(risk_options)
                risk_choice = input(f"{Fore.GREEN}[?] {Fore.WHITE}Pilih level risiko (1-4): ")
                
                risk = "Medium"  # Default
                if risk_choice == "1":
                    risk = "Low"
                elif risk_choice == "3":
                    risk = "High"
                elif risk_choice == "4":
                    risk = "Critical"
                
                self.db.add_dork(category, dork, description, risk)
                print(f"\n{Fore.GREEN}[+] {Fore.WHITE}Dork berhasil ditambahkan!")
                input(f"\n{Fore.CYAN}[*] {Fore.WHITE}Tekan Enter untuk melanjutkan...")
            
            elif action == "4":
                break
            
            else:
                print(f"\n{Fore.RED}[!] {Fore.WHITE}Pilihan tidak valid!")
                time.sleep(1)
    
    def run(self):
        while True:
            self.display.clear_screen()
            self.display.show_banner()
            self.display.show_menu()
            
            choice = input(f"\n{Fore.GREEN}[?] {Fore.WHITE}Pilih opsi (1-12): ")
            
            if choice == "1":
                self.handle_category_menu("xss")
            
            elif choice == "2":
                self.handle_category_menu("sql")
            
            elif choice == "3":
                self.handle_category_menu("lfi")
            
            elif choice == "4":
                self.handle_category_menu("ssrf")
            
            elif choice == "5":
                self.handle_category_menu("command_injection")
            
            elif choice == "6":
                self.handle_category_menu("open_redirect")
            
            elif choice == "7":
                self.handle_category_menu("info_disclosure")
            
            elif choice == "8":
                self.handle_category_menu("xxe")
            
            elif choice == "9":
                self.display.clear_screen()
                print(f"\n{Fore.CYAN}=== PENCARIAN DORK ===")
                keyword = input(f"\n{Fore.GREEN}[?] {Fore.WHITE}Masukkan kata kunci: ")
                
                if keyword:
                    self.display.loading_animation("Mencari dork...", 2)
                    results = self.db.search_dorks(keyword)
                    self.dork_finder.display_search_results(results, keyword)
                    
                    if results:
                        save = input(f"\n{Fore.GREEN}[?] {Fore.WHITE}Simpan hasil pencarian ke file? (y/n): ")
                        if save.lower() == 'y':
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            filename = f"{self.dork_finder.results_folder}/hasil_pencarian_{keyword}_{timestamp}.txt"
                            
                            with open(filename, 'w', encoding='utf-8') as f:
                                f.write(f"=== HASIL PENCARIAN UNTUK: '{keyword}' ===\n")
                                f.write(f"Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                                
                                for i, dork in enumerate(results, 1):
                                    category_name = dork["category"].replace("_", " ").upper()
                                    f.write(f"[{i}] {dork['dork']}\n")
                                    f.write(f"    • Kategori: {category_name}\n")
                                    f.write(f"    • Deskripsi: {dork['description']}\n")
                                    f.write(f"    • Risiko: {dork['risk']}\n\n")
                            
                            print(f"\n{Fore.GREEN}[+] {Fore.WHITE}Hasil pencarian disimpan ke: {filename}")
                
                input(f"\n{Fore.CYAN}[*] {Fore.WHITE}Tekan Enter untuk kembali ke menu utama...")
            
            elif choice == "10":
                self.display.clear_screen()
                self.show_references()
                input(f"\n{Fore.CYAN}[*] {Fore.WHITE}Tekan Enter untuk kembali ke menu utama...")
            
            elif choice == "11":
                self.display.clear_screen()
                self.show_about()
                input(f"\n{Fore.CYAN}[*] {Fore.WHITE}Tekan Enter untuk kembali ke menu utama...")
            
            elif choice == "12":
                self.display.clear_screen()
                print(f"\n{Fore.YELLOW}╔{'═' * 40}╗")
                print(f"{Fore.YELLOW}║ {Fore.CYAN}TERIMA KASIH TELAH MENGGUNAKAN {Fore.YELLOW}{' ' * 10}║")
                print(f"{Fore.YELLOW}║ {Fore.CYAN}ADVANCED BUG BOUNTY DORK FINDER {Fore.YELLOW}{' ' * 9}║")
                print(f"{Fore.YELLOW}╚{'═' * 40}╝")
                print(f"\n{Fore.GREEN}[*] {Fore.WHITE}Sampai jumpa kembali!")
                sys.exit(0)
            
            else:
                print(f"\n{Fore.RED}[!] {Fore.WHITE}Pilihan tidak valid!")
                time.sleep(1)

# Program utama
if __name__ == "__main__":
    try:
        # Nonaktifkan peringatan untuk unverified HTTPS requests
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Jalankan aplikasi
        app = BugBountyDorkFinder()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] {Fore.WHITE}Program dihentikan oleh pengguna.")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Terjadi kesalahan: {e}")
        sys.exit(1)