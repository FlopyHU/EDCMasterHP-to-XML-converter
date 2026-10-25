import tkinter as tk
from tkinter import filedialog, messagebox
import re

def convert_html():
    html = text_input.get("1.0", tk.END)
    log_output.config(state=tk.NORMAL)
    log_output.delete("1.0", tk.END)
    
    # Regex to find map rows without needing external libraries like BeautifulSoup
    row_pattern = re.compile(r'<tr id="mltr_[^>]+>(.*?)</tr>', re.DOTALL)
    col_pattern = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)
    
    rows = row_pattern.findall(html)
    if not rows:
        log_output.insert(tk.END, "Error: No maps found. Ensure the HTML contains 'mltr_' table rows.\n", "error")
        log_output.config(state=tk.DISABLED)
        return

    xdf = ['<?xml version="1.0"?>', '<XDFFHEADER version="1.0">', '  <XDFCATEGORIES>', '    <CATEGORY index="0" name="EDC Imported"/>', '  </XDFCATEGORIES>', '  <XDFTABLES>']
    
    success, errors = 0, 0
    for idx, row in enumerate(rows):
        cols = col_pattern.findall(row)
        if len(cols) < 4:
            errors += 1
            log_output.insert(tk.END, f"Warning: Row {idx+1} skipped (missing columns).\n", "warning")
            continue
            
        try:
            # Strip inner tags like <b> from the hex address
            hex_addr = re.sub(r'<[^>]+>', '', cols[1]).strip()
            dims = cols[2].strip().split('x')
            map_name = cols[3].strip()
            
            x_size = int(dims[0].strip()) if dims[0].strip().isdigit() else 1
            y_size = int(dims[1].strip()) if len(dims) > 1 and dims[1].strip().isdigit() else 1
            
            table = f"""    <XDFTABLE uniqueid="{1000 + idx}" category="0">
      <TITLE>{hex_addr} - {map_name} ({x_size}x{y_size})</TITLE>
      <ADDRESS offset="0x{hex_addr}" units="" decimalplaces="2"/>
      <ZAXIS id="1" boardid="0" title="Z Axis">
        <EMBEDDEDDATA mmedaddress="0x{hex_addr}" mmedelementsizebits="16" mmedrowstride="{x_size * 2}" mmedcolstride="2" mmedtypeflags="0x10000"/>
      </ZAXIS>
      <AXIS id="x" Index="0" label="X Axis">
        <EMBEDDEDDATA mmedelementsizebits="16" mmedrowstride="0" mmedcolstride="2" mmedtypeflags="0x10000"/>
      </AXIS>"""
            if y_size > 1:
                table += f"""
      <AXIS id="y" Index="1" label="Y Axis">
        <EMBEDDEDDATA mmedelementsizebits="16" mmedrowstride="2" mmedcolstride="0" mmedtypeflags="0x10000"/>
      </AXIS>"""
            table += "\n    </XDFTABLE>"
            xdf.append(table)
            success += 1
        except Exception as e:
            errors += 1
            log_output.insert(tk.END, f"Warning: Failed to parse row {idx+1} ({str(e)}).\n", "warning")

    xdf.extend(['  </XDFTABLES>', '</XDFFHEADER>'])
    
    log_output.insert(tk.END, f"\nSuccess: Converted {success} maps. Errors: {errors}.\n", "success")
    log_output.config(state=tk.DISABLED)
    
    if success > 0:
        filepath = filedialog.asksaveasfilename(defaultextension=".xdf", filetypes=[("TunerPro XDF", "*.xdf")], title="Save XDF File")
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(xdf))
            messagebox.showinfo("Export Complete", f"Saved successfully to:\n{filepath}")

# GUI Setup
root = tk.Tk()
root.title("EDC to XDF Converter")
root.geometry("700x500")
root.configure(bg="#2c2f33")

tk.Label(root, text="Paste EDCMasterHP HTML Below:", bg="#2c2f33", fg="white", font=("Segoe UI", 12)).pack(pady=(10, 5))
text_input = tk.Text(root, height=12, bg="#1c1c1c", fg="#43b581", insertbackground="white", font=("Consolas", 10))
text_input.pack(padx=20, fill=tk.BOTH, expand=True)

btn = tk.Button(root, text="Select Directory & Export XDF", bg="#7289da", fg="white", font=("Segoe UI", 12, "bold"), command=convert_html, relief=tk.FLAT)
btn.pack(pady=15, padx=20, fill=tk.X)

log_output = tk.Text(root, height=6, bg="#23272a", fg="white", font=("Consolas", 10), state=tk.DISABLED)
log_output.tag_config("error", foreground="#f04747")
log_output.tag_config("warning", foreground="#faa61a")
log_output.tag_config("success", foreground="#43b581")
log_output.pack(padx=20, pady=(0, 20), fill=tk.X)

root.mainloop()
