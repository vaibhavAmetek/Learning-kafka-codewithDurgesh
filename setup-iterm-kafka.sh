#!/bin/bash

# 🎨 iTerm2 Quick Setup for Kafka Development
# This script configures iTerm2 with transparency and optimal settings

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎨 iTerm2 Setup for Kafka Development"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if iTerm2 is installed
if [ ! -d "/Applications/iTerm.app" ]; then
    echo "❌ iTerm2 not found!"
    echo "📦 Installing iTerm2..."
    brew install --cask iterm2
    echo "✅ iTerm2 installed!"
else
    echo "✅ iTerm2 found"
fi

echo ""
echo "⚙️  Configuring iTerm2 settings..."

# Set transparency (0.35 = 35%)
defaults write com.googlecode.iterm2 Transparency -float 0.35
echo "  ✓ Transparency set to 35%"

# Enable blur
defaults write com.googlecode.iterm2 Blur -bool true
echo "  ✓ Blur enabled"

# Set blur radius
defaults write com.googlecode.iterm2 BlurRadius -float 12
echo "  ✓ Blur radius set to 12"

# Set window size
defaults write com.googlecode.iterm2 "Columns" -int 130
defaults write com.googlecode.iterm2 "Rows" -int 35
echo "  ✓ Window size: 130x35"

# Enable anti-aliasing
defaults write com.googlecode.iterm2 "Anti-aliased" -bool true
echo "  ✓ Anti-aliasing enabled"

echo ""
echo "🔤 Checking fonts..."

# Check if Meslo Nerd Font is installed
if ! brew list --cask font-meslo-lg-nerd-font &>/dev/null; then
    echo "📦 Installing Meslo Nerd Font..."
    brew tap homebrew/cask-fonts
    brew install --cask font-meslo-lg-nerd-font
    echo "✅ Font installed!"
else
    echo "✅ Meslo Nerd Font already installed"
fi

echo ""
echo "🎨 Downloading color schemes..."

# Create directory for color schemes
mkdir -p ~/Downloads/iTerm-Colors

# Download Dracula
if [ ! -f ~/Downloads/iTerm-Colors/Dracula.itermcolors ]; then
    curl -sL -o ~/Downloads/iTerm-Colors/Dracula.itermcolors \
      https://raw.githubusercontent.com/dracula/iterm/master/Dracula.itermcolors
    echo "  ✓ Dracula theme downloaded"
fi

# Download Solarized Dark
if [ ! -f ~/Downloads/iTerm-Colors/Solarized-Dark.itermcolors ]; then
    curl -sL -o ~/Downloads/iTerm-Colors/Solarized-Dark.itermcolors \
      "https://raw.githubusercontent.com/altercation/solarized/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors"
    echo "  ✓ Solarized Dark theme downloaded"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ iTerm2 Configuration Complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Next Steps:"
echo ""
echo "1. 🔄 Restart iTerm2 to apply changes"
echo ""
echo "2. 🎨 Import color scheme:"
echo "   • Open iTerm2"
echo "   • Press Cmd + ,"
echo "   • Go to: Profiles → Colors → Color Presets → Import"
echo "   • Import from: ~/Downloads/iTerm-Colors/"
echo "   • Select: Dracula.itermcolors (recommended)"
echo ""
echo "3. 🔤 Set font:"
echo "   • Go to: Profiles → Text → Font"
echo "   • Select: MesloLGS NF, 14pt"
echo ""
echo "4. 🖼️  Verify transparency:"
echo "   • Go to: Profiles → Window"
echo "   • Check transparency slider (should be at 35%)"
echo "   • Ensure 'Blur' is checked"
echo ""
echo "5. 🚀 Create Kafka layout:"
echo "   • Run: ./kafka-iterm-layout.sh"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📖 Full guide: ITERM_SETUP.md"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
