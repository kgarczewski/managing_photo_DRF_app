from colorthief import ColorThief
import matplotlib.pyplot as plt

ct = ColorThief("images/6dd9cb.png")
dominant_color = ct.get_color(quality=1)

plt.imshow([[dominant_color]])
plt.show()
# print(f"{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}")
print('#%02x%02x%02x' % dominant_color)

# palette = ct.get_palette(color_count=5)
# plt.imshow([[palette[i] for i in range(5)]])
# plt.show()
# for color in palette:
#     print(f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')
#     break
