exec(open('util.py').read())
def test2(inp):
	
	import cv2

	def save_frame(video_path, output_path, frame_number):
	    # Open the video file
	    cap = cv2.VideoCapture(video_path)

	    # Set the frame position
	    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

	    # Read the frame
	    ret, frame = cap.read()

	    if ret:
	        # Save the frame as an image
	        cv2.imwrite(output_path, frame)
	        print(f"Frame {frame_number} saved as {output_path}")
	    else:
	        print("Error: Could not read frame")

	    # Release the video capture object
	    cap.release()

	# Example usage
	video_path = "C:\\Users\\--\\Downloads\\tennis.mp4"
	frame_number = 10  # Specify the frame number you want to save
	output_path = "C:\\Users\\--\\Downloads\\tennis-frame-"+str(frame_number)+".jpg"
	save_frame(video_path, output_path, frame_number)


	
	
inp = []
test2(inp)