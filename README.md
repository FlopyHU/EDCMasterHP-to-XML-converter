![Tech](https://img.shields.io/badge/Tech-HTML5%20%7C%20JavaScript-yellow.svg)
![Target](https://img.shields.io/badge/Target-TunerPro%20XDF-blue.svg)
![License](https://img.shields.io/badge/license-Open_Source-green.svg)

# ⚡ EDCMasterHP to TunerPro XDF Converter

A quick, browser-based tool that turns map lists from [EDCMasterHP](https://www.edcmasterhp.com/) into ready-to-use XDF files for TunerPro. 

> [!TIP]
> **Try it live here:** [https://flopyhu.github.io/EDCMasterHP-to-XML-converter/](https://flopyhu.github.io/EDCMasterHP-to-XML-converter/)

---

> [!NOTE]
> ## 🚗 The Story Behind This Tool
> This whole project started with a single check engine light and a limp mode on a diesel Opel Astra H Caravan (running a Z17DTL engine block with a Z17DTH turbo and ECU). I was sick of the EGR throwing codes, so I grabbed my MPPS cable and started digging. Every commercial tuning service wanted a fortune just to change a couple of numbers, and I wasn't about to pay a fortune for that. 
> 
> Then I found EDCMasterHP, which worked wonders—except I spent **two full days** manually typing out and transcription-mapping every single map address into TunerPro by hand. Now that I have to work on some of my friends' cars too, I definitely didn't want to spend another two days inputting maps. So, I built this browser tool to do the heavy lifting automatically and uploaded it for everyone to use. 
> 
> *(Truth be told... I might also be getting a little bit addicted to uploading projects to GitHub.)*

---

> [!IMPORTANT]
> ### 🛡️ Disclaimer & Credits
> This is an unofficial community tool and isn't affiliated with or endorsed by EDCMasterHP. 
> 
> EDCMasterHP does an amazing job providing accurate map definitions for ECUs, so please support their platform! This tool was simply built to save tuners from spending hours typing out map data by hand. It doesn't bypass any security, doesn't hand out free maps, and requires you to legitimately log into your own EDCMasterHP account to grab your data. All map addresses and calculation logic remain the property of EDCMasterHP.

---

## 🛠️ How to Use It

Since EDCMasterHP displays your map data inside the browser, this tool reads the raw webpage code and reformats it into TunerPro's XML structure. 

### Step 1: Copy your map page source
Log into your [EDCMasterHP](https://www.edcmasterhp.com/) account, open your analyzed ECU map list, press **`Ctrl + U`** on your keyboard (or right-click the page background and choose "View Page Source") to open the raw HTML in a new tab, and select everything (**`Ctrl + A`**) to copy it (**`Ctrl + C`**).

### Step 2: Convert to XDF
Head over to the [Web Converter](https://flopyhu.github.io/EDCMasterHP-to-XML-converter/), paste the HTML into the text box (**`Ctrl + V`**) where the tool parses it instantly and shows you a grid of all detected maps, type a clean export filename if you want (sticking to letters, numbers, and underscores to keep TunerPro happy), and hit **Generate & Download XDF**.

### Step 3: Load it into TunerPro
Open TunerPro, load your original `.bin` file via **File -> Open Bin...**, load your newly downloaded XDF via **XDF -> Select XDF...**, and your parameter tree will populate with all your maps, correct matrix dimensions, and byte orders.

---

> [!NOTE]
> ## ⚠️ Important Note on Limitations & Axes
> **Axis Scaling & Conversion Numbers:** The converter reads the main map directory catalog from the EDCMasterHP interface, giving you all map titles, hex addresses, and matrix dimensions like `16x16`. However, individual conversion factors, axis labels, and precise physical unit values are stored separately inside individual map sub-pages and are not exposed on the front-page HTML code. 
> 
> **What this means for you:** The tool handles the heavy lifting by instantly compiling all map headers and structures into a clean XDF file. Once imported into TunerPro, you will still want to double-check your map configurations and apply your preferred axis definitions or conversions where necessary, but the hard part of cataloging every address by hand is completely done for you.

---

> [!TIP]
> ### 🔒 Privacy & Security
> Everything runs entirely inside your browser (client-side), meaning your map code, addresses, and files never get uploaded to any external server.

---

### 📜 License & Open Source
This project is open source. You can check the full usage permissions, fork rules, and attribution guidelines in the [LICENSE](https://github.com/FlopyHU/EDCMasterHP-to-XML-converter/blob/main/LICENSE) file.

### 💡 A Note to EDCMasterHP & Developers
**EDCMasterHP:** If you guys see this and want to link the tool, or build a native export button into your site to save users time, you have total permission, because the goal is just to make the workflow smoother for everyone. 

**Forks:** Feel free to fork and improve the project, as long as proper visible credit is given to both FlopyHU and EDCMasterHP, and please don't repackage and sell it as a basic cash-grab.
