<p align="center">
  <img src="assets/lune_logo.png" alt="LUNE Logo" width="220"/>
</p>

<h1 align="center">LUNE/h1>

<p align="center">
  <b>Live Deception &nbsp;|&nbsp; Persona Engine &nbsp;|&nbsp; Attribution Poisoning</b><br>
  <br>
  LUNE is a next generation red team and adversary simulation toolkit.<br>
  Not another scanner. Not another wrapper.<br>
  This is psychological warfare, deception, and chaos—refined into a hacker’s TUI you’ll actually want to use.
</p>

---

<h2 align="center">Screenshots</h2>

<p align="center">
  <b>Menu:</b><br>
  <img src="assets/screenshot_menu.png" width="700"/><br><br>
  <b>Persona Engine:</b><br>
  <img src="assets/screenshot_persona_engine.png" width="700"/><br><br>
  <b>GhostSignature:</b><br>
  <img src="assets/screenshot_ghostsignature.png" width="700"/><br><br>
  <b>Tripwire Monitor:</b><br>
  <img src="assets/screenshot_tripwire.png" width="700"/><br><br>
  <b>Hall of Mirrors:</b><br>
  <img src="assets/screenshot_hallofmirrors.png" width="700"/><br><br>
  <b>BlackNoise:</b><br>
  <img src="assets/screenshot_blacknoise.png" width="700"/><br><br>
  <b>Loot Watcher:</b><br>
  <img src="assets/screenshot_lootwatcher.png" width="700"/><br>
</p>


---

<h2 align="center">What is LUNE?</h2>

<p align="center">
LUNE lets you:<br>
- <b>Select an adversary persona</b> (Lazarus, APT29, FIN7, NSA Equation Group, Script Kiddie, and more)<br>
- <b>Live generate deception artifacts</b>: DNS beacons, registry keys, fake logs, malware stubs, C2 traffic, and more matching real world threat group TTPs<br>
- <b>Flood blue teams and DFIRs with noise and false indicators</b> (real “attribution poisoning”)<br>
- <b>Spin up multi layered decoy environments</b> with just a few keystrokes<br>
- <b>Export a full simulated DFIR report</b> showing all artifacts planted<br>
- <b>Clean up instantly</b> (stealth kill switch)<br>
- <b>All from a terminal menu you can actually be proud of</b>
</p>

---

<h2 align="center">Features</h2>

<p align="center">
- <b>Adversary Persona Engine</b> — Pick your APT, see their tactics, simulate their artifacts, and poison attribution like a pro.<br>
- <b>GhostSignature</b> — Forge false IOCs, malware signatures, and staged C2s for any persona.<br>
- <b>Tripwire Monitor</b> — Simulate decoy tripwires and detection triggers with realistic events.<br>
- <b>Attribution Poisoner</b> — Drop artifacts that frame your adversary persona, not yourself.<br>
- <b>Hall of Mirrors</b> — Multi-layer deception overlay: fake persistence, staged logs, and more.<br>
- <b>BlackNoise</b> — Synthetic network traffic generator, DNS beacons, C2 callbacks.<br>
- <b>Loot Watcher</b> — View all decoy loot, artifacts, and planted evidence from a single place.<br>
- <b>Stealth Cleanup</b> — Nuke every planted artifact in one move (clean exit for OPSEC).
</p>

---

<h2 align="center">Install & Usage</h2>

<p align="center">
<b>Requirements:</b><br>
Python 3.8+<br>
Runs on Kali, Ubuntu, most Linux distros out-of-the-box
</p>

<p align="center">
<b>Quickstart:</b>
</p>

<p align="center">
  
<code>
git clone https://github.com/GnomeMan4201/Lune.git<br>
cd Lune<br>
python3 -m venv venv<br>
source venv/bin/activate<br>
pip install -r requirements.txt<br>
python3 lune_operator.py
</code>
</p>

<p align="center">
To run globally (optional):<br>
<code>
sudo ln -s $PWD/lune_operator.py /usr/local/bin/lune<br>
sudo chmod +x /usr/local/bin/lune_operator.py<br>
lune
</code>
</p>

---

<h2 align="center">Why LUNE?</h2>

<p align="center">
Most “red team tools” are just wrappers.<br>
LUNE is a psychological ops engine, an adversary persona system, and a fully modular deception lab that pushes the boundaries of attribution, obfuscation, and defense evasion—<b>in a way blue teams haven’t seen before</b>.
</p>

---

<h2 align="center">License</h2>
<p align="center">
MIT License.<br>
See <a href="LICENSE">LICENSE</a> for details.
</p>

---

<h2 align="center">Credits</h2>
<p align="center">
Developed by <b>NMAPKin</b><br>
Inspired by real-world threat actor tradecraft and the need for chaos.<br><br>
<b>Stay unpredictable.<br>Welcome to the arena.</b>
</p>
