# Final project

Emotion Detector — IBM Build & Deploy AI Applications with Python & Flask.

The application uses the Watson NLP EmotionPredict service to return anger, disgust, fear, joy, sadness, and the dominant emotion. The Flask interface uses the supplied starter templates and JavaScript.

## Run in the Skills Network lab

```bash
python3 -m pip install requests flask pylint
python3 -m unittest -v
pylint server.py
python3 server.py
```

Open port 5000 with Launch Application. The Watson endpoint is provided by the course; availability outside the lab is not guaranteed.

## Validation

The five required dominant-emotion examples and blank-input handling passed against the live service. Static analysis of server.py scored 10.00/10. Blank input displays: Invalid text! Please try again!
