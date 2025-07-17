# 🔐 Secure File Transfer with Encryption

A Python-based system for securely transferring files between devices over a local network using sockets and AES encryption.

---

## 📸 Demo (Optional but STRONGLY recommended)
<!-- Replace with an actual demo gif or screenshot -->
![demo](link_to_image_or_demo.gif)

---

## 📂 Features

- ✅ Secure file transfers using AES symmetric encryption
- ✅ Supports binary files of any type
- ✅ Command-line interface for custom port and IP settings
- ✅ Length-prefixed protocol for structured communication

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python     | Core programming language |
| socket     | For creating TCP server/client communication |
| struct     | Handling binary data for structured messaging |
| argparse   | Command-line interface |
| dotenv     | Managing environment variables securely |
| pycryptodome | Encryption and decryption (AES) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip` installed

### Installation

```bash
git clone https://github.com/phuProjects/secure-file-transfer.git
cd secure-file-transfer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
