import cv2
vidcap = cv2.VideoCapture('test_video.mp4')
success,image = vidcap.read()
count = 0
success = True

length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = vidcap.get(cv2.CAP_PROP_FPS)
print(length,width,height,fps)

while success:
  success,image = vidcap.read()
  print()
  print('Read a new frame: ', success)
  # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
  print(count)