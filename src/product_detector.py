import sys
import cv2
from ultralytics import YOLOWorld

# ---------------------------------------------------------
# AI OBJECT DETECTION SYSTEM
# ---------------------------------------------------------

MODEL_NAME = "yolov8s-worldv2.pt"
CAMERA_INDEX = 0
CONFIDENCE_THRESHOLD = 0.20
IMAGE_SIZE = 640

# Prompts are written to help the open-vocabulary model
# recognize the requested everyday objects.
PRODUCTS = [
    ("Phone", "smartphone"),
    ("Charger", "phone charger"),
    ("Bangle", "bangle bracelet"),
    ("Body Lotion", "body lotion bottle"),
    ("Lipgloss", "lip gloss tube"),
    ("Spoon", "spoon"),
    ("Bournvita", "Bournvita drink container"),
    ("Snacks", "packaged snack packet"),
    ("Notebook", "notebook"),
    ("Pen", "pen"),
    ("Glue", "glue bottle"),
    ("Cup", "drinking cup"),
    ("Bottle", "water bottle"),
]

PROMPTS = [prompt for _, prompt in PRODUCTS]
DISPLAY_NAMES = {index: name for index, (name, _) in enumerate(PRODUCTS)}


def get_detection_classes():
    print("\nEnter object names separated by commas (for example: keys, mug, remote control).")
    print("Press Enter to use the built-in product list.")

    while True:
        user_input = input("Objects to detect: ").strip()
        if not user_input:
            return PROMPTS, DISPLAY_NAMES

        prompts = []
        seen_prompts = set()
        for value in user_input.split(","):
            prompt = value.strip()
            normalized_prompt = prompt.casefold()
            if prompt and normalized_prompt not in seen_prompts:
                prompts.append(prompt)
                seen_prompts.add(normalized_prompt)

        if prompts:
            return prompts, {index: prompt for index, prompt in enumerate(prompts)}

        print("Please enter at least one object name.")


def main():
    prompts, display_names = get_detection_classes()

    print("\n" + "=" * 52)
    print("             AI OBJECT DETECTION")
    print("=" * 52)
    print("Loading YOLO-World model. First launch may take a while...")

    try:
        model = YOLOWorld(MODEL_NAME)
        model.set_classes(prompts)
    except Exception as error:
        print("\nCould not load the AI model.")
        print("Check your internet connection and try again.")
        print(f"Details: {error}")
        input("\nPress Enter to close...")
        return

    camera = cv2.VideoCapture(CAMERA_INDEX)
    if not camera.isOpened():
        print("\nCould not open the webcam.")
        print("Close other camera apps or try CAMERA_INDEX = 1 in this file.")
        input("\nPress Enter to close...")
        return

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("\nCamera started!")
    print("Show the requested objects to the camera. Press Q in the camera window to quit.")

    try:
        while True:
            success, frame = camera.read()
            if not success:
                print("Could not read a frame from the webcam.")
                break

            # Run open-vocabulary object detection on the current frame.
            results = model.predict(
                source=frame,
                conf=CONFIDENCE_THRESHOLD,
                imgsz=IMAGE_SIZE,
                verbose=False
            )

            # Add a clean header to the live camera view.
            display = frame.copy()
            cv2.rectangle(display, (0, 0), (display.shape[1], 58), (25, 25, 25), -1)
            cv2.putText(
                display,
                "AI OBJECT DETECTION",
                (20, 38),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 255, 255),
                2,
                cv2.LINE_AA
            )

            detected_names = []

            if results and results[0].boxes is not None:
                boxes = results[0].boxes

                for box in boxes:
                    class_id = int(box.cls[0].item())
                    confidence = float(box.conf[0].item())

                    if class_id not in display_names:
                        continue

                    name = display_names[class_id]
                    detected_names.append(name)

                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    label = f"{name}  {confidence * 100:.0f}%"

                    # Draw detection box and label.
                    cv2.rectangle(display, (x1, y1), (x2, y2), (40, 220, 120), 2)
                    label_y = max(y1 - 10, 75)
                    cv2.rectangle(
                        display,
                        (x1, label_y - 28),
                        (x1 + max(150, len(label) * 12), label_y + 4),
                        (40, 220, 120),
                        -1
                    )
                    cv2.putText(
                        display,
                        label,
                        (x1 + 6, label_y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.65,
                        (15, 25, 20),
                        2,
                        cv2.LINE_AA
                    )

            # Show the current result in a fixed bottom panel.
            if detected_names:
                unique_names = list(dict.fromkeys(detected_names))
                result_text = "Detected: " + ", ".join(unique_names[:3])
            else:
                result_text = "Detected: Looking for an object..."

            panel_y = display.shape[0] - 52
            cv2.rectangle(
                display,
                (0, panel_y),
                (display.shape[1], display.shape[0]),
                (25, 25, 25),
                -1
            )
            cv2.putText(
                display,
                result_text[:100],
                (20, panel_y + 34),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (255, 255, 255),
                2,
                cv2.LINE_AA
            )

            cv2.imshow("AI Object Detection - Press Q to Quit", display)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except KeyboardInterrupt:
        print("\nStopping camera...")
    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")
    finally:
        camera.release()
        cv2.destroyAllWindows()
        print("\nCamera closed. Thank you for using the project!")


if __name__ == "__main__":
    main()
