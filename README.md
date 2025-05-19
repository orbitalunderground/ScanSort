# ScanSort

**ScanSort** is a versatile Python desktop tool built for high-efficiency photo archiving, tagging, and metadata cleaning. Designed for professionals and hobbyists alike, it combines image scanning, manual import, and EXIF stripping — all from a clean, modern GUI.

## 🔧 Features

* 📁 Open image files (JPG, PNG, BMP, GIF)
* 🖨️ Scan directly from connected TWAIN/WIA-compatible scanners (via `pyinsane2`)
* 📝 Tag photos with **Year** and **Notes**
* 💾 Save renamed images with metadata-stamped filenames
* 📃 Sidecar `.txt` file generated with saved notes
* ❌ One-click **EXIF stripping** for privacy-safe image sharing
* 🖼️ Scales thumbnails to preview image

## 🛠 Requirements

* Python 3.8–3.12
* Windows 10/11
* `Pillow` — image handling
* `pyinsane2` — (optional) scanner interface

Install dependencies:

```bash
pip install pillow pyinsane2
```

## 🚀 How to Run

1. Clone or download this repo.
2. Navigate to the directory:

   ```bash
   cd ScanSort
   ```
3. Launch the app:

   ```bash
   python ScanSort.py
   ```

## 📦 Build as EXE (Optional)

Use [PyInstaller](https://pyinstaller.org) to build an `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico ScanSort.py
```

Your `.exe` will be in the `dist/` folder.

## 📁 Folder Structure

```
ScanSort/
├── ScanSort.py
├── README.md
├── requirements.txt
├── nda_template.txt (optional)
├── assets/ (optional images/icons)
└── dist/ (build output)
```

## 📜 License

MIT License. Use it, fork it, tweak it, share it.

---

Built by Hud with a mind for speed, clarity, and practical use in real photo archiving workflows.