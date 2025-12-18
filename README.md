# My Obsidian Vault

Welcome to my Obsidian knowledge base! This repository serves as a backup and sync solution for my Obsidian vault.

## 📁 Vault Structure

```
.
├── Notes/              # General notes and knowledge base
├── Resources/
│   └── Images/        # Images and visual assets
└── Templates/         # Note templates for consistent formatting
```

## 🔄 Syncing with Obsidian Git Plugin

This vault uses the [Obsidian Git plugin](https://github.com/denolehov/obsidian-git) for automatic version control and synchronization.

### Initial Setup

1. **Install Obsidian Git Plugin**
   - Open Obsidian Settings → Community Plugins
   - Browse and search for "Obsidian Git"
   - Install and enable the plugin

2. **Clone This Repository**
   ```bash
   git clone https://github.com/seoneum/new_my_Obsidian.git
   ```

3. **Open as Vault**
   - In Obsidian, click "Open folder as vault"
   - Select the cloned repository folder

4. **Configure Git Plugin** (Optional)
   - Open Settings → Obsidian Git
   - Set auto-backup interval (default: 10 minutes)
   - Configure commit message template
   - Enable auto-pull on startup

### Usage

#### Automatic Sync
- The plugin automatically commits changes at your configured interval
- Pull updates from remote on startup (if enabled)
- Push changes to GitHub automatically

#### Manual Sync
Use Command Palette (`Ctrl/Cmd + P`) and search for:
- `Obsidian Git: Commit all changes` - Stage and commit all changes
- `Obsidian Git: Push` - Push commits to remote
- `Obsidian Git: Pull` - Pull updates from remote
- `Obsidian Git: Backup` - Commit and push in one command

### Recommended Plugin Settings

- **Vault backup interval**: 10-30 minutes
- **Auto pull interval**: 10 minutes
- **Commit message**: `vault backup: {{date}}`
- **Pull updates on startup**: Enabled
- **Disable push**: Disabled (allow automatic push)

## 📝 Best Practices

1. **Commit Messages**: The plugin handles this automatically, but you can customize the format
2. **Conflict Resolution**: Pull before making major changes to avoid conflicts
3. **Private Information**: Be mindful of sensitive information if this is a public repository
4. **Large Files**: Consider using Git LFS for large attachments if needed
5. **Workspace Settings**: Personal workspace settings are gitignored by default

## 🚀 Getting Started

1. Create your first note in the `Notes/` folder
2. Add any images or resources to `Resources/Images/`
3. Create custom templates in `Templates/` folder
4. Let the Git plugin handle the rest!

## 🔧 Troubleshooting

### Plugin Not Working
- Ensure Git is installed on your system
- Check that you have write permissions to the repository
- Verify your Git credentials are configured

### Merge Conflicts
- Use the Command Palette: `Obsidian Git: Edit remotes`
- Pull changes first, then resolve conflicts manually
- Commit the resolved changes

### Authentication Issues
- Set up SSH keys or use a personal access token
- Configure Git credentials in your system

## 📚 Resources

- [Obsidian Documentation](https://help.obsidian.md/)
- [Obsidian Git Plugin](https://github.com/denolehov/obsidian-git)
- [Git Documentation](https://git-scm.com/doc)

## 📄 License

This vault structure is available under the license specified in the LICENSE file.