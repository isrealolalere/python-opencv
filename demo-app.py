import streamlit as st
import cv2

# Streamlit app configuration
st.title("DroidCam Video Feed Viewer")

# Input field for DroidCam IP address
droidcam_ip = st.text_input("Enter DroidCam IP Address (e.g., http://192.168.1.196:4747/video):")

if droidcam_ip:
    # Create a VideoCapture object with the DroidCam IP address
    cap = cv2.VideoCapture(droidcam_ip)
    
    # Check if the video capture is successful
    if not cap.isOpened():
        st.error("Failed to connect to the DroidCam feed. Please check the IP address and try again.")
    else:
        st.success("Connected to DroidCam feed successfully!")

        # Stream video feed
        frame_placeholder = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to retrieve frame from DroidCam.")
                break
            
            # Display the video feed in Streamlit
            frame_placeholder.image(frame, channels="BGR")

        # Release the video capture object
        cap.release()
