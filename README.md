# EDCMasterHP to TunerPro XDF Converter

A quick, browser-based tool that turns map lists from [EDCMasterHP](https://www.edcmasterhp.com/) into ready-to-use XDF files for TunerPro. 

**Try it live here:** [https://flopyhu.github.io/EDCMasterHP-to-XML-converter/](https://flopyhu.github.io/EDCMasterHP-to-XML-converter/)

### Disclaimer & Credits
This is an unofficial community tool and isn't affiliated with or endorsed by EDCMasterHP. 

EDCMasterHP does an amazing job providing accurate map definitions for ECUs, so please support their platform! This tool was simply built to save tuners from spending hours typing out map data by hand. It doesn't bypass any security, doesn't hand out free maps, and requires you to legitimately log into your own EDCMasterHP account to grab your data. All map addresses and calculation logic remain the property of EDCMasterHP.

---

## How to Use It

Since EDCMasterHP displays your map data inside the browser, this tool reads the raw webpage code and reformats it into TunerPro's XML structure. 

### Step 1: Copy your map page source
1. Log into your [EDCMasterHP](https://www.edcmasterhp.com/) account and open your analyzed ECU map list.
2. Press **`Ctrl + U`** on your keyboard (or right-click the page background and choose "View Page Source") to open the raw HTML in a new tab.
3. Select everything (**`Ctrl + A`**) and copy it (**`Ctrl + C`**).

### Step 2: Convert to XDF
1. Head over to the [Web Converter](https://flopyhu.github.io/EDCMasterHP-to-XML-converter/).
2. Paste the HTML into the text box (**`Ctrl + V`**). The tool parses it instantly and shows you a grid of all detected maps.
3. Type a clean export filename if you want (stick to letters, numbers, and underscores to keep TunerPro happy).
4. Hit **Generate & Download XDF**.

### Step 3: Load it into TunerPro
1. Open TunerPro and load your original `.bin` file via **File -> Open Bin...**
2. Load your newly downloaded XDF via **XDF -> Select XDF...**
3. Your parameter tree will populate with all your maps, correct matrix dimensions, and byte orders.

---

### Privacy & Security
Everything runs entirely inside your browser (client-side). Your map code, addresses, and files never get uploaded to any external server.

---

### License & Open Source
This project is open source. You can check the full usage permissions, fork rules, and attribution guidelines in the [LICENSE](https://github.com/FlopyHU/EDCMasterHP-to-XML-converter/blob/main/LICENSE) file.

### A Note to EDCMasterHP & Developers
* **EDCMasterHP:** If you guys see this and want to link the tool—or build a native export button into your site to save users time—you have total permission! The goal is just to make the workflow smoother for everyone.
* **Forks:** Feel free to fork and improve the project, as long as proper visible credit is given to both Flopy and EDCMasterHP. Please don't repackage and sell it as a basic cash-grab.
