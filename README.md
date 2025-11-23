# 🌅 Arch Linux + Qtile Dotfiles

A sleek, warm, and Spider-Man-inspired theme for Arch Linux.

Sunset Swing is a cohesive configuration ecosystem for **Qtile** on Arch Linux. It features a custom color palette derived from Alex Ross's golden-hour Spider-Man artwork, blending deep city‑shadow blues with vibrant sunset oranges and classic spider‑reds.

<img width="1919" height="1079" alt="2025-10-21_18-53_1" src="https://github.com/user-attachments/assets/e69192a5-0423-4815-9026-4acdac9fe9e6" />
<img width="1919" height="1078" alt="2025-10-21_18-52" src="https://github.com/user-attachments/assets/c7c7d001-2189-44a9-a8f4-5379b2418a3f" />
<img width="780" height="728" alt="Screenshot 2025-11-12 215112" src="https://github.com/user-attachments/assets/5be158d3-3ed7-4a5e-8228-1c73187d1594" />


---

## 🧩 Components

This setup is built around a modular and lightweight stack:

- **Window Manager:** Qtile (Python-based, extensible tiling WM)  
- **Bar Status:** Built-in Qtile Bar with a custom “Block” design and Powerline separators  
- **Compositor:** Picom (Fork) – transparency, rounded corners, shadows  
- **Terminal:** Alacritty – GPU accelerated  
- **Shell:** Zsh + Powerlevel10k  
- **Application Launcher:** Rofi (rounded themed)  
- **Power Menu:** Custom Bash + Rofi + loginctl  
- **System Fetch:** Fastfetch (custom Spider-Man ASCII)  
- **File Manager:** Nautilus (GTK4, Catppuccin Mocha Peach)  
- **Screenshot Tool:** Flameshot  
- **Music:** Spotify + Spicetify theme (ziro theme + custom color theme) 

---

## 📦 Requirements (Packages)

### Core System & WM

```bash
sudo pacman -S qtile picom rofi alacritty dunst libnotify
```

### Shell & Prompt

```bash
sudo pacman -S zsh zsh-syntax-highlighting zsh-autosuggestions
yay -S zsh-theme-powerlevel10k-git
```

### Wallpaper & Appearance

```bash
sudo pacman -S nitrogen lxappearance nwg-look
```

### Dependencies & Widgets

```bash
sudo pacman -S python-psutil python-netifaces
sudo pacman -S alsa-utils brightnessctl pamixer
sudo pacman -S flameshot betterlockscreen
```

### Fonts & Theming

```bash
yay -S ttf-jetbrains-mono-nerd
yay -S catppuccin-gtk-theme-mocha papirus-icon-theme
```

### Optional Apps

```bash
sudo pacman -S nautilus fastfetch spotify-launcher
yay -S spicetify-cli
```

---

## 🎨 The “Sunset Swing” Palette

| Color Name | Hex Code | Usage |
|-----------|----------|--------|
| Background | `#24283b` | Deep Blue/Grey (City Shadows) |
| Foreground | `#c0caf5` | Soft White/Blue |
| Focus/Accent | `#ff9e64` | Sunset Orange |
| Red | `#f7768e` | Spider-Man Suit Red |
| Blue | `#7aa2f7` | Sky Blue |
| Yellow | `#e0af68` | Golden Hour Sun |
| Green | `#9ece6a` | Status Indicators |
| Magenta | `#bb9af7` | Soft Accents |
| Cyan | `#7dcfff` |Bright Accents |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/sunset-swing-dots.git
cd sunset-swing-dots
```

### 2. Back up your existing configs

```bash
mkdir ~/backup_dots
mv ~/.config/qtile ~/backup_dots/
mv ~/.config/picom ~/backup_dots/
# repeat for others
```

### 3. Copy the dotfiles

```bash
cp -r .config/* ~/.config/
cp .zshrc ~/
cp .p10k.zsh ~/
```

### 4. Make scripts executable

```bash
chmod +x ~/.config/qtile/autostart.sh
chmod +x ~/.config/rofi/powermenu.sh
```

### 5. Reload Qtile  
Log out and back in, or press:

```
Super + Ctrl + R
```

---
