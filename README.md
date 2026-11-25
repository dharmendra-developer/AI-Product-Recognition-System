# 🤖 AI Object Detection System

### Real-Time Object Detection Using YOLO-World & Custom Product Classification

> **An AI-powered computer vision application that detects objects through a webcam using text prompts and supports custom product recognition through machine learning.**

**Developed by [DHARMENDRA_DEVELOPER](https://github.com/dharmendra-developer)**

---

## 📌 Project Overview

The **AI Object Detection System** is a Python-based computer vision application that uses the YOLO-World model to detect objects in real time through a webcam.

Users can enter object names as text prompts, such as `keys`, `mug`, or `remote control`, and the application attempts to identify those objects in the camera feed.

The project also provides a separate custom product classification workflow. Users can collect their own product images, train a classifier, and recognize those specific products through live webcam input.

The application provides two recognition approaches:

- **Prompt-Based Detection:** Detect objects using YOLO-World without collecting a custom dataset.
- **Custom Product Recognition:** Train a classifier using example photos of your own products.

---

## ✨ Key Features

- 🎥 Real-time webcam object detection.
- 🤖 YOLO-World AI model integration.
- 🔍 Text-prompt-based object detection.
- 🛍️ Built-in product detection list.
- 📸 Custom product image collection.
- 🧠 Train your own product classifier.
- 🎯 Recognition of 13 predefined products.
- ⚡ Lightweight live recognition using a 160px classifier input.
- 📊 Confidence-based prediction output.
- 💻 Windows batch-file setup and execution.
- 🔧 Separate scripts for data collection, training, and recognition.

---

## 🏗️ System Architecture

```text
             USER
               |
               v
          Webcam Input
               |
               v
       Select Detection Mode
               |
       +-------+-------+
       |               |
       v               v
  YOLO-World       Custom Classifier
       |               |
  Text Prompts     Collect Images
       |               |
       v               v
  Object Detection  Train Model
       |               |
       v               v
  Detected Objects  Live Recognition
       |               |
       +-------+-------+
               |
               v
        Display Results
```

---

## 🔍 Detection Modes

### 1. YOLO-World Text-Prompt Detection

<badge color="success">Prompt-based detection</badge>

YOLO-World allows users to detect objects by entering their names as text prompts.

**Example prompts:**

```text
keys, mug, remote control
```

**How it works:**

1. Launch the webcam application.
2. Enter object names separated by commas.
3. The model processes the text prompts.
4. The webcam captures live video frames.
5. YOLO-World attempts to detect matching objects.
6. Detection results are displayed on the camera window.

If no prompt is entered, the application uses its built-in product list.

**Important:** Detection depends on the model's understanding of the provided object names. It cannot guarantee recognition of every possible object.

### 2. Custom Product Classifier

<badge color="info">Custom-trained recognition</badge>

The project also supports training a classifier for the 13 products defined in:

```text
src/labels.py
```

This workflow recognizes the products represented in the training dataset rather than arbitrary text prompts.

**Main steps:**

- Collect product images.
- Prepare the training dataset.
- Train the classifier.
- Run live product recognition.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| YOLO-World | Prompt-based object detection |
| Ultralytics | AI model integration |
| OpenCV | Webcam and image processing |
| Custom Classifier | Product-specific recognition |
| PowerShell | Development environment |
| VS Code | Code editor |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
AI-Object-Detection/
│
├── src/
│   ├── labels.py
│   ├── collect_data.py
│   ├── train_model.py
│   └── recognize.py
│
├── setup.bat
├── run.bat
├── .gitignore
└── README.md
```

**Main files:**

| File | Description |
|---|---|
| `setup.bat` | Installs project dependencies |
| `run.bat` | Starts webcam-based YOLO-World detection |
| `labels.py` | Defines the 13 supported products |
| `collect_data.py` | Collects custom product images |
| `train_model.py` | Trains the custom classifier |
| `recognize.py` | Runs live custom product recognition |
| `.gitignore` | Excludes datasets, model weights and virtual environments |

---

## ⚙️ Installation & Setup

### Requirements

- Windows operating system
- Python 3.11
- Webcam
- VS Code (recommended)
- Internet connection for the first YOLO-World model download

### Method 1: Quick Setup

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Open the project folder**

```bash
cd AI-Object-Detection
```

**Step 3: Install dependencies**

Run:

```text
setup.bat
```

**Step 4: Start the application**

Run:

```text
run.bat
```

**Step 5: Enter object names**

For example:

```text
keys, mug, remote control
```

Press Enter without typing anything to use the built-in product list.

**Step 6: Exit the application**

Press `Q` in the camera window.

> **Note:** The first launch downloads the YOLO-World model and may take some time.

---

## 🧠 Custom Product Classifier Training

This workflow is designed for recognizing your own products.

### Requirements

Use an existing `.venv` if it already contains Ultralytics and OpenCV. Otherwise, create a new environment.

### Setup Using VS Code PowerShell

**Step 1: Create a virtual environment**

```powershell
py -3.11 -m venv .venv
```

**Step 2: Upgrade pip**

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

**Step 3: Install dependencies**

```powershell
.\.venv\Scripts\python.exe -m pip install ultralytics opencv-python
```

### Step 1: Collect Product Images

Run:

```powershell
.\.venv\Scripts\python.exe src\collect_data.py
```

**Controls:**

| Key | Action |
|---|---|
| Product Letter | Select a product |
| SPACE | Capture and save an image |
| Q | Quit image collection |

**Dataset recommendation:**

Collect approximately 30–50 varied images per product.

Try to capture:

- Different viewing angles.
- Different distances.
- Different backgrounds.
- Different lighting conditions.
- Different object positions.

### Step 2: Train the Classifier

After collecting the product images, run:

```powershell
.\.venv\Scripts\python.exe src\train_model.py
```

Training is a one-time step for each dataset version and may take several minutes on a CPU.

### Step 3: Run Live Recognition

Execute:

```powershell
.\.venv\Scripts\python.exe src\recognize.py
```

Show one product at a time inside the green square.

Press `Q` to close the recognition window.

---

## 📊 Recognition Workflow

| Stage | Description |
|---|---|
| Input | Webcam video |
| Capture | Read live frames |
| Processing | Prepare image data |
| Detection | Detect objects or classify trained products |
| Prediction | Generate object label |
| Confidence | Estimate prediction confidence |
| Output | Display recognition results |

---

## 💡 Tips for Better Recognition

1. Use bright and consistent lighting.
2. Keep the product centred inside the green square.
3. Make sure the object is reasonably large.
4. Collect photos from different angles and backgrounds.
5. If two products are confused, collect more varied images of both.
6. Retrain the classifier after adding new training examples.

**Important:** Confidence scores are estimates, not guarantees of correct recognition.

---

## 🔐 Data Privacy & Security

- Raw product photos are excluded through `.gitignore`.
- Datasets should not be uploaded publicly without permission.
- Model weights and virtual environments are excluded from Git uploads.
- Webcam access should be used with appropriate user permission.
- Avoid collecting private or sensitive images.

---

## ⚠️ Limitations

- YOLO-World may not recognize every object name.
- Prompt-based detection depends on model understanding.
- Custom classification is limited to the products represented in the training dataset.
- Poor lighting can reduce recognition quality.
- Similar-looking products may be confused.
- Training requires sufficient example images.
- CPU-based training and inference speed depends on laptop hardware.
- Confidence scores do not guarantee prediction correctness.

---

## 🚀 Future Enhancements

- Support for more custom products.
- Improved recognition accuracy.
- Real-time object counting.
- Object tracking across video frames.
- Voice-based object identification.
- Mobile application integration.
- Web-based object detection dashboard.
- Improved model optimization.
- GPU acceleration support.
- Product inventory management integration.

---

## 🧪 Testing Checklist

- [ ] Webcam initialization.
- [ ] YOLO-World model download.
- [ ] Text-prompt input.
- [ ] Built-in product list.
- [ ] Real-time object detection.
- [ ] Product image collection.
- [ ] Custom classifier training.
- [ ] Live product recognition.
- [ ] Application exit using Q.
- [ ] `.gitignore` verification.

---

## 📜 GitHub Repository Guidelines

The project's `.gitignore` excludes:

- Raw product photos.
- Training datasets.
- Model weights.
- Virtual environments.

Upload the source code and README file. Avoid uploading private photos or unnecessarily large generated files.

---

## 🎓 Project Information

| Field | Details |
|---|---|
| Project Name | AI Object Detection System |
| Domain | Artificial Intelligence & Computer Vision |
| Detection Model | YOLO-World |
| Programming Language | Python |
| Main Library | OpenCV |
| Custom Recognition | Product Classifier |
| Supported Products | 13 predefined products |
| Platform | Windows |
| Development Tool | VS Code |
| Developer | Dharmendra Kumar Singh |
| GitHub | [dharmendra-developer](https://github.com/dharmendra-developer) |

---

## 👨‍💻 Developer

**Dharmendra Kumar Singh**

Python Developer | AI Enthusiast | Future Software Engineer

- GitHub: https://github.com/dharmendra-developer
- Instagram: https://www.instagram.com/dharmendra_developer/

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your changes.
5. Push your branch.
6. Submit a Pull Request.

---

## 📄 License

Add a `LICENSE` file to the repository to specify the terms under which this project can be used, modified, and distributed.

---

## ⭐ Support

If you find this project useful:

- Give this repository a ⭐ Star.
- Fork the project.
- Share it with other developers.
- Contribute to future improvements.

---

<p align="center">

### 🤖 Making Object Detection Smarter with AI

**Developed with ❤️ by DHARMENDRA_DEVELOPER**

</p>
