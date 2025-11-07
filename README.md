# JetBot-AI-Traffic-Interaction-System
  
This project presents an integrated intelligent autonomous driving system based on the NVIDIA JetBot platform. The system performs road following, real-time traffic sign recognition, and semantic interaction through an external FastAPI server connected to the OpenAI API. By combining vision-based navigation, object detection, and natural language reasoning, the system mimics simplified human decision-making behavior in a controlled traffic environment.
  
---

## System Overview
  
The final implementation integrates three components originally developed as separate course projects:
  
| Module | Source Project | Description |  
|-------|---------------|-------------|  
| **Road Following (Navigation)** | Midterm Project | TensorRT-optimized ResNet18 steering model controlling continuous navigation. |  
| **Traffic Sign Recognition** | Project05 | YOLOv4-tiny based detection of six traffic sign categories. |  
| **AI Semantic Interaction** | Project06 | FastAPI server relays detected sign information to OpenAI for descriptive interpretation. |  
  
---

## Recognized Traffic Signs
  
| Class Index | Traffic Sign | Meaning (Behavior Applied) |  
|------------|-------------|----------------------------|  
| 0 | block | Stop / Do not proceed |  
| 1 | max60 | Slow down |  
| 2 | min30 | Speed up |  
| 3 | pedestrian | Pedestrian crossing caution |  
| 4 | railway | Stop and wait before crossing |  
| 5 | stop | Full stop before proceeding |  
  
---  

## System Data Flow  
JetBot Camera → Road-Following Model (TensorRT) → Controls Motors  
↓   
Traffic Sign Detection (YOLOv4-tiny)  
↓ (Detected Sign)  
Local FastAPI Server (on PC) → OpenAI → Language Reasoning JetBot Action Response / Human-Readable Explanation  

---

## Key Features

- Real-time embedded vision-based navigation
- Multi-threaded processing allows simultaneous driving + detection
- Traffic signs dynamically influence speed and motion behavior
- OpenAI provides contextual, human-understandable explanations
- Modular design — each model can be retrained or replaced independently

---

## Project Structure

JetBot-AI-Traffic-Interaction-System/  
│  
├─ final/ # Final integrated system notebook  
│ └─ final.ipynb  
│  
├─ utils/ # YOLO helper modules (required)  
│  
├─ server/ # FastAPI server (runs on local PC)  
│ └─ server.py 
│  
├─ standard_sign/ # Reference sign images (used for OpenAI prompts)  
│  
├─ detected_img/ # Output directory for captured detections  
│  
├─ models/ # (Empty) Place model files here manually  
│ └─ README.md # "Insert downloaded model files here"  
│  
└─ requirements.txt # Environment dependencies  

> **Note:** Model files are **not** included in this repository and should be placed manually in `/models/`.  
> (Download link to be provided by the user.)  

---

## Hardware & Software Environment

- NVIDIA Jetson Nano / JetBot platform  
- Python 3.6+  
- TensorRT + PyCUDA optimization  
- YOLOv4-tiny traffic sign model  
- FastAPI server running on PC  
- OpenAI API for semantic interpretation  

---

## Execution Notes

1. Place trained models in `/models/`  
2. Start FastAPI server on PC  
3. Connect JetBot and PC to the same network  
4. Run `final.ipynb` to begin road following and sign detection  

---

## Acknowledgements  

This project was developed as part of an embedded systems curriculum focused on AI-driven autonomous navigation and human-interactive robotics.  
