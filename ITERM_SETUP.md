# 🖥️ iTerm2 Setup for Kafka Development (Mac)

> Make your terminal look professional with transparency and better settings

---

## 🎯 Goal

Create a setup similar to the tutorial:

- **Transparent terminal** background
- **Website visible** behind terminal
- **Better readability** with proper colors
- **Professional look** for coding

---

## 📦 Step 1: Install iTerm2 (If Not Installed)

### Check if iTerm2 is installed:

```bash
# Check if iTerm2 exists
ls -la /Applications/iTerm.app
```

### If not installed:

```bash
# Install via Homebrew
brew install --cask iterm2

# Or download from website
# https://iterm2.com/downloads.html
```

---

## 🎨 Step 2: Configure Transparency

### Method 1: Quick Setup (Recommended)

1. **Open iTerm2**

2. **Press:** `Cmd + ,` (Opens Preferences)

3. **Navigate to:**

   ```
   Preferences → Profiles → Default → Window
   ```

4. **Set Transparency:**

   - Find "Transparency" slider
   - Move slider to **30-40%** (sweet spot for readability)
   - Check ✅ "Blur" (optional, makes text more readable)

5. **Set Background Image (Optional):**
   - Scroll down to "Background Image"
   - Check ✅ "Background Image"
   - Click "Choose" and select an image
   - Set "Blending" to **0.3-0.5**

---

### Method 2: Using Command Line

```bash
# Set transparency (0.0 = opaque, 1.0 = fully transparent)
defaults write com.googlecode.iterm2 Transparency -float 0.35

# Enable blur
defaults write com.googlecode.iterm2 Blur -bool true

# Restart iTerm2 to apply
```

---

## 🌈 Step 3: Color Scheme (Better Visibility)

### Install Popular Color Schemes

```bash
# Clone iTerm2 color schemes
cd ~/Downloads
git clone https://github.com/mbadolato/iTerm2-Color-Schemes.git

# Open iTerm2 Preferences
# Cmd + ,
```

### Apply Color Scheme:

1. **Go to:** `Preferences → Profiles → Default → Colors`

2. **Click:** "Color Presets..." (bottom right)

3. **Click:** "Import..."

4. **Navigate to:** `~/Downloads/iTerm2-Color-Schemes/schemes/`

5. **Recommended Schemes:**

   - **Dracula** (Dark, popular)
   - **Solarized Dark** (Professional)
   - **Monokai** (Vibrant)
   - **Nord** (Cool blue tones)
   - **Gruvbox Dark** (Warm, easy on eyes)

6. **Select and Apply** your favorite

---

## 🔤 Step 4: Font Settings (Better Readability)

### Install Powerline Fonts

```bash
# Install Meslo Nerd Font (Recommended)
brew tap homebrew/cask-fonts
brew install --cask font-meslo-lg-nerd-font

# Or install Fira Code (with ligatures)
brew install --cask font-fira-code

# Or install JetBrains Mono
brew install --cask font-jetbrains-mono
```

### Apply Font in iTerm2:

1. **Go to:** `Preferences → Profiles → Default → Text`

2. **Font Section:**

   - Click "Change Font"
   - Select: **"MesloLGS NF"** or **"Fira Code"**
   - Size: **14-16** (adjust to preference)
   - Check ✅ "Use ligatures" (if using Fira Code)

3. **Anti-aliasing:**
   - Check ✅ "Anti-aliased"
   - Check ✅ "Use thin strokes for anti-aliased text"

---

## 🖼️ Step 5: Window Settings

### Configure Window Appearance:

1. **Go to:** `Preferences → Profiles → Default → Window`

2. **Settings:**

   ```
   Transparency: 30-40%
   Blur: ✅ Enabled (Blur Radius: 10-15)

   Window Appearance:
   - Style: Normal
   - Screen: Main Screen

   Settings for New Windows:
   - Columns: 120-140
   - Rows: 30-40
   ```

3. **Advanced Settings:**
   - Check ✅ "Keep background colors opaque"
   - Uncheck ❌ "Blur behind window" (if performance issue)

---

## 🎬 Step 6: Split Panes Setup (Like Tutorial)

### Create Multiple Panes:

```bash
# Horizontal split
Cmd + D

# Vertical split
Cmd + Shift + D

# Navigate between panes
Cmd + [ or Cmd + ]

# Close pane
Cmd + W
```

### Example Layout for Kafka:

```
┌─────────────────────────────────────┐
│  Pane 1: Zookeeper                  │
│  zookeeper-server-start ...         │
├─────────────────────────────────────┤
│  Pane 2: Kafka Server               │
│  kafka-server-start ...             │
├──────────────────┬──────────────────┤
│  Pane 3:         │  Pane 4:         │
│  Producer        │  Consumer        │
│  kafka-console-  │  kafka-console-  │
│  producer ...    │  consumer ...    │
└──────────────────┴──────────────────┘
```

---

## 🌐 Step 7: Browser + Terminal Setup (Like Tutorial)

### Method 1: Manual Positioning

1. **Open Safari/Chrome** with Kafka documentation

   - URL: https://kafka.apache.org/quickstart

2. **Make browser full screen** or resize

3. **Open iTerm2**

   - Press `Cmd + Enter` (Toggle fullscreen)
   - Or resize to cover part of browser

4. **Adjust transparency** so website is visible behind

---

### Method 2: Using Rectangle (Window Manager)

```bash
# Install Rectangle for window management
brew install --cask rectangle

# Usage:
# Ctrl + Option + Left Arrow  = Left half
# Ctrl + Option + Right Arrow = Right half
# Ctrl + Option + Enter       = Maximize
```

**Setup:**

1. Browser on left half (Ctrl + Option + Left)
2. iTerm2 on right half (Ctrl + Option + Right)
3. Adjust iTerm2 transparency to see browser

---

### Method 3: Picture-in-Picture Browser

```bash
# Install Helium (Floating Browser)
brew install --cask helium

# Usage:
# 1. Open Helium
# 2. Navigate to Kafka docs
# 3. Make it always on top
# 4. Open iTerm2 below it
```

---

## 🎨 Step 8: Complete iTerm2 Profile Setup

### Create Custom Profile for Kafka Development:

1. **Open iTerm2 Preferences** (`Cmd + ,`)

2. **Go to:** `Profiles`

3. **Click:** `+` (Create new profile)

4. **Name it:** "Kafka Dev"

5. **Configure:**

#### General Tab:

```
Name: Kafka Dev
Command: Login shell
Working Directory: ~/Projects/Learning-kafka-codewithDurgesh
```

#### Colors Tab:

```
Color Preset: Dracula (or your choice)
```

#### Text Tab:

```
Font: MesloLGS NF, 14pt
Anti-aliased: ✅
Use ligatures: ✅
```

#### Window Tab:

```
Transparency: 35%
Blur: ✅ (Radius: 12)
Columns: 130
Rows: 35
Style: Normal
```

#### Terminal Tab:

```
Scrollback lines: 10000
Character Encoding: UTF-8
```

#### Keys Tab:

```
(Keep default or customize)
```

6. **Set as Default:**
   - Select "Kafka Dev" profile
   - Click "Other Actions..." → "Set as Default"

---

## 🚀 Step 9: Useful iTerm2 Shortcuts

### Window Management:

```bash
Cmd + N          # New window
Cmd + T          # New tab
Cmd + D          # Split horizontally
Cmd + Shift + D  # Split vertically
Cmd + [          # Previous pane
Cmd + ]          # Next pane
Cmd + W          # Close pane/tab
Cmd + Enter      # Toggle fullscreen
```

### Text Operations:

```bash
Cmd + F          # Find
Cmd + K          # Clear screen
Cmd + ;          # Autocomplete
Cmd + Shift + H  # Paste history
Ctrl + A         # Go to start of line
Ctrl + E         # Go to end of line
Ctrl + U         # Clear line
```

### Selection:

```bash
Double-click     # Select word
Triple-click     # Select line
Cmd + Click      # Open URL
Option + Click   # Move cursor
```

---

## 🎯 Step 10: Kafka-Specific iTerm2 Setup

### Create Startup Script:

```bash
cat > ~/kafka-iterm-setup.sh << 'EOF'
#!/bin/bash

# Open iTerm2 with 4 panes for Kafka development

# This script creates the layout shown in tutorial
osascript <<APPLESCRIPT
tell application "iTerm"
    activate

    -- Create new window
    create window with default profile

    tell current session of current window
        -- Pane 1: Zookeeper
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "echo '🐘 Zookeeper - Ready to start'"
        write text "echo 'Run: zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties'"

        -- Split horizontally for Kafka
        split horizontally with default profile
    end tell

    tell second session of current tab of current window
        -- Pane 2: Kafka
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "echo '🚀 Kafka Server - Ready to start'"
        write text "echo 'Run: kafka-server-start /opt/homebrew/etc/kafka/broker.properties'"

        -- Split vertically for Producer
        split vertically with default profile
    end tell

    tell third session of current tab of current window
        -- Pane 3: Producer
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "echo '📤 Producer - Ready'"
        write text "echo 'Run: kafka-console-producer --topic test --bootstrap-server localhost:9092'"
    end tell

    tell second session of current tab of current window
        -- Split vertically for Consumer
        split vertically with default profile
    end tell

    tell fourth session of current tab of current window
        -- Pane 4: Consumer
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "echo '📥 Consumer - Ready'"
        write text "echo 'Run: kafka-console-consumer --topic test --from-beginning --bootstrap-server localhost:9092'"
    end tell

end tell
APPLESCRIPT
EOF

chmod +x ~/kafka-iterm-setup.sh
```

### Run the setup:

```bash
~/kafka-iterm-setup.sh
```

---

## 🎨 Step 11: Recommended Color Schemes

### Dracula (Most Popular)

```bash
# Download and import
curl -o ~/Downloads/Dracula.itermcolors \
  https://raw.githubusercontent.com/dracula/iterm/master/Dracula.itermcolors

# Import: Preferences → Profiles → Colors → Color Presets → Import
```

### Solarized Dark

```bash
curl -o ~/Downloads/Solarized-Dark.itermcolors \
  https://raw.githubusercontent.com/altercation/solarized/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors
```

### Nord

```bash
curl -o ~/Downloads/Nord.itermcolors \
  https://raw.githubusercontent.com/arcticicestudio/nord-iterm2/develop/src/xml/Nord.itermcolors
```

---

## 🔧 Step 12: Advanced Settings

### Enable Natural Text Editing:

1. **Go to:** `Preferences → Profiles → Keys → Key Mappings`

2. **Click:** "Presets..." → "Natural Text Editing"

3. **This enables:**
   - Option + Left/Right Arrow = Move by word
   - Cmd + Left/Right Arrow = Move to start/end of line
   - Option + Delete = Delete word

---

### Enable Shell Integration:

```bash
# Install iTerm2 shell integration
curl -L https://iterm2.com/shell_integration/install_shell_integration.sh | bash

# Restart iTerm2
```

**Benefits:**

- Command history
- Current directory tracking
- Better autocomplete

---

## 📊 Step 13: Status Bar (Optional)

### Add Status Bar:

1. **Go to:** `Preferences → Profiles → Session`

2. **Check:** ✅ "Status bar enabled"

3. **Click:** "Configure Status Bar"

4. **Add components:**

   - CPU Utilization
   - Memory Utilization
   - Network Throughput
   - Current Directory
   - Git Status

5. **Position:** Bottom

---

## 🎯 Final Setup for Tutorial-Like Experience

### Complete Configuration:

```bash
# 1. Transparency
Transparency: 35%
Blur: ✅ Enabled (Radius: 12)

# 2. Colors
Color Scheme: Dracula or Solarized Dark

# 3. Font
Font: MesloLGS NF, 14pt
Anti-aliased: ✅

# 4. Window
Columns: 130
Rows: 35
Style: Normal

# 5. Background
Keep background colors opaque: ✅
```

---

## 🌐 Step 14: Browser + Terminal Workflow

### Recommended Setup:

```bash
# Screen Layout:
┌─────────────────────────────────────────────┐
│  Browser (Safari/Chrome)                    │
│  https://kafka.apache.org/quickstart        │
│  ┌───────────────────────────────────────┐  │
│  │  iTerm2 (35% transparent)             │  │
│  │  ┌─────────────┬─────────────┐        │  │
│  │  │ Zookeeper   │ Kafka       │        │  │
│  │  ├─────────────┼─────────────┤        │  │
│  │  │ Producer    │ Consumer    │        │  │
│  │  └─────────────┴─────────────┘        │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Steps:

1. Open browser with Kafka docs
2. Make browser window larger
3. Open iTerm2 on top
4. Set iTerm2 transparency to 35%
5. Resize iTerm2 to see docs behind

---

## 🎨 Quick Setup Script

```bash
cat > ~/setup-iterm-kafka.sh << 'EOF'
#!/bin/bash

echo "🎨 Setting up iTerm2 for Kafka Development..."

# Set transparency
defaults write com.googlecode.iterm2 Transparency -float 0.35

# Enable blur
defaults write com.googlecode.iterm2 Blur -bool true

# Set blur radius
defaults write com.googlecode.iterm2 BlurRadius -float 12

# Set font size
defaults write com.googlecode.iterm2 "Normal Font" -string "MesloLGSNF-Regular 14"

# Set columns and rows
defaults write com.googlecode.iterm2 "Columns" -int 130
defaults write com.googlecode.iterm2 "Rows" -int 35

echo "✅ iTerm2 configured!"
echo "📝 Restart iTerm2 to apply changes"
echo ""
echo "Next steps:"
echo "1. Install color scheme (Dracula recommended)"
echo "2. Run: ~/kafka-iterm-setup.sh for multi-pane layout"
EOF

chmod +x ~/setup-iterm-kafka.sh
```

### Run it:

```bash
~/setup-iterm-kafka.sh
```

---

## 🐛 Troubleshooting

### Issue 1: Transparency Not Working

**Solution:**

```bash
# Check if iTerm2 is running
killall iTerm2

# Reset preferences
defaults delete com.googlecode.iterm2

# Restart iTerm2 and reconfigure
```

---

### Issue 2: Font Not Showing

**Solution:**

```bash
# Reinstall font
brew reinstall font-meslo-lg-nerd-font

# Restart iTerm2
# Go to Preferences → Profiles → Text → Change Font
```

---

### Issue 3: Blur Not Working

**Solution:**

1. Check macOS version (Blur requires macOS 10.10+)
2. Disable "Reduce transparency" in System Preferences
   - System Preferences → Accessibility → Display
   - Uncheck "Reduce transparency"

---

## 📚 Additional Resources

### iTerm2 Documentation:

```
https://iterm2.com/documentation.html
```

### Color Schemes:

```
https://iterm2colorschemes.com/
```

### Fonts:

```
https://www.nerdfonts.com/
```

---

## ✅ Verification Checklist

```bash
✅ iTerm2 installed
✅ Transparency set (30-40%)
✅ Blur enabled
✅ Color scheme applied (Dracula/Solarized)
✅ Font installed (MesloLGS NF)
✅ Window size configured (130x35)
✅ Split panes working (Cmd+D, Cmd+Shift+D)
✅ Browser + Terminal layout tested
✅ Kafka commands visible and readable
```

---

## 🎯 Summary

**To get tutorial-like setup:**

1. **Install iTerm2** (if not installed)
2. **Set transparency** to 35%
3. **Enable blur** for readability
4. **Apply color scheme** (Dracula recommended)
5. **Install font** (MesloLGS NF)
6. **Open browser** with Kafka docs
7. **Position iTerm2** on top with transparency
8. **Split panes** for Zookeeper, Kafka, Producer, Consumer

**Quick commands:**

```bash
# Setup iTerm2
~/setup-iterm-kafka.sh

# Create multi-pane layout
~/kafka-iterm-setup.sh

# Start working!
```

---

**Your terminal will look professional and functional! 🚀**
