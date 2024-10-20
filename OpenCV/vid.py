#uses OpenCV to capture a video add greyscale efect and show both 
#the orignal and the new video

import cv2

def main():
    # Start video capture 
    cap = cv2.VideoCapture(0)  # 0 for the default camera
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Get the w and h of the video frame
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object to save the processed video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for video saving
    out = cv2.VideoWriter('processed_video.avi', fourcc, 20.0, (frame_width, frame_height))

    print("Press 'q' to exit the video window.")

    while True:
        ret, frame = cap.read()  # webcam
        if not ret:
            print("Error: Could not read frame.")
            break

        # convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame_colored = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  

        # Write the processed frame to output file
        out.write(gray_frame_colored)

        # Display the original and processed frames
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Processed Frame (Grayscale)", gray_frame_colored)

        # Exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and writer objects and close all windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
