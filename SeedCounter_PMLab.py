from ultralytics import YOLO

def main():
    # Load a pretrained model (YOLOv11n is the nano version)
    model = YOLO('yolov11n.pt')  # or 'yolov11s.pt', 'yolov11m.pt', etc.

    # Train the model
    results = model.train(
        data='seed_dataset.yaml',
        epochs=100,
        batch=8,
        imgsz=640,
        name='yolov11n_seeds'
    )

    # Evaluate model performance on validation set
    metrics = model.val()

    model.save('./outputs/best_model.pt')

    print("Training complete. Model saved as 'best_model.pt'.")

if __name__ == "__main__":
    main()