#!/bin/bash
# CPZ Vault Setup Script
# CMDS + PARA + Zettelkasten 통합 시스템

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_PATH="${1:-$SCRIPT_DIR}"

echo "🚀 CPZ Vault Setup"
echo "===================="
echo "Vault path: $VAULT_PATH"
echo ""

create_folder() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
        echo "  ✅ Created: $1"
    else
        echo "  ⏭️  Exists: $1"
    fi
}

echo "📁 Creating folder structure..."

create_folder "$VAULT_PATH/📥 Inbox/_quick"
create_folder "$VAULT_PATH/📥 Inbox/_webclip"

create_folder "$VAULT_PATH/🎯 Projects"

create_folder "$VAULT_PATH/🔄 Areas/Daily"
create_folder "$VAULT_PATH/🔄 Areas/Engineering"
create_folder "$VAULT_PATH/🔄 Areas/Philosophy"

create_folder "$VAULT_PATH/📚 Resources/Papers"
create_folder "$VAULT_PATH/📚 Resources/Books"
create_folder "$VAULT_PATH/📚 Resources/People"

create_folder "$VAULT_PATH/🗃️ Archive"

create_folder "$VAULT_PATH/💎 Zettel/Concepts"
create_folder "$VAULT_PATH/💎 Zettel/Claims"
create_folder "$VAULT_PATH/💎 Zettel/Questions"
create_folder "$VAULT_PATH/💎 Zettel/_MOC"

create_folder "$VAULT_PATH/⚙️ Meta/Templates"
create_folder "$VAULT_PATH/⚙️ Meta/Scripts"
create_folder "$VAULT_PATH/⚙️ Meta/Dashboard"

echo ""
echo "🔧 Setting up CLI tool..."

if [ -f "$VAULT_PATH/scripts/vault-cli.py" ]; then
    chmod +x "$VAULT_PATH/scripts/vault-cli.py"
    
    if [ ! -f "/usr/local/bin/vault" ]; then
        echo ""
        echo "📌 To install 'vault' command globally, run:"
        echo "   sudo ln -sf $VAULT_PATH/scripts/vault-cli.py /usr/local/bin/vault"
    fi
    
    echo "  ✅ vault-cli.py is ready"
else
    echo "  ⚠️  vault-cli.py not found"
fi

echo ""
echo "📝 Creating config file..."

CONFIG_FILE="$VAULT_PATH/scripts/config.yaml"
if [ ! -f "$CONFIG_FILE" ]; then
    cat > "$CONFIG_FILE" << 'EOF'
# CPZ Vault Configuration
# Customize these settings for your vault

author: "[[Your Name]]"

folders:
  inbox: "📥 Inbox"
  quick: "📥 Inbox/_quick"
  webclip: "📥 Inbox/_webclip"
  projects: "🎯 Projects"
  areas: "🔄 Areas"
  resources: "📚 Resources"
  archive: "🗃️ Archive"
  zettel: "💎 Zettel"
  meta: "⚙️ Meta"
  templates: "⚙️ Meta/Templates"
  daily: "🔄 Areas/Daily"

cmds_stages:
  - inbox
  - connect
  - merge
  - develop
  - share

status_levels:
  - seed
  - sapling
  - evergreen
  - archive

domains:
  - cs
  - ee
  - phil
  - math
  - robotics
  - general

prefixes:
  daily: "D"
  lecture: "L"
  concept: "C"
  problem: "P"
  reference: "R"
  meeting: "MTG"
  project: "PRJ"
  zettel: "Z"
  question: "Q"
EOF
    echo "  ✅ Created config.yaml"
else
    echo "  ⏭️  config.yaml exists"
fi

echo ""
echo "🔌 Checking Obsidian plugins..."
echo "   Required plugins:"
echo "   - Templater (templates)"
echo "   - Dataview (queries)"
echo "   - Calendar (daily notes)"
echo "   - Spaced Repetition (flashcards)"
echo ""

echo "✅ Setup complete!"
echo ""
echo "📖 Next steps:"
echo "   1. Open this folder in Obsidian"
echo "   2. Install required plugins from Community Plugins"
echo "   3. Set Templater template folder to: ⚙️ Meta/Templates"
echo "   4. Edit scripts/config.yaml with your name"
echo "   5. Try: python scripts/vault-cli.py today"
echo ""
echo "📚 Documentation: ⚙️ Meta/Dashboard/Dashboard.md"
