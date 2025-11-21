import cv2

def get_video_capture(input_path):
    # create a video capture object
    vid_capture = cv2.VideoCapture(input_path)
    
    if not vid_capture.isOpened():
        print("Error opening the video file")
    else:
        # Get frame rate information
        fps = vid_capture.get(cv2.CAP_PROP_FPS)
        print('Frames per second : ', fps, 'FPS')
   
        # Get frame count
        frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        print('Frame count : ', frame_count)
	
    return vid_capture



def preview_video(capture):
    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
       	    cv2.imshow('Frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break
	
    # Release the video capture object and close all windows
    capture.release()
    cv2.destroyAllWindows()


def main():
    # Where the video is located
    input_path = "videos/run.mp4"

    capture = get_video_capture(input_path)
    preview_video(capture)

    
if __name__ == "__main__":
    main()
