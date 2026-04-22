import cv2
import numpy as np

img = cv2.imread("gi_mask.png", cv2.IMREAD_COLOR)

# To draw a bezier curve in OpenCV, we evaluate it or just draw the points.
# Let's evaluate the cubic bezier.
def eval_bezier(p0, p1, p2, p3, t):
    return (
        int((1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]),
        int((1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1])
    )

curves = [
    # Esophagus
    [(514,439), (514,470), (514,490), (520,515)],
    # Stomach
    [(520,515), (600,530), (640,570), (540,600)],
    # Pylorus / Upper Duodenum
    [(540,600), (510,610), (500,620), (500,650)],
    # Lower Duodenum
    [(500,650), (500,680), (530,710), (573,739)]
]

for curve in curves:
    for t in np.linspace(0, 1, 20):
        pt = eval_bezier(curve[0], curve[1], curve[2], curve[3], t)
        cv2.circle(img, pt, 3, (0, 255, 0), -1)

# Draw control points in red
for curve in curves:
    for p in curve:
        cv2.circle(img, p, 5, (0, 0, 255), 1)

cv2.imwrite(r"c:\Users\Abdel\.gemini\antigravity\brain\c6adabb5-4c6d-4444-85af-c1f422180412\test_bezier.png", img)
