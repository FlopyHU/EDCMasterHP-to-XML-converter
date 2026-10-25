import re
import xml.etree.ElementTree as ET

def convert_edc_html_to_xdf(html_content, output_filename="EDCMaster_Export.xdf"):
    """
    Parses EDCMasterHP HTML map tables and generates a TunerPro V1.80 XDF file.
    
    Args:
        html_content (str): The raw HTML string containing the 'mltr_' table rows.
        output_filename (str): The desired output file name.
    """
    # Regex patterns to extract table rows and columns without external dependencies
    row_pattern = re.compile(r'<tr id="mltr_[^>]+>(.*?)</tr>', re.DOTALL)
    col_pattern = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)
    
    rows = row_pattern.findall(html_content)
    
    if not rows:
        print("Error: No maps found. Ensure the HTML contains 'mltr_' table rows.")
        return False

    # Initialize the XDF structure matching TunerPro V1.80 standards
    xdf_lines = [
        '<?xml version="1.0"?>',
        '<XDFFORMAT version="1.80">',
        '  <XDFHEADER>',
        '    <flags>0x1</flags>',
        '    <deftitle>EDCMasterHP Exported XDF</deftitle>',
        '    <description>Generated via Python Converter</description>',
        '    <BASEOFFSET offset="0" subtract="0" />',
        '    <DEFAULTS datasizeinbits="8" sigdigits="2" outputtype="1" signed="0" lsbfirst="0" float="0" />',
        '    <REGION type="0xFFFFFFFF" startaddress="0x0" size="0x200000" regioncolor="0x0" regionflags="0x0" name="Binary File" desc="This region describes the bin file edited by this XDF" />',
        '  </XDFHEADER>'
    ]
    
    success_count = 0
    error_count = 0

    for row in rows:
        cols = col_pattern.findall(row)
        if len(cols) < 4:
            error_count += 1
            continue
            
        try:
            # Clean HTML tags (like <b>) from the extracted text
            hex_addr = re.sub(r'<[^>]+>', '', cols[1]).strip()
            dims = cols[2].strip().split('x')
            map_name = cols[3].strip()
            
            x_size = int(dims[0].strip()) if dims[0].strip().isdigit() else 1
            y_size = int(dims[1].strip()) if len(dims) > 1 and dims[1].strip().isdigit() else 1
            
            # Construct the individual map table
            table = f"""  <XDFTABLE uniqueid="0x{hex_addr}" flags="0x0">
    <title>{hex_addr} - {map_name}</title>
    <XDFAXIS id="x" uniqueid="0x0">
      <EMBEDDEDDATA mmedelementsizebits="8" mmedmajorstridebits="-32" mmedminorstridebits="0" />
      <indexcount>{x_size}</indexcount>
      <datatype>0</datatype>
      <unittype>0</unittype>
      <DALINK index="0" />
      <MATH equation="X">\n        <VAR id="X" />\n      </MATH>
    </XDFAXIS>
    <XDFAXIS id="y" uniqueid="0x0">
      <EMBEDDEDDATA mmedelementsizebits="8" mmedmajorstridebits="-32" mmedminorstridebits="0" />
      <indexcount>{y_size}</indexcount>
      <datatype>0</datatype>
      <unittype>0</unittype>
      <DALINK index="0" />
      <MATH equation="X">\n        <VAR id="X" />\n      </MATH>
    </XDFAXIS>
    <XDFAXIS id="z">
      <EMBEDDEDDATA mmedaddress="0x{hex_addr}" mmedelementsizebits="16" mmedrowcount="{y_size}" mmedcolcount="{x_size}" mmedmajorstridebits="0" mmedminorstridebits="0" />
      <decimalpl>2</decimalpl>
      <min>0.000000</min>
      <max>255.000000</max>
      <outputtype>1</outputtype>
      <MATH equation="X">\n        <VAR id="X" />\n      </MATH>
    </XDFAXIS>
  </XDFTABLE>"""
            
            xdf_lines.append(table)
            success_count += 1
            
        except Exception as e:
            error_count += 1
            print(f"Warning: Failed to parse a row due to: {e}")

    xdf_lines.append('</XDFFORMAT>')

    # Write the completed XML structure to file
    if success_count > 0:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(xdf_lines))
        print(f"Successfully exported {success_count} maps to {output_filename}. (Errors: {error_count})")
        return True
    else:
        print("No maps were successfully converted.")
        return False

# ==========================================
# Example Usage:
# ==========================================
if __name__ == "__main__":
    # In a real environment, you would read this from a file or network request
    sample_html = """
    <table>
        <tr id="mltr_1">
            <td>1</td>
            <td>C12B8</td>
            <td>10x10</td>
            <td>Driver's Wish</td>
        </tr>
    </table>
    """
    
    convert_edc_html_to_xdf(sample_html, "EDCMaster_Export.xdf")
