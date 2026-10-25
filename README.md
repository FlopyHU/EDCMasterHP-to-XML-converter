# EDCMasterHP to TunerPro XDF Converter

A dual-interface tool (Web and Desktop) that parses raw HTML from EDCMasterHP's map lists and automatically generates ready-to-import TunerPro `.xdf` definition files.

**Features**
* Extracts map names, hexadecimal addresses, and dimensions directly from the DOM.
* Automatically configures 16-bit high-low (Intel) Z-axis data structures for EDC16/EDC17 maps.
* Flags corrupted or incomplete map rows during extraction.
* Eliminates manual hex-to-decimal conversion and manual map sizing.

**Usage: Web Version (GitHub Pages)**
1. Navigate to the hosted `index.html` page.
2. Log into EDCMasterHP, load your project, right-click the page, and select **View Page Source**.
3. Copy all HTML and paste it into the converter's text area.
4. Click **Generate & Download XDF** and load the resulting file into TunerPro.

**Usage: Desktop App (Python)**
Run `EDCMasterHP to XML[APP].py` to launch the dark-themed GUI. Paste the HTML into the text area and click export to select your save directory.

**Building the Executable**
To compile the Python script into a standalone `.exe` for Windows users without Python installed, run:
`pyinstaller --onefile --windowed "EDCMasterHP to XML[APP].py"`
