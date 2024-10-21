from colorthief import ColorThief
import matplotlib.pyploy as plt

ct = ColorThief("testimg.png")
dominant_color = ct.get_color(quality=1)

plt.imshow ([[dominant_color]])
plt.show()

