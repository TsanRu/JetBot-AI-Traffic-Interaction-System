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
JetBot Camera
↓
Road-Following Model (TensorRT)
↓ (Controls Motors)
YOLO Traffic Sign Detection (TensorRT)
↓ (Detected Sign)
Local FastAPI Server (on PC)
↓
OpenAI Language Reasoning
↓
JetBot Action Response / Human-Readable Explanation
