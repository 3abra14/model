import cv2
import numpy as np
import base64
import re
from xml.dom import minidom
import os

def main():
    html_file = r"c:\Users\Abdel\OneDrive\Desktop\ASP\gi_endoscopy\index.html"
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract base64 image
    match = re.search(r'<img id="baby-img"\s*src="data:image/png;base64,([^"]+)"', content)
    if not match:
        print("Could not find base64 image")
        return

    base64_data = match.group(1)
    img_data = base64.b64decode(base64_data)
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Resize to 1024x1024 since viewBox is 1024x1024
    img = cv2.resize(img, (1024, 1024))

    # Parse SVG path
    path_match = re.search(r'<path id="gi-path" d="([^"]+)"', content)
    if not path_match:
        print("Could not find gi-path")
        return
        
    path_d = path_match.group(1)
    print("Found path:", path_d)
    
    # We can draw the SVG path on the image roughly
    # Split path commands
    commands = path_d.replace(',', ' ').split()
    
    pts = []
    i = 0
    while i < len(commands):
        if commands[i] == 'M':
            x = float(commands[i+1])
            y = float(commands[i+2])
            pts.append((x, y))
            i += 3
        elif commands[i] == 'C':
            x1 = float(commands[i+1])
            y1 = float(commands[i+2])
            x2 = float(commands[i+3])
            y2 = float(commands[i+4])
            x3 = float(commands[i+5])
            y3 = float(commands[i+6])
            
            # Subdivide Bezier curve
            p0 = pts[-1]
            p1 = (x1, y1)
            p2 = (x2, y2)
            p3 = (x3, y3)
            
            for t in np.linspace(0, 1, 20)[1:]:
                bx = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]
                by = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1]
                pts.append((bx, by))
            i += 7
        else:
            i += 1

    # Draw the path on the image
    for i in range(len(pts) - 1):
        pt1 = (int(pts[i][0]), int(pts[i][1]))
        pt2 = (int(pts[i+1][0]), int(pts[i+1][1]))
        cv2.line(img, pt1, pt2, (0, 0, 255), 3)

    output_path = r"c:\Users\Abdel\.gemini\antigravity\brain\7b86ccb9-bc2a-40bb-a3c7-abadff5827cf\path_debug.png"
    cv2.imwrite(output_path, img)
    print("Saved image to", output_path)

if __name__ == "__main__":
    main()
