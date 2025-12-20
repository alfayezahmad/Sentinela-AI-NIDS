"""
Project: Sentinela-AI-NIDS
Author: Alfayez Ahmad
Copyright: (c) 2025 Alfayez Ahmad
License: Apache License 2.0
Description: Real-time Network Forensics Engine.
"""

import sys
import joblib
import pandas as pd
from scapy.all import sniff, IP, TCP, UDP
from rich.console import Console
from rich.table import Table
from rich.live import Live

# Setup UI and Load Model
console = Console()
try:
    model = joblib.load('sentinela_model.pkl')
except:
    console.print("[red]Error: 'sentinela_model.pkl' not found! Run engine.py first.[/red]")
    sys.exit()


# This table will hold our live results
def generate_table(results):
    table = Table(title="Sentinela Live Network Forensics", style="cyan")
    table.add_column("Verdict", justify="center")
    table.add_column("Source IP", style="magenta")
    table.add_column("Destination IP", style="green")
    table.add_column("Port", justify="right")
    table.add_column("Size", justify="right")

    for row in results[-10:]:  # Only show last 10 packets
        table.add_row(*row)
    return table


packet_log = []


def sniff_callback(packet):
    if IP in packet:
        # 1. Feature Extraction
        length = len(packet)
        proto = packet.proto
        port = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else 0

        # 2. Prediction
        features = pd.DataFrame([[length, proto, port]], columns=['packet_size', 'protocol', 'dest_port'])
        prediction = model.predict(features)[0]

        # 3. Formatting for Dashboard
        verdict = "[bold red]⚠️ ATTACK[/bold red]" if prediction == 1 else "[bold green]✅ NORMAL[/bold green]"
        packet_log.append([verdict, packet[IP].src, packet[IP].dst, str(port), f"{length}b"])


# Main Loop
with Live(generate_table(packet_log), refresh_per_second=4) as live:
    console.print(f"[bold yellow][*] Sentinela active on M4 Pro. Sniffing live packets...[/bold yellow]")
    sniff(prn=lambda x: [sniff_callback(x), live.update(generate_table(packet_log))], store=0)
