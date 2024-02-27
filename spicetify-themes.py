import os

theme_inp = input("Theme 󰉦 : ")
scheme_inp = input("Color Scheme 󰏘 : ")
start_spt = input("Start Spotify?  (Y/n): ")

os.system(f"spicetify config current_theme {theme_inp}")
os.system(f"spicetify config color_scheme {scheme_inp}")
os.system("spicetify config inject_css 1 inject_theme_js 1 replace_colors 1 overwrite_assets 1")
os.system("spicetify apply")

if start_spt == "y":
    os.system("spotify")
