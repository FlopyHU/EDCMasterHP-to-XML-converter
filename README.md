# EDCMasterHP to TunerPro XDF Converter

A fast, client-side web tool designed to convert map definitions from [EDCMasterHP](https://www.edcmasterhp.com/) into ready-to-use XDF files for TunerPro. 

**Access the live tool here:** [https://flopyhu.github.io/EDCMasterHP-to-XML-converter/](https://flopyhu.github.io/EDCMasterHP-to-XML-converter/)

### ⚠️ Disclaimer & Credits
**This is an unofficial community tool and is NOT affiliated with, endorsed by, or sponsored by EDCMasterHP.** 

EDCMasterHP provides an incredible service to the tuning community by analyzing ECUs and providing highly accurate map definitions. Please support their business! This tool was created solely out of respect for their platform, with the goal of saving tuners hours of manual data entry. It does not bypass their security, it does not provide free maps, and it requires you to legally access your own map data via your EDCMasterHP account. All map data, addresses, and conversion factors remain the intellectual property of EDCMasterHP.

---

## 📖 How to Use the Converter

Because EDCMasterHP displays your map data securely inside a web browser, this tool works by reading the raw website code (HTML) and translating it into TunerPro's XML format (XDF). 

Follow these steps for the fastest extraction:

**Step 1: Get Your Map Data**
1. Log into your [EDCMasterHP](https://www.edcmasterhp.com/) account.
2. Upload your ECU `.bin` file and navigate to the **ECU Analyze** page where your list of maps is displayed.
3. Once the table containing your map addresses loads, press **`Ctrl + U`** on your keyboard (or right-click the background and select "View Page Source"). This opens the raw HTML code in a new tab.
4. Press **`Ctrl + A`** to highlight all the code.
5. Press **`Ctrl + C`** to copy it.

**Step 2: Convert to XDF**
1. Open the [Web Converter](https://flopyhu.github.io/EDCMasterHP-to-XML-converter/).
2. Click inside the large text box and press **`Ctrl + V`** to paste your HTML.
3. The tool will automatically process the code in real-time and display a grid of all successfully detected maps.
4. Type a custom name for your export file in the "Export Filename" box. *Use only letters, numbers, and underscores to prevent TunerPro import errors.*
5. Click **Generate & Download XDF**. Your new `.xdf` file will download immediately.

**Step 3: Open in TunerPro**
1. Open TunerPro.
2. Go to **File -> Open Bin...** and select your original ECU `.bin` file.
3. Go to **XDF -> Select XDF...** and choose the newly downloaded `.xdf` file.
4. Your Parameter Tree will populate with all the maps, complete with the correct matrix sizes, conversion math, and byte-order configuration. 

---

### Privacy & Security
This tool operates 100% client-side. When you paste your HTML code, it is processed entirely within your own web browser. No map addresses, file data, or personal account information are ever uploaded to an external server.

---

### 🤝 A Note to EDCMasterHP & Community Developers
* **EDCMasterHP:** If the team at EDCMasterHP sees this and wants to link this tool—or natively integrate an export option to help users save time—you have my full permission! The goal is purely to enhance the community experience and complement your platform.
* **Forks & Contributions:** Everyone is free to fork this project and publish new versions under the terms of the project license, provided that **visible credit to both Flopy and EDCMasterHP** is strictly maintained. Do not repackage and sell this tool as your own without adding substantial new features.
