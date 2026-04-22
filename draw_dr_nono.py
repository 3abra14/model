import cv2
import numpy as np
from svgpathtools import parse_path

def main():
    img_path = r"c:\Users\Abdel\OneDrive\Desktop\ASP\dr_nono_baby.png"
    img = cv2.imread(img_path)
    if img is None:
        print("Could not load image.")
        return
        
    h, w = img.shape[:2]
    
    # User's path
    path_d = "M 514,439 C 514.3,442.3 516.5,452.3 516,459 C 515.5,465.7 511.2,472.3 511,479 C 510.8,485.7 513.0,492.3 515,499 C 517.0,505.7 515.8,512.3 523,519 C 530.2,525.7 543.5,532.3 558,539 C 572.5,545.7 601.7,552.3 610,559 C 618.3,565.7 617.5,572.3 608,579 C 598.5,585.7 567.0,592.3 553,599 C 539.0,605.7 528.2,612.3 524,619 C 519.8,625.7 530.7,632.3 528,639 C 525.3,645.7 510.7,652.3 508,659 C 505.3,665.7 510.2,672.3 512,679 C 513.8,685.7 514.7,692.3 519,699 C 523.3,705.7 529.0,712.3 538,719 C 547.0,725.7 573.7,732.3 573,739 C 572.3,745.7 543.5,752.3 534,759 C 524.5,765.7 519.0,775.7 516,779"
    
    try:
        path = parse_path(path_d)
        points = []
        for i in range(1001):
            t = i / 1000.0
            pt = path.point(t)
            points.append((pt.real, pt.imag))
            
        points = np.array(points)
        
        # Scale if image size != 1024
        scale_x = w / 1024.0
        scale_y = h / 1024.0
        
        for pt in points:
            px = int(pt[0] * scale_x)
            py = int(pt[1] * scale_y)
            if 0 <= px < w and 0 <= py < h:
                cv2.circle(img, (px, py), 2, (0, 0, 255), -1)
                
    except Exception as e:
        print("Error parsing:", e)
        
    out_path = r"c:\Users\Abdel\.gemini\antigravity\brain\7b86ccb9-bc2a-40bb-a3c7-abadff5827cf\nono_path_debug.png"
    cv2.imwrite(out_path, img)
    print("Saved to", out_path)

if __name__ == "__main__":
    main()
