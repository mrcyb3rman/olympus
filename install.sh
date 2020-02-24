#!/bin/bash

echo
echo "[!] Updating Database..."
sudo apt-get update >> install.log
echo

echo "[!] Information Gathering Tools:"
echo

echo "		[+] Installing theHarvester..."
apt-get install theharvester >> install.log
echo "		[+] Installing dmitry..."
apt-get install dmitry >> install.log
echo "		[+] Installing knockpy..."
apt-get install knockpy >> install.log
echo "		[+] Installing gobuster..."
apt-get install gobuster >> install.log
echo "		[+] Installing dnsenum..."
apt-get install dnsenum >> install.log
echo "		[+] Installing dnsrecon..."
apt-get install dnsrecon >> install.log
echo "		[+] Installing fierce..."
apt-get install fierce >> install.log
echo "		[+] Installing wafw00f..."
apt-get install wafw00f >> install.log
echo "		[+] Installing netdiscover..."
apt-get install netdiscover >> install.log
echo

echo "[!] Scanning Tools:"
echo

echo "		[+] Installing nmap..."
apt-get install nmap >> install.log
echo "		[+] Installing skipfish..."
apt-get install skipfish >> install.log
echo "		[+] Installing wpscan..."
apt-get install wpscan >> install.log
echo "		[+] Installing nikto..."
apt-get install nikto >> install.log
echo

echo "[!] Wireless Attack Tools:"
echo

echo "		[+] Installing aircrack-ng..."
apt-get install aircrack-ng >> install.log
echo "		[+] Installing reaver..."
apt-get install reaver >> install.log
echo "		[+] Installing bully..."
apt-get install bully >> install.log
echo

echo "[!] Password Attack Tools:"
echo

echo "		[+] Installing crunch..."
apt-get install crunch >> install.log
echo "		[+] Installing hashcat..."
apt-get install hashcat >> install.log
echo "		[+] Installing hash-identifier..."
apt-get install hash-identifier >> install.log
echo "		[+] Installing john..."
apt-get install john >> install.log
echo "		[+] Installing medusa..."
apt-get install medusa figlet >> install.log
echo

