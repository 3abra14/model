import cv2
import numpy as np

img = cv2.imread("gi_mask.png", cv2.IMREAD_COLOR)

points = [
(514,439),
(516,459),
(511,479),
(515,499),
(523,519),
(558,539),
(610,559),
(608,579),
(553,599),
(524,619),
(528,639),
(508,659),
(512,679),
(519,699),
(538,719),
(573,739),
(534,759),
(516,779)
]

for p in points:
    cv2.circle(img, p, 5, (0, 0, 255), -1)

cv2.imwrite(r"c:\Users\Abdel\.gemini\antigravity\brain\c6adabb5-4c6d-4444-85af-c1f422180412\scraped_path.png", img)
