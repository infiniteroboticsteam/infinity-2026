# Developer Setup Guide

This guide walks you through everything you need to contribute to
`infiniteroboticsteam/infinity-2026`: creating a GitHub account, generating an
SSH key, connecting it to GitHub, and cloning the repository.

You only need to do this once per computer. When you're done, continue with
[Getting Started](GETTING_STARTED.md) to set up the robot and VS Code.

---

## 1. Prerequisites

### Install Git

- **macOS:** open Terminal and run `git --version`. If Git isn't installed,
  macOS will prompt you to install the Xcode Command Line Tools — accept it.
- **Windows:** download and install [Git for Windows](https://git-scm.com/download/win).
  During setup, keep the default options. Use **Git Bash** for all commands below.
- **Linux (Debian/Ubuntu):** `sudo apt install git`

Verify:

```bash
git --version
```

### Create a GitHub account

If you don't have one, sign up at <https://github.com/signup>. Then send your
GitHub username to the team lead so you can be added as a collaborator on the
repository. **You will not be able to push until you've been added.**

---

## 2. Tell Git who you are

Git records a name and email on every commit. Use the same email as your
GitHub account so commits are linked to your profile.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

> If you use a different identity for other projects, drop `--global` and run
> these inside the repository folder after cloning (step 5) to apply them to
> this repo only.

---

## 3. Generate an SSH key

An SSH key lets your computer authenticate with GitHub without typing a
password each time.

First, check whether you already have one:

```bash
ls ~/.ssh/id_ed25519.pub
```

If the file exists, skip to step 4. Otherwise generate a key (replace the
email with your GitHub email):

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

- When asked where to save the key, press **Enter** to accept the default.
- When asked for a passphrase, you can press **Enter** for none, or set one for
  extra security (you'll be prompted for it when the key is used).

Then start the SSH agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

On **macOS**, to have the key loaded automatically in future sessions, create
(or edit) `~/.ssh/config` and add:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

---

## 4. Add the SSH key to GitHub

1. Copy your **public** key to the clipboard:

   - **macOS:** `pbcopy < ~/.ssh/id_ed25519.pub`
   - **Windows (Git Bash):** `cat ~/.ssh/id_ed25519.pub | clip`
   - **Linux:** `cat ~/.ssh/id_ed25519.pub` and copy the output manually

   The key is a single line starting with `ssh-ed25519`. Only ever share the
   `.pub` file — never the private key (`id_ed25519` without `.pub`).

2. Go to <https://github.com/settings/ssh/new> (Settings → SSH and GPG keys →
   New SSH key).
3. **Title:** something that identifies the computer, e.g. `MacBook Air`.
4. **Key type:** Authentication Key.
5. **Key:** paste the contents of your clipboard.
6. Click **Add SSH key**.

Test the connection:

```bash
ssh -T git@github.com
```

The first time, you'll be asked to trust GitHub's host key — type `yes`.
You should then see:

```
Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

If you instead see `Permission denied (publickey)`, see
[Troubleshooting](#troubleshooting).

---

## 5. Clone the repository

```bash
git clone git@github.com:infiniteroboticsteam/infinity-2026.git
cd infinity-2026
```

Note the URL starts with `git@github.com:` (SSH), **not** `https://`. Using the
SSH URL is what lets your key handle authentication.

If you already cloned with HTTPS, switch the remote:

```bash
git remote set-url origin git@github.com:infiniteroboticsteam/infinity-2026.git
```

---

## 6. Daily workflow

```bash
git pull                       # get the latest changes before you start
git checkout -b my-feature     # work on a branch, not directly on main
# ... edit files ...
git add .
git commit -m "Describe what you changed"
git push -u origin my-feature  # first push of a new branch
```

Then open a Pull Request on GitHub so the team can review and merge your
branch into `main`.

---

## Troubleshooting

**`Permission denied (publickey)`**
- Make sure you added the `.pub` key to GitHub (step 4), not the private key.
- Run `ssh-add -l` — if your key isn't listed, run `ssh-add ~/.ssh/id_ed25519`.
- Run `ssh -vT git@github.com` and check that it's offering `~/.ssh/id_ed25519`.

**`Key is already in use`** when adding the key on GitHub
- An SSH key can only belong to one GitHub account. Either remove it from the
  other account, or generate a second key with a different filename
  (`ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_infinity`) and point this repo
  at it in `~/.ssh/config`.

**`remote: Permission to infiniteroboticsteam/infinity-2026.git denied`**
- Your key works, but your GitHub account hasn't been granted access to the
  repo. Ask the team lead to add you as a collaborator.

**`Host key verification failed`**
- Run `ssh -T git@github.com` once interactively and answer `yes` to the
  prompt to add GitHub to `~/.ssh/known_hosts`.

**Git asks for a username/password on push**
- Your remote is still HTTPS. Switch it to SSH (see step 5).
